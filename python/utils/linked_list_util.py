"""
    list_node
    ~~~

    Creator, printer and validator for list node

    :author: dilless(Huangbo)
    :date: 2020/7/12
"""
from typing import List, Optional

from data_structures.list_node import ListNode


class LinkedListUtil:

    @staticmethod
    def create_linked_list(values: List[int]) -> Optional[ListNode]:
        """
        Create linked list from values list
        :param values: the values list of linked list
        :type values: list of int
        :return: head node of linked list
        :rtype: ListNode or None
        """
        if not values:
            return None
        head = ListNode(values[0])
        cur_node = head
        for val in values[1:]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
        return head

    @staticmethod
    def print_linked_list(head: ListNode, name: str = '[LinkedList]') -> None:
        """
        Print linked list in a human-readable-way, example: `1 -> 2 -> 3 -> None`
        :param head: head node of linked list
        :type head: ListNode
        :param name: name of liked list
        :type name: str
        :return: None
        """
        print(name, ': ', sep='', end='')
        cur_node = head
        while cur_node:
            print(cur_node.val, ' -> ', sep='', end='')
            cur_node = cur_node.next
        print('None')

    @staticmethod
    def is_same(head1: ListNode, head2: ListNode) -> bool:
        """
        Compare if two linked list is same in memory
        :param head1: head of the first linked list
        :type head1: ListNode
        :param head2: head of the second linked list
        :type head2: ListNode
        :return: True if same, False otherwise
        :rtype: bool
        """
        cur_node1 = head1
        cur_node2 = head2
        while cur_node1 and cur_node2:
            if cur_node1 is not cur_node2:
                return False

        if cur_node1 or cur_node2:
            return False

        return True

    @staticmethod
    def is_equal(head1: ListNode, head2: ListNode) -> bool:
        """
        Compare if two linked list have same values
        :param head1: head of the first linked list
        :type head1: ListNode
        :param head2: head of the second linked list
        :type head2: ListNode
        :return: True if same, False otherwise
        :rtype: bool
        """
        cur_node1 = head1
        cur_node2 = head2
        while cur_node1 and cur_node2:
            if cur_node1.val != cur_node2.val:
                return False
            cur_node1 = cur_node1.next
            cur_node2 = cur_node2.next

        if cur_node1 or cur_node2:
            return False

        return True
