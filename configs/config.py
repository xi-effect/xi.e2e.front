from dataclasses import dataclass

from _secrets import LOGIN, PASSWORD, USER_PASSWORD

base_url = "https://xieffect.ru/"

app_base_url = "https://app.xieffect.ru"
signin_page = f"{app_base_url}/signin"
signup_page = f"{app_base_url}/signup"
recovery_page = f"{app_base_url}/reset-password"


@dataclass
class Credentials:
    test_login: str = LOGIN
    test_password: str = PASSWORD
    user_password: str = USER_PASSWORD
