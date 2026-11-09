#!/usr/bin/env python3
"""Fast functional tests for the completed Unit 7 service."""

import tempfile
import unittest
from pathlib import Path

import app
import audit
import config
import scoring
import stylometry


class ProvenanceGuardTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.original_audit_log = config.AUDIT_LOG
        self.original_credentials_file = config.CREDENTIALS_FILE
        self.original_model_signal = app.detector.model_signal
        config.AUDIT_LOG = Path(self.temporary.name) / "audit.jsonl"
        config.CREDENTIALS_FILE = Path(self.temporary.name) / "credentials.json"
        app.detector.model_signal = lambda text: 0.9
        self.client = app.app.test_client()

    def tearDown(self):
        config.AUDIT_LOG = self.original_audit_log
        config.CREDENTIALS_FILE = self.original_credentials_file
        app.detector.model_signal = self.original_model_signal
        self.temporary.cleanup()

    def submit(self, creator_id="writer"):
        return self.client.post("/submit", json={
            "creator_id": creator_id,
            "text": (
                "The system helps users. The system helps writers. "
                "The system helps everyone."
            ),
        })

    def test_submit_returns_and_logs_all_signals(self):
        response = self.submit()
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        for field in (
            "content_id", "guess", "confidence", "label", "model_score",
            "style_score", "repetition_score", "verified_human",
        ):
            self.assertIn(field, body)
        self.assertEqual(body["repetition_score"], 1.0)
        self.assertEqual(audit.read_entries()[0]["content_id"], body["content_id"])

    def test_all_label_ranges_are_reachable(self):
        self.assertEqual(scoring.score_to_label(0.20)[0], "human")
        self.assertEqual(scoring.score_to_label(0.51)[0], "unsure")
        self.assertEqual(scoring.score_to_label(0.95)[0], "ai")

    def test_vocabulary_measure_is_length_normalized(self):
        varied = "one two three four five six seven eight nine ten "
        short = (varied * 3).strip()
        long = (varied * 9).strip()
        self.assertAlmostEqual(
            stylometry.type_token_ratio(short),
            stylometry.type_token_ratio(long),
            places=2,
        )

    def test_punctuation_stuffing_is_not_maximally_human(self):
        stuffed = "A clause; another—clause... really?! (yes): more, marks!!!"
        self.assertGreater(stylometry.punctuation_density(stuffed), 0.06)
        self.assertGreater(stylometry.style_signal(stuffed), 0.20)

    def test_invalid_and_oversized_input_is_rejected_without_decision(self):
        cases = (
            (self.client.post("/submit", json={"creator_id": "x"}), 400),
            (self.client.post("/submit", json={"creator_id": "x", "text": ""}), 400),
            (self.client.post("/submit", json=[]), 400),
            (self.client.post("/submit", json={
                "creator_id": "x",
                "text": "x" * (config.MAX_TEXT_CHARACTERS + 1),
            }), 413),
        )
        self.assertTrue(all(response.status_code == status for response, status in cases))
        entries = audit.read_entries()
        self.assertEqual(len(entries), 4)
        self.assertTrue(all(entry["event"] == "rejected" for entry in entries))
        self.assertTrue(all(entry["status"] == "rejected" for entry in entries))
        self.assertTrue(all(entry["guess"] is None for entry in entries))
        required = {
            "timestamp", "content_id", "creator_id", "guess", "model_score",
            "style_score", "combined_score", "label", "status",
        }
        self.assertTrue(all(required <= entry.keys() for entry in entries))

    def test_rate_limit_is_per_creator_and_audits_rejection(self):
        allowed = [self.submit("rate-limit-writer") for _ in range(10)]
        rejected = self.submit("rate-limit-writer")
        other_creator = self.submit("different-writer")

        self.assertTrue(all(response.status_code == 200 for response in allowed))
        self.assertEqual(rejected.status_code, 429)
        self.assertEqual(other_creator.status_code, 200)
        rejection = audit.read_entries()[-2]
        self.assertEqual(rejection["creator_id"], "rate-limit-writer")
        self.assertEqual(rejection["reason"], "rate_limited")

    def test_appeal_updates_content_status(self):
        content_id = self.submit().get_json()["content_id"]
        appeal = self.client.post("/appeal", json={
            "content_id": content_id,
            "reasoning": "I wrote this and can provide my drafting notes.",
        })
        self.assertEqual(appeal.status_code, 200)
        content = self.client.get(f"/content/{content_id}")
        self.assertEqual(content.status_code, 200)
        self.assertTrue(content.get_json()["appealed"])
        self.assertEqual(content.get_json()["status"], "under_review")

    def test_unknown_content_returns_404(self):
        self.assertEqual(self.client.get("/content/not-real").status_code, 404)
        response = self.client.post("/appeal", json={
            "content_id": "not-real",
            "reasoning": "Please review this decision.",
        })
        self.assertEqual(response.status_code, 404)

    def test_verified_credential_appears_on_later_work(self):
        verification = self.client.post("/verify-human", json={
            "creator_id": "verified-writer",
            "verification_statement": (
                "I attest that I completed the local verification step."
            ),
        })
        self.assertEqual(verification.status_code, 201)
        credential_id = verification.get_json()["credential"]["credential_id"]

        submission = self.submit("verified-writer").get_json()
        self.assertTrue(submission["verified_human"])
        self.assertEqual(
            submission["human_credential"]["credential_id"],
            credential_id,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
