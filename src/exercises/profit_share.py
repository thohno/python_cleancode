import numpy as np


# Rename
# Introduce variable/constant
# Change signature
# Extract method
# Go to declaration
# See usages
# Inline


# type definitions:
# 1: scientist
# 2: developer
# 3: boss
# 4: it guy
def calc_profit_share(e_type, details, money) -> int:
    company_share_service = CompanyShareService()
    email_service = EmailService()

    if e_type == 1:
        if details.is_expert():
            profit_share_percentage = 20
        else:
            profit_share_percentage = 10
        profi_share_relevant = money / 4
        return profi_share_relevant / 100 * profit_share_percentage
    elif e_type == 2:
        if details.is_advanced():
            profit_share_percentage = 10
        elif details.is_expert():
            profit_share_percentage = 15
        else:
            profit_share_percentage = 5
        if money > 100000:
            return money / 100 * profit_share_percentage
        else:
            return money / 100 * (profit_share_percentage + 5)
    elif e_type == 3:
        company_share_service.assign_shares(100)
        return money / 100 * 20
    elif e_type == 4:
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


class Employer:
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
