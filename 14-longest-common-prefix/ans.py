def sol(strs):
    if len(strs)==1:
        return strs[0]
    ans=""
    ind=1
    prefix=strs[0]
    done = False
    while not(done):
        for i in strs[1:]:
            if prefix[:ind] != i[:ind]:
                done=True
                break
        if not(done):
            ans=prefix[:ind]
            ind+=1
    return ans
strs=["flower","flow"]
print(sol(strs))