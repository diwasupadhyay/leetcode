class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        total = 0
        counter = collections.Counter()

        for x in nums:
            if k - x in counter:
                total += 1
                counter [k - x] -= 1
                if counter[k - x] == 0:
                    del counter[k - x]
                continue 

            counter[x] += 1
        return total 