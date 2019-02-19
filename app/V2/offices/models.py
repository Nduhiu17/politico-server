"""office models"""
from attr import dataclass
from datetime import datetime

from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_offices_table()


@dataclass
class Office:
    """Class that models an office"""
    id: str
    name: str
    office_type: str
    date_created: str
    date_modified: str

    def json_dumps(self):
        """method to return a json object from the office details"""
        office_obj = {
            "id":self.id,
            "name": self.name,
            "office_type": self.office_type,
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }
        return office_obj

    def save(self, *args):
        """method to save an office"""
        self.name, self.office_type, self.date_created, self.date_modified = args
        format_str = f"""
                   INSERT INTO public.offices (name,office_type,date_created,date_modified)
                   VALUES ('{args[0]}','{args[1]}','{(datetime.now())}','{(datetime.now())}');
                   """
        cursor.execute(format_str)

    @classmethod
    def get_office_by_type(cls, office_type):
        """method to get a office by type"""
        try:
            cursor.execute("select * from offices where office_type = %s", (office_type,))
            retrieved_office = cursor.fetchone()
            retrieved_office = Office(id=retrieved_office[0], name=retrieved_office[1], office_type=retrieved_office[2],
                                      date_created=retrieved_office[3],
                                      date_modified=retrieved_office[4])
            return retrieved_office.json_dumps()
        except Exception:
            return False

    @classmethod
    def get_office_by_name(cls, name):
        """method to get a office by name"""
        try:
            cursor.execute("select * from offices where name = %s", (name,))
            retrieved_office = cursor.fetchone()
            retrieved_office = Office(id=retrieved_office[0], name=retrieved_office[1], office_type=retrieved_office[2],
                                      date_created=retrieved_office[3],
                                      date_modified=retrieved_office[4])
            return retrieved_office.json_dumps()
        except Exception:
            return False

