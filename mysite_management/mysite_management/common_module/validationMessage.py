import enum 


class Messages(enum.Enum):
    """Enum for messages."""
    SUCCESS = "Success"
    FAILURE = "Failure"
    INVALID_INPUT = "Invalid input"
    INVALID_PASSWORD = "Invalid password"
    USER_ALREADY_EXISTS = "User already exists"
    USER_NOT_FOUND = "User not found"
    LOGIN_USER = "Login user"
    YOU_ARE_NOW_LOGGED_IN = "you are now logged in"
    LOGOUT_USER = "Logout user"
    INVALID_CREDENTIALS = "Invalid credentials"
    USER_ALREADY_LOGGED_IN = "User already logged in"
    USER_NOT_LOGGED_IN = "User not logged in"
    INVALID_TOKEN = "Invalid token"
    TOKEN_EXPIRED = "Token expired"
    USER_NOT_VERIFIED = "User not verified"
    USER_ALREADY_VERIFIED = "User already verified"
    USER_IS_REGISTER = "User is register successfully"
    USER_IS_NOT_REGISTER = "User is not register"
    USER_IS_VERIFIED = "User is verified successfully"
    USER_IS_UPDATED_SUCCESSFULLY = "User is updated successfully"
    USER_IS_DELETED_SUCCESSFULLY = "User is deleted successfully"
