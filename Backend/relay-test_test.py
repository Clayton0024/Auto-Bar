import os
import sqlite3
from string import ascii_uppercase
from CocktailDB import CocktailDBAPI
import time

# Establish Connection
conn = sqlite3.connect('cocktails.db')
cursor = conn.cursor()

# Instantiate API
api = CocktailDBAPI(os.getenv("API_KEY"))

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktails (
    idDrink TEXT PRIMARY KEY,
    strDrink TEXT,
    strDrinkAlternate TEXT,
    strTags TEXT,
    strVideo TEXT,
    strCategory TEXT,
    strIBA TEXT,
    strAlcoholic TEXT,
    strGlass TEXT,
    strInstructions TEXT,
    strInstructionsES TEXT,
    strInstructionsDE TEXT,
    strInstructionsFR TEXT,
    strInstructionsIT TEXT,
    strInstructionsZH_HANS TEXT,
    strInstructionsZH_HANT TEXT,
    strDrinkThumb TEXT,
    strIngredient1 TEXT,
    strIngredient2 TEXT,
    strIngredient3 TEXT,
    strIngredient4 TEXT,
    strIngredient5 TEXT,
    strIngredient6 TEXT,
    strIngredient7 TEXT,
    strIngredient8 TEXT,
    strIngredient9 TEXT,
    strIngredient10 TEXT,
    strIngredient11 TEXT,
    strIngredient12 TEXT,
    strIngredient13 TEXT,
    strIngredient14 TEXT,
    strIngredient15 TEXT,
    strMeasure1 TEXT,
    strMeasure2 TEXT,
    strMeasure3 TEXT,
    strMeasure4 TEXT,
    strMeasure5 TEXT,
    strMeasure6 TEXT,
    strMeasure7 TEXT,
    strMeasure8 TEXT,
    strMeasure9 TEXT,
    strMeasure10 TEXT,
    strMeasure11 TEXT,
    strMeasure12 TEXT,
    strMeasure13 TEXT,
    strMeasure14 TEXT,
    strMeasure15 TEXT,
    strImageSource TEXT,
    strImageAttribution TEXT,
    strCreativeCommonsConfirmed TEXT,
    dateModified TEXT,
    letter TEXT
);
''')
conn.commit()

# Loop over each letter of the alphabet
for letter in ascii_uppercase:
    response_data = api.get_cocktails_by_first_letter(letter)
    cocktails = response_data.get('drinks', [])
    for cocktail in cocktails:
        try:
            cursor.execute('''
            INSERT INTO cocktails (
            idDrink, strDrink, strDrinkAlternate, strTags, strVideo, strCategory,
            strIBA, strAlcoholic, strGlass, strInstructions, strInstructionsES,
            strInstructionsDE, strInstructionsFR, strInstructionsIT, strInstructionsZH_HANS,
            strInstructionsZH_HANT, strDrinkThumb, strIngredient1, strIngredient2, strIngredient3,
            strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8,
            strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13,
            strIngredient14, strIngredient15, strMeasure1, strMeasure2, strMeasure3, strMeasure4,
            strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10,
            strMeasure11, strMeasure12, strMeasure13, strMeasure14, strMeasure15, strImageSource,
            strImageAttribution, strCreativeCommonsConfirmed, dateModified, letter)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                cocktail.get('idDrink'), cocktail.get('strDrink'), cocktail.get('strDrinkAlternate'),
                cocktail.get('strTags'), cocktail.get('strVideo'), cocktail.get('strCategory'),
                cocktail.get('strIBA'), cocktail.get('strAlcoholic'), cocktail.get('strGlass'),
                cocktail.get('strInstructions'), cocktail.get('strInstructionsES'), cocktail.get('strInstructionsDE'),
                cocktail.get('strInstructionsFR'), cocktail.get('strInstructionsIT'), cocktail.get('strInstructionsZH_HANS'),
                cocktail.get('strInstructionsZH_HANT'), cocktail.get('strDrinkThumb'), cocktail.get('strIngredient1'),
                cocktail.get('strIngredient2'), cocktail.get('strIngredient3'), cocktail.get('strIngredient4'),
                cocktail.get('strIngredient5'), cocktail.get('strIngredient6'), cocktail.get('strIngredient7'),
                cocktail.get('strIngredient8'), cocktail.get('strIngredient9'), cocktail.get('strIngredient10'),
                cocktail.get('strIngredient11'), cocktail.get('strIngredient12'), cocktail.get('strIngredient13'),
                cocktail.get('strIngredient14'), cocktail.get('strIngredient15'), cocktail.get('strMeasure1'),
                cocktail.get('strMeasure2'), cocktail.get('strMeasure3'), cocktail.get('strMeasure4'),
                cocktail.get('strMeasure5'), cocktail.get('strMeasure6'), cocktail.get('strMeasure7'),
                cocktail.get('strMeasure8'), cocktail.get('strMeasure9'), cocktail.get('strMeasure10'),
                cocktail.get('strMeasure11'), cocktail.get('strMeasure12'), cocktail.get('strMeasure13'),
                cocktail.get('strMeasure14'), cocktail.get('strMeasure15'), cocktail.get('strImageSource'),
                cocktail.get('strImageAttribution'), cocktail.get('strCreativeCommonsConfirmed'), cocktail.get('dateModified'),
                letter
            ))
        except sqlite3.OperationalError as e:
            print(f"Error inserting {cocktail.get('strDrink')}: {e}")
            
    conn.commit()  # Commit after inserting all cocktails for a given letter
    time.sleep(1.0)

# Close connection to the database
conn.close()
