"""party models"""
from attr import dataclass

from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_parties_table()


@dataclass
class Party:
    """Class that models a party"""
    id: str
    name: str
    hqaddress: str
    logoUrl: str

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
    def get_all_parties(cls):
        """method to get all parties from the database"""
        cursor.execute(
            f"SELECT * FROM public.parties")
        rows = cursor.fetchall()
        party_dicts = []

        for item in rows:
            party = Party(id=item[0], name=item[1], hqaddress=item[2], logoUrl=item[3])
            party_dicts.append(party.json_dumps())
        return party_dicts
