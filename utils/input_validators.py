import re


class Validate:
    """Class for validating data input"""

    @staticmethod
    def validate_name(name):
        """method to validate a name"""
        regex = r"[A-Z][a-zA-Z]"
        if re.match(regex, name):
            return True
        return False

    @staticmethod
    def validate_name_length(name):
        """Method to check name should be more than one characters"""
        if len(name) < 2:
            return False
        return True


