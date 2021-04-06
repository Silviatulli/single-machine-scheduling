# import required libraries, variables and functions
from extract_data import *
from disp_solution_2 import disp_solution
import get_array_of_comp_tasks
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
n_comp_tasks = result["objective"]
comp_tasks_str = result.solution._output_item
comp_tasks_str_edit = comp_tasks_str.strip("[").strip("]").split(", ")
comp_tasks = get_array_of_comp_tasks.get_bool_comp_tasks(comp_tasks_str_edit)

disp_solution(comp_tasks, n_frags, n_comp_tasks, st_frag, frag_t, task_cor_frag)


