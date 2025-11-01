"""
Practical 05 - CP1404 - Hex Colours
"""

COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aqua": "#00ffff", "asparagus": "#87a96b",
                 "beige": "#f5f5dc", "bistre": "#3d2b1f", "black": "#000000", "blond": "faf0be",
                 "blueviolet": "#8a2be2", "brown": "#a52a2a"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name.title(), " is ", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name, try again.")
    colour_name = input("Enter a colour name: ").lower()
