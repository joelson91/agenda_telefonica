from flask import render_template, request, redirect, url_for
from models.user import Contato, db
from form import UserForm


class UserController:
    @staticmethod
    def index():
        contatos = Contato.query.all()
        return render_template("index.html", contatos=contatos)

    @staticmethod
    def add_user():
        form = UserForm()

        if request.method == "POST":
            nome = request.form["nome"]
            telefone = request.form["telefone"]
            email = request.form["email"]

            novo_contato = Contato(nome=nome, telefone=telefone, email=email)
            db.session.add(novo_contato)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("insert.html", form=form)

    @staticmethod
    def update_user(id):
        contato = Contato.query.get_or_404(id)
        form = UserForm(obj=contato)

        if request.method == "POST":
            contato.nome = request.form["nome"]
            contato.telefone = request.form["telefone"]
            contato.email = request.form["email"]

            db.session.commit()
            return redirect(url_for("index"))

        return render_template("update.html", contato=contato, form=form)

    @staticmethod
    def delete_user(id):
        contato = Contato.query.get_or_404(id)
        db.session.delete(contato)
        db.session.commit()
        return redirect(url_for("index"))
