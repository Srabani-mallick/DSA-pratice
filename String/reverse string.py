def reverseString(s: str) -> str:
        rev=""
        for ch in s:
            rev=ch+rev
        return rev
s="hello"
print(reverseString(s))