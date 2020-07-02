class Solution:
    def mergeKLists(self, lists):
        root = None
        for link in lists:
            if root and link:
                b = link
                if root.val < link.val:
                    top = root
                    b = link
                else:
                    top = link
                    b = root
                    root = link
                while b:
                    if top.next:
                        if top.val <= b.val <= top.next.val:
                            top.next, b.next, b = b, top.next, b.next
                        elif b.val < top.val:
                            b.next, top, b = top, b, b.next
                        else:
                            top = top.next
                    else:
                        top.next = b
                        break
            elif link:
                    root = link
        return root
