"""party models"""
from attr import dataclass
from datetime import datetime

from app.V2.auth.models import User
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
            "id": self.id,
            "name": self.name,
            "hqaddress": self.hqaddress,
            "logoUrl": self.logoUrl,
            "slogan": self.slogan,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
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
            party = Party(id=item[0], name=item[1], hqaddress=item[2], logoUrl=item[3], slogan=item[4],
                          date_created=item[5], date_modified=item[6])
            party = party.json_dumps()
            party['candindates'] = Party.get_party_candindates(party_id=item[0])
            party_dicts.append(party)
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

    @staticmethod
    def retrieve_by_id(id):
        """method to get a party by id"""
        try:
            cursor.execute("select * from parties where id = %s", (id,))
            retrieved_party = cursor.fetchone()
            retrieved_party = Party(id=retrieved_party[0], name=retrieved_party[1], hqaddress=retrieved_party[2],
                                    logoUrl=retrieved_party[3], slogan=retrieved_party[4],
                                    date_created=retrieved_party[5],
                                    date_modified=retrieved_party[6])
            retrieved_party = retrieved_party.json_dumps()
            retrieved_party['candindates'] = Party.get_party_candindates(party_id=id)
            return retrieved_party
        except Exception:
            return False

    @classmethod
    def update(cls, name, id):
        """Method to update a party"""
        format_str = f"""
          UPDATE public.parties SET name = '{name}', date_modified = '{str(datetime.now())}' WHERE id = {id};
          """

        cursor.execute(format_str)

        return {
            "id": id,
            "name": name,
        }

    @classmethod
    def delete_a_party(cls, id):
        """method to delete a party"""
        try:
            cursor.execute('DELETE FROM public.parties CASCADE WHERE id = %s', (id,))
            return True
        except Exception:
            return False

    @staticmethod
    def get_party_candindates(party_id):
        """method to get all candindates for a given party"""
        cursor.execute(
            f"SELECT * FROM public.candidates where party = {party_id};")
        rows = cursor.fetchall()
        candindate_objects = []
        for item in rows:
            candindate = User.find_user_by_id(id=item[3])
            candindate_objects.append(candindate)
        return candindate_objects
