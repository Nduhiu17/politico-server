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

    @staticmethod
    def check_password_strength(input_password):
        """check password strength"""
        if re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", input_password):
            return True
        else:
            return False

    @staticmethod
    def check_email_int(email):
        """method to check whether the first digit is an integer"""
        try:
            int(list(email)[0])
            return True
        except ValueError:
            return False
    

    @staticmethod
    def check_number_format(input_value):
        """Check if value is a number."""
        try:
            int(input_value)
        except ValueError:
            return True
        else:
            if int(input_value) < 8:
                return False
            return True

    @staticmethod
    def check_phone_number(phone_number):
        """Check phone number validity"""
        if re.match(r"^0(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$", phone_number):
            return True
        return False

