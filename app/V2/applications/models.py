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
    status: str

    def save(self, *args):
        """method to save an application"""
        self.party_name, self.office_name, self.user_id, self.date_created, self.status = args
        format_str = f"""
                   INSERT INTO public.applications (party_name,office_name,user_id,date_created,status)
                   VALUES ('{args[0]}','{args[1]}','{args[2]}','{(datetime.now())}','pending');
                   """
        cursor.execute(format_str)

    def json_dumps(self):
        """method to return a json object from the application details"""
        application_obj = {
            "id": self.id,
            "party": Party.get_party_by_name(name=self.party_name),
            "office": Office.get_office_by_name(name=self.office_name),
            "user": User.find_user_by_id(id=self.user_id),
            "date_created": self.date_created,
            "status":self.status
        }
        return application_obj

    @staticmethod
    def get_application_by_user_id(user_id):
        """method to get applications"""
        try:
            cursor.execute("select * from applications where user_id = %s", (user_id,))
            retrieved_application = cursor.fetchone()
            retrieved_application = Application(id=retrieved_application[0], party_name=retrieved_application[1],
                                                office_name=retrieved_application[2], user_id=retrieved_application[3],
                                                date_created=retrieved_application[4],status=retrieved_application[5])
            return retrieved_application.json_dumps()
        except Exception:
            return False

    @staticmethod
    def get_all_applications():
        """method to get all applications from the database"""
        cursor.execute(
            f'SELECT * FROM public.applications where status = %s', ("pending",))
        rows = cursor.fetchall()
        application_dicts = []

        for item in rows:
            application = Application(id=item[0], party_name=item[1], office_name=item[2], user_id=item[3],
                                      date_created=item[4],status=item[5])
            application = application.json_dumps()
            application_dicts.append(application)
        return application_dicts

    @staticmethod
    def make_done(user_id):
        cursor.execute(
            f"UPDATE public.applications SET status = 'done' WHERE user_id = {user_id};")
