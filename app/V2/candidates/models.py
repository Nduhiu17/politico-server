from attr import dataclass
from datetime import datetime

from app.V2.auth.models import User
from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_candidates_table()


@dataclass
class Candindate:
    """Class that models a candidate"""
    id: str
    office: str
    party: str
    candidate: str
    date_created: str
    date_modified: str

    def save(self, *args):
        """method to save a candidate"""
        self.office, self.party, self.candidate, self.date_created, self.date_modified = args
        format_str = f"""
                   INSERT INTO public.candidates (office,party,candidate,date_created,date_modified)
                   VALUES ('{args[0]}','{args[1]}','{args[2]}','{(datetime.now())}','{(datetime.now())}');
                   """
        cursor.execute(format_str)

    @staticmethod
    def find_candidate_using_id(id):
        """This method gets a candidate using id"""
        try:
            cursor.execute("select * from candidates where candidate= %s", (id,))
            user = cursor.fetchone()
            if user:
                return True
        except Exception:
            return False

    def json_dumps(self):
        """method to return a json object from the candidate details"""
        candidate_obj = {
            "office":self.office,
            "party": self.party,

            "candidate": User.find_by_id(self.candidate),
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }
        return candidate_obj
