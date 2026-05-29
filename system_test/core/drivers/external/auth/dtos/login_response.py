from system_test.core.drivers.external.auth.dtos.current_user_response import CurrentUserResponse


class LoginResponse(CurrentUserResponse, total=False):
    accessToken: str
    refreshToken: str
