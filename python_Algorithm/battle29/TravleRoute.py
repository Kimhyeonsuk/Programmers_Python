from collections import defaultdict
def solution(tickets):
    answer = []
    tickets.sort(key=lambda ticket:ticket[1],reverse=True)
    dic=defaultdict(list)
    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])
    st=['ICN']
    while st:
        here=st[-1]
        if here not in dic or len(dic[here])==0:
            answer.append(st.pop())
        else:
            st.append(dic[here].pop())

    answer.reverse()
    return answer