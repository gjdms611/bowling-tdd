from submit_form import submit_form


def test_missing_email_key_is_rejected():
    result = submit_form({"name": "Alice"})
    assert result == {"error": "Email required"}


def test_empty_string_email_is_rejected():
    result = submit_form({"name": "Alice", "email": ""})
    assert result == {"error": "Email required"}


def test_whitespace_only_email_is_rejected():
    result = submit_form({"name": "Alice", "email": "   "})
    assert result == {"error": "Email required"}


def test_valid_email_is_accepted():
    data = {"name": "Alice", "email": "alice@example.com"}
    result = submit_form(data)
    assert result == {"success": True, "data": data}
