import pytest

from submit_form import submit_form


def test_rejects_empty_email():
    result = submit_form({"email": ""})
    assert result["error"] == "Email required"


@pytest.mark.parametrize("email", ["", "   ", "\t\n"])
def test_rejects_blank_email(email):
    result = submit_form({"email": email})
    assert result["error"] == "Email required"
