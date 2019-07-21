loh = [4,1,1,2,2,6,5,3,6,2,1,1] # CHANGE THIS

ALPHANUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def TryPath(hour, current_path, depth, verbose=False):
    if clock[hour][0] not in current_path:
        new_hour = clock[hour][0]
        TryPath(new_hour, current_path+[new_hour], depth+1)
    if clock[hour][1] not in current_path:
        new_hour = clock[hour][1]
        TryPath(new_hour, current_path+[new_hour], depth+1)
    if depth==max_depth:
        print '\n\nVICTORY, KUPO! PATH:\n{}'.format(current_path)
    elif verbose:
        print 'Failure at depth {}; path:\n{}'.format(depth, current_path)

def GenHourIDs(list_of_hours):
    occ_count = {}
    hour_ids = []
    for j in range(max_depth):
        occ_count[j] = 0
    for hour in list_of_hours:
        oc = ALPHANUM[occ_count[hour]]
        hour_ids += [str(hour)+oc]
        occ_count[hour] += 1
    return hour_ids

def GenClock(list_of_hours):
    max_depth = len(list_of_hours)
    clock = {}
    hour_ids = GenHourIDs(list_of_hours)
    for j,hid in enumerate(hour_ids):
        h = list_of_hours[j]
        idx_m = j-h
        idx_p = j+h
        if idx_p >= max_depth:
            idx_p -= max_depth
        clock[hid] = [hour_ids[idx_m], hour_ids[idx_p]]
    return clock

max_depth = len(loh)
print("I'm guessing your clock contains {} hours; if not, you probably bonked up the LOH".format(
      max_depth))

clock = GenClock(loh)
hours = clock.keys()
for hour in hours:
    TryPath(hour, [hour], 1)
