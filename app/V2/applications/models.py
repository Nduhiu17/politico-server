from attr import dataclass
from datetime import datetime

from app.V2.auth.models import User
from app.V2.database.db import Database
from app.V2.offices.models import Office
from app.V2.parties.models import Party

cursor = Database.connect_to_db()
Database.create_offices_table()
Database.create_parties_table()
Database.create_applications_table()


@dataclass
class Application:
    """Class that models an application"""
    id: str
    party_name: str
    office_name: str
    user_id: str
    date_created: str

    def save(self, *args):
        """method to save an application"""
        self.party_name, self.office_name, self.user_id, self.date_created = args
        format_str = f"""
                   INSERT INTO public.applications (party_name,office_name,user_id,date_created)
                   VALUES ('{args[0]}','{args[1]}','{args[2]}','{(datetime.now())}');
                   """
        cursor.execute(format_str)

    def json_dumps(self):
        """method to return a json object from the application details"""
        application_obj = {
            "id": self.id,
            "party": Party.get_party_by_name(name=self.party_name),
            "office":Office.get_office_by_name(name=self.office_name),
            "user": User.find_user_by_id(id=self.user_id),
            "date_created": self.date_created,
        }
        return application_obj

    @staticmethod
    def get_application_by_user_id(user_id):
        """method to get application by user id"""
        try:
            cursor.execute("select * from applications where user_id = %s", (user_id,))
            retrieved_application = cursor.fetchone()
            retrieved_application = Application(id=retrieved_application[0],party_name=retrieved_application[1],office_name=retrieved_application[2],user_id=retrieved_application[3],date_created=retrieved_application[4])
            return retrieved_application.json_dumps()
        except Exception:
            return False
