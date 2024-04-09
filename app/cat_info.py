from dataclasses import dataclass
from typing import List

# Importing necessary modules


@dataclass
class Cat:
    name: str
    description: str


# Defining a data class called "Cat" using the @dataclass decorator.
# A data class is a class that is primarily used to store data.
# It automatically generates special methods like __init__, __repr__, and __eq__.

CAT = {
    "S'more": Cat(
        "S'more",
        "Kariel's second son",
    ),
    "Finn": Cat(
        "Finn",
        "Kariel's first son",
    ),
    "Yams": Cat(
        "Yams",
        "Kariel's second daughter",
    ),
}

# Creating a dictionary called "CAT" that stores instances of the "Cat" class.
# The keys of the dictionary are the names of the cats, and the values are the corresponding Cat objects.
# Each Cat object is created using the class constructor and initialized with a name and description.
