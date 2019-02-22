"""user models comes here"""
from attr import dataclass
from flask_jwt_extended import create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from datetime import datetime

from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_users_tables()


@dataclass
class User:
    """Class that models a user"""
    id: str
    firstname: str
    lastname: str
    othername: str
    email: str
    phonenumber: str
    passporturl: str
    roles: str
    nationalid: str
    county: str
    password: str
    date_created: str
    date_modified: str

    def save(self, *args):
        """method to save a user"""
        self.firstname, self.lastname, self.othername, self.email, self.phonenumber, self.passporturl, self.roles, self.nationalid, self.county, self.password, self.date_created, self.date_modified = args
        format_str = f"""
                  INSERT INTO public.users (firstname,lastname,othername,email,phonenumber,passporturl,roles,nationalid,county,password,date_created,date_modified)
                  VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}','{args[6]}','{args[
            7]}','{args[8]}','{args[9]}','{(datetime.now())}','{(datetime.now())}');
                  """
        cursor.execute(format_str)

    def json_dump(self):
        """method that returns a user json"""
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othername": self.othername,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "passporturl": self.passporturl,
            "roles": self.roles,
            "nationalid": self.nationalid,
            "county": self.county,
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }

    @staticmethod
    def generate_hash(password):
        """method that returns a hash"""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def generate_token(email):
        """Method that generates user token"""
        access_token = create_access_token(email)
        return access_token

    @classmethod
    def get_by_email(cls, email):
        """This method gets a user using email"""
        try:
            cursor.execute("select * from users where email = %s", (email,))
            user = cursor.fetchone()
            return list(user)
        except Exception:
            return False

    @staticmethod
    def verify_hashed_password(password, hashed_password):
        """Method to verify password with the hashed password"""
        return pbkdf2_sha256.verify(password, hashed_password)

    @classmethod
    def find_by_nationaid(cls, id):
        """This method gets a user using nationalid"""
        try:
            cursor.execute("select * from users where nationalid = %s", (id,))
            user = cursor.fetchone()
            user = User(id=user[0], firstname=user[1], lastname=user[2],othername=user[3], email=user[4],phonenumber=user[5], passporturl=user[6], roles=user[7], nationalid=user[8], county=user[9],password=user[10], date_created=user[11], date_modified=user[12])
            return user.json_dump()
        except Exception:
            return False

    @staticmethod
    def find_user_by_id(id):
        """This method gets a user using id"""
        try:
            cursor.execute("select * from users where id = %s", (id,))
            user = cursor.fetchone()
            user = User(id=user[0], firstname=user[1], lastname=user[2], othername=user[3], email=user[4],phonenumber=user[5], passporturl=user[6], roles=user[7], nationalid=user[8], county=user[9],password=user[10], date_created=user[11], date_modified=user[12])
            return user.json_dump()
        except Exception:
            return False


