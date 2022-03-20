"""Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
 7 -> 1 -> 6 
"""
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295. Output: 2 -) 1 -) 9.That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295. Output: 9 -) 1 -) 2.That is, 912.


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def add_first(self, value):
    self.head = Node(value, next=self.head)

  def print_list(self):
    if self.head == None:
      print("The list is EMPTY!")

    cur = self.head

    while cur:
      print(cur.value, end=" -> ")
      cur = cur.next

  def reverse(self):
    if self.head == None:
      return

    current = self.head
    prev = None
    next = None

    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next

    self.head = prev

  def make_array(self):
    arr = []
    
    if self.head == None:
      return arr

    current = self.head

    while current:
      arr.append(current.value)
      current = current.next

    return arr

  def length(self):
    cur = self.head
    count = 0

    while cur:
      count += 1
      cur = cur.next

    return count

    
if __name__ == '__main__':
  # CREATE LINKED LISTS TO TEST
  ll1 = LinkedList()
  n1 = [6, 1, 7]
  for n in n1:
    ll1.add_first(n)
    
  ll2 = LinkedList()
  n2 = [2, 9, 5]
  for n in n2:
    ll2.add_first(n)
  ##################################
  # Alas: lists of ints cannot be joined

  length_1 = ll1.length()
  length_2 = ll2.length()

  return_ll = LinkedList()

  # 7 -> 1 -> 6
  # 5 -> 9 -> 2

  # 617
  # 295
  #______
  # 912

  # ll1.print_list()
  # print()
  # ll2.print_list()
  # print()

  # if lists are the same length
  if length_1 == length_2:
    cur_1 = ll1.head
    cur_2 = ll2.head
    carry_one = 0
    
    while cur_1:
      total = cur_1.value + cur_2.value + carry_one

      if total > 9:
        ones = total % 10
        return_ll.add_first(ones)
        carry_one = total // 10

      else:
        # If single digit
        return_ll.add_first(total)
        carry_one = 0

      cur_1 = cur_1.next
      cur_2 = cur_2.next

    return_ll.reverse()
    return_ll.print_list()