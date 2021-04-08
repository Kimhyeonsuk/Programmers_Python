import math
def solution(numbers, hand):
    answer = ''
    keypad={'1':[0,0],'2':[0,1],'3':[0,2]
            ,'4':[1,0],'5':[1,1],'6':[1,2]
            ,'7':[2,0],'8':[2,1],'9':[2,2]
            ,'*':[3,0],'0':[3,1],'#':[3,2]}
    left='*'
    right='#'

    for num in numbers:
        if num==1 or num==4 or num==7:
            left=str(num)
            answer+='L'
        elif num==3 or num==6 or num==9:
            right=str(num)
            answer+='R'
        else:
            leftdiffer=abs(keypad[left][0]-keypad[str(num)][0])+abs(keypad[left][1]-keypad[str(num)][1])
            rightdiffer=abs(keypad[right][0]-keypad[str(num)][0])+abs(keypad[right][1]-keypad[str(num)][1])

            if(leftdiffer<rightdiffer):
                left=str(num)
                answer+='L'
            elif(leftdiffer>rightdiffer):
                right=str(num)
                answer+='R'
            else:
                if hand=='left':
                    left = str(num)
                    answer += 'L'
                else:
                    right = str(num)
                    answer += 'R'
    return answer