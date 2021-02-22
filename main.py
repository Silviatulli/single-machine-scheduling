# import required libraries, variables and functions
from extract_data import *
from disp_solution import disp_solution
import pymzn
from minizinc import Instance, Model, Solver

# get a minizinc model
sms = Model("./sms.mzn")
gecode = Solver.lookup("gecode")

# create a .dzn file using extracted data from .txt file
dzn = {'n_tasks':n_tasks, 'n_frags':n_frags, 'process_t':process_t, 'deadline_t':deadline_t,
        'depend_data':depend_data, 'task_cor_fr':task_cor_frag, 'prt_frag':frags, 'EST':EST}
pymzn.dict2dzn(dzn, fout="task_data.dzn")

# assign data file to model and initiate an instance of it
sms.add_file("./task_data.dzn")
instance = Instance(gecode, sms)

# solve and get results
result = instance.solve()
st_frag = result["st_frag"]
comp_tasks = result["objective"]

# write the solution .txt file in given format
disp_solution(comp_tasks, st_frag, frag_t, frags, deadline_t, task_cor_frag)

# print(st_frag, comp_tasks)


