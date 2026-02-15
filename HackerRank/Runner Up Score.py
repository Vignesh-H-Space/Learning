# Runner Up Score in HackerRank

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Output Format
#Print the runner-up score.

# Sample Input 
# 5 
# 2 3 6 6 5 

# Output - 5 

n = int(input())
large = 0
arr = map(int, input().split())
for element in arr:
        if (element>large):
            num = large
            large = element
        elif element > num and element != large : 
            num = element
        
# print (large) The largest number 

print (num) # Second largest number 