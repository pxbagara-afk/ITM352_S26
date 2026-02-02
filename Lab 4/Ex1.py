
# Lab 4 Exercise 1
#Name: Paul Bagara
#Date: February 2, 2026
first = input("Enter first name: ")
middle = input("Enter middle initial: ")
last = input("Enter last name: ")

# - String concatenation
full_name_concat = first + " " + middle + " " + last
print("Concatenation:", full_name_concat)

#  f-string
full_name_f = f"{first} {middle} {last}"
print("F-string:", full_name_f)

#  K - % operator
full_name_percent = "%s %s %s" % (first, middle, last)
print("% Operator:", full_name_percent)

# T - format() method
full_name_format = "{} {} {}".format(first, middle, last)
print("format():", full_name_format)

# bb - join() method
full_name_join = " ".join([first, middle, last])
print("join():", full_name_join)

# jj - format() with unpacked list
parts = [first, middle, last]
full_name_format_unpacked = "{} {} {}".format(*parts)
print("format() with unpack:", full_name_format_unpacked)