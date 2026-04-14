class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                    if last == "(" and char == ")" or last == "[" and char == "]" or last == "{" and char == "}":
                        continue
                    else:
                        return False
                else:
                    return False

        return stack == []