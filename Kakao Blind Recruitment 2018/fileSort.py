def solution(files):
    answer = []

    special_char = [' ', '.', '-']
    middle_s = 0
    copy_files = files[:]
    my_files = []
    
    while copy_files:
        file = copy_files.pop()
        find_head, find_middle = False, False
        for index, char in enumerate(file):
            if not find_head:
                if char.isalpha() or char in special_char:
                    continue
                else:
                    head = file[:index]
                    find_head = True
                    middle_s = index
                    middle_count = 1
            elif find_head and not find_middle:
                if char.isdigit() and middle_count < 5:
                    middle_count += 1
                    continue
                else:
                    middle = file[middle_s:index]
                    find_middle = True
                    tail = file[index:]
                    break
        if not find_middle:
            middle = file[middle_s:]
            tail = ''
        my_files.append((head, middle, tail))

    my_files.sort(key=lambda x : [x[0].lower(), int(x[1]), files.index(''.join(x))], reverse=True)
    
    while my_files:
        answer.append(''.join(my_files.pop()))
    return answer