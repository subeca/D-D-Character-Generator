#!/usr/bin/python3

from application import app, db
from application.models import Character
from flask import request, render_template, jsonify
import requests
import random
from sqlalchemy import desc

@app.route('/')
def index():
    race1 = requests.get("http://service-2:5001/race")
    class1 = requests.get("http://service-3:5002/class0")
    trait=requests.get("http://service-4:5003/trait", json={"class2":class1.text, "race2":race1.text})
    char=Character.query.order_by(desc("Id")).limit(5).all()
    maxno=Character.query.order_by(desc("Id")).first()
    randno=random.randint(1,maxno.Id)
    randchar=Character.query.filter_by(Id=randno).all()
    new_character= Character(character_class=class1.text, character_race=race1.text, character_trait=trait.text)
    
    db.session.add(new_character)
    db.session.commit()
    
    old_characters = Character.query.order_by(desc("Id")).limit(3).all()

    return render_template("index.html", race=race1.text, class0=class1.text, trait=trait.text, char=char, randchar=randchar)
