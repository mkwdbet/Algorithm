doc = input() # 문서 
word = input() # 찾을 문자열
word_len = len(word) #문자열의 길이
i = 0 # doc 인덱스
cnt = 0 # 문자열이 나온 횟수 = 답
while (len(doc) >= i):
    try:
        if doc[i : i + word_len] == word:
            i += word_len
            cnt += 1
        else:
            i += 1
    except:
        break
print(cnt)
