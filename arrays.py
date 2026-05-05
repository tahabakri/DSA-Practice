# Arrays Problems - HackerRank
# Student: Taha Hamza
# See NOTES.md for explanations.

# Task 1: Reverse an Array
def reverseArray(a):
    return a[::-1]

# Task 2: Array Left Rotation
def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

# Task 3: Sparse Arrays
def matchingStrings(stringList, queries):
    result = []
    for query in queries:
        result.append(stringList.count(query))
    return result

# Task 4: Counting Sort 1
def countingSort(arr):
    result = []
    for i in range(100):
        result.append(0)
    for number in arr:
        result[number] = result[number] + 1
    return result


if __name__ == '__main__':
    print(reverseArray([1, 2, 3, 4, 5]))
    print(rotateLeft(2, [1, 2, 3, 4, 5]))
    print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))
    print(countingSort([1, 1, 3, 2, 1])[:5])
