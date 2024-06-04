class Users:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, password, country):
        """Initialize first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.country = country
        self.login_attempt = 0

    def increment_login_attempts(self):
        """Increases the value of login_attempt by 1."""
        self.login_attempt += 1

    def reset_login_attempts(self):
        """Reset the login_attempts to zero."""
        self.login_attempt = 0

    def describe_user(self):
        """Prints a summary of a user information"""
        print(
            "users details: \n"
            + "\tfirst name:"
            + self.first_name.title()
            + "\n\tlast name: "
            + self.last_name.title()
            + "\n\tCountry: "
            + self.country.title()
        )

    def greet_user(self):
        """Print a personalized greeting to users."""
        print("Hello " + self.first_name.title() + "!")


user_1 = Users(
    first_name="john", last_name="doe", password="john123", country="england"
)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempt)
user_1.reset_login_attempts()
print(user_1.login_attempt)


class Privilege:
    """A simple model of a user's privileges."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print the privileges of an admin user."""
        for privilege in self.privileges:
            print(privilege)


class Admin(Users):
    """A simple model of an admin user."""

    def __init__(self, first_name, last_name, password, country):
        """Initialize attributes of the parent class. Then Initialize attributes
        specific to an admin user."""
        super().__init__(first_name, last_name, password, country)

        self.privilege = Privilege()


admin_user = Admin(
    "frank",
    "alimimian",
    "frank123",
    "nigeria"
)
admin_user.privilege.show_privileges()
