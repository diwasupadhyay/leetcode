class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(eating_speed: int) -> bool:
            total_hours = sum((pile_size + eating_speed - 1) // eating_speed
                            for pile_size in piles)
            return total_hours <= h

        left, right = 1, max(piles)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index