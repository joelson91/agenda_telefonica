import os
from flask import Flask
from config import Config
from controllers.user_controller import UserController
from models.user import db


app = Flask(__name__, template_folder=os.path.join("view", "templates"))
app.config.from_object(Config)


db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule("/", "index", UserController.index)
app.add_url_rule("/criar", "add_user", UserController.add_user, methods=["GET", "POST"])
app.add_url_rule("/editar/<int:id>", "update_user", UserController.update_user, methods=["GET", "POST"])
app.add_url_rule("/excluir/<int:id>", "delete_user", UserController.delete_user)


if __name__ == "__main__":
    app.run(debug=True)
