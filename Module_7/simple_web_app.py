from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])  # Fixed 'methods'
def add_todos():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_todo():
    todo = request.form.get('todo')
    if todo in todos:
        todos.remove(todo)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
