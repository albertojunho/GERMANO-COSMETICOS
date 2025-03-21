from flask import Flask,render_template


app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template('cadastro.html')

if __name__ == '__app__':
    app.run()