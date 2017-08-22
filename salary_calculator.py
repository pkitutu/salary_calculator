"""
Author: Kitutu Paul
August, 2017
"""

class SalaryCalculator(object):
	""" SalaryCalculator is able to calculate the net salary of a person 
	after deducting the Pay As You Earn (PAYE) and Social Security contribution (NSSF)"""
	NSSF_RATE = 0.05
	def __init__(self, gross_salary):
		super(SalaryCalculator, self).__init__()
		self.gross_salary = gross_salary
		self.__find_tax()
		self.__nssf_contribution()
		self.__find_netsalary()

	#calculate the PAYE tax depending on the range of the gross salary
	def __find_tax(self):
		if self.gross_salary <= 235000:
			self.tax = 0
		elif self.gross_salary > 235000 and self.gross_salary <= 335000:
			self.tax = (self.gross_salary-235000)*0.1
		elif self.gross_salary > 335000 and self.gross_salary <= 410000:
			self.tax = 10000 + (self.gross_salary-335000)*0.2
		elif self.gross_salary > 410000:
			self.tax = 25000 + (self.gross_salary-410000)*0.3
			if self.gross_salary > 10000000:
				 self.tax += (self.gross_salary-10000000)*0.1
		else:
			self.tax = 0

	#calculate the social security contribution
	def __nssf_contribution(self):
		self.nssf_amount = self.gross_salary*self.NSSF_RATE

	#calculate the net salary
	def __find_netsalary(self):
		self.netsalary = self.gross_salary-(self.tax+self.nssf_amount)

	def get_tax(self):
		return self.tax

	def get_nssfamount(self):
		return self.nssf_amount

	def get_netsalary(self):
		return self.netsalary