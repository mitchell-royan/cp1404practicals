"""
Practical 07 - Project class file
Estimated Time: 15 minutes
Actual Time: 25 minutes
"""


class Project:
    """A project with name, start date priority, cost estimate and completion percentage"""
    def __init__(self, name, start_date, priority, cost_estimate, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        start_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_str}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f},"
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Order by priority (ascending)"""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if project is fully complete"""
        return self.completion >= 100

    def starts_after(self, other_date):
        """Return true if the start date is after the given date"""
        return self.start_date > other_date
