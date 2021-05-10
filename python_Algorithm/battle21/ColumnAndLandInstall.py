def chk(frame,answer):
    for otherFrame in answer:
        x=otherFrame[0]
        y=otherFrame[1]
        what=otherFrame[2]
        if what==0:
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            else:
                return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer:continue
            elif [x-1,y,1] in answer and [x+1,y,1] in answer:continue
            else:
                return False
    return True
def solution(n, build_frame):
    answer = []
    board=[[[] for _ in range(n+1)] for _ in range(n+1)]
    for frame in build_frame:
        if frame[3]==1:#설치
            answer.append([frame[0],frame[1],frame[2]])
            if chk(frame,answer)==False:
                answer.remove([frame[0],frame[1],frame[2]])
        else:
            answer.remove([frame[0],frame[1],frame[2]])
            if chk(frame,answer)==False:
                answer.append([frame[0],frame[1],frame[2]])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer