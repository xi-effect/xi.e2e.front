import os

from dotenv import load_dotenv

load_dotenv()

try:

    LOGIN = os.environ["LOGIN"]
    PASSWORD = os.environ["PASSWORD"]
    USER_PASSWORD = os.environ["DEFAULT_USER_PASSWORD"]
except KeyError as e:
    raise ValueError(f"Отсутствует необходимая переменная окружения: {e}") from None
