

from dataclasses import dataclass


# ---------------------------------------------------------
# FENIX TOOL PERMISSIONS
# ---------------------------------------------------------


@dataclass(frozen=True)
class ToolRequest:
    """
    Describes an action that Fenix wants to perform.
    """

    tool_name: str
    requires_admin: bool = False
    requires_confirmation: bool = False
    confirmed: bool = False


@dataclass(frozen=True)
class PermissionResult:
    """
    Result of a permission check.
    """

    allowed: bool
    reason: str = ""


def check_permission(
    request: ToolRequest,
    is_admin: bool = False
) -> PermissionResult:
    """
    Decide whether Fenix is allowed to execute a tool.
    """

    if not request.tool_name.strip():
        return PermissionResult(
            allowed=False,
            reason="Tool name cannot be empty."
        )

    if request.requires_admin and not is_admin:
        return PermissionResult(
            allowed=False,
            reason="Administrator permission is required."
        )

    if (
        request.requires_confirmation
        and not request.confirmed
    ):
        return PermissionResult(
            allowed=False,
            reason="User confirmation is required."
        )

    return PermissionResult(
        allowed=True
    )
