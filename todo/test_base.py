from todo import app
from todo.database import init_db, Base, engine, drop_tables

import unittest
import os

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        if os.environ.get("CI"):
            app.config["DATABASE"] = "postgresql://ubuntu:@localhost/circle_test"
        else:
            app.config["DATABASE"] = "sqlite://"
        self.app = app.test_client()
        init_db()
        self.context = app.test_request_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()
        drop_tables()
