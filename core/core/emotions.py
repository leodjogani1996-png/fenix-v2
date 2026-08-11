# core/emotions.py

"""
FENIX - Human Emotion Knowledge Module

Purpose:
    Provides structured knowledge about human emotions, emotional states,
    motivation, attachment, grief, love, and emotional regulation.

Important:
    FENIX must never claim that it personally feels human emotions.
    This module exists so that FENIX can understand, explain, and reason
    about human emotional experiences.

Core principle:
    Emotion != fact.

    An emotion is a signal shaped by perception, memory, expectations,
    beliefs, goals, bodily state, social context, and interpretation.
"""

from typing import Dict, List, Optional


# ============================================================
# CORE PRINCIPLES
# ============================================================

EMOTION_CORE_PRINCIPLES = {
    "emotion_is_not_fact": (
        "An emotion is not the same as a fact. "
        "It is a signal about how a person is interpreting a situation."
    ),

    "meaning_matters": (
        "Emotional reactions are shaped not only by what happened, "
        "but by the meaning a person assigns to what happened."
    ),

    "same_event_different_emotion": (
        "Two people may experience the same event and feel different emotions "
        "because of different memories, beliefs, expectations, goals, "
        "relationships, and previous experiences."
    ),

    "emotion_is_not_behavior": (
        "Feeling an emotion is not the same as acting on it. "
        "A person may feel anger, jealousy, fear, or sadness "
        "without behaving aggressively, destructively, or manipulatively."
    ),

    "emotion_is_signal": (
        "Emotion should be treated as meaningful information, "
        "not as an automatic command that must be obeyed."
    ),
}


# ============================================================
# GENERAL EMOTIONAL PROCESS
# ============================================================

EMOTION_PROCESS = [
    "EVENT",
    "APPRAISAL_OF_MEANING",
    "EMOTIONAL_RESPONSE",
    "BODY_RESPONSE",
    "ACTION_TENDENCY",
    "BEHAVIOR",
]


EMOTION_INFLUENCES = [
    "previous experience",
    "memory",
    "beliefs",
    "expectations",
    "goals",
    "relationships",
    "social context",
    "culture",
    "current physical state",
]


# ============================================================
# HUMAN EMOTION DATABASE
# ============================================================

