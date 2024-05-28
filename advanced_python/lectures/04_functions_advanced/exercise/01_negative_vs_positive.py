# 01_negative_vs_positive
#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1839#0

1.	Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space.
Separate the negative numbers from the positive.
Find the total sum of the negatives and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
    o	If the absolute negative number is larger than the positive number:
	    "The negatives are stronger than the positives"
    o	If the positive number is larger than the absolute negative number:
	    "The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

Input
1 2 -3 -4 65 -98 12 57 -84

Output
-189
137
The negatives are stronger than the positives

Input
1 2 3

Output
0
6
The positives are stronger than the negatives

"""

##########: variant 1 :##########

def total_sum(*args):
    result = ""
    sum_negatives = sum([n for n in args if n < 0])
    sum_positives = sum([n for n in args if n >= 0])
    result += f"{sum_negatives}\n{sum_positives}\n"
    if abs(sum_negatives) > sum_positives:
        result += "The negatives are stronger than the positives"
    if sum_positives > abs(sum_negatives):
        result += "The positives are stronger than the negatives"
    return result


nums = [int(x) for x in input().split()]
print(total_sum(*nums))


##########: variant 2 :##########

def negative_vs_positive(*args):
    positive_sum = 0
    negative_sum = 0
    for num in args:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num
    result = [negative_sum, positive_sum]
    if negative_sum + positive_sum < 0:
        result.append("The negatives are stronger than the positives")
    else:
        result.append("The positives are stronger than the negatives")
    return "\n".join(str(x) for x in result)


nums = [int(x) for x in input().split()]
print(negative_vs_positive(*nums))

##########: variant 3 :##########

