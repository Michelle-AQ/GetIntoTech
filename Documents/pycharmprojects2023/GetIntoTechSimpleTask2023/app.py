from flask import Flask, Response, request


app = Flask(__name__)

# different HTTP methods
# when making a request on a site -  we return a response
# building a web API - we return data

@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"

@app.route('/bye')
def bye_from_flask():
    return "Goodbye from Flask! See you again soon."

@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit response object", mimetype='text/plain')


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You sent this data: " + data_sent)

@app.route('/dynamic/<word>')
def dynamic_route_a(word):
    return "Echo " + word

@app.route('/square/<int:number>')
def square(number):
    squared_number = number ** 2
    message = "Your number squared is: " + str(squared_number)
    return message


@app.route('/greeting/<name>')
def hi_greeting(name):
    return "Hi " + name



if __name__ == "__main__":
    app.run(debug=True)

# main trick always goes at the bottom

