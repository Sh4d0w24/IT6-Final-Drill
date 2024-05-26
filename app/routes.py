from app import app, mysql
from flask import jsonify

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM jake''')
    results = cur.fetchall()
    return jsonify(results)