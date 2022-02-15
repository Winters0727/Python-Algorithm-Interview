from collections import defaultdict

def solution(id_list, report, k):
    report_history = defaultdict(list)
    report_counter = defaultdict(int)
    for call in report:
        reporter, reportee = call.split(' ')
        if reportee not in report_history[reporter]:
            report_history[reporter].append(reportee)
            report_counter[reportee] += 1
    answer = [len([user for user in report_history[reporter_id] if report_counter[user] >= k]) for reporter_id in id_list]
    return answer