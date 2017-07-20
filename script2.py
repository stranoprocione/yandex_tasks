import time
with open('/home/mapache/python/data_task4.txt','r') as in_file:
    in_file.readline()
    m = 0
    total_microtasks = 0
    for line in in_file:
        login, tid, Microtasks, assigned_ts, closed_ts = line.strip().split('\t')
        t1 = time.mktime(time.strptime(assigned_ts, "%Y-%m-%d %H:%M:%S"))
        t2 = time.mktime(time.strptime(closed_ts, "%Y-%m-%d %H:%M:%S"))
        m += t2 - t1
        total_microtasks += float(Microtasks)
total_time = m / total_microtasks
microtask_cost = total_time / 30 
print('{}N'.format(microtask_cost))
