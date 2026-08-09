import hmac
from typing import Optional


def verify_secret(
    provided_secret: str,
    stored_secret: Optional[str]
) -> bool:
    """
    Safely compare an administrator secret.

    Returns False if either value is missing.
    """

    if not provided_secret or not stored_secret:
        return False

    return hmac.compare_digest(
        provided_secret,
        stored_secret
    )
