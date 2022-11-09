import datetime


class User:

    users = set()

    def __init__(self, name: str, birth_year: int) -> None:
        """Initialize user, add user instance to set users.

        Args:
            name (str): Username.
            birth_year (int): User's birth year.
        """
        self.name = name
        self.birth_year = birth_year
        self.users.add(self)

    def __repr__(self) -> str:
        return f"<Username: {self.name}, age: {self.calc_age}>"

    def calc_age(self) -> int:
        """Return calculated age of user (current year - birth year)."""
        return datetime.date.today().year - self.birth_year

    def introduce(self) -> str:
        """Return a silly introduction string (just to have something to test)."""
        return f"Hello, my name is {self.name} and I'm {self.calc_age()} years old."
