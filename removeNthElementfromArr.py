# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        for node in range(len(head)-n, len(head)-1):
            head[node] = head[node+1]
        head.pop()
        return head

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# head = [1,2,3,4,5] ,#n = 2
head = [1,2] #n = 1
s = Solution()
print(s.removeNthFromEnd(head, 1))
        