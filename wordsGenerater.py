# Importing the Faker library
from faker import Faker

def createName():
    # Creating an instance of the Faker class to generate fake data
    fake = Faker()

    # Using list comprehension to create a list of 10 fake first names
    first_names = [fake.first_name() for _ in range(10)]
    print(first_names)

    # Defining the file name where the names will be saved
    file_path = "names.txt"

    # Opening the file in write mode
    with open(file_path, 'w') as f:
        for name in first_names:
            f.write(name + "\n") # Writing each name to the file followed by a newline
