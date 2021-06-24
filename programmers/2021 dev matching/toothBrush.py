import math
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    account = defaultdict(dict)
    length = len(enroll)
    for index in range(length):
        account[enroll[index]] = {'refer':referral[index], 'money':0}

    sell_length = len(seller)
    for index in range(sell_length):
        man, money = seller[index], amount[index]*100
        while True:
            account[man]['money'] += math.ceil(money * 0.9)
            if money < 10:
                break
            if account[man]['refer'] != '-':
                money = math.floor(money * 0.1)
                man = account[man]['refer']
            else:
                break
    answer = [account[name]['money'] for name in enroll]
    return answer