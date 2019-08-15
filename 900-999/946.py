class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tmp = []
        while pushed:
            p = pushed.pop(0)
            tmp.append(p)
            while tmp and popped[0] == tmp[-1]:
                popped.pop(0)
                tmp.pop()

        return not tmp