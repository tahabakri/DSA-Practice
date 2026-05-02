# Arrays Problems - HackerRank
# Student: Taha Hamza
# Course: Algorithms & Data Structures

# Task 1: Reverse an array
def reverseArray(a):
    return a[::-1]

# Task 2: Rotate array to the left by d positions
def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

# Task 3: Count matching strings
def matchingStrings(stringList, queries):
    result = []
    for query in queries:
        result.append(stringList.count(query))
    return result

# Task 4: Count frequency of each number
def countingSort(arr):
    result = []
    for i in range(100):
        result.append(0)
    for number in arr:
        result[number] = result[number] + 1      
    return result