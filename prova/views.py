from prova import app, db
from flask import render_template, url_for, request, redirect

from prova.models import Telefone




@app.route('/', methods=['GET', 'POST'])
def about(): 
    context = {}
    nome = None
    cpf = None
    if request.method == 'POST':
         nome = request.form.get('nome')
         cpf = request.form.get('cpf')

         telefone = Telefone(
             nome = nome,
             cpf = cpf 
       ) 
         


         db.session.add(telefone)
         db.session.commit()
         return redirect(url_for('index'))

    return render_template('teste.html', context=context)


# views.py

@app.route('/', methods=['GET'])  # <--- Adicione isto!
def index():
    context = {
        'usuarios': 'usuarios',
    }
    return render_template('index.html', context=context)