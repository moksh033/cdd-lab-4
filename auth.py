# Authentication Module

def validate_credentials(username, password):
    """
    Validate user credentials ensuring standard security constraints:
    - Username must be non-empty and at least 3 characters.
    - Password must be at least 6 characters.
    """
    if not username or not password:
        return False
    return len(username) >= 3 and len(password) >= 6

if __name__ == "__main__":
    assert validate_credentials("moksh", "secret123") == True
    assert validate_credentials("ab", "123") == False
    print("Authentication validation logic passed.")
