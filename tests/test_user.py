import datetime
from src.data.test_data import TestData


def test_new_user(new_user_fixture):
    """Test new user's name and verify that the user is added to User.users."""
    assert new_user_fixture.name == TestData.USERNAME
    assert new_user_fixture in new_user_fixture.users


def test_user_calc_age(new_user_fixture):
    """Verify that calc_age method returns correct age."""
    assert (
        new_user_fixture.calc_age() == datetime.date.today().year - TestData.BIRTH_YEAR
    )


def test_user_introduce(new_user_fixture):
    """Verify introduce method returns correct introduction."""
    assert (
        new_user_fixture.introduce()
        == f"Hello, my name is {TestData.USERNAME} and I'm {datetime.date.today().year - TestData.BIRTH_YEAR} years old."
    )
