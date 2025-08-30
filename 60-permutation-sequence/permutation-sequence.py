class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l=list(range(1,n+1))
        l1=sorted(list(itertools.permutations(l,n)))
        return "".join(map(str,l1[k-1]))
        