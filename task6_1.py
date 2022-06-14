with open('nginx_logs.txt', 'r', encoding='utf-8') as log:
    for l in log:
        parts = l.split()
        record = (parts[0], parts[5].strip('"'), parts[6])
        print(record)