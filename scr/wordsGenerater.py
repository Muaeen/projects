# Importing necessary libraries
from faker import Faker
import yaml

def load_config():
    with open("./config/config.yaml", "r") as f:
        return yaml.safe_load(f)
        

def createName():
    # Creating an instance of the Faker class to generate fake data
    fake = Faker()

    config = load_config()

    # Using list comprehension to create a list of 10 fake first names
    first_names = [fake.first_name() for _ in range(10)]
    

    # Defining the file name where the names will be saved
    file_path = config['pathes']['text_path']

    # Opening the file in write mode
    with open(file_path, 'w') as f:
        for name in first_names:
            f.write(name + "\n") # Writing each name to the file followed by a newline
