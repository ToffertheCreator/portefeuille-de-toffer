class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def insert_at_end(self, data):
        node = Node(data)

        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def search(self, data):
        current_node = self.head
        pos = 0
        while current_node:
            if current_node.data == data:
                return True, pos
            current_node = current_node.next
            pos += 1
        return False, None

    def insert_at(self, pos, data):
        if pos < 0 or pos > self.size:
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        elif pos == self.size:
            self.insert_at_end(data)
            return
        
        curr_node = self.head
        for _ in range(pos-1):
            curr_node = curr_node.next
        new_node = Node(data)
        next_node = curr_node.next
        curr_node.next = new_node
        new_node.next = next_node
        self.size += 1
    
    def remove_at_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return removed_data
    
    def remove_at_end(self):
        if not self.head:
            return
        
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return removed_data
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            removed_data = curr.next.data
            curr.next = None
            self.tail = curr
            self.size -= 1
            return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        
        if self.head.data == data:
            return self.remove_at_beginning()
            
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                removed_data = curr.data
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                self.size -= 1
                return removed_data
            prev = curr
            curr = curr.next
        
        return None

    def display(self):
        data = []
        curr = self.head
        while curr:
            data.append(curr.data)
            curr = curr.next
        return data


if __name__ == "__main__":
    sll = LinkedList()

    # Insert elements
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(20)
    sll.insert_at_end(30)
    sll.insert_at_end(40)
    print("After insertions:", sll.display())  # [20, 10, 30, 40]

    # Remove at beginning
    removed = sll.remove_at_beginning()
    print("Removed at beginning:", removed)    # 20
    print("List now:", sll.display())          # [10, 30, 40]

    # Remove at end
    removed = sll.remove_at_end()
    print("Removed at end:", removed)          # 40
    print("List now:", sll.display())          # [10, 30]

    # Remove at specific data
    removed = sll.remove_at(10)
    print("Removed 10:", removed)              # 10
    print("List now:", sll.display())          # [30]

    # Remove non-existing
    removed = sll.remove_at(99)
    print("Removed 99 (not found):", removed)  # None
    print("List now:", sll.display())          # [30]

    # Remove last remaining
    removed = sll.remove_at_end()
    print("Removed last:", removed)            # 30
    print("List now:", sll.display())          # []

    # Remove from empty list
    removed = sll.remove_at_beginning()
    print("Removed from empty list:", removed) # None
    print("Final list:", sll.display())        # []