from typing import NamedTuple


class AuthenticationResponse(NamedTuple):
    error: bool = False
    error_message: str = None
    is_authenticated: bool = False
    session_id: str = None
    expired_license: bool = None
    invalid_hwid: bool = None
    invalid_credentials: bool = None
    account_type: str = None


class RegistrationResponse(NamedTuple):
    error: bool = False
    error_message: str = None
    registration_enabled: bool = None
    invalid_key: bool = None
    success: bool = False
    max_users: bool = None


class HWIDResetResponse(NamedTuple):
    error: bool = False
    error_message: str = None
    hwid_resets: bool = None
    invalid_key: bool = None
    invalid_credentials: bool = None
    success: bool = None
    reset_today: bool = None


class LicenseGenerationResponse(NamedTuple):
    error: bool = False
    error_message: str = None
    license: str = None
    success: bool = None


class HWIDKeyGenerationResponse(NamedTuple):
    error: bool = False
    error_message: str = None
    key: str = None
    success: bool = None
