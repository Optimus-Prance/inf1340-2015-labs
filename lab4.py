#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it
FTAX = 0.025
PTAX = 0.05
TTAX = 0.075


def federal_sales_tax(purchase):
    #try to just return a number and then format the strings during the writing part!!!
    fal = purchase * FTAX
    return fal

def provincial_sales_tax(purchase):
    pal = purchase * PTAX
    return pal

def total_tax(purchase):
    cal = purchase * TTAX
    return cal

def total_sale(purchase):
    tal = purchase * 1.075
    return tal


def bill_of_sale(purchase):
    file_name = "purchases.txt"
    with open(file_name, "w") as output_file:
        output_file.write("Amount of Purchase: {0:.2f}\n".format(purchase))
        output_file.write("Provincial tax: {0:.2f}\n".format(provincial_sales_tax(purchase)))
        output_file.write(("Federal tax: {0:.2f}\n".format(federal_sales_tax(purchase))))
        output_file.write(("Total tax: {0:.2f}\n".format(total_tax(purchase))))
        output_file.write(("Total sale: {0:.2f}\n".format(total_sale(purchase))))

bill_of_sale(100)