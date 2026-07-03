class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
      
        start_row, start_col = entrance
        queue = deque([(start_row, start_col)])
      
        maze[start_row][start_col] = "+"
      
        steps = 0
      
        while queue:
            steps += 1
          
            for _ in range(len(queue)):
                current_row, current_col = queue.popleft()
              
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for row_offset, col_offset in directions:
                    next_row = current_row + row_offset
                    next_col = current_col + col_offset
                  
                    if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                        if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                            return steps
                      
                        queue.append((next_row, next_col))
                        maze[next_row][next_col] = "+"
        return -1
