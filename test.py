from CC1 import *

c = CC1()
str = "Hello world!"
str2 = "asdfg"
str3 = "gsdfa"
str4 = "gggfa"

str5 = "waterbottle"
str6 = "erbottlewat"

print str + " reversed: " + c.reverse("Hello world!")

print "Is \"" + str + "\" unique? %s" %c.isUnique(str)
print "Is \"" + str2 + "\" unique? %s" %c.isUnique(str2)

print "Are " + str3 + " and " + str4 + " permutations of each other? %s" %c.isPerm(str3, str4)
print "Are " + str3 + " and " + str2 + " permutations of each other? %s" %c.isPerm(str3, str2)

print "Replacing spaces in " + str + ": " + c.replaceSpaces(str+'  ', 12)

print str4 + " compressed is: " + c.compressString(str4)
print str + " compressed is: " + c.compressString(str)

print str6 + " is a rotation of " + str5 + ": %s" %c.isRotation(str6, str5)
