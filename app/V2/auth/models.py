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
    roles:str
    password: str
    date_created: str
    date_modified: str

    def save(self, *args):
        """method to save a user"""
        self.firstname, self.lastname, self.othername, self.email, self.phonenumber, self.passporturl,self.roles, self.password, self.date_created, self.date_modified = args
        format_str = f"""
                 INSERT INTO public.users (firstname,lastname,othername,email,phonenumber,passporturl,roles,password,date_created,date_modified)
                 VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}','{args[6]}','{args[7]}','{(
            datetime.now())}','{(datetime.now())}');
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
            "roles":self.roles,
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


