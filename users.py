from unittest import result
from winreg import QueryInfoKey
from mysqlconnection import connectToMySQL  # connects my database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod  # this method pulles up everything in the database
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL('users').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
        #

    @classmethod  # this method inserts the new user's first name, last name, and email. create and update is already automated
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email) VALUES ( %(f_name)s, %(l_name)s, %(email)s);"
        results = connectToMySQL('users').query_db(query, data)
        return results
        # This is the function that will allow to add the new user to the table

    @classmethod  # this method will update a current user's info per what the user inputs
    def update(cls, data):
        # this will update each fields that the user inputed
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s WHERE id = %(id)s"
        connectToMySQL('users').query_db(query, data)
        return data['id']

    @classmethod  # this method will query one user per the id#
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        # this function will search the database by id
        results = connectToMySQL('users').query_db(query, data)
        # it will be shown as [0] always as it would the first one in the dictionary
        this_user = cls(results[0])
        return this_user  # this will pass the user back to the page and show that user only

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        return results
