from node import Node

palindrome = Node('a', Node('b', Node('c', Node('b', Node('a', None)))))
non_palindrome = Node('a', Node('b', Node('b', Node('b', Node('a', Node('a', None))))))


def is_palindrome(head: Node):
    fast = head
    slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next

    return True


assert is_palindrome(palindrome) is True
assert is_palindrome(non_palindrome) is False
