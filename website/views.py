from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def menu():
    return render_template('menu.html')

@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        # Logika tworzenia notatki
        # Pobierz dane z formularza
        title = request.form.get('title')
        content = request.form.get('content')
        # Wykonaj operacje zapisu notatki (np. w bazie danych)
        # ...
        return 'Notatka została utworzona!'
    return render_template('create_note.html')

@views.route('/delete_note')
def delete_note():
    # Logika usuwania notatki
    # ...
    return 'Notatka została usunięta!'
