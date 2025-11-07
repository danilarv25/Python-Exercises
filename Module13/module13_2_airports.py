from flask import Flask, request, Response
import json
import mariadb

from Module12.module12_1_chucknorris import response

app = Flask(__name__)

@app.route('/airport/<code>')
def get_airport_basic(code):
    try:
        connection = mariadb.connect(
            host='127.0.0.1',
            port=3306,
            user='reader',
            password='Oklg2302!le',
            database='flight_game',
            autocommit=True
        )
    except mariadb.OperationalError:
        response = {
            "message" : "Unable to establish connection to database",
            "status" : 500
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=500,
                                 mimetype="application/json")
        return http_response

    sql = """
          select ident, name, municipality
          from airport
          where ident = ?
          """

    cursor = connection.cursor()
    cursor.execute(sql,(code,))
    results = cursor.fetchall()
    if results:
        response = {
            "ICAO" : results[0][0],
            "Name" : results[0][1],
            "Location" : results[0][2]
        }
        cursor.close()
        return response
    else:
        response = {
            "Message" : "No data matched given code"
        }
        cursor.close()
        return response

if __name__ == '__main__':
    app.run(use_reloader=False,
            host='127.0.0.1',
            port=5000)
