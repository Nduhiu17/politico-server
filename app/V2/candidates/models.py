from attr import dataclass
from datetime import datetime

from app.V2.auth.models import User
from app.V2.database.db import Database
from app.V2.parties.models import Party
from app.V2.votes.models import Vote

cursor = Database.connect_to_db()
Database.create_users_tables()
Database.create_offices_table()
Database.create_parties_table()
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
            "candidate": User.find_user_by_id(id=self.candidate),
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }
        return candidate_obj

    @staticmethod
    def make_politician(candidate_id):
        cursor.execute(
            f"UPDATE public.users SET roles = 'politician' WHERE id = {candidate_id};")

    @staticmethod
    def get_office_candindates(office_id):
        """method to get all candindates for a given office"""
        try:
            cursor.execute(
                f"SELECT * FROM public.candidates where office = {office_id};")
            rows = cursor.fetchall()

            candindate_objects = []
            for item in rows:
                candindate = User.find_user_by_id(id=item[3])
                candindate['party']= Party.retrieve_by_id(id=item[2])
                candindate['votes'] = Vote.get_number_of_votes(candidate_id=item[2])
                candindate_objects.append(candindate)
            return candindate_objects
        except Exception:
            return []

    @staticmethod
    def to_json(rows):
        return {
            "party": rows[2],
            "user": User.find_user_by_id(id=rows[3]),
            "date_created": rows[3],
            "date_modified": rows[3]
        }

    @staticmethod
    def get_by_id(id):
        """method to get a candidate by id"""
        try:
            cursor.execute("select * from candidates where id = %s", (id,))
            retrieved = cursor.fetchone()
            found = Candindate(id=retrieved[0], office=retrieved[1], party=retrieved[2],candidate=retrieved[3],date_created=retrieved[4],date_modified=retrieved[5])
            return found
        except Exception:
            return False

    @staticmethod
    def get_candidates(office_id):
        """method to get candidates using office if"""
        cursor.execute(
            f"SELECT * FROM public.candidates where office = {office_id};")
        rows = cursor.fetchall()
        return rows
