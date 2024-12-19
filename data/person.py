from dataclasses import dataclass, field

from faker import Faker

from configs.config import Credentials

faker_en = Faker()


@dataclass
class Person:
    """
    Represents a person with their basic information.

    Attributes:
        display_name (str): Full name of the person.
        username (str): Automatically generated username based on the display name.
        community_name (str): Name of the person's community.
        email (str): Email address of the person.
        password (str): Password associated with the account.
    """

    display_name: str
    username: str = field(init=False)
    community_name: str = field(init=False)
    email: str
    password: str

    def __post_init__(self):
        self.username = self.display_name.replace(" ", "_").lower()
        self.community_name = self.display_name + " community"


class PersonCreateInfo:

    @staticmethod
    def user_create_info() -> Person:
        return Person(
            display_name=faker_en.name(),
            email=faker_en.email(),
            password=Credentials().user_password,
        )
