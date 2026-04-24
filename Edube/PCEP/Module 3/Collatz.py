''' In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis 
(it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number
(it may even require artificial intelligence), but you can use Python to check some individual numbers.
Maybe you'll even find the one which would disprove the hypothesis.


Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

Test your code using the data we've provided.

Test Data

Sample input: 15

Expected output:

46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17 ''' 


num = int(input("Enter the number: "))
if num < 1:
    print("Non Negative and non-zero numbers only. Try again")
else:
    val = 0
    while num != 1:
        num = num //2 if num % 2 == 0 else 3 * num + 1 
        print(num)
        val+=1
    print("Steps = ",val)   
        