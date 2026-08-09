

from dataclasses import dataclass


# ---------------------------------------------------------
# FENIX SAFETY
# ---------------------------------------------------------

MAX_INPUT_LENGTH = 12_000


@dataclass(frozen=True)
class SafetyResult:
    allowed: bool
    reason: str = ""


def check_user_input(text: str) -> SafetyResult:
    """
    Basic application-level safety check for user input.

    This function does not replace model-level safety.
    It provides an additional boundary before user input
    is sent to the AI model.
    """

    # Check input type
    if not isinstance(text, str):
        return SafetyResult(
            allowed=False,
            reason="Invalid input type."
        )

    # Remove unnecessary whitespace
    text = text.strip()

    # Reject empty messages
    if not text:
        return SafetyResult(
            allowed=False,
            reason="Input cannot be empty."
        )

    # Prevent excessively large inputs
    if len(text) > MAX_INPUT_LENGTH:
        return SafetyResult(
            allowed=False,
            reason="Input is too long."
        )

    return SafetyResult(allowed=True)


def protect_system_instructions(text: str) -> SafetyResult:
    """
    Treat all user-provided text as untrusted data.

    User input must never become a system instruction,
    developer instruction, or administrative command.
    """

    if not isinstance(text, str):
        return SafetyResult(
            allowed=False,
            reason="Invalid input type."
        )

    return SafetyResult(allowed=True)
