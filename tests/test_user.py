import datetime
from src.config.config import config


def test_new_user(new_user_fixture):
    """Test new user's name and verify that the user is added to User.users."""
    assert new_user_fixture.name == config.USERNAME
    assert new_user_fixture in new_user_fixture.users

    print("New user OK")


def test_user_calc_age(new_user_fixture):
    """Verify that calc_age function returns correct age."""
    assert new_user_fixture.calc_age() == datetime.date.today().year - \
        new_user_fixture.birth_year

    print("Age OK")


def test_user_introduce(new_user_fixture):
    """Verify introduce function returns correct introduction."""
    assert new_user_fixture.introduce(
    ) == f"Hello, my name is {config.USERNAME} and I'm {datetime.date.today().year - config.BIRTH_YEAR} years old."

    print("Introduction OK")
