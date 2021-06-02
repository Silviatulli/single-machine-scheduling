# Single Machine Scheduling
Real-time systems found their application in an increasingly wide range of domains  e.g., healthcare, industrial production. To alleviate the problem of systems' overload leading to failure or catastrophe, researchers extensively studied classical scheduling. However, the large diversity of the proposed solvers poses challenges to test the models' validity. Hence, we develop a software tool for solving a single machine scheduling (SMS) problem using an high-level language that is solver-independent. We refer to previous Satisfiability Modulo Theories (SMT) formulations and use a MiniZinc framework for Constraint Satisfaction Problems (CSP). 

This is project is a coursework for [Optimization and Boolean Constraints](https://fenix.tecnico.ulisboa.pt/disciplinas/ROB/2019-2020/1-semestre/programa).

# test
To run the code: python main.py "inputname.sms" > "outputname.out"

# references
* [Maximum Satisfiability Formulation for Optimal Scheduling in Overloaded Real-Time Systems](https://link.springer.com/chapter/10.1007/978-3-030-29908-8_49)
* [Scheduling overload for real-time systems using SMT solver](https://ieeexplore.ieee.org/document/7515899)
