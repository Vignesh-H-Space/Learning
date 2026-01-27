#Task
#Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird

a = int(input().strip())
if (a%2==1):
    print ("Weird")
elif (a > 2 and a < 5):
    print ("Not Weird")
elif (a > 5 and a < 20):
    print ("Weird")
else :
    print ("Not Weird")
