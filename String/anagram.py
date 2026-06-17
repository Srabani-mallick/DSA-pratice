def areAnagrams(s1, s2):
        if len(s1) != len(s2):
            return False
        count = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1
        for ch in s2:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(areAnagrams(s1,s2))