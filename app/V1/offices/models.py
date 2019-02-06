"""office model"""

OFFICE_MOCK_DATABASE = {
    "offices": [],
}


class Office:
    """Class to model an office"""

    def __init__(self, office_type, name):
        """Initializing the office class"""
        self.id = len(OFFICE_MOCK_DATABASE["offices"]) + 1
        self.office_type = office_type
        self.name = name

    def json_dumps(self):
        """method to return a json object from the office details"""
        office_obj = {
            "id": str(self.id),
            "office_type": self.office_type,
            "name": self.name,
        }
        return office_obj

    def save(self):
        """Method to save a party"""
        OFFICE_MOCK_DATABASE["offices"].append(self)
        return self.json_dumps()

    @staticmethod
    def get_office_by_name(name):
        """Method to get an office by name"""
        all_offices = OFFICE_MOCK_DATABASE['offices']
        for office in all_offices:
            if office.name == name:
                return office.json_dumps()

    @classmethod
    def get_all_offices(cls):
        """method to get all offices"""
        all_offices = OFFICE_MOCK_DATABASE['offices']
        get_all_json = []
        for item in all_offices:
            get_all_json.append(item.json_dumps())
        return get_all_json

    @classmethod
    def get_office_by_id(cls, id):
        """Method to get an office by id"""
        list_office_data = []
        for item in OFFICE_MOCK_DATABASE['offices']:
            if item.id == id:
                list_office_data.append(item.json_dumps())
                return list_office_data
