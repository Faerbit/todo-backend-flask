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

    def test_entries_get_created_unfinished(self):
        entry = Entry("some text")
        db_session.add(entry)
        db_session.commit()
        query = Entry.query.filter(Entry.completed == True).first()
        self.assertEqual(None, query)
        query = Entry.query.filter(Entry.completed == False).first()
        self.assertEqual(entry, query)

    def test_entries_are_ordered(self):
        text1 = "some text"
        text2 = "more text"
        text3 = "additional text"
        entry1 = Entry(text1)
        db_session.add(entry1)
        entry2 = Entry(text2)
        db_session.add(entry2)
        entry3 = Entry(text3)
        db_session.add(entry3)
        db_session.commit()
        query = Entry.query.all()
        self.assertEqual([entry1, entry2, entry3], query)
        self.assertNotEqual([entry2, entry1, entry3], query)

    def test_entries_can_be_created_with_order(self):
        text  = "text"
        order = 10
        entry = Entry(text, order)
        db_session.add(entry)
        db_session.commit()
        query = Entry.query.all()
        self.assertEqual([entry], query)
