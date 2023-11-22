# Code smell
def verify_login(username, password):
    """
    Verifies the login with username and password.
    :return true if the login is valid.
    """
    return username == "TestEngineer" and password == "pwdadmin"

# Better
def verify_login(username, password):
    """
    Verifies the login with username and password.
    :return true if the login is valid.
    """
    return username == "TestEngineer" and hash(password) == 8721669614390452154


if __name__ == '__main__':
    pass