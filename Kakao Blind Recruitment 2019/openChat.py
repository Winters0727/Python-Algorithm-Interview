def solution(record):
    answer = []
    temp_list = []
    name_dict = {}
    for r in record:
        temp_log = r.split(' ')
        if len(temp_log) < 3:
            cmd, user_id = temp_log
        else:
            cmd, user_id, name = temp_log
        if cmd == "Enter":
            temp_list.append((user_id, "님이 들어왔습니다."))
            if user_id not in name_dict:
                name_dict[user_id] = name
            else:
                if name_dict[user_id] != name:
                    name_dict[user_id] = name
        elif cmd == "Leave":
            temp_list.append((user_id, "님이 나갔습니다."))
        elif cmd == "Change":
            name_dict[user_id] = name
        else:
            raise Exception("존재하지 않는 명령어입니다.")
    
    for log in temp_list:
        user_id, text = log
        answer.append(name_dict[user_id] + text)
    
    return answer