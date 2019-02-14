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
    password: str
    date_created: str
    date_modified: str

    def save(self, *args):
        """method to save a user"""
        self.firstname, self.lastname, self.othername, self.email, self.phonenumber, self.passporturl, self.password, self.date_created, self.date_modified = args
        format_str = f"""
                 INSERT INTO public.users (firstname,lastname,othername,email,phonenumber,passporturl,password,date_created,date_modified)
                 VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}','{args[6]}','{(
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
    def get_user_by_id(cls, id):
        """method to find a user by id"""
        try:
            cursor.execute("select * from users where id = %s", (id,))
            retrieved_user = list(cursor.fetchone())
            user = User(id=retrieved_user[0], firstname=retrieved_user[1],lastname=retrieved_user[2],othername=retrieved_user[3], email=retrieved_user[4],phonenumber=retrieved_user[5],passporturl=retrieved_user[6],
                        password=retrieved_user[7], date_created=retrieved_user[8],date_modified=retrieved_user[9])

            return user
        except Exception:
            return False

