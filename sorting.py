# Sorting Problems - HackerRank
# Student: Taha Hamza
# See NOTES.md for explanations.

# Task 1: Intro to Tutorial Challenges
def introTutorial(V, arr):
    return arr.index(V)

# Task 2: Insertion Sort - Part 1
def insertionSort1(n, arr):
    last_number = arr[n - 1]
    position = n - 2
    while position >= 0 and arr[position] > last_number:
        arr[position + 1] = arr[position]
        print(' '.join(map(str, arr)))
        position = position - 1
    arr[position + 1] = last_number
    print(' '.join(map(str, arr)))

# Task 3: Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, n):
        current_number = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_number:
            arr[position + 1] = arr[position]
            position = position - 1
        arr[position + 1] = current_number
        print(' '.join(map(str, arr)))

# Task 4: Counting Sort 1
def countingSort(arr):
    count = []
    for i in range(100):
        count.append(0)
    for number in arr:
        count[number] = count[number] + 1
    return count

# Task 5: Find the Median
def findMedian(arr):
    arr.sort()
    middle = len(arr) // 2
    return arr[middle]


if __name__ == '__main__':
    print(introTutorial(4, [1, 4, 5, 7, 9, 12]))
    insertionSort1(5, [2, 4, 6, 8, 3])
    insertionSort2(6, [1, 4, 3, 5, 6, 2])
    print(countingSort([1, 1, 3, 2, 1])[:5])
    print(findMedian([5, 3, 1, 2, 4]))
