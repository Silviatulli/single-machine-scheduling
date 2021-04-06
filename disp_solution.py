# function to write solution to standard output
def disp_solution(comp_tasks, n_frags, n_comp_tasks, st_frag, frag_t, task_cor_frag) -> None:
    list_comp_task = []
    for i in range(len(comp_tasks)):
        if comp_tasks[i]==1:
            list_comp_task.append(i+1)
        else:
            continue
    
    frag_st_times = []
    for i in range(n_frags):
        if task_cor_frag[i] in list_comp_task:
            frag_st_times.append(st_frag[i])
        else:
            continue

    print(str(n_comp_tasks))
    count = 0
    for i in range(n_comp_tasks):
        print(str(list_comp_task[i]),end="")
        for _ in range(frag_t[list_comp_task[i]-1]):
            print((" "+str(frag_st_times[count])),end="")
            count += 1
        print("\n",end="")

