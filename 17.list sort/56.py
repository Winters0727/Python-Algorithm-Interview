class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        sorted_list = sorted(intervals, reverse=True, key=lambda x : [x[0], x[1]])
        app_start, app_end = -1, -1
        while sorted_list:
            start, end = sorted_list.pop()
            if app_start == -1 or app_end == -1:
                app_start, app_end = start, end
            else:
                if end <= app_end:
                    continue
                elif start <= app_end:
                    app_end = end
                else:
                    answer.append([app_start, app_end])
                    app_start, app_end = start, end
        if [app_start, app_end] not in answer:
            answer.append([app_start, app_end])
            
        return answer