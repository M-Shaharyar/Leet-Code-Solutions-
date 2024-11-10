# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        lst = head
        while lst:
            nums.append(lst.val)
            lst = lst.next
        l , r = 0 , len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l , r = l + 1, r - 1
        return True