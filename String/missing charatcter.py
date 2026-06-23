import string
def missingCharacters(s):
    digits="0123456789"
    letters=string.ascii_lowercase
    md=[]
    ml=[]
    for d in digits:
        if d not in s:
            ml.append(d)
    for l in letters:
        if l not in s:
            ml.append(l)
    return ''.join(md)+''.join(ml)
s="7985interdisciplinary12"
print(missingCharacters(s))