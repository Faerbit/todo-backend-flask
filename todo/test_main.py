import todo.main

import unittest
from flask import json

class MainTestCase(unittest.TestCase):

    def setUp(self):
        todo.main.app.config["TESTING"] = True
        self.app = todo.main.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cors_headers(self):
        response = self.app.get("/", headers={"Origin": "www.example.com"})
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "www.example.com")

    def test_index_allows_posts(self):
        response = self.app.post("/")
        self.assertEqual(response.status_code, 200)

    def test_index_returns_json(self):
        response = self.app.get("/" )
        json_ = json.loads(response.data)
        self.assertIsInstance(json_, dict)

if __name__ == "__main__":
    unittest.main()
