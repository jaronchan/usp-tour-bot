import sqlite3


class DBHelper:
    def __init__(self, dbname="tourbot.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS users (user_id integer PRIMARY KEY, username text, status integer, progress integer, route_id integer, current_state integer, check_in_time text, check_out_time text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_user(self, user_id, username):
        stmt = "INSERT INTO users (user_id, username, status) VALUES (?,?,?)"
        args = (user_id, username, 0)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_user(self, user_id):
        stmt = "DELETE FROM users WHERE user_id = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "SELECT user_id FROM users"
        return [x[0] for x in self.conn.execute(stmt)]
