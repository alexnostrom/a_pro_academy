import sqlite3


class Database:
	def __init__(self, db_name):
		self.db_name = db_name
		self.connection = sqlite3.connect(db_name, check_same_thread=False)
		self.cur = self.connection.cursor()

	def create_database(self):
		self.cur.execute(
			'''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT, register_date TEXT)''')

	def single_read_database(self, id):
		single = self.cur.execute('SELECT * FROM users WHERE id=?', (id,))
		res = single.fetchone()
		return {'id': res[0], 'username': res[1], 'email': res[2], 'register_date': res[4]}

	def multy_read_database(self):
		multy = self.cur.execute('SELECT * FROM users')
		res = multy.fetchall()
		new_list = []
		for row in res:
			new_list.append({'id': row[0], 'username': row[1], 'email': row[2], 'register_date': row[4]})
		return new_list
