class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()
      
        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 2:
                    # Add rotten orange position to queue
                    queue.append((row_idx, col_idx))
                elif grid[row_idx][col_idx] == 1:
                    # Count fresh oranges
                    fresh_count += 1
      
        # Time elapsed (in minutes)
        minutes_elapsed = 0
      
        # Direction vectors for 4-directional movement (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        # BFS to rot adjacent fresh oranges
        while queue and fresh_count > 0:
            minutes_elapsed += 1
          
            # Process all oranges that rot in the current minute
            current_level_size = len(queue)
            for _ in range(current_level_size):
                curr_row, curr_col = queue.popleft()
              
                # Check all 4 adjacent cells
                for row_delta, col_delta in directions:
                    next_row = curr_row + row_delta
                    next_col = curr_col + col_delta
                  
                    # Check if the adjacent cell is within bounds and contains a fresh orange
                    if (0 <= next_row < rows and 
                        0 <= next_col < cols and 
                        grid[next_row][next_col] == 1):
                      
                        # Rot the fresh orange
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        fresh_count -= 1
                      
                        # Early termination if all oranges are rotten
                        if fresh_count == 0:
                            return minutes_elapsed
      
        return -1 if fresh_count > 0 else 0