class Validate:
    """Class for validating data input"""
    @staticmethod
    def validate_empty_string(data_inputed):
        """Checks if data presented by a user is empty."""
        if data_inputed.strip() == "":
            return True
        return False


