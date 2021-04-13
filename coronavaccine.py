from pywebio.input import *
from pywebio.output import *

def vaccine():
	name =  input("Enter your Name: ", type='text')
	age = input("Enter your age:" , type=NUMBER)
	
	if age >=18:
		put_text('Check if your details')
		put_table([['NAME','AGE'],[name,age]])
		check = checkbox(options =['All Details are correct'])
		if check:
			selection = radio("Select your vaccine",['Moderna','Pfizer','JnJ'])
			put_text('Your Vaccine Information is Recorded')
			put_table([['NAME','AGE','Vaccine'],[name,age,selection]])
vaccine()