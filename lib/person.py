#!/usr/bin/env python3
class Person:
    approved_jobs = [
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

    def __init__(self):
        self._name = ""
        self._job = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Name must be a string.")
        elif len(value) > 25:
            print("Name must be under 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
