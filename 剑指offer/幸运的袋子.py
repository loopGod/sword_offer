from functools import reduce 

def func(x,y):
    return x*y
def allson(sl,sub,d,res,count=[],f=0):
    if d>=len(sl):
        if sub not in res:
            res.append(sub)
            if sub!=[]:
                if sum(sub)>reduce(func,sub):
                    count.append(1)
                else:
                    f=1
        return
    if f==0:
        allson(sl,sub+[sl[d]],d+1,res,count,f)
        allson(sl,sub,d+1,res,count,f)
n=int(input())
xi=list(map(int,input().split()))
res=[]
count=[]
allson(sorted(xi),[],0,res,count,0)
print(sum(count))

'''
def func(x,y):
    return x*y
n=int(input())
xi=list(map(int,input().split()))
res=[]
allson(xi,[],0,res)
#res=list(set(tuple(map(tuple,res))))
count=0
for i,v in enumerate(res):
    if v!=():
        if sum(v)>reduce(func,v):
            count+=1
print(count)
'''