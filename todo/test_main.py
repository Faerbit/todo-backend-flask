from todo.test_base import BaseTestCase

import unittest
from flask import json

class MainTestCase(BaseTestCase):

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cors_headers(self):
        response = self.app.get("/", headers={"Origin": "www.example.com"})
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "www.example.com")

    def test_index_allows_posts(self):
        data = dict(title="some text")
        response = self.app.post("/", data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_index_returns_json(self):
        response = self.app.get("/" )
        json_ = json.loads(response.data)
        self.assertIsInstance(json_, dict)

    def test_index_returns_entry(self):
        data = dict(title="some other text")
        response = self.app.post("/", data=json.dumps(data), content_type="application/json")
        self.assertEqual(data, json.loads(response.data))

if __name__ == "__main__":
    unittest.main()
