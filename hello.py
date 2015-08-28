from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "Hello World!"
    return render_template("base.html",title=title)

@app.route('/greet/<person>')
def greet_person(person):
    title = "Greetings!"
    return render_template("greet.html",title=title,person=person)

if __name__ == '__main__':
    app.run()
