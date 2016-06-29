__author__ = 'thecreator232'
"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    try:
        if head.next is not None:
            Insert(head.next, data)
        else:
            node = Node(data=data)
            head.next = node
    except AttributeError:
        head = Node(data=data)
    return head
