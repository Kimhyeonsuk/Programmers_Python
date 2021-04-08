def solution(board, moves):
    answer = 0
    listBaguni=[]
    for loc in moves:
        for i in range(0,len(board)):
            if(board[i][loc-1]!=0):
                if len(listBaguni)!=0 and listBaguni[-1]==board[i][loc-1]:
                    listBaguni.pop()
                    answer+=2
                else:
                    listBaguni.append(board[i][loc-1])
                board[i][loc-1]=0
                break
    return answer