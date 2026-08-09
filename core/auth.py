

"""
Fenix Authentication Module

Responsible for securely verifying authentication secrets.

Important:
- No secrets are stored in this file.
- Secrets must come from a secure environment such as Streamlit Secrets.
- Authentication does not override Fenix safety or ethics rules.
"""

from __future__ import annotations

import hmac
import hashlib


def verify_secret(
    provided_secret: str,
    stored_secret: str
) -> bool:
    """
    Safely verify a provided secret against the stored secret.

    Uses constant-time comparison to reduce the risk of
    timing-based attacks.

    Args:
        provided_secret: Secret supplied by the user.
        stored_secret: Secret loaded from secure configuration.

    Returns:
        True if the secrets match.
        False otherwise.
    """

    if not isinstance(provided_secret, str):
        return False

    if not isinstance(stored_secret, str):
        return False

    if not provided_secret or not stored_secret:
        return False

    provided_hash = hashlib.sha256(
        provided_secret.encode("utf-8")
    ).digest()

    stored_hash = hashlib.sha256(
        stored_secret.encode("utf-8")
    ).digest()

    return hmac.compare_digest(
        provided_hash,
        stored_hash
    )


def is_authenticated(
    provided_secret: str,
    stored_secret: str
) -> bool:
    """
    Clear public interface for authentication checks.

    This function is intentionally simple so the authentication
    mechanism can be extended later without changing the rest
    of the application.
    """

    return verify_secret(
        provided_secret=provided_secret,
        stored_secret=stored_secret
    )
