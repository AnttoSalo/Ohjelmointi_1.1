from flask import Flask, jsonify
import mariadb
import os
import sys

app = Flask(__name__)

try:
    conn = mariadb.connect(
        user="root",
        password=os.environ.get("DBPASS") or "admin",
        host="localhost",
        port=3306,
        database="flight_game"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = conn.cursor()


@app.route('/airport/<icao>')
def kentan_tiedot(icao):
    cursor.execute(
        "SELECT name, municipality FROM airport WHERE ident=?", (icao,))
    result = cursor.fetchone()
    if result is None:
        return jsonify({"error": "Lentokenttää ei löydy"})
    else:
        return jsonify({"ICAO": icao, "Name": result[0], "Municipality": result[1]})


if __name__ == '__main__':
    app.run(port=3000)
