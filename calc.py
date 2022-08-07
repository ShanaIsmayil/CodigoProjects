

import math #importing math to use appropriate mathematical functions
#function to calculate nCr
def nCr(n, r):
    return (fact(n) / (fact(r)
                       * fact(n-r)))

#function to calculate nPr
def nPr(n, r):
    return (fact(n) / fact(n-r))

# Returns factorial of n - recursive function
def fact(n):
    if n == 0:
        return 1
    res = 1

    for i in range(2, n + 1):
        res = res * i

    return res


def calc():
 # Simple Calculator
 # use triple quotes for choice cases , accept the operation to be perfomed by user to op
 op = input('''
   Enter:
   + for add
   - for subtract
   * for multiplication          
   / for division
   ^ for power function
   log for logarithmic function
   ln for natural log
   ncr for combination
   npr for permutation
   e for exponential
   
  ''')
 #for each cases of op perform appropriate operations
 if op == '+':
	  n1 = int(input("Enter your first number:\n")) #inputing numbers from users to n1 and n2
	  n2 = int(input("Enter your second number:\n"))
	  print('{} + {} = {}'.format(n1,n2,n1+n2))#additiona operation

 elif op == '-':
       n1 = int(input("Enter your first number:\n"))
       n2 = int(input("Enter your second number:\n"))
       print('{} - {} = {}'.format(n1,n2,n1-n2))#subtraction operation

 elif op == '*':
      n1 = int(input("Enter your first number:\n"))
      n2 = int(input("Enter your second number:\n"))
      print('{} * {} = {}'.format(n1, n2, n1*n2))#multiplication operation

 elif op == '/':
      n1 = int(input("Enter your first number:\n"))
      n2 = int(input("Enter your second number:\n"))
      print('{} / {} = {}'.format(n1, n2, n1/n2))#division operation

 elif op == '^':
      n1 = int(input("Enter your base:\n"))
      n2 = int(input("Enter your exponent:\n"))
      print('{} ^ {} = {}'.format(n1, n2, n1**n2))#power operation

 elif op == 'log':
      n1 = int(input("Enter number:\n"))
      n2 = int(input("Enter base of log:\n"))
      print('log({}) = {}'.format(n1,math.log(n1,100)))#log function

 elif op == 'ln':
      n1 = int(input("Enter number:\n"))
      n2 = int(input("Enter base of log:\n"))
      print('log({}) = {}'.format(n1,math.log(n1,n2)))#natural log function

 elif op == 'ncr':
      n1 = int(input("Enter n:\n"))
      n2 = int(input("Enter r:\n"))
      print('{}C{} = {}'.format(n1,n2,nCr(n1,n2)))#nCr

 elif op == 'npr':
      n1 = int(input("Enter n:\n"))
      n2 = int(input("Enter r:\n"))
      print('{}P{} = {}'.format(n1,n2,nPr(n1,n2)))#nPr

 elif op == 'e':
      n1 = int(input("Enter n:\n"))
      print('e^{} = {}'.format(n1,math.exp(n1)))#exponential
 else:
      print("\nInvalid operation\n")
 again()

#again method to perform operations again
def again():
	c = input('''
	 Enter
	 Y to calculate again
	 N for stop calculation
	''')

	if c.upper() == 'Y':#c.upper() to convert entyering value to its uppercase
		calc()
	elif c.upper() == 'N':
		print("\nCALCULATION STOPPED\n")
	else:
		again()

calc()