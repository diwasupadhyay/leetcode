class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def count_reversals(current_city: int, parent_city: int) -> int:
            total_reversals = 0
          
            # Visit all neighbors of current city
            for neighbor_city, needs_reversal in adjacency_list[current_city]:
                if neighbor_city != parent_city:
                    total_reversals += needs_reversal + count_reversals(neighbor_city, current_city)
          
            return total_reversals
      
        adjacency_list = [[] for _ in range(n)]
      
        for from_city, to_city in connections:
            adjacency_list[from_city].append((to_city, 1))
            adjacency_list[to_city].append((from_city, 0))
      
        return count_reversals(0, -1)