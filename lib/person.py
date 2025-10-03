#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC",
        "Production", "Legal", "Finance", "Sales",
        "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Unemployed"):
        self.name = name   # Uses property setter
        self.job = job     # Uses property setter

    # name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # job property
    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
