def filtering_start_end(string):
    new_string = ''
    if len(string) == 1: # 문자열의 길이가 1인 경우 빈 문자열 리턴
        return new_string
    else:
        if string[0] == '.': new_string = string[1:]
        else: new_string = string[:-1]
            
    if new_string[0] == '.' or new_string[-1] == '.': # 1차 필터링 이후, 다시 앞 뒤 변환이 필요할 경우 재귀호출
        return filtering_start_end(new_string)
    else:
        return new_string
    
def solution(new_id):
    forbidden = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower() # 소문자로 만들어줌
    for i in range(len(forbidden)):
        new_id = new_id.replace(forbidden[i], '') # 특수문자 제거
    while ('..' in new_id): # 마침표 중복 제거
        new_id = new_id.replace('..', '.')
    if new_id[0] == '.' or new_id[-1] == '.': # 글자수 15 제한 이전 앞 뒤 문자 필터링
        new_id = filtering_start_end(new_id)
    if new_id == '':
        new_id = 'a'
    new_id = new_id[:15]
    if new_id[0] == '.' or new_id[-1] == '.': # 글자수 15 제한 이후 앞 뒤 문자 필터링
        new_id = filtering_start_end(new_id)
        
    while (len(new_id) < 3):
        new_id += new_id[-1]
    
    return new_id
