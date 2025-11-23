"""
CP1404 Practical 09
Band Class
"""


class Band:
    """Band Class - a name and list of musicians"""
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())
