#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/trait", methods=["GET", "POST"])
def trait():
    desc= {
        "Barbarian":"Rabid",
        "Bard":"Ugly as sin but still charasmatic", 
        "Cleric":"Bright",
        "Druid":"Hairy",
        "Fighter":"Brainless",
        "Monk":"Drunken",
        "Paladin":"Overzealous",
        "Ranger":"Spider obsessed",
        "Rogue":"Shady",
        "Sorceror":"Overpowered",
        "Warlock":"Patron fearing",
        "Wizard":"Mad",
        "Artificer":"Genius", 
        "Blood-hunter":"Sadistic beyond belief",
        "Dragonborn":"Greeed"
        "Dwarf":"Extremely fat",
        "Elf":"Really old",
        "Gnome":"Halfling looking",
        "Halfling":"More agile than a bunny", 
        "Half-Elf":"Good at eveything",
        "Half-Orc":"Stronger than everyone", 
        "Human":"Boring",
        "Tiefling":"Conniving"

    char=request.get_json()
    race= char["race2"]
    class1= char["class2"]
    a= ["Completely stubborn", "Super bad"]
    a.extend(desc[class1])
    a.extend(desc[race])
    b=random.choice(a)

    return Response(b, mimetype="text/plain")