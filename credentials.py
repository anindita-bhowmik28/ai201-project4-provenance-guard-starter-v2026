"""Persistent local credentials for the verified-human stretch path."""

import json
import threading
import uuid
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _read() -> dict[str, dict]:
    if not config.CREDENTIALS_FILE.exists():
        return {}
    try:
        value = json.loads(config.CREDENTIALS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return value if isinstance(value, dict) else {}


def get_credential(creator_id: str) -> dict | None:
    """Return a copy of a creator's credential, if one exists."""
    credential = _read().get(creator_id)
    return dict(credential) if isinstance(credential, dict) else None


def verify_creator(creator_id: str) -> tuple[dict, bool]:
    """Issue one persistent self-attestation credential per creator."""
    with _lock:
        credentials = _read()
        existing = credentials.get(creator_id)
        if isinstance(existing, dict):
            return dict(existing), False

        credential = {
            "credential_id": str(uuid.uuid4()),
            "creator_id": creator_id,
            "method": "local_self_attestation",
            "verified_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        credentials[creator_id] = credential
        config.CREDENTIALS_FILE.parent.mkdir(parents=True, exist_ok=True)
        temporary = config.CREDENTIALS_FILE.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(credentials, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(config.CREDENTIALS_FILE)
        return dict(credential), True
