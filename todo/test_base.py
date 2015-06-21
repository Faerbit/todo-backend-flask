import todo.main
from todo.database import init_db, Base, engine

import unittest
import os

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        todo.main.app.config["TESTING"] = True
        if os.environ.get("CI"):
            todo.main.app.config["DATABASE"] = "postgresql://ubuntu:@localhost/circle_test"
        else:
            todo.main.app.config["DATABASE"] = "sqlite://"
        self.app = todo.main.app.test_client()
        init_db()

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)
