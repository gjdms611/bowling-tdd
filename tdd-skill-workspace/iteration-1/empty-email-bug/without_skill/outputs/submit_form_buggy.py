"""
Original (buggy) version of submit_form, kept here for reference.

Bug: the function only checks that the "email" key EXISTS in the data
dict. It never checks that the value is non-blank, so an empty string
(or a whitespace-only string) sails through validation as if it were a
real email address.
"""


def submit_form(data):
    if "email" not in data:
        return {"error": "Email required"}

    # BUG: no check that data["email"] is actually non-blank.
    # An empty string "" or "   " passes right through here.

    return {"success": True, "data": data}
