# Assignment the formated string with digit to a variable 'x'.
x = "There are %d types of people." % 10
# Assignment a string to variable 'binary'.
binary = "binary"
# Assignment a string to variable 'do_not'.
do_not = "don't"
# Assignment the formated string with two strings to a variable 'y'.
y = "Those who knows %s and those who %s." % (binary, do_not)

# Printing variable x.
print x
# Printing variable y.
print y

# Printing the string which is formated by variable x.
print "I said: %r." % x
# Printing the string which is formated by variable y.
print "I also said: '%s'." % y

# Assignment the boolean value to variable 'hilarious'.
hilarious = False

# Assignment the formated string.
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing the formated variable 'joke_evaluation' by variable 'hilarious'.
print joke_evaluation % hilarious

# Assignment a string to a variable 'w'.
w = "That is the left side of..."
# Assignment a string to a variable 'e'.
e = "a string with a right side."

# Printing a concatenation of variables 'w' and 'e'.
print w + e
