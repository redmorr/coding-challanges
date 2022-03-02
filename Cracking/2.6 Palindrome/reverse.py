from node import Node


palindrome = Node('a', Node('b', Node('c', Node('b', Node('a', None)))))
non_palindrome = Node('a', Node('b', Node('b', Node('b', Node('a', Node('a', None))))))


def reverse_and_count(head: Node):
    pointer = head
    current = Node(pointer.val, None)
    i = 1

    while pointer.next:
        pointer = pointer.next
        previous = current
        current = Node(pointer.val, previous)
        i += 1

    return current, i


def is_palindrome(head: Node):
    p = head
    rev, length = reverse_and_count(head)
    i = 0

    rounded_up_half = length // 2 + length % 2
    while i < rounded_up_half:
        if p.val != rev.val:
            return False
        p = p.next
        rev = rev.next
        i += 1

    return True


assert is_palindrome(palindrome) is True
assert is_palindrome(non_palindrome) is False
