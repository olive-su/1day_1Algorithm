N = list(map(int, input()))
ln = N[:len(N)//2]
rn = N[len(N)//2:]
if sum(ln) == sum(rn):
    print("LUCKY")
else:
    print("READY")
