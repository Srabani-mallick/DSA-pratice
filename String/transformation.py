def transformSentence(sentence):
    word=sentence.split(' ')
    r=[]
    for w in word:
        if not w:
            r.append(w)
            continue
        nw=w[0]
        for i in range(1,len(w)):
            p=w[i-1].lower()
            c=w[i].lower()
            if p<c:
                nw=nw+w[i].upper()
            elif c<p:
                nw=nw+w[i].lower()             
            else:
                nw=nw+w[i]
        r.append(nw)
    return ' '.join(r)
s="coOL dog"
print(transformSentence(s))