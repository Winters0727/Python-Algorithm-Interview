from collections import defaultdict

# 정확성 통과, 효율성 통과X
def solution(info, query):
    answer = []
    langs, positions, careers, foods = [], [], [], []
    persons = defaultdict(list)
    for recruit in info:
        person = ''
        lang, position, career, food, point = recruit.split(' ')
        
        if lang not in langs:
            langs.append(lang)
        person += str(langs.index(lang))
        
        if position not in positions:
            positions.append(position)
        person += str(positions.index(position))
        
        if career not in careers:
            careers.append(career)
        person += str(careers.index(career))
        
        if food not in foods:
            foods.append(food)
        person += str(foods.index(food))
        
        persons[point].append(person)
        
    for q in query:
        counter = 0
        lang, position, career, food_and_point = q.split(' and ')
        food, point = food_and_point.split(' ')
        person_query = ''
        
        if lang == '-':
            person_query += str(9)
        else:
            if lang not in langs:
                langs.append(lang)
            person_query += str(langs.index(lang))
        
        if position == '-':
            person_query += str(9)
        else:
            if position not in positions:
                positions.append(position)
            person_query += str(positions.index(position))
        
        if career == '-':
            person_query += str(9)
        else:
            if career not in careers:
                careers.append(career)
            person_query += str(careers.index(career))
        
        if food == '-':
            person_query += str(9)
        else:
            if food not in foods:
                foods.append(food)
            person_query += str(foods.index(food))
        
        for key in persons.keys():
            if int(key) >= int(point):
                for person in persons[key]:
                    for index in range(4):
                        if person_query[index] == '9':
                            continue
                        elif person[index] != person_query[index]:
                            break
                    else:
                        counter += 1
        answer.append(counter)
    return answer

# 정확성 통과, 효율성 통과 X
from collections import defaultdict

def solution(info, query):
    def create_except(arr):
        n = 0
        temp_arr = [arr[n], '9']
        while n < 3:
            n += 1
            new_arr = []
            while temp_arr:
                temp_val = temp_arr.pop()
                new_arr.append(temp_val+arr[n])
                new_arr.append(temp_val+'9')
            temp_arr = new_arr[:]
        return new_arr

    answer = []
    langs = ['cpp', 'java', 'python']
    positions = ['frontend', 'backend']
    careers = ['junior', 'senior']
    foods = ['chicken', 'pizza']
    recruit = defaultdict(list)
    dict_key = []
    for index, person in enumerate(info):
        lang, position, career, food, point = person.split(' ')
        temp_person = [
            langs.index(lang),
            positions.index(position),
            careers.index(career),
            foods.index(food)
        ]
        case_all = create_except(list(map(str, temp_person)))
        key = '{0}-{1}'.format(point,str(index))
        recruit[key] = case_all
        dict_key.append(key)
    dict_key.sort(key = lambda x : int(x.split('-')[0]))
    
    for q in query:
        counter = 0
        lang, position, career, food_and_point = q.split(' and ')
        food, point = food_and_point.split(' ')
        temp_query = [
            langs.index(lang) if lang in langs else 9,
            positions.index(position) if position in positions else 9,
            careers.index(career) if career in careers else 9,
            foods.index(food) if food in foods else 9,
        ]
        new_query = ''.join(map(str, temp_query))
        for key in dict_key:
            person_point = key.split('-')[0]
            if int(person_point) >= int(point):
                if new_query in recruit[key]:
                    counter += 1
        answer.append(counter)
    return answer