from attr import dataclass
from datetime import datetime

from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_offices_table()
Database.create_parties_table()
Database.create_users_tables()
Database.create_candidates_table()
Database.create_votes_table()


@dataclass
class Vote:
    """Class that models a vote"""
    id: str
    createdOn: str
    createdBy: str
    office: str
    candidate: str

    def save(self, *args):
        """method to save a vote"""
        self.createdOn, self.createdBy, self.Office, self.candidate = args
        format_str = f"""
                   INSERT INTO public.votes (createdOn,createdBy,office,candidate)
                   VALUES ('{(datetime.now())}','{args[1]}','{args[2]}','{args[3]}');
                   """
        cursor.execute(format_str)

    @staticmethod
    def check_already_voted(createdBy):
        try:
            cursor.execute("select * from votes where createdBy = %s", (createdBy,))
            retrieved_vote = cursor.fetchone()
            if retrieved_vote:
                return True
        except Exception:
            return False
