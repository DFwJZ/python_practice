from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0


            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10


            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next
    
    def create_linked_list(self, arr: List[int]):
        dummy = ListNode(0)

        cur = dummy

        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next

    def print_linked_list(self, head: ListNode):
        res = []
        while head:
            res.append(str(head.val))
            head = head.next
        return "->".join(res)



def main():
    solution = Solution()
    arr1 = [2,4,3]
    arr2 = [5,6,4]

    solution = Solution()
    l1 = solution.create_linked_list(arr1)
    l2 = solution.create_linked_list(arr2)
    result = solution.addTwoNumbers(l1, l2)
    print(solution.print_linked_list(result))



if __name__ == '__main__':
    main()   

