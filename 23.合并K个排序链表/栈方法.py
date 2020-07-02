class Solution:
    '''超时了'''
    def mergeKLists(self, lists):
        root = None
        dp1 = []
        dp2 = []
        for root in lists:
            while dp2 and root:
                if root.val > dp2[-1].val:
                    dp1.append(dp2.pop())
                else:
                    dp1.append(root)
                    root = root.next
            while root:
                dp1.append(root)
                root = root.next
            while dp2:
                dp1.append(dp2.pop())
            while dp1:
                dp2.append(dp1.pop())
            print([i.val for i in dp2])
        if dp2:
            root = d = dp2.pop()
            root.next = None
        while dp2:
            z = dp2.pop()
            d.next = z
            d = z
            d.next = None
        return root