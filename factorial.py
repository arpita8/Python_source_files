from os import system

def say(something):
	system('say "%s"'% something)
def factorial(n):
	if n == 1:
		return n
	else:
		return n* factorial(n-1) 	
first_line = "Type the number you want to do factorial for."
print(first_line)
say(first_line)
number = input('?')
answer = factorial(number)
answer_string = "The answer is %d" % answer
print(answer_string)
say(answer_string)		
