from django.db import models


import json
import random
import os

# Create your models here.
class Quotes():
    def __init__(self, json_file):

        with open("quote_app/json/" + json_file) as json_file:
            data = json.load(json_file)
        self.data = dict(data)

    def get_random_quote(self):
        quote_header = random.choice(list(self.data.keys()))
        random_qoute = random.choice(self.data[quote_header])
        return (quote_header, random_qoute)

    def get_all_keys(self):
        return list(self.data.keys())