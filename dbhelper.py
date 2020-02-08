import sqlite3


class DBHelper:
    def __init__(self, dbname="tourbot.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    # Set Up
    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS users (user_id integer PRIMARY KEY, username text, status integer, progress integer, route_id integer, current_state integer, check_in_time text, check_out_time text)"
        self.conn.execute(stmt)
        self.conn.commit()

    # Users
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

    # Status
    def update_user_status(self, user_id, status):
        stmt = "UPDATE users SET status = (?) WHERE user_id= (?)"
        args = (status, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    # Check In and Out
    def set_check_in(self, user_id, status, progress, route_id, current_state, check_in_time):
        stmt = "UPDATE users SET status = (?), progress = (?), route_id = (?), current_state = (?), check_in_time = (?) WHERE user_id = (?)"
        args = (status, progress, route_id,
                current_state, check_in_time, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def set_check_out(self, user_id, status, current_state, check_out_time):
        stmt = "UPDATE users SET status = (?), current_state = (?), check_out_time = (?) WHERE user_id= (?)"
        args = (status, current_state, check_out_time, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    # Route
    def update_route(self, user_id, route_id):
        stmt = "UPDATE users SET route_id = (?) WHERE user_id= (?)"
        args = (route_id, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    # Current State
    def get_current_state(self, user_id):
        stmt = "SELECT current_state FROM users WHERE user_id = (?)"
        args = (user_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def update_current_state(self, user_id, current_state):
        stmt = "UPDATE users SET current_state = (?) WHERE user_id= (?)"
        args = (current_state, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    # Progress and Scores
    def get_progress(self, user_id):
        stmt = "SELECT progress FROM users WHERE user_id = (?)"
        args = (user_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def update_progress(self, user_id, new_progress):
        stmt = "UPDATE users SET current_state = (?) WHERE user_id= (?)"
        args = (new_progress, user_id)
        self.conn.execute(stmt, args)
        self.conn.commit()
