from flask import Flask, jsonify
from database.database import Database as db

app = Flask(__name__)

database = db('database/database.db')


@app.route('/api/users', methods=['GET'])
def get_users():

	data = database.multy_read_database()
	return jsonify(data)


if __name__ == '__main__':
	app.run()
