# Linked Lists Problems - HackerRank
# Student: Taha Hamza
# See NOTES.md for explanations.

# HackerRank provides this class on the platform; defined here so
# the file also runs locally.
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Task 1: Print the Elements of a Linked List
def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

# Task 2: Insert a Node at the Tail
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Task 3: Insert a Node at the Head
def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node

# Task 4: Insert a Node at a Specific Position
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

# Task 5: Delete a Node
def deleteNode(llist, position):
    if position == 0:
        return llist.next
    current = llist
    for i in range(position - 1):
        current = current.next
    current.next = current.next.next
    return llist


if __name__ == '__main__':
    head = None
    for value in [10, 20, 30]:
        head = insertNodeAtTail(head, value)
    printLinkedList(head)

    head = insertNodeAtHead(head, 5)
    head = insertNodeAtPosition(head, 99, 2)
    head = deleteNode(head, 0)
    printLinkedList(head)
