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
        response=self.client.post(url_for("trait"), json={"class2":"Barbarian", "race2":"Dwarf"})
        self.assertEqual(response.status_code,200)
        self.assertIn(response.data, [b"Meaty", b"Completely useless", b"Super bad", b"Rabid", b"Extremely fat", b"Too greedy", b"Irresponsible when drunk" ])
