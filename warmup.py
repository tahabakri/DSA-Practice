# Warmup Problems - HackerRank
# Student: Taha Hamza
# See NOTES.md for explanations.

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

# Task 6: Plus Minus
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
        else:
            zero = zero + 1
    print(round(positive / n, 6))
    print(round(negative / n, 6))
    print(round(zero / n, 6))

# Task 7: Staircase
def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

# Task 8: Birthday Cake Candles
def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

# Task 9: Time Conversion
def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == '12':
            return s[:-2]
        return str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    print(solveMeFirst(2, 3))
    print(simpleArraySum([1, 2, 3, 4, 10, 11]))
    print(compareTriplets([5, 6, 7], [3, 6, 10]))
    print(aVeryBigSum([1000000001, 1000000002, 1000000003]))
    miniMaxSum([1, 2, 3, 4, 5])
    plusMinus([-4, 3, -9, 0, 4, 1])
    staircase(4)
    print(birthdayCakeCandles([3, 2, 1, 3]))
    print(timeConversion('07:05:45PM'))
    print(timeConversion('12:01:00AM'))
