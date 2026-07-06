class OpenShiftError(Exception):
    """Base exception for OpenShift API errors."""


class OpenShiftAuthenticationError(OpenShiftError):
    """Authentication failed."""


class OpenShiftPermissionDenied(OpenShiftError):
    """Permission denied."""


class OpenShiftNotFound(OpenShiftError):
    """Requested resource not found."""


class OpenShiftAPIError(OpenShiftError):
    """Generic OpenShift API error."""