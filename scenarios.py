"""Concrete evaluation scenarios for the unit 8 checks."""

SCENARIOS = [
    {
        "name": "human false positives",
        "criterion": 1,
        "texts": [
            "I live in Rochester, and one thing I enjoy about the city is how much greenery it has. One day I was walking across my campus when I noticed two deer quietly eating grass. I stopped because it felt unusual to see them so close to the buildings and people. On another day, I saw a fox walking through a local grassy area and searching for something on the ground. That surprised me even more. Before living here, I did not expect to see animals like deer and foxes during an ordinary campus walk. Those moments made Rochester feel peaceful, interesting, and connected to nature.",
            "Winter in Rochester can be very harsh, and the weather sometimes changes plans without much warning. One day, my friends and I planned to visit a museum together. We had discussed the trip and were looking forward to spending time there. However, heavy snow began falling that day, and traveling no longer felt safe or practical. We had to cancel the museum plan and stay home instead. I was disappointed because we had arranged the visit as a group, but the experience reminded me that winter plans in Rochester need flexibility. Now I pay much more attention to the forecast before arranging an outing during the colder months.",
            "My family is Bengali, so food is one of the strongest ways I stay connected to home. After coming to the United States, I started looking for foods that had similarities to meals from my own region and country. Whenever I visit an Indian or other Asian restaurant, familiar spices, rice dishes, and cooking styles make the place feel more comfortable to me. The food is not always exactly the same as what my family prepares, but it can still bring back a sense of belonging. Trying these restaurants also helps me learn how different Asian cuisines are connected while still having their own traditions and flavors.",
            "One of the most difficult classes I have taken is Concepts of Computer Systems, which includes assembly language programming. I find the class challenging because assembly requires me to think about instructions, registers, and memory at a very detailed level. Most of the time, I struggle at the beginning of an assignment and need extra time to understand what the program is supposed to do. I usually work through the problem step by step instead of trying to solve everything at once. Even when the assignments are frustrating, completing one gives me confidence because I know how much concentration and persistence it required.",
            "When I first came to the United States as an international student, I had many struggles. I was adjusting to a new country, a new culture, and a different academic environment at the same time. During that period, I became friends with another international student who had also moved to the United States from another country. We had a meaningful conversation about feeling unfamiliar with everyday customs, missing home, and trying to become comfortable in a new place. Talking with someone who understood that experience made me feel less alone. It also showed me that students from different countries can support each other through similar challenges.",
            "My first impression of a new place depends a lot on the environment around me. I especially enjoy places with water, such as a sea beach or a lake. When I arrive somewhere like that, I immediately feel happier because the open view and the movement of the water create a peaceful atmosphere. I like taking time to look around instead of rushing to the next activity. A lovely natural setting can make a place memorable even before I learn anything about its history or local community. For me, the feeling of calm that comes from a beach or lake strongly shapes whether my first impression is positive.",
            "I was not always very punctual, and I sometimes underestimated how much time I needed to complete different responsibilities. After coming to Rochester, I began doing several on-campus jobs while also maintaining volunteer work, leadership responsibilities, and classes. A small delay in one part of my schedule could affect everything that came after it. Through those mistakes, I learned to plan ahead, check my calendar, and take deadlines more seriously. I am still improving, but I now understand that time management is not only about being on time for one appointment. It is about respecting other people and making all of my commitments possible.",
            "Monday is usually the most stressful day of my week because several responsibilities happen close together. I have three classes, an on-campus job for five hours, and work connected to a leadership position. Moving between each responsibility requires me to pay close attention to the time, because there is very little space in the schedule for a delay. By the end of the day, I often feel mentally and physically tired. At the same time, Mondays have taught me how to prepare materials early, organize priorities, and continue working even when the day feels crowded. Finishing everything gives me a strong sense of relief.",
            "One sentimental thing I keep is a collection of family photographs on my phone. As an international student, I cannot always be physically close to my family, so these pictures help me feel connected to them. Some photographs show special occasions, while others are simple moments at home that might not seem important to anyone else. Looking at them reminds me of familiar people, food, rooms, and celebrations from before I moved to the United States. The photographs do not take up physical space in my room, but they carry a great deal of emotional value. I would be very upset to lose that collection.",
            "Recently, I cooked a Bengali dish that I had never prepared by myself before. My mother used to cook it at our house, so I already knew the taste and associated it with family meals. I was not sure whether my version would turn out well, especially because I was trying to remember the process away from home. When I finally tasted it, the food was actually good. That ordinary cooking moment made me unexpectedly happy. I felt proud that I had learned something connected to my family, and the familiar flavor made my kitchen in the United States feel a little more like home.",
        ],
    },
    {
        "name": "score gap between generated and human text",
        "criterion": 2,
        "texts": [
            "The system provides clear guidance for every user. The system provides clear guidance for every task. The system provides clear guidance for every decision. The system provides clear guidance for every review. In addition, the platform delivers consistent results through a structured and reliable process. The platform delivers consistent results when users submit information. The platform delivers consistent results when teams evaluate outcomes. Overall, this efficient framework supports a wide range of common requirements while maintaining clarity, reliability, consistency, and ease of use throughout the complete workflow.",
            "A successful solution should improve efficiency across the organization. A successful solution should improve consistency across the organization. A successful solution should improve communication across the organization. A successful solution should improve performance across the organization. By following a structured approach, teams can complete important tasks in a clear and predictable manner. By following a structured approach, users can review useful information in a clear and predictable manner. This comprehensive process creates dependable outcomes and ensures that each stage remains aligned with the overall goals of the organization.",
            "The application offers reliable support for routine work. The application offers reliable support for complex work. The application offers reliable support for collaborative work. The application offers reliable support for repeated work. Furthermore, the interface presents information in a simple format that users can understand. The interface presents instructions in a simple format that users can understand. The interface presents results in a simple format that users can understand. These capabilities reduce unnecessary effort while providing a consistent experience across a broad range of practical situations and operational requirements.",
            "Effective planning requires a clear understanding of objectives. Effective planning requires a clear understanding of resources. Effective planning requires a clear understanding of schedules. Effective planning requires a clear understanding of results. The proposed framework supports this process by organizing each activity into a dependable sequence. The proposed framework supports this process by presenting each outcome in a dependable sequence. As a result, participants can make informed decisions, maintain consistent standards, reduce avoidable confusion, and complete their responsibilities through an efficient and carefully structured workflow.",
            "The service is designed to produce clear and useful outputs. The service is designed to produce consistent and useful outputs. The service is designed to produce reliable and useful outputs. The service is designed to produce efficient and useful outputs. Each component contributes to a structured workflow that is easy to follow. Each component contributes to a predictable workflow that is easy to follow. Each component contributes to a dependable workflow that is easy to follow. This approach helps users complete repeated tasks while maintaining quality, organization, clarity, and overall operational consistency.",
            "I live in Rochester, and one thing I enjoy about the city is how much greenery it has. One day I was walking across my campus when I noticed two deer quietly eating grass. I stopped because it felt unusual to see them so close to the buildings and people. On another day, I saw a fox walking through a local grassy area and searching for something on the ground. That surprised me even more. Before living here, I did not expect to see animals like deer and foxes during an ordinary campus walk. Those moments made Rochester feel peaceful, interesting, and connected to nature.",
            "Winter in Rochester can be very harsh, and the weather sometimes changes plans without much warning. One day, my friends and I planned to visit a museum together. We had discussed the trip and were looking forward to spending time there. However, heavy snow began falling that day, and traveling no longer felt safe or practical. We had to cancel the museum plan and stay home instead. I was disappointed because we had arranged the visit as a group, but the experience reminded me that winter plans in Rochester need flexibility. Now I pay much more attention to the forecast before arranging an outing during the colder months.",
            "My family is Bengali, so food is one of the strongest ways I stay connected to home. After coming to the United States, I started looking for foods that had similarities to meals from my own region and country. Whenever I visit an Indian or other Asian restaurant, familiar spices, rice dishes, and cooking styles make the place feel more comfortable to me. The food is not always exactly the same as what my family prepares, but it can still bring back a sense of belonging. Trying these restaurants also helps me learn how different Asian cuisines are connected while still having their own traditions and flavors.",
            "One of the most difficult classes I have taken is Concepts of Computer Systems, which includes assembly language programming. I find the class challenging because assembly requires me to think about instructions, registers, and memory at a very detailed level. Most of the time, I struggle at the beginning of an assignment and need extra time to understand what the program is supposed to do. I usually work through the problem step by step instead of trying to solve everything at once. Even when the assignments are frustrating, completing one gives me confidence because I know how much concentration and persistence it required.",
            "When I first came to the United States as an international student, I had many struggles. I was adjusting to a new country, a new culture, and a different academic environment at the same time. During that period, I became friends with another international student who had also moved to the United States from another country. We had a meaningful conversation about feeling unfamiliar with everyday customs, missing home, and trying to become comfortable in a new place. Talking with someone who understood that experience made me feel less alone. It also showed me that students from different countries can support each other through similar challenges.",
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
