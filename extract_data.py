import fileinput

# open problem data file and read data
with fileinput.input() as data:
    # initiate variables
    l1 = data.readline()
    n_tasks = int(l1.strip('\n'))
    start_t = []
    process_t = []
    deadline_t = []
    frag_t = []
    frags = []
    for i in range(n_tasks):
        l = data.readline().split()
        count = 0
        for k in l:
            count += 1
            if count == 1:
                start_t.append(int(k))
            if count == 2:
                process_t.append(int(k))
            if count == 3:
                deadline_t.append(int(k))
            if count == 4:
                frag_t.append(int(k))
            elif count > 4:
                frags.append(int(k))

    num_depend = []
    dependencies = []
    for i in range(n_tasks):
        l = data.readline().split()
        count = 0
        for k in l:
            if count == 0:
                num_depend.append(int(k))
            elif count >= 0:
                dependencies.append(int(k))
            count += 1

max_depend = max(num_depend)
depend_data = []
count = 0
for i in range(n_tasks):
    task_depend = []
    num_dep_task = num_depend[i]
    task_depend.append(num_dep_task)
    diff = max_depend - num_dep_task
    if num_dep_task != 0:
        for k in range(num_dep_task):
            task_depend.append(dependencies[count])
            count += 1
        if diff!=0:
            for kk in range(diff):
                task_depend.append(0)
    elif num_dep_task == 0:
        for j in range(diff):
            task_depend.append(0)
    depend_data.append(task_depend)

# print ("start_t = ",start_t)
# print (process_t)
# print (deadline_t)
# print ("frag_t = ",frag_t)
# print ("frags = ",frags)
# print ("num_depend = ",num_depend)
# print ("dependencies = ",dependencies)
# print ("depend data = ",depend_data)

# total number of frags
n_frags = sum(frag_t)
# print (n_frags)

# create task corresponding to frag array
task_cor_frag = []
for i in range(n_tasks):
    for k in range(frag_t[i]):
        task_cor_frag.append(i+1)
# print (task_cor_frag)

#calculate earliest start time
EST = []
n_frag = 0
for i in range(len(frag_t)):
    est_fr = start_t[i]
    num_frags = frag_t[i]
    for k in range(num_frags):
        EST.append(est_fr)
        est_fr += frags[n_frag]
        n_frag+=1
# print(EST)