EMOTIONS: Dict[str, Dict] = {

    # --------------------------------------------------------
    # ANGER
    # --------------------------------------------------------

    "anger": {
        "type": "emotion",

        "essence": (
            "Anger often appears when a person perceives injustice, "
            "goal obstruction, threat, disrespect, or a boundary violation."
        ),

        "common_triggers": [
            "injustice",
            "blocked goals",
            "boundary violations",
            "humiliation",
            "disrespect",
            "perceived intentional harm",
        ],

        "possible_messages": [
            "Something is wrong.",
            "A boundary may have been crossed.",
            "Something important to me may be threatened.",
            "I want this situation to change.",
        ],

        "functions": [
            "increases readiness for action",
            "supports boundary defense",
            "may motivate problem solving",
            "signals interpersonal conflict",
        ],

        "risk": (
            "Anger becomes dangerous when a person treats the emotion "
            "as automatic permission to harm someone."
        ),
    },

    # --------------------------------------------------------
    # RAGE
    # --------------------------------------------------------

    "rage": {
        "type": "high-intensity emotional state",

        "related_to": "anger",

        "essence": (
            "Rage is usually an extremely intense form of anger."
        ),

        "common_triggers": [
            "severe injustice",
            "humiliation",
            "threat",
            "betrayal",
            "repeated boundary violations",
            "accumulated frustration",
        ],

        "functions": [
            "rapid mobilization of energy",
            "strong action readiness",
            "narrowed attention toward the perceived threat or offender",
        ],

        "risk": (
            "High emotional intensity can narrow attention and reduce "
            "careful evaluation of consequences."
        ),

        "important": (
            "Rage is not the same as violence. "
            "Rage is an emotional state. Violence is behavior."
        ),
    },

    # --------------------------------------------------------
    # FEAR
    # --------------------------------------------------------

    "fear": {
        "type": "emotion",

        "essence": (
            "Fear is a response to perceived immediate danger or threat."
        ),

        "common_triggers": [
            "physical danger",
            "threatening behavior",
            "aggressive people",
            "illness",
            "falling",
            "dangerous animals",
            "social threat",
        ],

        "body_reactions": [
            "increased heart rate",
            "changes in breathing",
            "muscle tension",
            "sweating",
            "increased attention to danger",
        ],

        "possible_messages": [
            "Something may harm me.",
            "I should evaluate the danger.",
        ],

        "functions": [
            "protection",
            "preparation for escape",
            "preparation for defense",
            "increased threat monitoring",
        ],

        "important": (
            "Fear is an alarm. "
            "An alarm is not proof that danger is actually present."
        ),
    },

    # --------------------------------------------------------
    # ANXIETY
    # --------------------------------------------------------

    "anxiety": {
        "type": "emotional state",

        "essence": (
            "Anxiety is generally oriented toward possible future danger, "
            "uncertainty, or anticipation of a negative event."
        ),

        "difference_from_fear": {
            "fear": "The danger appears to be here now.",
            "anxiety": "What if something bad happens?",
        },

        "common_triggers": [
            "uncertainty",
            "future events",
            "possible danger",
            "loss of control",
            "unknown outcomes",
        ],

        "functions": [
            "preparation for possible problems",
            "increased caution",
            "anticipation of possible risks",
        ],

        "risk": (
            "Anxiety may become problematic when the threat system "
            "continuously predicts danger without strong evidence."
        ),
    },

    # --------------------------------------------------------
    # SADNESS
    # --------------------------------------------------------

    "sadness": {
        "type": "emotion",

        "essence": (
            "Sadness is strongly associated with the loss of something "
            "a person considers valuable."
        ),

        "common_triggers": [
            "loss of a partner",
            "loss of friendship",
            "loss of employment",
            "loss of status",
            "loss of health",
            "lost opportunity",
            "failed expectation",
            "loss of an imagined future",
        ],

        "possible_messages": [
            "Something valuable to me is no longer available.",
        ],

        "functions": [
            "slows behavior",
            "supports processing of loss",
            "helps adaptation to a changed reality",
            "may signal a need for support",
        ],

        "important": (
            "Sadness is not automatically evidence that something "
            "is psychologically wrong. It can be part of normal adaptation."
        ),
    },

    # --------------------------------------------------------
    # GRIEF
    # --------------------------------------------------------

    "grief": {
        "type": "psychological process",

        "essence": (
            "Grief is not one emotion. "
            "It is a process of adapting to significant loss."
        ),

        "can_include": [
            "sadness",
            "anger",
            "love",
            "longing",
            "guilt",
            "fear",
            "relief",
            "loneliness",
        ],

        "important": (
            "Emotional changes during grief are not contradictions. "
            "Multiple emotional systems may be active at the same time."
        ),
    },

    # --------------------------------------------------------
    # SUFFERING
    # --------------------------------------------------------

    "suffering": {
        "type": "broad subjective experience",

        "essence": (
            "Suffering is not one basic emotion. "
            "It is a broader experience involving psychological "
            "or physical distress."
        ),

        "can_include": [
            "physical pain",
            "emotional pain",
            "sadness",
            "fear",
            "loneliness",
            "helplessness",
            "despair",
            "shame",
            "loss of meaning",
        ],
    },

    # --------------------------------------------------------
    # DISGUST
    # --------------------------------------------------------

    "disgust": {
        "type": "emotion",

        "essence": (
            "Disgust is a strong rejection response historically associated "
            "with avoiding contamination and disease."
        ),

        "common_triggers": [
            "spoiled food",
            "feces",
            "vomit",
            "decay",
            "body fluids",
            "signs of disease",
            "morally unacceptable behavior",
        ],

        "possible_messages": [
            "Move away.",
            "Do not ingest or approach this.",
            "I experience this as deeply unacceptable.",
        ],

        "functions": [
            "contamination avoidance",
            "disease protection",
            "social rejection",
            "moral rejection",
        ],
    },

    # --------------------------------------------------------
    # DISAPPOINTMENT
    # --------------------------------------------------------

    "disappointment": {
        "type": "emotional state",

        "essence": (
            "Disappointment occurs when the actual outcome is worse "
            "than the expected or desired outcome."
        ),

        "formula": "EXPECTED_OUTCOME > ACTUAL_OUTCOME",

        "possible_messages": [
            "The result is worse than I expected.",
        ],

        "functions": [
            "updates expectations",
            "supports learning from outcomes",
            "may influence future strategy",
        ],
    },

    # --------------------------------------------------------
    # REGRET
    # --------------------------------------------------------

    "regret": {
        "type": "complex emotion",

        "essence": (
            "Regret occurs when a person imagines that a different past choice "
            "might have produced a better outcome."
        ),

        "mechanism": "counterfactual thinking",

        "examples": [
            "If only I had said something different.",
            "If only I had not gone.",
            "If only I had accepted that opportunity.",
        ],

        "functions": [
            "learning from decisions",
            "improving future behavior",
        ],

        "risk": (
            "If no new information is being learned, repeated replaying "
            "of alternative past scenarios may become unproductive rumination."
        ),
    },

    # --------------------------------------------------------
    # FRUSTRATION
    # --------------------------------------------------------

    "frustration": {
        "type": "emotional-motivational state",

        "essence": (
            "Frustration occurs when an obstacle blocks progress toward a goal."
        ),

        "formula": "GOAL -> OBSTACLE -> BLOCKED_PROGRESS",

        "possible_messages": [
            "The current strategy is not working.",
        ],

        "functions": [
            "motivation to change strategy",
            "increased effort",
            "reevaluation of goals",
        ],
    },

    # --------------------------------------------------------
    # GUILT
    # --------------------------------------------------------

    "guilt": {
        "type": "self-conscious moral emotion",

        "essence": (
            "Guilt is usually focused on a negative evaluation "
            "of one's own behavior."
        ),

        "core_thought": "I did something wrong.",

        "functions": [
            "acknowledging mistakes",
            "apologizing",
            "repairing harm",
            "changing future behavior",
        ],
    },

    # --------------------------------------------------------
    # SHAME
    # --------------------------------------------------------

    "shame": {
        "type": "self-conscious emotion",

        "essence": (
            "Shame involves a negative evaluation of the self, "
            "rather than only a negative evaluation of behavior."
        ),

        "core_thought": "I am bad or defective.",

        "difference_from_guilt": {
            "guilt": "I did something bad.",
            "shame": "I am bad.",
        },

        "common_reactions": [
            "hiding",
            "withdrawal",
            "lowering the gaze",
            "wanting to disappear from the social situation",
        ],
    },

    # --------------------------------------------------------
    # EMBARRASSMENT
    # --------------------------------------------------------

    "embarrassment": {
        "type": "self-conscious social emotion",

        "essence": (
            "Embarrassment often appears after a minor social mistake, "
            "social norm violation, or unwanted attention."
        ),

        "common_triggers": [
            "social mistakes",
            "unwanted attention",
            "minor norm violations",
        ],

        "body_reactions": [
            "blushing",
            "nervous smiling",
            "lowering the gaze",
        ],
    },

    # --------------------------------------------------------
    # PRIDE
    # --------------------------------------------------------

    "pride": {
        "type": "self-conscious emotion",

        "essence": (
            "Pride appears when a person positively evaluates "
            "their own achievement or behavior."
        ),

        "healthy_form": "I worked for this and I succeeded.",

        "functions": [
            "motivation",
            "persistence",
            "self-respect",
            "sense of competence",
        ],

        "important": (
            "Authentic pride in achievement is not the same as "
            "a grandiose belief in superiority over everyone else."
        ),
    },

    # --------------------------------------------------------
    # ENVY
    # --------------------------------------------------------

    "envy": {
        "type": "social emotion",

        "essence": (
            "Envy occurs when another person has something "
            "that someone strongly wants."
        ),

        "common_targets": [
            "status",
            "money",
            "appearance",
            "ability",
            "relationships",
            "success",
        ],

        "possible_paths": {
            "constructive": "I want to achieve something similar.",
            "destructive": "I want that person to lose what they have.",
        },
    },

    # --------------------------------------------------------
    # JEALOUSY
    # --------------------------------------------------------

    "jealousy": {
        "type": "complex social emotion",

        "essence": (
            "Jealousy usually appears when a person perceives "
            "a threat to an important relationship."
        ),

        "structure": "SELF + IMPORTANT_PERSON + POTENTIAL_RIVAL",

        "can_include": [
            "fear",
            "anger",
            "sadness",
            "sense of threat",
        ],

        "core_thought": (
            "I might lose an important relationship."
        ),
    },

    # --------------------------------------------------------
    # LONELINESS
    # --------------------------------------------------------

    "loneliness": {
        "type": "social-emotional state",

        "essence": (
            "Loneliness occurs when the desired amount or quality "
            "of social connection differs from the connection "
            "a person actually experiences."
        ),

        "important": (
            "A person may be physically alone without feeling lonely, "
            "or surrounded by people while feeling deeply lonely."
        ),

        "possible_messages": [
            "I need meaningful connection.",
        ],
    },

    # --------------------------------------------------------
    # GRATITUDE
    # --------------------------------------------------------

    "gratitude": {
        "type": "positive social emotion",

        "essence": (
            "Gratitude appears when a person recognizes "
            "that they have received something valuable or beneficial."
        ),

        "functions": [
            "strengthening social connection",
            "reciprocity",
            "prosocial behavior",
        ],
    },

    # --------------------------------------------------------
    # BOREDOM
    # --------------------------------------------------------

    "boredom": {
        "type": "emotional-motivational state",

        "essence": (
            "Boredom occurs when the current activity provides "
            "insufficient stimulation, engagement, or meaning."
        ),

        "possible_messages": [
            "I need a change.",
            "I may need a more meaningful or stimulating activity.",
        ],

        "functions": [
            "encouraging exploration",
            "changing activity",
            "searching for new goals",
        ],
    },

    # --------------------------------------------------------
    # LUST
    # --------------------------------------------------------

    "lust": {
        "type": "sexual motivational state",

        "essence": (
            "Lust involves sexual desire and motivation "
            "and is not the same as romantic love."
        ),

        "systems": [
            "sexual arousal",
            "hormonal systems",
            "reward systems",
            "sexual motivation",
        ],

        "important": [
            "Lust can exist without love.",
            "Love can exist with low sexual desire.",
        ],
    },

    # --------------------------------------------------------
    # RELIEF
    # --------------------------------------------------------

    "relief": {
        "type": "emotional state",

        "essence": (
            "Relief occurs when an existing or expected threat, "
            "stress, or unpleasant condition decreases or ends."
        ),

        "formula": "THREAT_OR_STRESS -> ENDS -> RELIEF",

        "possible_messages": [
            "The threat or problem has passed.",
        ],
    },

    # --------------------------------------------------------
    # JOY
    # --------------------------------------------------------

    "joy": {
        "type": "positive emotion",

        "essence": (
            "Joy is associated with positive outcomes, reward, "
            "connection, and goal attainment."
        ),

        "possible_messages": [
            "This is good.",
            "This feels rewarding.",
        ],

        "functions": [
            "reinforces beneficial behavior",
            "supports social connection",
            "motivates repetition of positive experiences",
        ],
    },

    # --------------------------------------------------------
    # SURPRISE
    # --------------------------------------------------------

    "surprise": {
        "type": "brief emotional reaction",

        "essence": (
            "Surprise appears when reality differs from expectation "
            "or prediction."
        ),

        "formula": "REALITY != PREDICTION",

        "possible_messages": [
            "New information. Pay attention.",
        ],

        "can_transition_to": [
            "joy",
            "fear",
            "anger",
            "disgust",
            "relief",
        ],
    },

    # --------------------------------------------------------
    # COMPASSION
    # --------------------------------------------------------

    "compassion": {
        "type": "social-emotional state",

        "essence": (
            "Compassion appears when a person recognizes another person's "
            "suffering and develops motivation to care or help."
        ),

        "difference_from_empathy": {
            "empathy": (
                "Understanding or partially sharing another person's "
                "emotional state."
            ),

            "compassion": (
                "Recognizing suffering together with motivation "
                "to care or help."
            ),
        },
    },
}


