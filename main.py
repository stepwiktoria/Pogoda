from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create_note():
    return render_template('create_note.html')

@app.route('/delete')
def delete_note():
    return render_template('delete_note.html')

if __name__ == '__main__':
    app.run()
