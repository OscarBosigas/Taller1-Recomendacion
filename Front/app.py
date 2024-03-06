from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de usuarios (esto debería ser una base de datos en un entorno real)
users = {'usuario': 'contraseña'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            return render_template('login.html', message='Usuario o contraseña incorrectos')
    return render_template('login.html', message='')

@app.route('/success')
def success():
    return 'Inicio de sesión exitoso'

if __name__ == '__main__':
    app.run(debug=True)
