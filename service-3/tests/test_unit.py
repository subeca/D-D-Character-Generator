#!/usr/bin/python3

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
            response=self.client.get(url_for("class0"))
            self.assertEqual(response.status_code,200)
            self.assertIn(response.data, [b"Barbarian", b"Bard", b"Cleric", b"Druid", b"Fighter", b"Monk", b"Paladin", b"Ranger", b"Rogue", b"Sorceror", b"Warlock", b"Wizard", b"Artificer"])