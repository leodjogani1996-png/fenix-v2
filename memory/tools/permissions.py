from dataclasses import dataclass


@dataclass(frozen=True)
class ToolRequest:
    """
    Describes a request to use a Fenix tool.
    """

    tool_name: str
    requires_admin: bool = False


@dataclass(frozen=True)
class PermissionResult:
    """
    Result of a permission check.
    """

    allowed: bool
    reason: str = ""


def check_permission(
    request: ToolRequest,
    is_admin: bool
) -> PermissionResult:
    """
    Check whether the current user may execute a tool.
    """

    if request.requires_admin and not is_admin:
        return PermissionResult(
            allowed=False,
            reason="Administrator authentication is required."
        )

    return PermissionResult(
        allowed=True,
        reason="Permission granted."
    )
