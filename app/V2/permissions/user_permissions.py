"""user permissions"""
from app.V2.auth.models import User
from app.V2.database.db import Database

Database.create_permissions_table()
Database.create_user_permissions_table()
cursor = Database.connect_to_db()


class Permission:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json_dump(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def get_permission_by_id(cls, id):
        cursor.execute(
            f"SELECT * FROM public.permissions where id = {id};")
        item = cursor.fetchone()
        if item is None:
            return None
        permission = Permission(id=item[0], name=item[1])
        return permission.json_dump()

    @classmethod
    def check_if_exists(cls):
        cursor.execute(
            f"SELECT * FROM public.permissions")
        items = cursor.fetchall()
        if items:
            return True
        return False

    @classmethod
    def make_permissions(cls):
        """Method to create permissions for the application"""
        cursor = Database.connect_to_db()
        sql_command = """INSERT INTO public.permissions (id, name) VALUES('1', 'admin'),('2', 'politician'),('3', 'normal_user');
                 """
        if Permission.check_if_exists():
            return False
        cursor.execute(sql_command)


class UserPermission:
    def __init__(self, user_id, permission_id):
        self.id = id
        self.user_id = user_id
        self.permission_id = permission_id

    def json_dump(self):
        """method to return user permission"""
        return {
            "id": self.id,
            "user": User.get_user_by_id(self.user_id),
            "permissions": Permission.get_permission_by_id(id=self.permission_id)
        }

    @classmethod
    def get_user_permissions(cls, user_id):
        """Method that gets user permissions"""
        cursor.execute(
            f"SELECT * FROM public.userpermissions where user_id = {user_id};")
        rows = cursor.fetchall()
        permissions_list = []
        for item in rows:
            permission_item = Permission.get_permission_by_id(item[2])
            permissions_list.append(permission_item)
        return permissions_list

    @staticmethod
    def make_admin(user_id):
        """method to make an admin"""
        cursor.execute(
            f"INSERT INTO public.userpermissions(user_id, permission_id) VALUES('{user_id}', '1');")

    @staticmethod
    def make_politician(user_id):
        """method to make a politician"""
        cursor.execute(
            f"INSERT INTO public.userpermissions(user_id, permission_id) VALUES('{user_id}', '2');")
