import re


class Validate:
    """Class for validating data input"""
    @staticmethod
    def validate_empty_string(data_inputed):
        """Checks if data presented by a user is empty."""
        if data_inputed.strip() == "":
            return True
        return False

    @staticmethod
    def validate_email_format(email):
        """checks correct email format"""
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regex, email, re.IGNORECASE):
            return True
        return False


