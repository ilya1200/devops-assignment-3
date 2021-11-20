# This code is legal will run and always print "finally"
# However it will not catch errors that occur in the try

try:
    x = 1
finally:
    print("finally")
