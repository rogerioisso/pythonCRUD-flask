from flask import flash, render_template, request, redirect
from app import app, db

from app.models.tables import User, locado, Results
from app.models.form import LoginForm, CreateForm, UpdateForm


@app.route("/", methods=["GET", "POST"])
@app.route("/login")
@app.route("/logout")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    print(form.errors)
    return render_template('login.html',
                            form=form)

@app.route("/home", methods=["GET", "POST"])
def index():
    results = []
    showall = db.session.query(locado)
    results = showall.all()
    table = Results(results)
    table.border = True
    return render_template('show.html',
                                  showall=showall,
                                  table=table)

@app.route("/add",  methods=["GET", "POST"])
def add():
    addForm = CreateForm(request.form)
    locados = locado()
    if addForm.validate_on_submit():
        salvar_alteracao(locados, addForm, new=True)
        return render_template('ok.html')
    print(addForm.errors)
    return render_template('add.html',
                            addForm=addForm,
                            locados=locados)

def salvar_alteracao(locados, addForm, new=False):

    locados.nome = addForm.nome.data
    locados.cpf = addForm.cpf.data
    locados.telcont = addForm.telcont.data
    locados.telcont_pais = addForm.telcont_pais.data
    locados.data_al = addForm.data_al.data

    if new:
        db.session.add(locados)

    db.session.commit()





@app.route("/editar", methods=["GET", "POST"])
def update():
    showall = ""
    results = []
    table = []
    updateForm = UpdateForm()
    if updateForm.validate_on_submit():
        if updateForm.nome_search.data == "":
            showall = db.session.query(locado)
            results = showall.all()
            table = Results(results)
            table.border = True
        else:
            showall = locado.query.filter(locado.nome==updateForm.nome_search.data)
            results = showall.all()
            table = Results(results)
            table.border = True
        print(showall)

    print(updateForm.errors)
    return render_template('editar.html',
                            updateForm=updateForm,
                            table=table,
                            showall=showall)

@app.route("/edicao/<int:id>", methods=["GET", "POST"])
def edicao(id):
    query = db.session.query(locado).filter(locado.id==id)
    locados = query.first()

    if locados:
        addForm = CreateForm(request.form)
        if request.method == 'POST' and addForm.validate():
            # save edits
            salvar_alteracao(locados, addForm)
            return render_template('ok.html')
        return render_template('edicao.html', addForm=addForm)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route("/deletar/<int:id>")
def deletar(id):
    query = db.session.query(locado).filter(locado.id==id).delete(),,,,00

    db.session.commit()

    return redirect('/home')
