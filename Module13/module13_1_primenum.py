from flask import Flask, request, Response
import json

from Module12.module12_1_chucknorris import response

app = Flask(__name__)

@app.route('/primetest/<number>')
def isprime(number):
    try:
        x = int(number)
    except ValueError:
        response = {
            "message": "Invalid input",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=400,
                                 mimetype="application/json")
        return http_response

    if x <= 0:
        response = {
            "error" : "A prime number must be greater than 0"
        }
        return response

    elif x > 0:
        # number to divide by
        y = 1

        # number of successful divisions
        z = 0

        # divide x by y until y == x
        try:
            for i in range(x):
                if x % y == 0:
                    z += 1
                y += 1

        except ValueError:
            response = {
                "message" : "Invalid input",
                "status" : 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response,
                                     status=400,
                                     mimetype="application/json")
            return http_response

        if z < 3:
            response = {
                "number" : x,
                "result" : "is prime"
            }
            return response
        else:
            response = {
                "number" : x,
                "result" : "not prime"
            }
            return response

if __name__ == '__main__':
    app.run(use_reloader=False,
            host='127.0.0.1',
            port=5000)