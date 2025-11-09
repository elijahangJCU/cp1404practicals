import datetime

"""
Module for managing projects with attributes such as name, start date, priority,
cost estimate, and completion percentage.

Time estimate: TBD
"""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.start_date < other.start_date
        return self.priority < other.priority

    def is_completed(self):
        return self.completion >= 100

    def starts_after(self, date_):
        return self.start_date > date_
