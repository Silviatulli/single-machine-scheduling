# function to write solution to .txt file in given format
def disp_solution(comp_tasks, st_frag, frag_t, frags, deadline_t, task_cor_frag):
    last_fr_idx = 0
    list_comp_task = []
    for i in range(len(frag_t)):
        last_fr_idx += frag_t[i]
        last_fr_st = st_frag[last_fr_idx-1]
        task_comp_t = last_fr_st + frags[last_fr_idx-1]
        if task_comp_t <= deadline_t[i]:
            list_comp_task.append(i+1)
    # print ("list of comp tasks = ", list_comp_task)
    frag_st_times = []
    idx_valid_st_frag = []
    for i in range(len(task_cor_frag)):
        if task_cor_frag[i] in list_comp_task:
            frag_st_times.append(st_frag[i])
            idx_valid_st_frag.append(i)
        else:
            continue
    # print (frag_st_times)
    # print (idx_valid_st_frag)

    print(str(comp_tasks))
    count = 0
    for i in range(comp_tasks):
        print(str(list_comp_task[i]),end="")
        for k in range(frag_t[list_comp_task[i]-1]):
            print((" "+str(frag_st_times[count])),end="")
            count += 1
        print("\n",end="")