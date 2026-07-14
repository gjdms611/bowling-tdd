def submit_form(data):
    email = data.get("email", "")
    if not email.strip():
        return {"error": "Email required"}
    # TODO: send confirmation email, persist record, etc.
    return {"success": True}
