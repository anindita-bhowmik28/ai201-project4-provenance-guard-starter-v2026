"""Concrete evaluation scenarios for the unit 8 checks."""

SCENARIOS = [
    {
        "name": "human false positives",
        "criterion": 1,
        "texts": [
            "I walked home with my notebook tucked under my arm and stopped at the bakery because the window smelled like cinnamon. A boy in line was humming to himself while the cashier wrapped a loaf in brown paper. When I finally reached the corner, the sky had gone from blue to a soft grey and the rain began before I crossed the street.",
            "We stayed in the apartment longer than usual because the wind kept rattling the windows. My sister sat on the floor with a cup of tea and we talked over the noise about the old neighborhood, the bus route, and the way the shops changed every few years. At some point the rain stopped and the whole street looked brighter.",
            "The bus was crowded enough that I had to stand near the back, but I did not mind. The woman next to me was reading a newspaper with the pages folded into a square, and the driver kept checking his mirror like he was timing the lights. By the time I got off, I had already decided to walk the last block instead of waiting for another one.",
            "I left the meeting with three pages of notes and no clear answer, which felt familiar enough to be reassuring. A few people stayed behind to talk about the timeline while the rest of us drifted toward the stairs. Outside, the afternoon had turned cold and the light looked more silver than gold.",
            "On the walk to class, the sidewalk was full of puddles that kept reflecting the afternoon sky. I kept my hands in my pockets and listened to the sound of shoes hitting the pavement in uneven patterns. When I reached the building, I stood for a moment under the awning and let the rain pass before going inside.",
            "I kept the old recipe card in the kitchen drawer for years because the margins were filled with my mother's handwriting. The ingredients were simple, but the smell of the onions cooking always made the room feel more settled. I still make it when I want the day to slow down for a while.",
            "At the station, everyone seemed to be moving in different directions without much urgency. I watched the train pull in and a few people stepped aside to let others through. I stood near the rails and listened to the announcement crackle through the speaker until the platform went quiet again.",
            "The light in the apartment was weak by the time I got home, but the room felt warm anyway. I put my keys down on the table and sat with the window open just enough to hear the sound of traffic from the street below. There was a small stack of mail waiting, and I left it there until I had eaten something first.",
            "My friend texted me from the bus stop and said the line had been moving slowly all morning. I laughed because that was the exact kind of answer I expected from her. We ended up talking for another fifteen minutes before she reached the stop where she was getting off.",
            "The first thing I noticed in the cafe was the smell of coffee and wet coats. The table by the window was taken, so I sat near the back and listened to the conversation at the next booth. It was one of those ordinary afternoons that feel mundane at the time and memorable later.",
        ],
    },
    {
        "name": "score gap between generated and human text",
        "criterion": 2,
        "texts": [
            "The implementation of this framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.",
            "This system is designed to support a wide range of user needs and to simplify repeated tasks. It provides clear outputs, consistent processing, and dependable workflows for teams that need reliable results from a structured process.",
            "The application is built to assist users with routine work and to reduce repeated effort across the workflow. It emphasizes clarity, consistency, and predictable execution so that decision making remains efficient and easy to follow.",
            "The model generates text by selecting likely next tokens, which makes its output highly regular in structure and phrase choice. This pattern is useful for automation, but it also creates recognizable repetition that differs from the variety found in ordinary human writing.",
            "A well-designed system should provide consistent output, clear instructions, and straightforward evaluation. In practice, this means balancing automation with human oversight, because both speed and accountability matter when content is produced at scale.",
            "I left the bakery with a paper bag and the door still swinging behind me. The woman behind the counter had a watch on her wrist that kept catching the light, and I remember thinking the whole morning looked more patient than usual. By the time I reached the corner, I had forgotten what I was originally planning to buy.",
            "We sat on the steps for a while and listened to the neighbourhood settle into the afternoon. A dog was barking somewhere behind the row of parked cars, and a man across the street was cleaning the windows of his shop with a long yellow cloth. The whole scene felt quiet in a way that made me pay attention.",
            "The rain had stopped by the time I reached the station, but the platform was still slick with reflection. A father was trying to keep his child dry with one umbrella while everyone else moved around them without much urgency. I waited for the train and watched the lights change in the puddles.",
            "I always keep a notebook in my bag because the best ideas never seem to arrive at a convenient time. Some of them disappear before I can write them down, but others stay long enough to become real plans. The ones that last usually have a small, ordinary beginning.",
            "My roommate was making tea when I came in from the cold, and the whole kitchen smelled faintly of lemon and steam. We stood there for a minute without speaking, just listening to the kettle and the road outside. It was one of those evenings when nothing important happened and that was exactly the point.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "mode": "labels",
        "scores": [0.20, 0.51, 0.95],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "mode": "appeals",
        "texts": [
            "I kept the old recipe card in the kitchen drawer because the notes in the margin reminded me which steps mattered most.",
            "The train arrived after sunset and everyone on the platform moved toward the doors with the same tired patience.",
            "We talked through the afternoon while the rain tapped against the window and the coffee slowly went cold.",
            "My notebook was open on the table beside a stack of letters that I had meant to answer all week.",
            "At the corner shop the owner was arranging fruit outside while two children drew circles on the pavement with chalk.",
        ],
    },
    {
        "name": "malformed and oversized submissions",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            [],
            {"text": "word " * 5000, "creator_id": "eval_oversized"},
        ],
    },
]


def validate() -> list[str]:
    """Validate the scenario list before a long run."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        if scenario.get("mode") == "labels":
            if scenario.get("scores") != [0.20, 0.51, 0.95]:
                problems.append(f"scenario {i} has the wrong label coverage scores")
            continue
        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        if texts and bodies:
            problems.append(f"scenario {i} ('{scenario.get('name')}') has both texts and bodies")
            continue
        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, (dict, list)):
                    problems.append(f"scenario {i}, body {j} is not JSON-compatible")
            continue
        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue
        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(f"scenario {i}, text {j} is empty")
    return problems
