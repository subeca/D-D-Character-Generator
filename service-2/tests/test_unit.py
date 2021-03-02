import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
import requests_mock

from application import app

class Testbase(TestCase):
    def create_app(self):
        return app

class TestCreate(Testbase):
    def test_char(self):
        for _ in range(10):
            response=self.client.get(url_for("race"))
            self.assertEqual(response.status_code,200)
            self.assertIn(response.data, [b"Dragonborn", b"Dwarf", b"Elf", b"Gnome", b"Half-Elf", b"Halfling", b"Half-Orc", b"Human", b"Tiefling"])