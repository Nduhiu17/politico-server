"""models"""

MOCK_DATABASE = {
    "parties": [],
}


class Party:
    """Class to model a party"""

    def __init__(self, name, hqaddress, logoUrl):
        """Initializing the party class"""
        self.id = len(MOCK_DATABASE["parties"]) + 1
        self.name = name
        self.hqaddress = hqaddress
        self.logoUrl = logoUrl

    def json_dumps(self):
        """method to return a json object from the party details"""
        party_obj = {
            "id": str(self.id),
            "name": self.name,
            "hqaddress": self.hqaddress,
            "logoUrl": self.logoUrl
        }
        return party_obj

    @classmethod
    def get_all(cls):
        """method to get all parties"""
        all_parties = MOCK_DATABASE['parties']
        get_all_json = []
        for item in all_parties:
            get_all_json.append(item.json_dumps())
        return get_all_json

    def save(self):
        """Method to save a party"""
        MOCK_DATABASE["parties"].append(self)
        return self.json_dumps()

    def get_party_by_name(self,name):
        """Method to get a party by name"""
        all_parties = MOCK_DATABASE['parties']
        for party in all_parties:
            if party.name == name:
                return party.json_dumps()
