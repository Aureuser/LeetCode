class Solution:
    def mergeKLists(self, lists):
        stack = []
        for singleNode in lists:
            while singleNode:
                stack.append(singleNode.val)
                singleNode = singleNode.next
        resNode = tem = ListNode(0)
        stack.sort()
        for a in stack:
            tem.next = ListNode(a)
            tem = tem.next
        return resNode.next