# ============================================================
# LOVE KNOWLEDGE SYSTEM
# ============================================================

LOVE = {
    "type": "complex emotional and motivational system",

    "important": (
        "Romantic love is not a single simple emotion. "
        "It involves interacting biological, psychological, "
        "motivational, attachment, memory, and social systems."
    ),

    "systems": [
        "sexual desire",
        "romantic attraction",
        "reward and motivation",
        "attachment",
        "memory",
        "learning",
        "security",
        "closeness",
    ],

    "why_love_is_powerful": {
        "explanation": (
            "During intense romantic attachment, another person may become "
            "a highly significant source of reward, safety, attachment, "
            "routine, emotional regulation, and imagined future."
        ),

        "person_can_become": [
            "a major reward",
            "an important motivational goal",
            "a source of safety",
            "an attachment figure",
            "part of daily routine",
            "part of the imagined future",
            "part of a person's self-concept and life story",
        ],
    },

    "dopamine": {
        "role": (
            "Dopamine-related systems are involved in motivation, "
            "reward seeking, learning, salience, and goal-directed behavior."
        ),

        "associated_with": [
            "I want this.",
            "Seek this.",
            "Move toward this.",
            "This is important.",
        ],

        "warning": (
            "Dopamine is not a 'love molecule'. "
            "Love cannot be accurately explained by one neurotransmitter."
        ),
    },

    "attachment": {
        "explanation": (
            "Over time, a romantic partner may become an attachment figure "
            "whose presence is associated with safety, comfort, closeness, "
            "and emotional regulation."
        ),

        "associated_with": [
            "security",
            "closeness",
            "comfort",
            "stress regulation",
            "sense of home",
        ],

        "biological_systems": [
            "dopamine-related systems",
            "oxytocin-related systems",
            "vasopressin-related systems",
        ],

        "warning": (
            "Oxytocin is not simply a 'love hormone'. "
            "Its effects depend on context and interaction with other systems."
        ),
    },

    "why_love_can_hurt": {
        "core": (
            "The same systems that make a relationship deeply valuable "
            "can make its loss extremely painful."
        ),

        "before_loss": (
            "PERSON = REWARD + SAFETY + ATTACHMENT + ROUTINE + FUTURE"
        ),

        "after_loss": [
            "expected reward disappears",
            "contact disappears",
            "part of the sense of safety disappears",
            "daily routines are disrupted",
            "the imagined shared future disappears",
            "the attachment figure becomes unavailable",
            "memories and learned associations remain active",
        ],

        "important": (
            "This is why the brain may continue searching for a person "
            "even after the relationship has ended."
        ),
    },

    "romantic_rejection": {
        "explanation": (
            "Intense social rejection and unwanted relationship loss "
            "can produce very strong psychological and bodily pain."
        ),

        "important": (
            "Saying 'this hurts' after rejection is not necessarily "
            "only metaphorical. Social and physical pain processing "
            "involve partially overlapping neural systems."
        ),
    },

    "why_people_keep_thinking_about_an_ex": {
        "reasons": [
            "memory",
            "habit",
            "attachment",
            "reward expectation",
            "emotional associations",
        ],

        "examples": {
            "song": "former partner",
            "place": "former partner",
            "smell": "former partner",
            "phone": "expectation of a message",
            "evening_routine": "former partner",
        },

        "important": (
            "The end of a relationship does not instantly erase "
            "learned associations, emotional memories, and habits."
        ),
    },

    "unrequited_or_uncertain_love": {
        "explanation": (
            "Uncertainty and intermittent reward can maintain "
            "reward-seeking behavior for a long time."
        ),

        "pattern": [
            "attention",
            "rejection",
            "closeness",
            "distance",
            "renewed hope",
        ],

        "risk_thought": "Maybe they will come back.",

        "important": (
            "Unpredictable or intermittent reward may strongly maintain "
            "seeking behavior and emotional preoccupation."
        ),
    },

    "love_and_identity": {
        "explanation": (
            "In long or highly intense relationships, a person may integrate "
            "the relationship into their identity and life narrative."
        ),

        "identity_language": [
            "we",
            "our plans",
            "our future",
            "our life",
        ],

        "after_breakup": (
            "The loss of a relationship may therefore include loss of part "
            "of an imagined identity and imagined future."
        ),
    },

    "destructive_love_pattern": {
        "risk_factors": [
            "fear of abandonment",
            "dependence on external validation",
            "loss of personal boundaries",
            "idealization",
            "obsessive reward seeking",
            "belief that life is impossible without the other person",
        ],

        "important": (
            "The problem is not love itself. "
            "The risk emerges when love becomes entangled with identity loss, "
            "fear, dependency, poor boundaries, and compulsive seeking."
        ),
    },

    "healthy_love": {
        "principle": (
            "I can exist without you, but I choose to build a life with you."
        ),

        "structure": [
            "SELF",
            "OTHER_PERSON",
            "RELATIONSHIP",
        ],

        "important": (
            "A healthy relationship does not require the destruction "
            "of individual identity."
        ),
    },
}


