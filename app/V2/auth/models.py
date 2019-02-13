"""user models comes here"""
from flask_jwt_extended import create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from datetime import datetime

from app.V2.database.db import Database

cursor = Database.connect_to_db()
Database.create_users_tables()


class User:
    """Class that models a user"""

    def __init__(self, id, firstname, lastname, othername, email, phonenumber, passporturl, password,
                 date_created,
                 date_modified):
        """Initializing user class"""
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phonenumber = phonenumber
        self.passporturl = passporturl
        self.password = password
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self, firstname, lastname, othername, email, phonenumber, passporturl, password):
        """method to save a user"""
        format_str = f"""
                 INSERT INTO public.users (firstname,lastname,othername,email,phonenumber,passporturl,password,date_created,date_modified)
                 VALUES ('{firstname}','{lastname}','{othername}','{email}','{phonenumber}','{passporturl}','{password}','{(
            datetime.now())}','{(datetime.now())}');
                 """
        cursor.execute(format_str)
        return {
            "id": self.id,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "passporturl": passporturl,
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }

    def json_dump(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othername": self.othername,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "passporturl": self.passporturl,
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }

    @staticmethod
    def generate_hash(password):
        """method that returns a hash"""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def generate_token(email):
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
