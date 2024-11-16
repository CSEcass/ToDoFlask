from flask import Flask, render_template, request
from tinydb import TinyDB, Query

db = TinyDB('./db.json')
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello():
    todoName = request.form.get('todoCre')
    if todoName == '':
        print('No Input.')
    else:
        db.insert({'Name': todoName})
    Name = todoName
    return render_template('index.html', Name=Name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')