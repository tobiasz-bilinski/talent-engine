import pytest
from src.config.config import config
from src.models.user import User


@pytest.fixture(scope="module")
def new_user_fixture():
    print("\nInitializing user")
    user = User(config.USERNAME, config.BIRTH_YEAR)
    yield user
    print("\nRemoving user")
    User.users.remove(user)


@pytest.fixture(scope="session", autouse=True)
def global_fixture():
    print("-----Doing some things before all tests-----")
    yield
    print("-----Cleaning up after testing-----")
