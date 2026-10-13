class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyHashSet:

    def __init__(self):
        # Using a dummy head makes removing nodes much cleaner
        self.dummy = Node(-1)
        

    def add(self, key: int) -> None:
        # A HashSet cannot contain duplicates; check if it exists first
        if self.contains(key):
            return
            
        # Find the end of the list to append the new node
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = Node(key)
        

    def remove(self, key: int) -> None:
        curr = self.dummy
        # Look ahead at the next node's data to safely delete it
        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next  # Bypass the node containing the key
                return                      # Item removed, exit early
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        curr = self.dummy.next  # Start at the actual first element
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False
