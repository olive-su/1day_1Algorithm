A, B = input().split()
A = int(A)
B = int(B)
if A > B:
  A, B = B, A
C = A % B
while C > 0:
  gcd = C
  A, B = B, C
  C = A % B
print(gcd)
