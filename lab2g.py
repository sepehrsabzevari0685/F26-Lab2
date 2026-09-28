# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.


# Tax rates
TAX_RATE_1 = 0.10
TAX_RATE_2 = 0.15
TAX_RATE_3 = 0.25

# Single limits
SINGLE_LIMIT_1 = 8000
SINGLE_LIMIT_2 = 32000

# Married limits
MARRIED_LIMIT_1 = 16000
MARRIED_LIMIT_2 = 64000

income = float(input("Enter your taxable income: "))
status = input("Enter your status (single/married): ").lower()

if status == "single":
    if income <= SINGLE_LIMIT_1:
        tax = income * TAX_RATE_1
    elif income <= SINGLE_LIMIT_2:
        tax = 800 + (income - SINGLE_LIMIT_1) * TAX_RATE_2
    else:
        tax = 4400 + (income - SINGLE_LIMIT_2) * TAX_RATE_3

elif status == "married":
    if income <= MARRIED_LIMIT_1:
        tax = income * TAX_RATE_1
    elif income <= MARRIED_LIMIT_2:
        tax = 1600 + (income - MARRIED_LIMIT_1) * TAX_RATE_2
    else:
        tax = 8800 + (income - MARRIED_LIMIT_2) * TAX_RATE_3

print(f"Tax: ${tax:.2f}")
