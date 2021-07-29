import sys

croatian_str = sys.stdin.readline().rstrip()
croatian_char = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = len(croatian_str)
for i in range(len(croatian_str)-1):
    if croatian_str[i] + croatian_str[i + 1] in croatian_char:
        cnt -= 1
for i in range(len(croatian_str)-2):
    if croatian_str[i] + croatian_str[i + 1] + croatian_str[i + 2] == 'dz=': # 이전 반복문에서 'z='를 이미 처리했기 때문에 -1만 해줌
        cnt -= 1
print(cnt)
