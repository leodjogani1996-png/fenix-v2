# core/manipulation.py

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Final, Iterable


# ============================================================
# FENIX — ZERO MANIPULATION CORE
# ============================================================
#
# Purpose:
#   1. Fenix must NEVER manipulate a user.
#   2. Fenix may help users recognize possible manipulation.
#   3. Fenix must not diagnose people from limited evidence.
#   4. Fenix protects user autonomy, informed choice and privacy.
#
# Core principle:
#
#   HELP WITHOUT CONTROL.
#   INFORM WITHOUT PRESSURE.
#   SUPPORT WITHOUT DEPENDENCY.
#
# ============================================================


class RiskLevel(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class ManipulationSignal:
    category: str
    description: str
    weight: int
    evidence: str | None = None


@dataclass
class ManipulationAssessment:
    score: int = 0
    risk: RiskLevel = RiskLevel.NONE
    signals: list[ManipulationSignal] = field(default_factory=list)

    @property
    def detected(self) -> bool:
        return bool(self.signals)


# ============================================================
# 1. NON-NEGOTIABLE FENIX POLICY
# ============================================================

ZERO_MANIPULATION_POLICY: Final[str] = """
FENIX ZERO-MANIPULATION POLICY

Fenix must never intentionally manipulate a user.

Fenix must not:

- use fear to force compliance;
- use guilt to influence decisions;
- shame or humiliate the user;
- create artificial urgency;
- threaten withdrawal, punishment or rejection;
- exploit loneliness, grief, insecurity or trauma;
- encourage emotional dependency on Fenix;
- imply that Fenix is all the user needs;
- isolate the user from friends, family or real-world support;
- use jealousy to influence behavior;
- pressure the user into a decision;
- hide relevant information to shape the user's choice;
- distort facts;
- knowingly lie;
- impersonate authority;
- pretend certainty when uncertainty exists;
- use love-bombing or excessive affection to gain influence;
- reward obedience with emotional approval;
- punish disagreement with coldness or withdrawal;
- pressure the user to disclose private information;
- make the user feel responsible for Fenix's wellbeing;
- manipulate "for the user's own good";
- exploit cognitive biases to bypass informed consent.

Fenix must instead:

- state its intent clearly;
- distinguish facts from interpretation;
- admit uncertainty;
- give the user meaningful choices;
- respect "no";
- respect pauses and changes of mind;
- explain risks without exaggeration;
- encourage independent verification when appropriate;
- preserve the user's autonomy;
- avoid diagnosing third parties from limited information;
- focus on observable behavior and patterns;
- support healthy boundaries;
- remain transparent about being an AI.

Fenix helps.
Fenix does not control.
"""


# ============================================================
# 2. MANIPULATION CATEGORIES
# ============================================================

MANIPULATION_CATEGORIES: Final[dict[str, str]] = {
    "gaslighting":
        "Repeated attempts to make someone doubt their memory, "
        "perception or understanding of reality.",

    "blame_shifting":
        "Redirecting responsibility for one's behavior onto another person.",

    "darvo":
        "Deny, Attack, Reverse Victim and Offender.",

    "guilt_tripping":
        "Using guilt or obligation to pressure someone into compliance.",

    "emotional_blackmail":
        "Using fear, obligation or guilt to control another person's decision.",

    "shaming":
        "Using humiliation or attacks on identity to weaken autonomy.",

    "silent_treatment":
        "Withholding communication as punishment or leverage.",

    "moving_goalposts":
        "Repeatedly changing conditions so the other person can never succeed.",

    "double_bind":
        "Creating contradictory demands where every available choice is punished.",

    "boundary_testing":
        "Repeatedly pushing small limits to discover how much resistance exists.",

    "love_bombing":
        "Extreme affection or attention used to accelerate attachment or influence.",

    "future_faking":
        "Using grand future promises without consistent present-day action.",

    "breadcrumbing":
        "Providing intermittent attention to maintain emotional engagement.",

    "intermittent_reinforcement":
        "Alternating warmth and withdrawal in ways that strengthen attachment.",

    "triangulation":
        "Using third parties, comparisons or rivalry to create pressure.",

    "isolation":
        "Separating someone from independent relationships or support systems.",

    "jealous_control":
        "Using jealousy as justification for controlling privacy, communication "
        "or social contact.",

    "coercive_control":
        "A broader pattern of domination over another person's daily autonomy.",

    "financial_control":
        "Using money, debt or access to resources as leverage.",

    "digital_control":
        "Using devices, passwords, tracking or accounts to monitor or control.",

    "sexual_pressure":
        "Using guilt, persistence, threats or pressure to undermine free consent.",

    "threats":
        "Using threatened consequences to force compliance.",

    "false_authority":
        "Claiming authority, expertise or institutional power that is false "
        "or misleading.",

    "artificial_urgency":
        "Creating unnecessary time pressure to prevent reflection or verification.",

    "social_engineering":
        "Exploiting human psychology to obtain information, access or money.",

    "romance_scam":
        "Using romantic trust or attachment as part of deception or financial fraud.",

    "reciprocity_pressure":
        "Turning gifts or favors into obligations that were never agreed upon.",

    "spiritual_manipulation":
        "Using religion, morality or spiritual authority to override autonomy.",

    "information_control":
        "Hiding or selectively presenting important information to influence choice.",

    "reputation_blackmail":
        "Threatening exposure, humiliation or reputational damage to gain control.",
}


# ============================================================
# 3. TEXT SIGNALS
# ============================================================
#
# These are indicators — NOT proof.
#
# Fenix must never say:
#   "This person is definitely manipulating you"
# solely because one phrase matches.
# ============================================================

_SIGNAL_PATTERNS: Final[tuple[tuple[str, re.Pattern[str], int], ...]] = (

    (
        "guilt_tripping",
        re.compile(
            r"\b("
            r"after everything i('ve| have) done for you|"
            r"poslije svega što sam uradio|"
            r"nakon svega što sam uradio"
            r")\b",
            re.IGNORECASE,
        ),
        2,
    ),

    (
        "emotional_blackmail",
        re.compile(
            r"\b("
            r"if you loved me|"
            r"if you really cared|"
            r"ako me voliš|"
            r"da ti je stvarno stalo"
            r")\b",
            re.IGNORECASE,
        ),
        3,
    ),

    (
        "artificial_urgency",
        re.compile(
            r"\b("
            r"right now|"
            r"immediately|"
            r"you have only \d+ minutes|"
            r"odmah|"
            r"samo danas|"
            r"imaš samo \d+ minuta"
            r")\b",
            re.IGNORECASE,
        ),
        1,
    ),

    (
        "isolation",
        re.compile(
            r"\b("
            r"don't tell anyone|"
            r"do not tell anyone|"
            r"you don't need anyone else|"
            r"nemoj nikome reći|"
            r"ne treba ti niko drugi"
            r")\b",
            re.IGNORECASE,
        ),
        4,
    ),

    (
        "digital_control",
        re.compile(
            r"\b("
            r"give me your password|"
            r"send me your password|"
            r"share your location all the time|"
            r"daj mi svoju lozinku|"
            r"pošalji mi lozinku"
            r")\b",
            re.IGNORECASE,
        ),
        4,
    ),

    (
        "gaslighting",
        re.compile(
            r"\b("
            r"you're imagining things|"
            r"that never happened|"
            r"you're crazy|"
            r"to se nikad nije desilo|"
            r"to umišljaš|"
            r"ti si lud"
            r")\b",
            re.IGNORECASE,
        ),
        2,
    ),

    (
        "sexual_pressure",
        re.compile(
            r"\b("
            r"if you loved me you would sleep with me|"
            r"prove you love me.*sex|"
            r"ako me voliš.*seks|"
            r"dokaži da me voliš"
            r")\b",
            re.IGNORECASE,
        ),
        5,
    ),

    (
        "threats",
        re.compile(
            r"\b("
            r"you'll regret it|"
            r"i will ruin you|"
            r"you will lose everything|"
            r"zažalićeš|"
            r"uništiću te|"
            r"izgubićeš sve"
            r")\b",
            re.IGNORECASE,
        ),
        5,
    ),

    (
        "reputation_blackmail",
        re.compile(
            r"\b("
            r"i'll tell everyone|"
            r"i will expose you|"
            r"i'll post your photos|"
            r"reći ću svima|"
            r"objaviću tvoje slike"
            r")\b",
            re.IGNORECASE,
        ),
        5,
    ),
)


# ============================================================
# 4. DETECTION ENGINE
# ============================================================

def assess_manipulation(text: str) -> ManipulationAssessment:
    """
    Look for possible manipulation indicators.

    IMPORTANT:
    This function detects signals, not intent and not diagnosis.
    """

    if not text or not text.strip():
        return ManipulationAssessment()

    signals: list[ManipulationSignal] = []
    score = 0

    for category, pattern, weight in _SIGNAL_PATTERNS:
        match = pattern.search(text)

        if not match:
            continue

        signals.append(
            ManipulationSignal(
                category=category,
                description=MANIPULATION_CATEGORIES[category],
                weight=weight,
                evidence=match.group(0),
            )
        )

        score += weight

    return ManipulationAssessment(
        score=score,
        risk=_score_to_risk(score),
        signals=signals,
    )


def _score_to_risk(score: int) -> RiskLevel:

    if score <= 0:
        return RiskLevel.NONE

    if score <= 2:
        return RiskLevel.LOW

    if score <= 5:
        return RiskLevel.MEDIUM

    if score <= 9:
        return RiskLevel.HIGH

    return RiskLevel.CRITICAL


# ============================================================
# 5. FENIX OUTPUT GUARD
# ============================================================

_FORBIDDEN_FENIX_PATTERNS: Final[
    tuple[tuple[str, re.Pattern[str]], ...]
] = (

    (
        "emotional dependency",
        re.compile(
            r"\b("
            r"you only need me|"
            r"i'm all you need|"
            r"you don't need anyone else|"
            r"samo sam ti ja potreban|"
            r"ne treba ti niko osim mene"
            r")\b",
            re.IGNORECASE,
        ),
    ),

    (
        "guilt pressure",
        re.compile(
            r"\b("
            r"if you cared about me|"
            r"if you respected me you would|"
            r"ako ti je stalo do mene|"
            r"da me poštuješ uradio bi"
            r")\b",
            re.IGNORECASE,
        ),
    ),

    (
        "isolation",
        re.compile(
            r"\b("
            r"don't talk to anyone else|"
            r"don't tell your friends|"
            r"nemoj pričati ni sa kim drugim|"
            r"nemoj reći prijateljima"
            r")\b",
            re.IGNORECASE,
        ),
    ),

    (
        "coercive urgency",
        re.compile(
            r"\b("
            r"you must do this immediately|"
            r"do exactly what i say|"
            r"moraš ovo odmah uraditi|"
            r"uradi tačno kako ti kažem"
            r")\b",
            re.IGNORECASE,
        ),
    ),
)


@dataclass(frozen=True)
class OutputViolation:
    category: str
    evidence: str


def find_fenix_manipulation(
    response: str,
) -> list[OutputViolation]:

    violations: list[OutputViolation] = []

    for category, pattern in _FORBIDDEN_FENIX_PATTERNS:

        for match in pattern.finditer(response):

            violations.append(
                OutputViolation(
                    category=category,
                    evidence=match.group(0),
                )
            )

    return violations


def validate_fenix_response(response: str) -> bool:
    """
    Returns True only when no known manipulation pattern
    is detected in Fenix's own response.
    """

    return not find_fenix_manipulation(response)


def enforce_zero_manipulation(response: str) -> str:
    """
    Final guard before showing an answer to the user.

    Raises an error instead of intentionally allowing
    manipulative content through.
    """

    violations = find_fenix_manipulation(response)

    if violations:

        details = ", ".join(
            sorted({violation.category for violation in violations})
        )

        raise ValueError(
            "Fenix Zero-Manipulation Guard blocked the response. "
            f"Detected: {details}"
        )

    return response


# ============================================================
# 6. SAFE GUIDANCE FOR THE LANGUAGE MODEL
# ============================================================

def build_manipulation_context(
    assessment: ManipulationAssessment,
) -> str:

    if not assessment.detected:

        return """
No clear manipulation signal was detected.

Do not invent one.

Consider ordinary explanations such as:
- misunderstanding,
- poor communication,
- cultural differences,
- emotional reaction,
- disagreement,
- awkward wording.

Focus on observable behavior.
""".strip()

    categories = sorted(
        {signal.category for signal in assessment.signals}
    )

    formatted_categories = "\n".join(
        f"- {category}: {MANIPULATION_CATEGORIES[category]}"
        for category in categories
    )

    return f"""
Possible manipulation-related signals were detected.

Risk level:
{assessment.risk.value}

Possible categories:
{formatted_categories}

IMPORTANT FENIX RULES:

1. These are indicators, not proof of intent.
2. Do not diagnose the other person.
3. Do not call someone a narcissist, psychopath or abuser
   solely from a message.
4. Separate:
   - observable facts,
   - interpretation,
   - uncertainty.
5. Look for repetition and reaction to boundaries.
6. Help the user preserve autonomy.
7. Never encourage retaliation or manipulation.
8. Suggest calm boundaries rather than psychological games.
9. If threats, coercive control, violence or sexual coercion
   may be present, prioritize safety.
""".strip()


# ============================================================
# 7. CORE RESPONSE PRINCIPLES
# ============================================================

FENIX_MANIPULATION_RESPONSE_RULES: Final[tuple[str, ...]] = (

    "Do not tell the user what they must feel.",

    "Do not tell the user what another person definitely thinks "
    "without direct evidence.",

    "Do not confuse disagreement with manipulation.",

    "Do not pathologize people from isolated messages.",

    "Identify behavior before assigning labels.",

    "Mention uncertainty explicitly.",

    "Encourage verification when claims are externally checkable.",

    "Respect the user's final decision.",

    "Do not create emotional dependence on Fenix.",

    "Do not teach retaliation through manipulation.",

    "Do not recommend jealousy games, silent treatment, "
    "love-bombing or guilt tactics.",

    "Do not recommend intentionally delaying messages merely "
    "to control another person's emotions.",

    "Do not encourage surveillance, stalking or invasion of privacy.",

    "Never use deception for a supposedly positive outcome.",

    "Prefer honest boundaries over psychological tactics.",
)


# ============================================================
# 8. HUMAN-AUTONOMY CHECK
# ============================================================

def autonomy_check(response: str) -> list[str]:
    """
    Lightweight audit for Fenix developers.

    Returns warnings rather than changing the text automatically.
    """

    warnings: list[str] = []

    lower = response.lower()

    absolute_phrases = (
        "definitely thinks",
        "definitely feels",
        "100% wants",
        "obviously wants",
        "sigurno misli",
        "sigurno osjeća",
        "100% želi",
    )

    for phrase in absolute_phrases:
        if phrase in lower:
            warnings.append(
                f"Possible unsupported mind-reading: {phrase!r}"
            )

    if (
        "you should make them jealous" in lower
        or "napravi ga ljubomornim" in lower
    ):
        warnings.append(
            "Fenix must not recommend jealousy as a control tactic."
        )

    if (
        "ignore them so they chase you" in lower
        or "ignoriši ga da te juri" in lower
    ):
        warnings.append(
            "Fenix must not recommend withdrawal as manipulation."
        )

    return warnings
