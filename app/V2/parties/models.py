"""party models"""
from attr import dataclass
from datetime import datetime
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
    slogan: str
    date_created: str
    date_modified: str

    def json_dumps(self):
        """method to return a json object from the party details"""
        party_obj = {
            "id": str(self.id),
            "name": self.name,
            "hqaddress": self.hqaddress,
            "logoUrl": self.logoUrl,
            "slogan": self.slogan,
            "date_created":self.date_created,
            "date_modified":self.date_modified

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
            party = Party(id=item[0], name=item[1], hqaddress=item[2], logoUrl=item[3],slogan=item[4],date_created=item[5],date_modified=item[6])
            party_dicts.append(party.json_dumps())
        return party_dicts

    def save(self, *args):
        """method to save a party"""
        self.name, self.hqaddress, self.logoUrl, self.slogan, self.date_created, self.date_modified = args
        format_str = f"""
                 INSERT INTO public.parties (name,hqaddress,logoUrl,slogan,date_created,date_modified)
                 VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{(datetime.now())}','{(datetime.now())}');
                 """
        cursor.execute(format_str)

    @staticmethod
    def get_party_by_name(name):
        """method to get a party by name"""
        try:
            cursor.execute("select * from parties where name = %s", (name,))
            retrieved_party = cursor.fetchone()
            retrieved_party = Party(id=retrieved_party[0], name=retrieved_party[1], hqaddress=retrieved_party[2],
                                    logoUrl=retrieved_party[3], slogan=retrieved_party[4],
                                    date_created=retrieved_party[5],
                                    date_modified=retrieved_party[6])
            return retrieved_party.json_dumps()
        except Exception:
            return False
