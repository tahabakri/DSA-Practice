# Linked Lists Problems - HackerRank
# Student: Taha Hamza
# Course: Algorithms & Data Structures

# Task 1: Print all elements in linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

# Task 2: Insert node at the tail
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Task 3: Insert node at the head
def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node

# Task 4: Insert node at a position
def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        return new_node
    current = llist
    for i in range(position - 1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return llist

# Task 5: Delete a node
def deleteNode(llist, position):
    if position == 0:
        return llist.next
    current = llist
    for i in range(position - 1):
        current = current.next
    current.next = current.next.next
    return llist