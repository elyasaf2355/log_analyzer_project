from reader import x

def external_ip(logs_list: list):
    return [log[1] for log in logs_list if not log[1].startswith('10.') and not log[1].startswith('192.168.')]

def sensitive_port(logs_list: list):
    return [log for log in logs_list if log[3] == '22' or log[3] == '23' or log[3] =='3389']

def size_over_5000(logs_list: list):
    return [log for log in logs_list if int(log[5]) > 5000]

def mark_over_size(logs_list: list):
    l = []
    for log in logs_list:
        state = "LARGE" if int(log[5]) > 5000 else "NORMAL"
        l.append((state, log))
    return l

print(mark_over_size(x))