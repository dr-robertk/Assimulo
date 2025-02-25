#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Copyright (C) 2010 Modelon AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from assimulo.solvers import IDA
from assimulo.problem import Implicit_Problem

def run_example(with_plots=True):
    r"""
    Example for demonstrating the use of a user supplied Jacobian
    
    ODE:
    
    .. math::
       
        \dot y_1-y_3 &= 0 \\
        \dot y_2-y_4 &= 0 \\
        \dot y_3+y_5 y_1 &= 0 \\
        \dot y_4+y_5 y_2+9.82&= 0 \\
        y_3^2+y_4^2-y_5(y_1^2+y_2^2)-9.82 y_2&= 0 
    
    on return:
    
       - :dfn:`imp_mod`    problem instance
    
       - :dfn:`imp_sim`    solver instance
       
    """
    global order
    order = []
    
    #Defines the residual
    def f(t,y,yd):
        
        res_0 = yd[0]-y[2]
        res_1 = yd[1]-y[3]
        res_2 = yd[2]+y[4]*y[0]
        res_3 = yd[3]+y[4]*y[1]+9.82
        res_4 = y[2]**2+y[3]**2-y[4]*(y[0]**2+y[1]**2)-y[1]*9.82

        return np.array([res_0,res_1,res_2,res_3,res_4])
    
    def handle_result(solver, t ,y, yd):
        global order
        order.append(solver.get_last_order())
        
        solver.t_sol.extend([t])
        solver.y_sol.extend([y])
        solver.yd_sol.extend([yd])
        
        
    #The initial conditions
    y0 = [1.0,0.0,0.0,0.0,5] #Initial conditions
    yd0 = [0.0,0.0,0.0,-9.82,0.0] #Initial conditions
    
    #Create an Assimulo implicit problem
    imp_mod = Implicit_Problem(f,y0,yd0,name = 'Example for plotting used order')
    imp_mod.handle_result = handle_result
    
    #Sets the options to the problem
    imp_mod.algvar = [1.0,1.0,1.0,1.0,0.0] #Set the algebraic components
    
    #Create an Assimulo implicit solver (IDA)
    imp_sim = IDA(imp_mod) #Create a IDA solver
    
    #Sets the parameters
    imp_sim.atol = 1e-6 #Default 1e-6
    imp_sim.rtol = 1e-6 #Default 1e-6
    imp_sim.suppress_alg = True #Suppress the algebraic variables on the error test
    imp_sim.report_continuously = True
    
    #Let Sundials find consistent initial conditions by use of 'IDA_YA_YDP_INIT'
    imp_sim.make_consistent('IDA_YA_YDP_INIT')
    
    #Simulate
    t, y, yd = imp_sim.simulate(5) #Simulate 5 seconds
    
    #Plot
    if with_plots:
        import pylab as pl
        pl.figure(1)
        pl.plot(t,y,linestyle="dashed",marker="o") #Plot the solution
        pl.xlabel('Time')
        pl.ylabel('State')
        pl.title(imp_mod.name)
        
        pl.figure(2)
        pl.plot([0] + np.add.accumulate(np.diff(t)).tolist(), order)
        pl.title("Used order during the integration")
        pl.xlabel("Time")
        pl.ylabel("Order")
        pl.show()
    
    #Basic tests
    assert abs(y[-1][0] - 0.9401995)   < 1e-4
    assert abs(y[-1][1] + 0.34095124)  < 1e-4
    assert abs(yd[-1][0] + 0.88198927) < 1e-4
    assert abs(yd[-1][1] + 2.43227069) < 1e-4
    assert abs(order[-1] - 5) < 1e-4
    
    return imp_mod, imp_sim

if __name__=='__main__':
    mod,sim = run_example()
