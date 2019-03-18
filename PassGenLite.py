# Generate a random password with user choice "length" with no duplicate characters in the password. 
# Limited to 74 characters length.
import random

a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
length = int(input('how many letters: '))
p = "".join(random.sample(a,length))
print (p)