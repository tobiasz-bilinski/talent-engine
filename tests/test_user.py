import datetime
from src.config.config import config


def test_new_user(user_fixture):
    """Test new user's name and verify that the user is added to User.users."""
    assert user_fixture.name == config.USERNAME
    assert user_fixture in user_fixture.users

    print("New user OK")


def test_user_calc_age(user_fixture):
    """Verify that calc_age function returns correct age."""
    assert user_fixture.calc_age() == datetime.date.today().year - \
        user_fixture.birth_year

    print("Age OK")


def test_user_introduce(user_fixture):
    """Verify introduce function returns correct introduction."""
    assert user_fixture.introduce(
    ) == f"Hello, my name is {config.USERNAME} and I'm {user_fixture.calc_age()} years old."

    print("Introduction OK")
