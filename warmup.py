# Warmup Problems - HackerRank
# Student: Taha Hamza
# Course: Algorithms & Data Structures

# Task 1: Solve Me First
def solveMeFirst(a, b):
    return a + b

# Task 2: Simple Array Sum
def simpleArraySum(ar):
    return sum(ar)

# Task 3: Compare the Triplets
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1
    return [alice, bob]

# Task 4: A Very Big Sum
def aVeryBigSum(ar):
    return sum(ar)

# Task 5: Mini-Max Sum
def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))

# Task 6: Count positive, negative and zero
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    for number in arr:
        if number > 0:
            positive = positive + 1
        elif number < 0:
            negative = negative + 1
        else: zero = zero + 1
    print(round(positive/n, 6))
    print(round(negative/n, 6))
    print(round(zero/n, 6))

# Task 7: Print a staircase of # symbols

def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '#' * i)

# Task 8: Find minimum and maximum sum of 4 numbers
def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))

# Task 9: Count tallest candles
def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest

# Task 10: Convert 12-hour to 24-hour time

def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == '12':
            return s[:-2]
        return str(int(s[:2]) + 12) + s[2:-2]
