# Assignment a value which can be formated to a variable 'formatter'.
formatter = "%r %r %r %r"

# Printing a 'formatted' variable with formating by foru digits.
print formatter % (1, 2, 3, 4)
# Printing a 'formatted' variable with formating by four strings.
print formatter % ("one", "two", "three", "four")
# Printong a 'formatter' variable with formating by four boolean values.
print formatter % (True, False, False, True)
# Printing a 'formatter' variable with formating by four 'formatter' variables.
print formatter % (formatter, formatter, formatter, formatter)
# Printing a 'formatter' variable with formating by four strings in four lines.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't string.",
    "So I said goodnight."
)
