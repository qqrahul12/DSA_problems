text = input()
pat = input()
ps = [0]
j,i = 0,1
while i< len(pat):
    if pat[i]==pat[j]:
        ps.append(j+1)
        j+=1
        i+=1
    elif j==0:
        ps.append(0)
        i+=1
    else:
        j = ps[j-1]
pp= pt = 0
while pt<len(text):
    if text[pt]==pat[pp]:
        pt+=1
        pp+=1
    elif pp!=0:
        pp = ps[pp-1]
    else:
        pt+=1
    if pp == len(pat):
        print("pattern found at {}".format(pt-len(pat)))
        pp = ps[pp-1]