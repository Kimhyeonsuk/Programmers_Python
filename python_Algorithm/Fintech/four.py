def solution(n, queries):
    answer = []
    #스택들이 중앙을 공유
    #push(i,x) i번 스택에 정수, 모든스택이 비어있으면 중앙에 x
    #pop(i번 스택의 바깥원소 제거
    #중앙이 제거되면-> 시계 방향으로 가장 가까운 스택의 원소들이 중앙공간으로 한칸씩 이동
    stacks=[[] for i in range(n)]
    center=-1
    for querie in queries:
        if querie[1]==-1:#pop
            if stacks[querie[0]-1]:
                answer.append(stacks[querie[0]-1].pop())
            elif not stacks[querie[0]-1]:
                answer.append(center)
                center=-1
                fnd=False
                for i in range(1,n):
                    idx=((querie[0]-1)+i)%n
                    if not stacks[idx]:
                        continue
                    else:
                        center=stacks[idx].pop(0)
                        fnd=True
                        break
        else:#push
            if center==-1:
                center=querie[1]
            else:
                stacks[querie[0]-1].append(querie[1])


    return answer