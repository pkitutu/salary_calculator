# About the app - Salary Calculator
This is a simple implementation of a salary calculator that takes into consideration the Pay As You Earn income tax (PAYE) as paid to the Uganda Revenue Authority for the different salary brackets and the Contribution to the National Social Security Fund (NSSF).
It is written in python complete with automated tests.

When the application is run, you are able to get the Amount payable to URA, then the Social Security Contribution then the net salary

## How to use it
### Run Tests
Run the python file in the terminal

* $ python test_salary_calculator.py

### Run the app
run the calculate python file with an input of the gross salary

* $ python calculate.py 1200000

## PAYE Calculations for the different age brackets
Below is the calculations for the different salary brackets

* <= 235,000 --- No Tax
* > 235,000 and <= 335,000  ---- 10% of the amount by which chargeable income exceeds Ushs. 235,000
* > 335,000 and <= 410,000  ---- Ushs. 10,000 plus 20% of the Amount by which chargeable income exceeds Ushs. 335,000.
* > 410,000 ---- Ushs 25,000 plus 30% of the amount by which chargeable income exceeds Ushs. 410,000 and (b) where the chargeable income of an individual exceeds shs.10,000,000 an additional 10% charged on the amount by which chargeable income exceeds shs. 10,000,000.

## Access Latest
git clone https://github.com/pkitutu/salary_calculator.git