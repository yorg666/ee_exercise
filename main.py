from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_there():
    return "Hello EE, Krystian Nowaczyk here, can anyone hear me?"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
