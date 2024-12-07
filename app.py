from flask import Flask, render_template, request, redirect
from tinydb import TinyDB, Query

db = TinyDB('db.json')
app = Flask(__name__)
todo = Query()
    
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        Name = request.form.get('todoName')
        Desc = request.form.get('todoDesc')
        db.insert({'Name': Name,'Desc': Desc})
    todos = db.all()
    return render_template('index.html', todos=todos)
@app.route('/dele', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        todoDel = request.form.get('todoDel')
        db.remove(todo.Name == todoDel)
    return redirect('/')
@app.route('/upda', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        Name = request.form.get('todoUpd')
        Newname = request.form.get('updName')
        Newdesc = request.form.get('updDesc')
        db.update({'Name': Newname,'Desc': Newdesc}, todo.Name == Name)
    todos = db.all()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')