name = 'Zed A. Shaw'
age = 35 # not a lik
height = 74 # inches
height_centimeters = height * 0.0254
weight = 180 # lbs
weight_kilograms = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usualy %s depending on the coffee." % teeth

# this line is trickly, try to get it exacly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
