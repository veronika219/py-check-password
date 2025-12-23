import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),          # валідний пароль
        ("Pass@12", False),              # занадто короткий
        ("THISISLONGPASSWORD1@", False), # занадто довгий
        ("nouppercase1@", False),      # без великої літери
        ("NoDigits!@", False),         # без цифр
        ("NoSpecial1", False),         # без спецсимволу
    ]
)
def test_check_password(password, expected):
    assert check_password(password) == expected, f"Password failed: {password}"