def print_message(dic_list, line):
    if line[0] == 'C':
        return ;
    uid = ''
    i = 6
    while (i != len(line) and line[i] != ' '): # 아이디 구하는 과정
        uid += line[i]
        i += 1
    if line[0] == 'E':
        return (dic_list[uid] + "님이 들어왔습니다.")
    else :
        return (dic_list[uid] + "님이 나갔습니다.")

def making_dict(dic_list, line): # 아이디 - 닉네임 쌍 딕셔너리 생성
    uid = ''
    nickname = ''
    i = 0
    if line[0] == 'L':
        return ;
    while (line[i] != ' '): i += 1 # 명령어 필터링
    i += 1
    while (line[i] != ' '): # 아이디 구하는 과정
        uid += line[i]
        i += 1
    i += 1
    while (i != len(line)): # 닉네임 구하는 과정
        nickname += line[i]
        i += 1
    if uid in dic_list:
        dic_list[uid] = nickname
    else:
        dic_list[uid] = nickname
        
def solution(record):
    answer = list()
    dic_list = dict()
    for i in record:
        making_dict(dic_list, i)
    for j in record:
        str = ''
        str = print_message(dic_list, j)
        if str != None: answer.append(str)
    return answer;
