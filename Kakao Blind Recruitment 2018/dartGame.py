def solution(dartResult):
    
    def convert_point(log, double_rear, double_now, sub_now):
        if log[1] != '0':
            num = int(log[0])
            case = log[1]
        else:
            num = 10
            case = log[2]
        if case == 'S':
            power_num = 1
        elif case == 'D':
            power_num = 2
        elif case == 'T':
            power_num = 3
        sub = -1 if sub_now else 1
        return pow(num, power_num)*pow(2, int(double_rear) + int(double_now))*sub
    
    answer = 0
    num_list = [str(num) for num in range(0,10)]
    data = []
    rear_point = 0
    for i, char in enumerate(dartResult):
        if char in num_list:
            if i and dartResult[i-1] not in num_list:
                data.append(dartResult[rear_point:i])
                rear_point = i
    data.append(dartResult[rear_point:])
    for i, log in enumerate(data[::-1]):
        double_rear, double_now, sub_now = False, False, False
        if i:
            if '*' in data[::-1][i-1]:
                double_rear = True
        if '*' in log:
            double_now = True
        if '#' in log:
            sub_now = True
        answer += convert_point(log, double_rear, double_now, sub_now)
    return answer