from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values: List):
        self.head = None
        if values:
            self.create_linked_list(values)

    def create_linked_list(self, values: List[int]):
        if not values:
            return
        
        self.head = ListNode(values[0])

        cur = self.head
        for val in values[1:]:
            cur.next = ListNode(val)
            cur = cur.next

    def print_linked_list_to_list(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

def main():
    solution = Solution()

    # Test case 1
    linked_list1 = LinkedList([1, 2, 3, 4, 5])
    print("Original list:", linked_list1.print_linked_list_to_list())
    linked_list1.head = solution.reverseList(linked_list1.head)
    print("Reversed list:", linked_list1.print_linked_list_to_list())

if __name__ == '__main__':
    main()