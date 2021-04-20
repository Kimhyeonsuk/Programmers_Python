def canInstallColumn(x,y,locMap):
    if len(locMap[x][y])>0:
        return True
    return False
def canInstallLand(x,y,locMap):
    columnNum=0
    landNum=0
    for num in locMap[x][y]:
        if num==1:
            columnNum+=1
        elif num==3:
            landNum+=1
    if x+1!= len(locMap):
        for num in locMap[x+1][y]:
            if num==1:
                columnNum+=1
            elif num==2:
                landNum+=1
    if columnNum>0 or landNum>=2:
        return True
    return False
def canRemoveLand(x, y, locMap):
    #양쪽 보 확인
    #왼쪽 확인
    if 1 not in  locMap[x][y]:
        if x==0 or 1 not in locMap[x-1][y]:
            return False
    if x+1!=len(locMap) and 1 not in locMap[x+1][y]:
        if 1 not in locMap[x+2][y]:
            return False
    return True

def canRemoveColumn(x,y,locMap):
    for num in locMap[x][y]:
        if num==0:
            return False
        elif num==2:
            cNum=0
            lNum=0
            if 3 in locMap[x][y]:
                lNum+=1
            for num2 in locMap[x+1][y]:
                if num2==1:
                    cNum+=1
                elif num2==2:
                    lNum+=1
            if cNum<=0 and lNum<2:
                return False
        elif num==3:
            cNum = 0
            lNum = 0
            if 2 in locMap[x][y]:
                lNum += 1
            for num2 in locMap[x - 1][y]:
                if num2 == 1:
                    cNum += 1
                elif num2 == 2:
                    lNum += 1
            if cNum<=0 and lNum<2:
                return False
    return True
def solution(n, build_frame):
    answer = []
    locMap=[[[] for i in range(n+1)]for j in range(n+1)]

    for idx,frameInfo in enumerate(build_frame):
        x=frameInfo[0]
        y=frameInfo[1]
        isLand=frameInfo[2]
        isDelete=frameInfo[3]

        if isDelete==0: #삭제
            if isLand:  # 보
                print(1)
                if canRemoveLand(x, y, locMap):
                    locMap[x][y].remove(2)
                    locMap[x + 1][y].remove(3)
            else:  #기둥
                if canRemoveColumn(x,y+1,locMap):
                    locMap[x][y].remove(0)
                    locMap[x][y+1].remove(1)
        else:#설치
            if isLand:# 보
                if canInstallLand(x,y,locMap):
                    locMap[x][y].append(2)
                    locMap[x+1][y].append(3)
            else:#기둥
                if y == 0:  # 최하단에 지을때
                    locMap[x][y].append(0)
                    locMap[x][y+1].append(1)
                elif canInstallColumn(x,y,locMap):
                    locMap[x][y].append(0)
                    locMap[x][y+1].append(1)
    for idx,numlist in enumerate(locMap):
        for jdx,num in enumerate(numlist):
            for k in num:
                if k == 0:
                    answer.append([idx, jdx, 0])
                elif k == 2:
                    answer.append([idx, jdx, 1])

    answer.sort()
    return answer