"""Delete middle item.

List length is odd -> middle
List length is even -> delete both middles

Input: Ints, assume valid input
Output: Return deleted value in a list to accommodate two values

Node class
LinkedList class
Add
length
delete_middle

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def length_list(self):
        cur = self.head
        count = 0

        while cur:
                cur = cur.next
                count += 1
        return count

    def delete_node(self, current, prev):
        # if current == None:
        #     return None
        if current == self.head:
            self.head = self.head.next
            current.next == None
        else:
            prev.next = current.next
            current.next = None

    def delete_middle(self):
        if self.head == None:
            return None

        slow = self.head
        fast = self.head
        prev = None

        deleted_vals = []
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if self.length_list() % 2 == 0:
            deleted_vals.append(slow.data)
            self.delete_node(slow, prev)

            mid_2 = prev
            deleted_vals.append(mid_2.data)
            self.delete_node(mid_2, prev)
        else:
            deleted_vals= [slow.data]
            self.delete_node(slow, prev)

        return deleted_vals

    def print_list(self):
        temp_list = []

        cur = self.head
        while cur:
            temp_list.append(str(cur.data))
            cur = cur.next

        return " ".join(temp_list)


if __name__ == '__main__':
    
    def test_delete_middle(nums):
        ll = LinkedList()

        for num in nums:
            ll.add_at_front(num)

        return ll.delete_middle()

    assert test_delete_middle([4, 3, 2]) == [3]
    assert test_delete_middle([4, 3, 2, 1]) == [3, 2]
    assert test_delete_middle([]) == None
    assert test_delete_middle([1]) == [1]
    assert test_delete_middle([1, 2]) == [1, 2]
    assert test_delete_middle([1, 2, 3, 4, 5, 6, 7, 8]) == [4, 5]