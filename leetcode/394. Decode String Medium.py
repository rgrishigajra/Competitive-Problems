class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        n = len(s)
        character = 0
        cur_str = ''
        cur_num = 0
        for character in s:
            if character == '[':
                string_stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif character == ']':
                prev_str, prev_num = string_stack.pop()
                cur_str = prev_str + cur_str * prev_num
            elif character.isdigit():
                cur_num = cur_num*10 + int(character)
            else:
                cur_str += character
        return cur_str
