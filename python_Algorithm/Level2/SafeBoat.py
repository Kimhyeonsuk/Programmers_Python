def solution(people, limit):
    answer = 0
    people.sort()
    first=0
    last=len(people)-1
    while first<=last:
        if first==last:
            first+=1
            last-=1
            answer+=1
        else:
            if people[first]+people[last]<=limit:
                answer+=1
                first+=1
                last-=1
            else:
                answer+=1
                last-=1

    return answer