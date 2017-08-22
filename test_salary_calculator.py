"""
Author: Kitutu Paul
August, 2017
"""
import unittest
from salary_calculator import SalaryCalculator


class TestSalaryCalculator(unittest.TestCase):
	calc0 = SalaryCalculator(100000)
	calc1 = SalaryCalculator(300000)
	calc2 = SalaryCalculator(400000)
	calc3 = SalaryCalculator(1000000)
	calc4 = SalaryCalculator(12000000)
	
	#test that the PAYE tax calculation is working well for the different sections
	def test_tax(self):
		self.assertEqual(self.calc0.get_tax(), 0)
		self.assertEqual(self.calc1.get_tax(), 6500)
		self.assertEqual(self.calc2.get_tax(), 23000)
		self.assertEqual(self.calc3.get_tax(), 202000)
		self.assertEqual(self.calc4.get_tax(), 3702000)

	#test that the NSSF contribution calculation is working well for the different sections
	def test_nssfamount(self):
		self.assertEqual(self.calc0.get_nssfamount(), 5000)
		self.assertEqual(self.calc1.get_nssfamount(), 15000)
		self.assertEqual(self.calc2.get_nssfamount(), 20000)
		self.assertEqual(self.calc3.get_nssfamount(), 50000)
		self.assertEqual(self.calc4.get_nssfamount(), 600000)

	def test_netsalary(self):
		self.assertEqual(self.calc0.get_netsalary(), 95000)
		self.assertEqual(self.calc1.get_netsalary(), 278500)
		self.assertEqual(self.calc2.get_netsalary(), 357000)
		self.assertEqual(self.calc3.get_netsalary(), 748000)
		self.assertEqual(self.calc4.get_netsalary(), 7698000)


if __name__ == '__main__':
	unittest.main()