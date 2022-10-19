x = int(input())
for tc in range(1, x+1):
    sentence = input()
    l = len(sentence)
    lst = []
    result=1
    for s in sentence:
        #( 이나 {이면 lst에 담음
        if s=='(' or s=='{' or s=='[':
            lst.append(s)
        elif s==')' or s=='}'or s==']':
            if len(lst)==0:
                result=0
                break
            else:
                check = lst.pop()
                if s==')' and check =='{':
                    result=0
                    break
                elif s==')' and check =='[':
                    result=0
                    break
                elif s=='}' and check =='(':
                    result=0
                    break
                elif s=='}' and check =='[':
                    result=0
                    break
                elif s==']' and check =='(':
                    result=0
                    break
                elif s==']' and check =='{':
                    result=0
                    break
    if len(lst):
        result=0
    if(result == 1):
        print('YES')
    else:
        print('NO')