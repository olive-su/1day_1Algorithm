def solution(word):
    alphabet = {0:'A', 1:'E', 2:'I', 3:'O', 4:'U'}
    rev_alphabet = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    cnt = 0
    string = []
    while True:
        cnt += 1
        if len(string) < 5:
            string.append('A')
        elif string[-1] == 'U':
            while string[-1] == 'U':
                string.pop()
            string[-1] = alphabet[rev_alphabet[string[-1]] + 1]
        else:
            string[-1] = alphabet[list(alphabet.values()).index(string[-1]) + 1]
        if string == list(word):
            return cnt
