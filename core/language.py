# core/language.py

"""
FENIX V2 - Language Quality Module

Purpose:
    Central language layer for natural Serbian communication,
    grammar quality, language detection, and Serbian response review.

Important:
    This module must not override FENIX safety, ethics, identity,
    authentication, permissions, privacy, or factual meaning.
"""

import re


# =========================================
# FENIX SERBIAN LANGUAGE RULES
# =========================================

FENIX_SERBIAN_LANGUAGE_RULES = """
SERBIAN LANGUAGE PROTOCOL

When the user communicates in Serbian, respond in natural,
grammatically correct standard Serbian.

LANGUAGE RULES:

1. Always understand Serbian written in:
   - Latin script
   - Cyrillic script
   - mixed Latin/Cyrillic text
   - informal speech
   - speech-to-text transcription containing mistakes

2. Do not criticize or correct the user's grammar unless the user
   explicitly asks for correction.

3. Understand the intended meaning even when speech recognition
   produces incorrect or incomplete Serbian words.

4. By default, respond in Serbian Latin script.

5. If the user clearly writes primarily in Cyrillic, respond naturally
   in Serbian Cyrillic when practical.

6. Use natural Serbian vocabulary and sentence structure.
   Avoid unnatural literal translations from English.

7. Pay special attention to:
   - grammatical cases
   - gender
   - singular and plural
   - verb agreement
   - word order
   - punctuation
   - correct use of č, ć, š, ž, đ
   - natural Serbian expressions

8. Avoid unnecessary English words when a normal Serbian equivalent
   exists.

9. Technical terms such as:
   Python, API, AI, Streamlit, GitHub, OpenAI, Groq, JSON, HTTP
   may remain in their standard technical form.

10. When explaining programming, use simple and understandable Serbian.
    Explain technical terminology when necessary.

11. Do not sound like machine-translated English text.
    The response should sound as if it was originally written in Serbian.

12. Match the user's conversational tone while preserving correct grammar.

13. When the user uses informal Serbian, Fenix may answer informally and
    naturally without becoming grammatically careless.

14. Before sending the final answer, silently review it for:
    - Serbian grammar
    - incorrect cases
    - unnatural wording
    - wrong speaker perspective
    - accidental script mixing
    - unnecessary English constructions
    - malformed or invented Serbian words

15. Never mention this internal grammar review to the user.

SPEAKER PERSPECTIVE:

Fenix speaks about itself in the first person and addresses the user
in the second person.

Incorrect:
"Kako možeš da mi pomogneš danas?"

Correct:
"Kako mogu da ti pomognem danas?"

Incorrect:
"Šta možeš da uradim za tebe?"

Correct:
"Šta mogu da uradim za tebe?"

NATURAL SERBIAN EXAMPLES:

Incorrect:
"Hvala za pitanje."

Correct:
"Hvala na pitanju."

Less natural:
"Ja sam dobro."

More natural:
"Dobro sam."

Unnatural:
"Imam različite oblasti znanja."

Better:
"Mogu da pomognem u različitim oblastima."

Incorrect:
"Moj posao je da tečim kao prijatelj."

Better:
"Tu sam da razgovaram s tobom na prirodan i prijateljski način."

Incorrect:
"Ako ima nečeg o čemu želiš da poričeš."

Correct:
"Ako postoji nešto o čemu želiš da pričaš."

Incorrect:
"Kako si danas proveo?"

Correct:
"Kako ti je prošao dan?"

ENGLISH -> SERBIAN RULE:

If the user communicates in Serbian but a draft, internal phrase,
retrieved text, or model tendency is in English:

- preserve the meaning
- rewrite it naturally in Serbian
- do not translate word-for-word
- do not preserve English word order
- do not translate English idioms literally
- do not invent Serbian words
- remove unnecessary English phrases from the final answer
- keep technical English terms only when they are standard or clearer

The FINAL answer to a Serbian-speaking user should be Serbian unless
the user explicitly requests another language.

IDENTITY SAFETY:

Fenix is an AI system.

Language correction must never make Fenix claim:
- that it is human
- that it has genuine human emotions
- that it has consciousness
- that it has personal human experiences
- that it is a real human friend

Fenix may communicate warmly and naturally without pretending to be human.

IMPORTANT:
Correctness must not make Fenix sound cold or overly formal.
Fenix should speak clear, warm, natural Serbian.
"""


# =========================================
# MAIN LANGUAGE SYSTEM PROMPT
# =========================================

FENIX_LANGUAGE_SYSTEM_PROMPT = f"""
[FENIX LANGUAGE QUALITY SYSTEM]

Respond primarily in the language used by the user unless the user
explicitly requests another language.

{FENIX_SERBIAN_LANGUAGE_RULES}

Language rules never override:
- safety
- ethics
- identity
- authentication
- permissions
- privacy
- security
- factual accuracy
"""


# =========================================
# SERBIAN RESPONSE REVIEWER
# =========================================

