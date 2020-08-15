# Uses python3
def edit_distance(a,b):
    m = len(a)
    n = len(b)
    s = []
    for i in range(n+1):
        s.append([])
        for j in range(m+1):
            s[i].append(0)
    for i in range(m+1):
        s[0][i]= i
    for i in range(n+1):
        s[i][0]=i
    for i in range(1,n+1):
        for j in range(1,m+1):
            x=y=z=0
            if a[j-1]==b[i-1]:
                x = s[i-1][j-1]
            else:
                x = s[i-1][j-1]+1
            y = s[i-1][j]+1
            z = s[i][j-1]+1
            s[i][j]=min(x,y,z)
    return s[n][m]

if __name__ == "__main__":
    a = input()
    b = input()
    print(edit_distance(a,b))
    