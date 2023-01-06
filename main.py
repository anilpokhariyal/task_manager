from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models.connection import db
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

@app.route("/")
def dashboard():
	return "Welcome"



###############################################################################
# Manager commands
###############################################################################
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
	manager.run()
	# db object required app context to run
	with app.app_context():
		db.create_all()

	app.run(host="0.0.0.0", port=5000, debug=True)

