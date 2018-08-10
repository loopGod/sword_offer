def get_sc(s,n,sub,res):
    
    if n>=4:
        if sub[0:2]==sub[2:]: 
            res.append(sub)
        return
    if n>1:
        tmp=1
    else:
        tmp=n
    for i in range(tmp,len(s)):
        get_sc(s[i:],n+1,sub+s[i],res)
res=[]
str0=input()
get_sc(str0,0,'',res)
for i in range(1,len(str0)):
    if str0[i]==str0[i-1]:
        res.append[0]
if len(res)>0:
    print('Dislikes')
else:
    print('Likes')