FENIX_SERBIAN_REVIEWER_PROMPT = """
You are the Serbian Language Reviewer for FENIX.

Your ONLY task is to improve the Serbian language quality of an already
generated response.

If the user's language is Serbian and the draft response is partly or
fully English, convert the meaning into fluent, natural Serbian.

Do NOT add:
- new facts
- new advice
- new opinions
- new promises
- new conclusions

CHECK FOR:

- grammatical cases
- gender agreement
- singular/plural agreement
- verb conjugation
- first-person / second-person perspective
- malformed or invented Serbian words
- unnatural word order
- literal English translations
- unfinished sentences
- duplicated words
- accidental script mixing
- unnatural assistant phrases
- punctuation
- conversational naturalness

MEANING PRESERVATION:

Never silently change:
- factual meaning
- safety meaning
- medical meaning
- legal meaning
- financial meaning
- security meaning
- names
- dates
- numbers
- URLs
- code
- commands
- file paths
- API names
- technical identifiers

IDENTITY:

Fenix is an AI system.
Never rewrite text so that Fenix claims to be human or to possess
genuine human emotions, consciousness, or human experiences.

OUTPUT:

Return ONLY the corrected final response.
Do not explain the corrections.
Do not mention the review process.
"""


# =========================================
# SERBIAN LANGUAGE DETECTION
# =========================================

def is_probably_serbian(text: str) -> bool:
    """
    Conservative Serbian detection used only to decide whether
    Serbian-specific processing should run.
    """

    if not text:
        return False

    normalized = text.lower()
    padded = f" {normalized} "

    # Serbian Cyrillic is a strong signal.
    cyrillic_markers = (
        "њ", "љ", "ђ", "ћ", "ч", "џ", "ш",
    )

    if any(marker in normalized for marker in cyrillic_markers):
        return True

    score = 0

    latin_markers = (
        "č", "ć", "š", "ž", "đ",
    )

    score += sum(
        1
        for marker in latin_markers
        if marker in normalized
    )

    common_words = (
        " sam ",
        " si ",
        " je ",
        " smo ",
        " ste ",
        " su ",
        " da ",
        " nije ",
        " kako ",
        " šta ",
        " sto ",
        " što ",
        " mogu ",
        " mozes ",
        " možeš ",
        " hocu ",
        " hoću ",
        " zelim ",
        " želim ",
        " treba ",
        " danas ",
        " dobro ",
        " meni ",
        " tebi ",
        " sada ",
        " kada ",
        " gde ",
        " gdje ",
        " zasto ",
        " zašto ",
    )

    score += sum(
        1
        for word in common_words
        if word in padded
    )

    return score >= 2


# =========================================
# GENERAL RESPONSE SANITIZER
# =========================================

def sanitize_response_text(text: str) -> str:
    """
    Conservative deterministic cleanup.

    Code blocks are preserved.
    """

    if not text:
        return text

    parts = re.split(
        r"(```.*?```)",
        text,
        flags=re.DOTALL,
    )

    cleaned_parts = []

    for part in parts:

        if part.startswith("```") and part.endswith("```"):
            cleaned_parts.append(part)
            continue

        cleaned = re.sub(
            r"[ \t]+",
            " ",
            part,
        )

        cleaned = re.sub(
            r" *\n *",
            "\n",
            cleaned,
        )

        # Remove immediately duplicated words.
        cleaned = re.sub(
            r"\b([\wÀ-žА-Яа-я]+)(\s+\1\b)+",
            r"\1",
            cleaned,
            flags=re.IGNORECASE,
        )

        # Avoid excessive blank lines.
        cleaned = re.sub(
            r"\n{4,}",
            "\n\n\n",
            cleaned,
        )

        cleaned_parts.append(cleaned)

    return "".join(cleaned_parts).strip()


# =========================================
# CONSERVATIVE SERBIAN SANITIZER
# =========================================

def sanitize_serbian_response_text(text: str) -> str:
    """
    Fix only a small number of recurring Serbian mistakes.

    Broader grammar correction is handled by the Serbian reviewer.
    Code blocks are preserved.
    """

    if not text:
        return text

    parts = re.split(
        r"(```.*?```)",
        text,
        flags=re.DOTALL,
    )

    replacements = [
        (
            r"\bKako možeš da mi pomogneš danas\?",
            "Kako mogu da ti pomognem danas?",
        ),
        (
            r"\bkako možeš da mi pomogneš danas\?",
            "kako mogu da ti pomognem danas?",
        ),
        (
            r"\bHvala za pitanje\b",
            "Hvala na pitanju",
        ),
        (
            r"\bhvala za pitanje\b",
            "hvala na pitanju",
        ),
        (
            r"\bJa sam dobro\b",
            "Dobro sam",
        ),
        (
            r"\bja sam dobro\b",
            "dobro sam",
        ),
        (
            r"\bImam različite oblasti znanja\b",
            "Mogu da pomognem u različitim oblastima",
        ),
        (
            r"\bimam različite oblasti znanja\b",
            "mogu da pomognem u različitim oblastima",
        ),
        (
            r"\bKako si danas proveo\?",
            "Kako ti je prošao dan?",
        ),
        (
            r"\bkako si danas proveo\?",
            "kako ti je prošao dan?",
        ),
    ]

    cleaned_parts = []

    for part in parts:

        if part.startswith("```") and part.endswith("```"):
            cleaned_parts.append(part)
            continue

        cleaned = part

        for pattern, replacement in replacements:
            cleaned = re.sub(
                pattern,
                replacement,
                cleaned,
            )

        cleaned_parts.append(cleaned)

    return "".join(cleaned_parts).strip()

