#!/usr/bin/env python3

import main

import unittest

class MainTestCase(unittest.TestCase):

    def setUp(self):
        main.app.config["TESTING"] = True
        self.app = main.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cors_headers(self):
        response = self.app.get("/", headers={"Origin": "www.example.com"})
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "www.example.com")

    def test_index_allows_posts(self):
        response = self.app.post("/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
