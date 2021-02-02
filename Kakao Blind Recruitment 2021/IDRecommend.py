def solution(new_id):
    def first(in_id):
        new_id = in_id[:]
        for index, char in enumerate(in_id):
            if char.isalpha():
                new_id[index] = char.lower()
        return new_id
    
    def second(in_id):
        new_id = []
        append_list = ['.', '-', '_']
        for index, char in enumerate(in_id):
            if not char.isalpha():
                if char.isdigit() or char in append_list:
                    new_id.append(char)
            else:
                new_id.append(char)
        return new_id
    
    def third(in_id):
        new_id = []
        for index, char in enumerate(in_id):
            if index == 0:
                pass
            elif char == '.':
                if new_id[-1] == '.':
                    continue
            new_id.append(char)
        return new_id
    
    def fourth(in_id):
        new_id = in_id[:]
        if len(new_id) > 1:
            if new_id[0] == '.':
                new_id.pop(0)
        if len(new_id) > 0:
            if new_id[-1] == '.':
                new_id.pop()
        return new_id
    
    def fifth(in_id):
        if len(in_id) == 0:
            return ['a']
        else:
            return in_id
        
    def sixth(in_id):
        if len(in_id) >= 16:
            new_id = in_id[:15]
            if new_id[-1] == '.':
                new_id.pop()
            return new_id
        else:
            return in_id
    
    def seventh(in_id):
        if len(in_id) < 3:
            new_id = in_id[:]
            while len(new_id) < 3:
                new_id.append(new_id[-1])
            return new_id
        return in_id
    
    list_id = list(new_id)
    first_id = first(list_id)
    second_id = second(first_id)
    third_id = third(second_id)
    fourth_id = fourth(third_id)
    fifth_id = fifth(fourth_id)
    sixth_id = sixth(fifth_id)
    seventh_id = seventh(sixth_id)
    answer = ''.join(seventh_id)

    return answer