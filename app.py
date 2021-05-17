from flask import Flask, render_template, request, json
from functions import add_function, subtract_function, multiply_function, division_function, sqrt_function
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기
@app.route("/add", methods=["GET"])
def add():
    num1, num2 = request.args.get("num1"), request.args.get("num2")
    result = add_function(num1, num2)
    if result == "check parameter":
        response = app.response_class(
            response=json.dumps(result),
            status=400,
            mimetype='application/json'
        )
    else:
        result = "{} + {} = {}".format(num1, num2, result)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/subtract", methods=["GET"])
def subtract():
    num1, num2 = request.args.get("num1"), request.args.get("num2")
    result = subtract_function(num1, num2)
    if result == "check parameter":
        response = app.response_class(
            response=json.dumps(result),
            status=400,
            mimetype='application/json'
        )
    else:
        result = "{} - {} = {}".format(num1, num2, result)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/multiply", methods=["GET"])
def multiply():
    num1, num2 = request.args.get("num1"), request.args.get("num2")
    result = multiply_function(num1, num2)
    if result == "check parameter":
        response = app.response_class(
            response=json.dumps(result),
            status=400,
            mimetype='application/json'
        )
    else:
        result = "{} * {} = {}".format(num1, num2, result)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/division", methods=["GET"])
def division():
    num1, num2 = request.args.get("num1"), request.args.get("num2")
    result = division_function(num1, num2)
    if result == "check parameter":
        response = app.response_class(
            response=json.dumps(result),
            status=400,
            mimetype='application/json'
        )
    else:
        result = "{} // {} = {}".format(num1, num2, result)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/sqrt", methods=["GET"])
def sqrt():
    num = request.args.get("num")
    result = sqrt_function(num)
    if result == "check parameter":
        response = app.response_class(
            response=json.dumps(result),
            status=400,
            mimetype='application/json'
        )
    else:
        result = "root {} = {}".format(num, result)
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
