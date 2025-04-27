import genanki
import json
from random import randrange

def generate_deck(model):
    # Load your JSON data
    with open(f'data/{model}.json', 'r', encoding='utf-8') as f:
        cards = json.load(f)
    
    # Define a model (note type)
    my_model = genanki.Model(
        # Random model ID (must be unique)
        randrange(1_000_000_000, 10_000_000_000),
        'Basic Model',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
            },
        ])
    
    # Create a deck
    my_deck = genanki.Deck(
        randrange(1_000_000_000, 10_000_000_000),  # Random deck ID (must be unique)
        f'{model}')
    
    # Add notes to the deck
    for card in cards:
        my_note = genanki.Note(
            model=my_model,
            fields=[card['front'], card['back']])
        my_deck.add_note(my_note)
    
    # Save the deck to an .apkg file
    genanki.Package(my_deck).write_to_file(f'output/{model}.apkg')

if __name__ == "__main__":
    for model in ["hsk1", "hsk2"]:
        generate_deck(model)
