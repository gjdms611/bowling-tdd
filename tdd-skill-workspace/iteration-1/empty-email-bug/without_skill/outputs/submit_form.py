"""
submit_form: validates and "submits" form data.

Fixed version: rejects a missing email, an empty-string email, and a
whitespace-only email, all with a clear {"error": "Email required"}
response.
"""


def submit_form(data):
    email = data.get("email", "")

    if not email or not email.strip():
        return {"error": "Email required"}

    return {"success": True, "data": data}
