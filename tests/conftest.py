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
