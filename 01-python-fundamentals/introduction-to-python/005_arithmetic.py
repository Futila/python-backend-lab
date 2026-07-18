# Sum

sum = 1 +1 
print("1 + 1 = ", sum)



# Subtraction
sub = 3 - 2
print("3 - 2 = ", sub)


# Multiplication
mult = 2 * 10
print("'2 * 10 = ", mult)


# Division
div = 10 / 2
print("10 / 2 = ", div)


# Division with no floating point (//) returns the whole number part of a division operation. It discards the decimal part and returns the integer quotient.
div_no_float = 10 // 3
print("10 // 3 = ", div_no_float)


# int() converts a number or string to an integer. If the number is a float, it will be rounded down to the nearest whole number.
number_float = 10.5
number_integer = int(number_float)
print("Float:", number_float)
print("Integer:", number_integer)


# float() converts a number or string to a float. If the number is an integer, it will be converted to a float with a decimal point.
print("Value in float:", float(number_integer))


# modulus operator (%) returns the remainder of a division operation. It can be used to determine if a number is even or odd.
number = 10
modulus = number % 2
print("10 % 2 = ", modulus)