#""https://www.hackerrank.com/challenges/re-findall-re-finditer?h_r=next-challenge&h_v=legacy "

import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
print('Enter the string')
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
if match:
    for i in match:
        print (i)
else:
    print (-1)
