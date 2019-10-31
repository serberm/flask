from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Hello World!"

@app.route('/pidr/<name>')
def pidr(name):
  return "Ti pidr " + name
if __name__=="__main__":
    app.run(debug=True)