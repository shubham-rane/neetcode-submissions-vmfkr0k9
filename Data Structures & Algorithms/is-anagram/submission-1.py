class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = dict()
        dictt = dict()

        # dictionary which represents frequency of characters in s
        for char in s:
            if char in dicts:
                dicts[char] += 1
            else:
                dicts[char] = 1
        
        # iterating through t and removing elements from s
        for char in t:
            if char in dicts:
                dicts[char] -= 1

                if dicts[char] == 0:
                    del dicts[char]
            else:
                return False
        
        return dicts == {}

        