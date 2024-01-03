# Write your code here :-)
from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1,3)
third_fixed = Decimal("0.333")
third_float = 1/3

print(third_fraction)
print (third_fixed)
print (third_float)

third_float = float(third_fraction)
print(third_float)

third_float = float(third_fixed)
print (third_float)



