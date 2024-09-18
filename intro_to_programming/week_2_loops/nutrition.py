"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently
consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print,
display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of
calories in one portion of that fruit, per the FDA's poster for fruits, which is also available as text.
Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn't a fruit.
"""
fruits = [
    {"name":"apple", "serving_size":"242 grams", "calories":130},
    {"name":"avocado", "serving_size":"30 grams", "calories":50},
    {"name":"banana", "serving_size":"126 grams", "calories":110},
    {"name":"cantaloupe", "serving_size":"134 grams", "calories":50},
    {"name":"grapefruit", "serving_size":"154 grams", "calories":60},
    {"name":"grapes", "serving_size":"126 grams", "calories":90},
    {"name":"honeydew melon", "serving_size":"134 grams", "calories":50},
    {"name":"kiwifruit", "serving_size":"148 grams", "calories":90},
    {"name":"lemon", "serving_size":"58 grams", "calories":15},
    {"name":"lime", "serving_size":"67 grams", "calories":20},
    {"name":"nectarine", "serving_size":"140 grams", "calories":60},
    {"name":"orange", "serving_size":"154 grams", "calories":80},
    {"name":"peach", "serving_size":"147 grams", "calories":60},
    {"name":"pear", "serving_size":"166 grams", "calories":100},
    {"name":"pineapple", "serving_size":"112 grams", "calories":50},
    {"name":"plums", "serving_size":"151 grams", "calories":70},
    {"name":"strawberries", "serving_size":"147 grams", "calories":50},
    {"name":"sweet cherries", "serving_size":"140 grams", "calories":100},
    {"name":"tangerine", "serving_size":"109 grams", "calories":50},
    {"name":"watermelon", "serving_size":"280 grams", "calories":80}
]
search = input("Item: ").lower()
for fruit in fruits:
    if fruit["name"] == search:
        print("Calories:", fruit["calories"])