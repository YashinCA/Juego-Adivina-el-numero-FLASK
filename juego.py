from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session['numero'] = int(round(random.random()*((100-0))+0))
    print(session['numero'])
    session['contador'] = 0
    return redirect("/juego")


@app.route("/juego")
def numerorandom():
    print("###############")
    print(request.form)
    print(session['numero'])
    session['numerousuario'] = 0
    print(session['numerousuario'])
    print("###############")
    temp = 0
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    oportunidades = 6
    return render_template('juegoplantilla.html', numerorandom=session['numero'], numerodeusuario=session['numerousuario'], contador=session['contador'], oportunidades=6-session['contador'])


@app.route('/juego', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    esnumero = int(request.form['numerousuario'].isnumeric())
    print(esnumero)
    validador = False
    if (esnumero == True):
        numusuario = int(request.form['numerousuario'])
        if((numusuario > 0) and (numusuario <= 100)):
            session['numerousuario'] = int(request.form['numerousuario'])
            texto_h3 = ''
            if session['numero'] == int(request.form['numerousuario']):
                texto_h3 = f"Great! The Number is {session['numero']}"

            if session['contador'] == 5:
                texto_h3 = f"GAME OVER"
                validador = True

            else:
                if (session['numero'] < int(request.form['numerousuario'])) and (validador == False):
                    texto_h3 = "Too High!!"
                    session['contador'] += 1
                if (session['numero'] > int(request.form['numerousuario'])) and (validador == False):
                    texto_h3 = "Too Low!!"
                    session['contador'] += 1

            return render_template("juegoplantilla.html", numerodeusuario=session['numerousuario'], numerorandom=int(session['numero']), texto_h3=texto_h3, contador=session['contador'], oportunidades=6-session['contador'], validador=validador)

    session['numerousuario'] = 0
    # session.pop('contador')
    session['contador'] -= 1
    return redirect("/juego")


if __name__ == "__main__":
    app.run(debug=True)
