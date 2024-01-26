import json

# Lataa tiedostotyypit json-tiedostosta.
with open('file_types.json') as f:
    FILE_TYPES = json.load(f)
