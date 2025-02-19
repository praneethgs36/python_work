glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'A collection in which each item must be unique.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'integer': 'A numerical value without a decimal component.',
    'boolean': 'A value representing either True or False.',
    'item()' : 'A method that returns a key-value pair in a dictionary.',
    }

for term in glossary:
    print(f"{term.title()}: {glossary[term]}\n")