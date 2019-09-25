from flask_script import Command
from flask_kakeibo import db


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
