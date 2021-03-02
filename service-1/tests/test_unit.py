#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
import requests_mock

from application import app, db
from application.models import Character

class Testbase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        test_character=Character(character_class="Paladin", character_race="Gnome", character_trait="Super evil")
        db.session.add(test_character)
        db.session.commit()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCreate(Testbase):
    def test_char(self):
        with requests_mock.mock() as r:
            r.get("http://roller_service-2:5000/race", text="Human")
            r.get("http://roller_service-3:5000/class0", text="Barbarian")
            r.get("http://roller_service-4:5000/trait", text="Drunken")
            response=self.client.get(url_for("index"))
            self.assertEqual(response.status_code,200)
            self.assertIn(b'A Drunken Human Barbarian', response.data)
