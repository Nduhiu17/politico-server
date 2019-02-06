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

    @staticmethod
    def get_party_by_name(name):
        """Method to get a party by name"""
        all_parties = MOCK_DATABASE['parties']
        for party in all_parties:
            if party.name == name:
                return party.json_dumps()

    @classmethod
    def get_party_by_id(cls, id):
        """Method to get a party by id"""
        list_party_data = []
        for item in MOCK_DATABASE['parties']:
            if item.id == id:
                list_party_data.append(item.json_dumps())
                return list_party_data

    def update_party(self, id, name, hqaddress, logoUrl):
        """Method to get a party by id"""
        list_party_data = []
        for item in MOCK_DATABASE['parties']:
            if item.id == id:
                party_to_update = Party(name=name, hqaddress=hqaddress, logoUrl=logoUrl)
                list_party_data.append(party_to_update.json_dumps())
                return list_party_data
            return None

    @classmethod
    def delete_party(cls, id):
        """Method delete a party"""
        for item in MOCK_DATABASE['parties']:
            if item.id == id:
                MOCK_DATABASE['parties'].remove(item)
