from attr import dataclass

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