#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/race", methods=["GET"])
def race():
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
    race= random.choice(races)
    return Response(str(race), mimetype="text/plain")