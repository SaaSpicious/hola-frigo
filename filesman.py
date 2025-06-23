# Contains functions covering file handling
import json

# Write dictionary to filename
def write_dict_to_file(dictionary, filename):
    filename = f"./store/{filename}"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

# Reads the dictionary from a file
def read_dict_from_file(filename):
    filename = f"./store/{filename}"
    #If file not found, return empty dictionary.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []