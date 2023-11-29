from abc import ABC, abstractmethod

import numpy as np
from enum import Enum


# Rename
# Introduce variable/constant
# Change signature
# Extract method
# Go to declaration
# See usages
# Inline


def calc_profit_share(employee_type, employee_details, base_salary) -> int:
    factory = SalaryFactory()
    strategy = factory.get_salary_strategy(EmployeeType(employee_type))
    return strategy.calculate_salary(employee_details, base_salary)


class EmployeeType(Enum):
    SCIENTIST = 1
    DEVELOPER = 2
    BOSS = 3
    IT_GUY = 4


class SalaryFactory:
    def get_salary_strategy(self, employee_type):
        if employee_type == EmployeeType.SCIENTIST:
            return ScientistSalaryStrategy()
        elif employee_type == EmployeeType.DEVELOPER:
            return DeveloperSalaryStrategy()
        elif employee_type == EmployeeType.BOSS:
            return BossSalaryStrategy()
        elif employee_type == EmployeeType.IT_GUY:
            return ITGuySalaryStrategy()
        else:
            raise ValueError("Unknown Employee Type")


class SalaryStrategy(ABC):
    @abstractmethod
    def calculate_salary(self, employee_details, base_salary):
        pass


class ScientistSalaryStrategy(SalaryStrategy):
    def calculate_salary(self, employee_details, base_salary):
        profit_share_percentage = 20 if employee_details.is_expert() else 10

        profit_share_relevant = base_salary / 4
        return profit_share_relevant / 100 * profit_share_percentage


class DeveloperSalaryStrategy(SalaryStrategy):
    def calculate_salary(self, employee_details, base_salary):
        if employee_details.is_expert():
            profit_share_percentage = 15
        elif employee_details.is_advanced():
            profit_share_percentage = 10
        else:
            profit_share_percentage = 5

        if base_salary <= 100000:
            profit_share_percentage += 5

        return base_salary / 100 * profit_share_percentage


class BossSalaryStrategy(SalaryStrategy):
    def calculate_salary(self, employee_details, base_salary):
        company_share_service = CompanyShareService()
        company_share_service.assign_shares(100)
        return base_salary / 100 * 20


class ITGuySalaryStrategy(SalaryStrategy):
    def calculate_salary(self, employee_details, base_salary):
        email_service = EmailService()
        email_service.send_sorry_mail()
        return 0


class CompanyShareService:
    def assign_shares(self, number):
        # assigning shares
        pass


class EmailService:
    def send_sorry_mail(self):
        # very sorry that you dont get anything
        pass


class Employee:
    def __init__(self, name, years_of_experience):
        self.name = name
        self.years_of_experience = years_of_experience

    def is_expert(self):
        """Determines if the employee is an expert."""
        return self.years_of_experience >= 10

    def is_advanced(self):
        """Determines if the employee is advanced, but not an expert."""
        return 5 <= self.years_of_experience < 10

    def is_normal(self):
        """Determines if the employee is at a normal level."""
        return self.years_of_experience < 5
