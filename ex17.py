from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying form %s to %s" % (from_file, to_file)

# we could do this two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exits? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL+C to abord."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alrigth, all done."

out_file.close()
in_file.close()
