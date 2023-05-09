# a. packages are imported

from types import SimpleNamespace

from scipy import optimize
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# b. class is defined 

class OLGModel(): # Defining the OLG model
    
    def __init__(self):
        # Creating namespace for parameters
        self.par = SimpleNamespace()
        self.setup()

    def setup(self): # Defining the general setup of the model - parameters etc.
        par = self.par

        # a. Defining parameters for the utility function and euler equation

        par.c_1t = sp.symbols('c_1t') # Consumption in period t
        par.c_2t = sp.symbols('c_{2t+1}') # Consumption in period t+1
        par.rho = sp.symbols('rho') # Time preference coefficient
        par.lamb = sp.symbols('lambda')

        # b. Defining parameters for the production function 

        par.alpha = sp.symbols('alpha')
        par.K_t = sp.symbols('K_t')
        par.K_t1 = sp.symbols('K_{t+1}')
        par.L_t = sp.symbols('L_t')
        par.L_t1 = sp.symbols('L_{t+1}')
        par.k_t = sp.symbols('k_t')
        par.k_t1 = sp.symbols('k_{t+1}')
        par.A = sp.symbols('A')

        # c. Defining parameters and variables for the constraints

        # For the constraint in period t

        par.w_t = sp.symbols('w_t') # The wage received by the young in period t

        par.w_t1 = sp.symbols('w_{t+1}') # The wage received by the young in period t+1

        par.s_t = sp.symbols('s_t') # The savings in period t

        par.tau = sp.symbols('tau')

        # For the constraint in period t+1
        par.r_t1 = sp.symbols('r_{t+1}') # The interest rate between period t and t+1
        par.n = sp.symbols('n') # The constant population growth rate

        # Creating variables for capital accumulation and steady state capital

        par.first = (1 / (1 + (1+par.rho)/(2+par.rho)*((1-par.alpha)/par.alpha) * par.tau))
        par.second = ((1-par.alpha)*(1-par.tau))/((1+par.n)*(2+par.rho))
        par.third = par.A * par.k_t**par.alpha
        par.fourth = 1 / (1-par.alpha)

    def utility(self):
        par = self.par

        return sp.log(par.c_1t)+1/(1+par.rho)*sp.log(par.c_2t)
    
    def constraints(self):

        par = self.par
        constraint1 = sp.Eq(par.c_1t+par.s_t, (1-par.tau)*par.w_t)
        constraint2 = sp.Eq(par.c_2t, (1+par.r_t1)*par.s_t+(1+par.n)*par.tau*par.w_t1)

        # Finding the lifetime constraint 

        constraint2_sub = sp.solve(constraint2, par.s_t)
        lifetimeconstraint = constraint1.subs(par.s_t, constraint2_sub[0])

        return sp.solve(lifetimeconstraint, (1-par.tau)*par.w_t)[0]-(1-par.tau)*par.w_t
    
    def euler(self):
        par = self.par

        lagrangian = self.utility()+par.lamb*self.constraints()

        foc1 = sp.Eq(sp.diff(lagrangian, par.c_1t),0)
        foc2 = sp.Eq(sp.diff(lagrangian, par.c_2t),0)

        lambda1 = sp.solve(foc1, par.lamb)[0]
        lambda2 = sp.solve(foc2, par.lamb)[0]

        euler = sp.solve(sp.Eq(lambda1, lambda2), par.c_1t)[0]

        return sp.Eq(par.c_1t, euler)
    
    def savings(self):
        par = self.par
        
        euler = self.euler()
        constraint1_iso =par.s_t-(1-par.tau)*par.w_t
        constraint2_iso = (1+par.r_t1)*par.s_t+(1+par.n)*par.tau*par.w_t1

        savings = (euler.subs(par.c_1t, constraint1_iso)).subs(par.c_2t, constraint2_iso)

        optsavings = sp.solve(savings, par.s_t)[0]

        return optsavings
    
    def capitalaccum(self):
        par = self.par 

        kt01 = par.first*par.second*par.third
        kt1 = sp.Eq(par.k_t1, kt01)

        return kt1
    
    def steadystatecap(self):
        par = self.par 

        kss = (par.first*par.second*par.A)**par.fourth

        return sp.Eq(sp.symbols('k^*'),kss)
    
    def steadystatecapnum(self):
        par = self.par 

        kss = (par.first*par.second*par.A)**par.fourth

        return kss
    
    def capitalaccumnum(self):
        par = self.par 

        kt01 = par.first*par.second*par.third

        return kt01