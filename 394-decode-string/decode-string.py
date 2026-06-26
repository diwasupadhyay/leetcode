class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_num = 0
        current_string = ''

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ''
            elif char == ']':
                prev_string = string_stack.pop()
                repeat_count = count_stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                current_string += char

        return current_string