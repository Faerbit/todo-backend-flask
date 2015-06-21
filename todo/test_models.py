from todo.test_base import BaseTestCase

from todo.models import Entry
from todo.database import db_session

class EntryTestCase(BaseTestCase):

    def test_string_representation(self):
        text = "some text"
        entry = Entry(text)
        db_session.add(entry)
        db_session.commit()
        query = Entry.query.all()[0]
        self.assertEqual(str(query), "<Entry: " + text + ">")
