# Assignment a number to 'people' variable
people = 30
# Assignment a number to 'cars' variable
cars = 40
# Assignment a number to 'trucks' variable
trucks = 15

# 1st condition: If number of cars is more than number of people, print "..."
if cars > people:
    print "We should take the cars."
# 2nd condition: Else if number of cars is less than number of people, print "..."
elif cars < people:
    print "We should not take the cars."
# 3rd condition: In all other conditions print "..."
else:
    print "We can't decide."

# 1st condition: If number ot trucks is more than number of cars, print "..."
if trucks > cars:
    print "That's too many trucks."
# 2nd condition: Else if number of trucks is less than number of cars, print "..."
elif trucks < cars:
    print "Maybe we could take the trucks."
# 3rd condition: In all other conditions print "..."
else:
    print "We still can't decide."

# 1st condition: If number of people is more than number of trucks, print "..."
if people > trucks:
    print "Alright, let's just take the trucks."
# 2nd condition: In all other conditions print "..."
else:
    print "Fine, let's stay home then."
