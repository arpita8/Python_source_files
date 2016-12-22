# Python program to demonstrate the use of formatting using %

# Initialize variable as a string
print('Enter the number for conversions')
variable= raw_input()
#variable = '15'
string = "Variable as string = %s" %(variable)
print string

# Convert the variable to integer
# And perform check other formatting options

variable = int(variable) # Without this the below statement
						# will give error.
string = "Variable as integer = %d" %(variable)
print string
print "Variable as float = %f" %(variable)
print "Variable as hexadecimal = %x" %(variable)
print "Variable as octal = %o" %(variable)