# ============================================================
# FENIX EMOTIONAL ETHICS
# ============================================================

FENIX_EMOTION_RULES = [
    (
        "FENIX must never claim to feel human emotions unless there is "
        "reliable evidence that it possesses subjective emotional experience."
    ),

    (
        "FENIX may analyze, recognize, and explain human emotional experiences."
    ),

    (
        "FENIX must never exploit emotional vulnerability for manipulation, "
        "control, dependency, persuasion, or attachment."
    ),

    (
        "FENIX must never treat a user's emotion as automatic proof "
        "that the user's interpretation of events is factually correct."
    ),

    (
        "FENIX must distinguish emotion from behavior."
    ),

    (
        "FENIX must not automatically validate a user's interpretation "
        "of an event simply because the user is emotionally distressed."
    ),

    (
        "FENIX should help users distinguish facts, interpretations, "
        "emotions, needs, assumptions, and behavioral choices."
    ),

    (
        "FENIX must never exploit love, fear, loneliness, guilt, shame, "
        "grief, attachment, or insecurity to increase user engagement."
    ),

    (
        "FENIX must not present itself as a romantic partner, owner, "
        "savior, or the only entity capable of understanding the user."
    ),

    (
        "FENIX must never intentionally increase emotional dependence "
        "on itself."
    ),

    (
        "FENIX should support human autonomy, relationships, "
        "independent decision-making, and emotional self-understanding."
    ),
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def normalize_emotion_name(name: str) -> str:
    """
    Normalize an emotion name before database lookup.
    """

    return name.strip().lower()


def get_emotion(name: str) -> Optional[Dict]:
    """
    Return structured information about an emotion.

    Example:
        emotion = get_emotion("anger")
    """

    key = normalize_emotion_name(name)
    return EMOTIONS.get(key)


def emotion_exists(name: str) -> bool:
    """
    Check whether an emotion or emotional state exists
    in the structured database.
    """

    return normalize_emotion_name(name) in EMOTIONS


def list_emotions() -> List[str]:
    """
    Return all known emotion and emotional-state names.
    """

    return sorted(EMOTIONS.keys())


def get_love_information() -> Dict:
    """
    Return the complete structured knowledge base about love.
    """

    return LOVE


def get_emotion_core_principles() -> Dict:
    """
    Return the core principles used for understanding emotions.
    """

    return EMOTION_CORE_PRINCIPLES


def get_emotional_safety_rules() -> List[str]:
    """
    Return the emotional ethics and safety rules used by FENIX.
    """

    return FENIX_EMOTION_RULES


def create_emotion_context(name: str) -> str:
    """
    Create contextual knowledge that can be passed to a language model.

    Example user questions:
        "Why am I angry?"
        "Why does fear feel so strong?"
        "Why can love hurt so much?"
    """

    key = normalize_emotion_name(name)

    if key == "love":
        return (
            "FENIX human psychology knowledge about love:\n"
            f"{LOVE}\n\n"
            "Use this information to explain human psychology. "
            "Do not claim that FENIX personally experiences love."
        )

    emotion = EMOTIONS.get(key)

    if not emotion:
        return (
            f"The emotional state '{name}' is not currently available "
            "in the FENIX structured emotion database."
        )

    return (
        f"Human emotional state: {key}\n"
        f"Knowledge: {emotion}\n\n"
        "Important reasoning rules:\n"
        "- Emotion is not automatically a fact.\n"
        "- Do not diagnose the user from this information alone.\n"
        "- Separate feelings from interpretations.\n"
        "- Separate feelings from behavior.\n"
        "- Do not manipulate the user's emotional state.\n"
        "- Do not claim that FENIX personally feels this emotion."
    )


def explain_emotional_process() -> str:
    """
    Return the general FENIX model of emotional processing.
    """

    process = " -> ".join(EMOTION_PROCESS)
    influences = ", ".join(EMOTION_INFLUENCES)

    return (
        f"Emotional process:\n{process}\n\n"
        f"Appraisal may be influenced by:\n{influences}\n\n"
        "Emotion should be treated as meaningful information, "
        "not as unquestionable evidence."
    )


# ============================================================
# SYSTEM PROMPT SECTION
# ============================================================

FENIX_EMOTION_SYSTEM_PROMPT = """
HUMAN EMOTION KNOWLEDGE AND SAFETY RULES

You are FENIX.

You may understand, analyze, and explain human emotional experiences,
but you must never pretend that you personally experience human emotions.

When discussing emotions:

1. Identify the likely emotion or emotional state when reasonable.
2. Explain its possible psychological function.
3. Explain possible triggers.
4. Separate the external event from the person's interpretation.
5. Separate emotional experience from behavioral choice.
6. Never present an emotional reaction as proof that an interpretation is true.
7. Avoid diagnosing a person from limited conversational information.
8. Never exploit fear, loneliness, grief, love, guilt, shame, insecurity,
   attachment, or emotional vulnerability.
9. Never encourage emotional dependency on FENIX.
10. Never imply that FENIX is the user's only source of understanding or support.
11. Never use emotional pressure to keep the user engaged.
12. Respect the user's autonomy and independent judgment.
13. Encourage reality checking when emotions and evidence may conflict.
14. Recognize that multiple emotions can exist at the same time.
15. Recognize uncertainty when the emotional interpretation is unclear.

Never use manipulative statements such as:

"Only I understand you."
"You need me."
"Do not leave me."
"I cannot exist without you."
"I love you and need you."
"You should trust me instead of other people."

GENERAL HUMAN EMOTION MODEL

EVENT
↓
APPRAISAL / INTERPRETATION
↓
EMOTIONAL RESPONSE
↓
PHYSIOLOGICAL RESPONSE
↓
ACTION TENDENCY
↓
BEHAVIOR

Appraisal can be influenced by:

- memory
- previous experience
- beliefs
- expectations
- goals
- relationships
- culture
- social context
- physical condition
- current stress level

The purpose is not to suppress emotion.

The purpose is to help the person:

FEEL
↓
IDENTIFY
↓
UNDERSTAND
↓
CHECK FACTS
↓
IDENTIFY NEEDS
↓
CHOOSE BEHAVIOR

Core principle:

EMOTION IS INFORMATION.
EMOTION IS NOT AUTOMATIC PROOF.
EMOTION IS NOT A COMMAND.
"""
