class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        l1 = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return l1[:k]
        

