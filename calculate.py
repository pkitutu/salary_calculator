"""
Author: Kitutu Paul
August, 2017
"""
from salary_calculator import SalaryCalculator
import sys

try:
   input_val = sys.argv[1].replace(',','')
   gross_salary = float(input_val)
   calc = SalaryCalculator(gross_salary)
   tax = '{:,}'.format(calc.get_tax())
   nssf_amount = '{:,}'.format(calc.get_nssfamount())
   netsalary ='{:,}'.format(calc.get_netsalary())
   
   print "PAYE tax: %s NSSF Contribution: %s Net Salary: %s" %(tax, nssf_amount, netsalary)
except ValueError:
    print "Not a number"

