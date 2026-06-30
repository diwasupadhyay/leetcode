class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)
        result = []
        if s_length < p_length:
            return result
        pattern_counter = Counter(p)
        window_counter = Counter(s[:p_length - 1])
        for i in range(p_length - 1, s_length):
            window_counter[s[i]] += 1
            if pattern_counter == window_counter:
                result.append(i - p_length + 1)
            left_char = s[i - p_length + 1]
            window_counter[left_char] -= 1
            if window_counter[left_char] == 0:
                del window_counter[left_char]
      
        return result