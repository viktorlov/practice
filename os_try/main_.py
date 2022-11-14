from data.data_ import data_ as df
import json

print(df)

with open('data/data_.json') as file0:
    questions = json.load(file0)

print(questions)
