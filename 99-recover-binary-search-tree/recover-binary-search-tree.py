# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):

        first = second = prev = None
        curr = root

        while curr:

            # if no left child
            if not curr.left:
                # check violation
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                # find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                # create temporary link
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    # remove link
                    pred.right = None

                    # check violation
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        # swap wrong nodes
        first.val, second.val = second.val, first.val