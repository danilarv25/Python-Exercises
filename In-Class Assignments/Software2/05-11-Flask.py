from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/sum/<number1>+<number2>')
def calculate_sum(number1, number2):
    try:
        num1 = float(number1)
        num2 = float(number2)
        total_sum = num1 + num2

        response = {
            "number1": num1,
            "number2": num2,
            "total_sum": total_sum
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=400,
                                 mimetype="application/json")
        return http_response

@app.route('/difference/<number1>-<number2>')
def calculate_difference(number1, number2):
    try:
        num1 = float(number1)
        num2 = float(number2)
        total = num1 - num2

        response = {
            "number1": num1,
            "number2": num2,
            "difference": total
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=400,
                                 mimetype="application/json")
        return http_response

@app.route('/fraction-float/<number1>/<number2>')
def calculate_fraction(number1, number2):
    try:
        num1 = float(number1)
        num2 = float(number2)
        total_sum = num1 / num2

        response = {
            "number1": num1,
            "number2": num2,
            "float": total_sum
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=400,
                                 mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 400
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response,
                             status=404,
                             mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=False,
            host='127.0.0.1',
            port=5000)
