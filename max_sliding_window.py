from collections import deque
def max_sliding_window_naive(sq, m):
    ans = []
    if m==len(sq):
        return [max(sq)]
    if len(sq)==0:
        return []
    if m==1:
        return sq
    q = deque()
    mx = sq[0]
    mxi = 0
    for i in range(m):
        if not q or sq[i]<sq[q[-1]]:
            q.append(i) 
        else:
            while q and sq[q[-1]]<=sq[i]:
                q.pop()
            q.append(i)
    ans.append(sq[q[0]])
    #print(q)
    for i in range(m,len(sq)):
        t = i-m
        while q and q[0]<=t:
            q.popleft()
        if not q or sq[i]<sq[q[-1]]:
            q.append(i)
        else:
            while q and sq[q[-1]]<=sq[i]:
                q.pop()
            q.append(i)
        #print(q)
        ans.append(sq[q[0]])
    return ans

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    m=  int(input())
    l = max_sliding_window_naive(input_sequence, m)
    print(l[0],end="")
    for i in range(1,len(l)):
        print(" {}".format(l[i]),end="")