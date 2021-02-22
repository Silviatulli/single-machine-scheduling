%%% Solve Single Machine Scheduling (SMS) Problem

%% Inputs required
int: n_tasks;  %total number of tasks
int: n_frags;  %total number of fragments
array[int] of int: process_t;  %1d array of process times of tasks
array[int] of int: deadline_t;  %1d array of deadlines of all tasks

%2d array consisting of number of dependencies of task (col 1) and dependent tasks (in following cols)
array[int,int] of 0..n_tasks: depend_data;

int: tot_prt = sum(process_t);  %add all process times
set of int: frags = 1..n_frags;  %set of frags

% 1d array of task corresponding to all fragments
array[frags] of 1..n_tasks: task_cor_fr;
% 1d array of process time of fragments
array[frags] of 0..max(process_t): prt_frag;
% 1d array of Earliest Start Time (EST) of fragments
array[frags] of 0..max(deadline_t): EST;

% main variable - actual start time of fragments
array[frags] of var 0..tot_prt: st_frag;

%% predicate definitions
% to ensure two fragments don't overlap
predicate no_overlap(var 0..tot_prt:st1, 0..max(process_t):pt1, var 0..tot_prt:st2, 0..max(process_t):pt2) = 
            st1 +  pt1 <= st2 \/ st2 + pt2 <= st1;
% to ensure no fragments in a set overlap
predicate exclusive(set of 0..n_frags: fr) =
  forall(f1, f2 in fr where f1>f2)
    (no_overlap(st_frag[f1], prt_frag[f1], st_frag[f2], prt_frag[f2]));

% to ensure fragment 1 precedes fragment 2
predicate precedes(var 0..tot_prt:st1, 0..max(process_t):pt1, var 0..tot_prt:st2) = st1 + pt1 <= st2;
% to ensure all fragments in a set are ordered
predicate frag_order(set of 0..n_frags: fr) = 
  forall(f1, f2 in fr where f1<f2)
    (precedes(st_frag[f1], prt_frag[f1], st_frag[f2]));

%% function definitions
% to get set of tasks that task 'i' depends on
function set of int: depends_on(0..n_tasks: i) =  {depend_data[i,j] | j in 2..depend_data[i,1]+1};
% to get fragments of a particular task
function set of 0..n_frags: frags_of(0..n_tasks: i) = {k | k in 1..n_frags where task_cor_fr[k]==i};
% to get an array with as many 1's as number of tasks completed before deadline
function array[int] of var opt 0..1: comp_tasks() = [1 | i in 1..n_tasks where st_frag[max(frags_of(i))] + prt_frag[max(frags_of(i))] <= deadline_t[i]];
% to sum elements of an array
function int: sum(array [$T] of int: x);

% variable to be maximized (objective) - completed tasks
var 0..n_tasks: comp_tasks = sum(comp_tasks());

%% Constraints
% C1 - fragment can start only after its EST
constraint forall(fr in 1..n_frags)
  (st_frag[fr]>=EST[fr]);
  
% C2 - fragments of a task should be ordered
constraint forall(t in 1..n_tasks)
  (frag_order(frags_of(t)));

%C3 - no fragment should overlap
constraint exclusive(1..n_frags);


%C4 - if a task t1 depends on t2; last fragment of t2 should precede first fragment of t1
constraint forall(t1 in 1..n_tasks where depend_data[t1,1]!=0) (
  forall(t2 in depends_on(t1))
    (precedes(st_frag[max(frags_of(t2))], prt_frag[max(frags_of(t2))], st_frag[min(frags_of(t1))])
  ));

%% solve
solve maximize comp_tasks;

