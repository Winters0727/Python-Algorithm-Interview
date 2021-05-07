def solution(m, musicinfos):
    def change_melody(s):
        return s.replace('A#','a').replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g')
    
    m = change_melody(m)
    new_infos = [music.split(',') for music in musicinfos]
    new_melody = []
    for music in new_infos:
        start, end, title, melody = music
        start_time = start.split(':')
        end_time = end.split(':')
        # if start_time[0] != '00' and end_time[0] == '00':
        #     end_time[0] == '24'
        time = (int(end_time[0]) - int(start_time[0]))*60 + (int(end_time[1]) - int(start_time[1]))
        melody = change_melody(melody)
        melody_length = len(melody)
        if time < melody_length:
            temp_melody = melody[:time]
        else:
            div, mod = divmod(time, melody_length)
            temp_melody = melody*div + melody[:mod]
        new_melody.append((title, temp_melody, time))
    answer = '(None)'
    answer_list = []
    for (title, melody, time) in new_melody:
        if m in melody:
            answer_list.append((title, time))
    if answer_list:
        answer_list.sort(key = lambda x : [x[1], len(x[0])])
        answer = answer_list.pop()[0]
    return answer