# Sorting Problems - HackerRank
# Student: Taha Hamza
# Course: Algorithms & Data Structures

# Task 1: Find index of a value in sorted array
def introTutorial(V, arr):
    return arr.index(V)

# Task 2: Insert one element into sorted position
def insertionSort1(n, arr):
    last_number = arr[n-1]
    position = n - 2
    while position >= 0 and arr[position] > last_number:
        arr[position + 1] = arr[position]
        position = position - 1
    arr[position + 1] = last_number
    print(' '.join(map(str, arr)))

# Task 3: Sort entire array using insertion sort
def insertionSort2(n, arr):
    for i in range(1, n):
        current_number = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_number:
            arr[position + 1] = arr[position]
            position = position - 1
        arr[position + 1] = current_number
        print(' '.join(map(str, arr)))

# Task 4: Count frequency of each number
def countingSort(arr):
    count = []
    for i in range(100):
        count.append(0)
    for number in arr:
        count[number] = count[number] + 1
    return count

# Task 5: Find the median of an array
def findMedian(arr):
    arr.sort()
    middle = len(arr) // 2
    return arr[middle]

    