import os

import psycopg2


class Database:
    """Class database"""

    @classmethod
    def connect_to_db(cls):
        """Method to create a database connection"""
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        conn.autocommit = True
        cursor = conn.cursor()

        return cursor

    @classmethod
    def create_users_tables(cls):
        """Method to create users table"""
        cursor = Database.connect_to_db()
        sql_command = """CREATE TABLE IF NOT EXISTS "public"."users"  (
        id SERIAL ,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        othername VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phonenumber VARCHAR(255) NOT NULL,
        passporturl TEXT NOT NULL,
        roles VARCHAR(255) NOT NULL,
        nationalid VARCHAR(255) NOT NULL,
        county VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        date_created VARCHAR(80),
        date_modified VARCHAR(80),
        PRIMARY KEY (id)
            )
            """
        cursor.execute(sql_command)

    @classmethod
    def create_parties_table(cls):
        """create parties table"""
        cursor = Database.connect_to_db()
        sql_command = """CREATE TABLE IF NOT EXISTS "public"."parties"  (
        id SERIAL ,
        name VARCHAR(255) NOT NULL,
        hqAddress VARCHAR(255) NOT NULL,
        logoUrl TEXT NOT NULL,
        slogan VARCHAR(255) NOT NULL,
        date_created VARCHAR(80),
        date_modified VARCHAR(80),
        PRIMARY KEY (id)
            )
            """
        cursor.execute(sql_command)

    @classmethod
    def create_offices_table(cls):
        """Method to create offices table"""
        cursor = Database.connect_to_db()
        sql_command = """CREATE TABLE IF NOT EXISTS "public"."offices"  (
        id SERIAL ,
        name VARCHAR(255) NOT NULL,
        office_type VARCHAR(255) NOT NULL,
        date_created VARCHAR(80),
        date_modified VARCHAR(80),
        PRIMARY KEY (id) 
            )
            """
        cursor.execute(sql_command)

    @classmethod
    def create_candidates_table(cls):
        """create candidates table"""
        cursor = Database.connect_to_db()
        sql_command = """CREATE TABLE IF NOT EXISTS "public"."candidates"  (
        id SERIAL ,
        office INTEGER NOT NULL,
        party INTEGER NOT NULL,
        candidate INTEGER NOT NULL,
        date_created VARCHAR(80),
        date_modified VARCHAR(80),
        FOREIGN KEY (office) REFERENCES offices (id) ON DELETE CASCADE,
        FOREIGN KEY (party) REFERENCES parties (id) ON DELETE CASCADE,
        FOREIGN KEY (candidate) REFERENCES users (id) ON DELETE CASCADE,
        PRIMARY KEY (id)
            )
            """
        cursor.execute(sql_command)

    @classmethod
    def create_votes_table(cls):
        """create votes table"""
        cursor = Database.connect_to_db()
        sql_command = """CREATE TABLE IF NOT EXISTS "public"."votes"  (
          id SERIAL PRIMARY KEY ,
          createdOn INTEGER NOT NULL,
          createdBy INTEGER NOT NULL,
          office INTEGER NOT NULL,
          candidate INTEGER NOT NULL,
          FOREIGN KEY (createdBy) REFERENCES users (id) ON DELETE CASCADE,
          FOREIGN KEY (office) REFERENCES offices (id) ON DELETE CASCADE,
          FOREIGN KEY (candidate) REFERENCES candidates (id) ON DELETE CASCADE
              )
              """
        cursor.execute(sql_command)

    @classmethod
    def drop_database_tables(cls):
        """Method to destroy database tables"""
        cursor = Database.connect_to_db()
        # drop users table
        sql_command = """ DROP TABLE IF EXISTS users CASCADE;
            """
        cursor.execute(sql_command)
        # drop parties table
        sql_command = """ DROP TABLE IF EXISTS parties CASCADE;
                   """
        cursor.execute(sql_command)
        # drop offices table
        sql_command = """ DROP TABLE IF EXISTS offices CASCADE;
                        """
        cursor.execute(sql_command)
        # drop candidates table
        sql_command = """ DROP TABLE IF EXISTS candidates CASCADE;
                              """
        cursor.execute(sql_command)
        # drop votes table
        sql_command = """ DROP TABLE IF EXISTS votes CASCADE;
                                    """
        cursor.execute(sql_command)
