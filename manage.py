import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_object(os.environ["APP_SETTINGS"])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)
# added the db command to the manager so that we can run the migrations from the command line.
# python3 manage.py db init

if __name__ == "__main__":
	manager.run()

