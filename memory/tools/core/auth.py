

import hmac


# =========================================================
# FENIX AUTHENTICATION
# =========================================================

def verify_secret(
    provided_secret: str,
    stored_secret: str
) -> bool:
    """
    Safely compare an authentication secret.

    Returns True only when both secrets match.
    """

    if not provided_secret or not stored_secret:
        return False

    return hmac.compare_digest(
        provided_secret,
        stored_secret
    )


def is_authenticated(
    provided_secret: str,
    stored_secret: str
) -> bool:
    """
    Determine whether authentication was successful.
    """

    return verify_secret(
        provided_secret,
        stored_secret
    )
