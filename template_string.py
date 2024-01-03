# Write your code here :-)
from string import Template

s= Template("$greeting, $user!")
print(s.substitute(greeting="Hi", user="Jason"))
