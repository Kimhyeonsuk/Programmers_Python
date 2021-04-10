def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx,phonenumber in enumerate(phone_book):
        if idx+1!=len(phone_book) and phone_book[idx+1][0:len(phonenumber)]==phonenumber:
            return False
    return answer