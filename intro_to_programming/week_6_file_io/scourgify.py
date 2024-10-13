"""
“Ah, well,” said Tonks, slamming the trunk's lid shut, “at least it's all in. That could do with a bit of cleaning, too.”
She pointed her wand at Hedwig's cage. “Scourgify.” A few feathers and droppings vanished.

— Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format.
Consider, for instance, this CSV file of students, before.csv, below:

name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
"Bulstrode, Millicent",Slytherin
"Chang, Cho",Ravenclaw
"Clearwater, Penelope",Ravenclaw
"Crabbe, Vincent",Slytherin
"Creevey, Colin",Gryffindor
"Creevey, Dennis",Gryffindor
"Diggory, Cedric",Hufflepuff
"Edgecombe, Marietta",Ravenclaw
"Finch-Fletchley, Justin",Hufflepuff
"Finnigan, Seamus",Gryffindor
"Goldstein, Anthony",Ravenclaw
"Goyle, Gregory",Slytherin
"Granger, Hermione",Gryffindor
"Johnson, Angelina",Gryffindor
"Jordan, Lee",Gryffindor
"Longbottom, Neville",Gryffindor
"Lovegood, Luna",Ravenclaw
"Lupin, Remus",Gryffindor
"Malfoy, Draco",Slytherin
"Malfoy, Scorpius",Slytherin
"Macmillan, Ernie",Hufflepuff
"McGonagall, Minerva",Gryffindor
"Midgen, Eloise",Gryffindor
"McLaggen, Cormac",Gryffindor
"Montague, Graham",Slytherin
"Nott, Theodore",Slytherin
"Parkinson, Pansy",Slytherin
"Patil, Padma",Gryffindor
"Patil, Parvati",Gryffindor
"Potter, Harry",Gryffindor
"Riddle, Tom",Slytherin
"Robins, Demelza",Gryffindor
"Scamander, Newt",Hufflepuff
"Slughorn, Horace",Slytherin
"Smith, Zacharias",Hufflepuff
"Snape, Severus",Slytherin
"Spinnet, Alicia",Gryffindor
"Sprout, Pomona",Hufflepuff
"Thomas, Dean",Gryffindor
"Vane, Romilda",Gryffindor
"Warren, Myrtle",Ravenclaw
"Weasley, Fred",Gryffindor
"Weasley, George",Gryffindor
"Weasley, Ginny",Gryffindor
"Weasley, Percy",Gryffindor
"Weasley, Ron",Gryffindor
"Wood, Oliver",Gryffindor
"Zabini, Blaise",Slytherin
Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name),
escaped with double quotes, with last name and first name separated by a comma and space.
Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it'd be strange to start a letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read,
the program should exit via sys.exit with an error message.
"""
import sys
import csv

def main():
    words = sys.argv
    readArgument(words)
    read = words[1]
    write = words[2]
    data_to_write = readWriteFile(read)
    writeFile(data_to_write, write)

#could be done via import
def readArgument(words):
    if len(words) < 3:
        sys.exit("Too few command-line arguments")
    if len(words) > 3:
        sys.exit("Too many command-line arguments")
    if '.csv' not in words[1]:
        sys.exit("Not a CSV file")
    if '.csv' not in words[2]:
        sys.exit("Not a CSV file")
    try:
        open(words[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {words[1]}")

def readWriteFile(read_file):
    names = []
    with open(read_file, 'r', newline='') as csv_read:
        reader = csv.DictReader(csv_read)
        keys = list(reader.fieldnames)
        for data_read in reader:
            full_names = {}
            last, first = data_read[keys[0]].split(',')
            full_names['first'] = first.strip()
            full_names['last'] = last.strip()
            full_names['house'] = data_read[keys[1]]
            names.append(full_names)
    csv_read.close()
    return names

def writeFile(data, write_file):
    with open(write_file, 'w', newline='') as csv_write:
        name_keys = ['first', 'last', 'house']
        writer = csv.DictWriter(csv_write, fieldnames=name_keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()