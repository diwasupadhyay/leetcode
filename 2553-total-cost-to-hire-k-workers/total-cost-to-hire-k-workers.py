class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        num_workers = len(costs)
      
        if candidates * 2 >= num_workers:
            return sum(sorted(costs)[:k])
      
        # Min heap to store (cost, index) pairs
        min_heap = []
      
        # Add first 'candidates' workers from the left side
        for index, cost in enumerate(costs[:candidates]):
            heappush(min_heap, (cost, index))
      
        # Add last 'candidates' workers from the right side
        for index in range(num_workers - candidates, num_workers):
            heappush(min_heap, (costs[index], index))
      
        left_pointer = candidates
        right_pointer = num_workers - candidates - 1
      
        total_cost = 0
      
        # Hire k workers
        for _ in range(k):
            
            worker_cost, worker_index = heappop(min_heap)
            total_cost += worker_cost
          
            
            if left_pointer > right_pointer:
                continue
        
            if worker_index < left_pointer:
                heappush(min_heap, (costs[left_pointer], left_pointer))
                left_pointer += 1
            else:
                heappush(min_heap, (costs[right_pointer], right_pointer))
                right_pointer -= 1
      
        return total_cost