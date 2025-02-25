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

import pytest
from assimulo.exception import AssimuloException
from assimulo.examples import *
from assimulo.solvers.sundials import get_sundials_version

class Test_Examples:
    def test_cvode_with_jac_sparse(self):
        try:
            cvode_with_jac_sparse.run_example(with_plots=False)
        except AssimuloException:
            pass #Handle the case when SuperLU is not installed
    
    def test_ida_with_user_defined_handle_result(self):
        ida_with_user_defined_handle_result.run_example(with_plots=False)
    
    def test_radau5dae_time_events_f(self):
        radau5dae_time_events.run_example(with_plots=False)
        
    def test_kinsol_basic(self):
        kinsol_basic.run_example(with_plots=False)
    
    def test_kinsol_with_jac(self):
        kinsol_with_jac.run_example(with_plots=False)
    
    @pytest.mark.filterwarnings("ignore::Warning") # SparseEfficiencyWarning
    def test_kinsol_ors(self):
        kinsol_ors.run_example(with_plots=False)
    
    def test_cvode_with_preconditioning(self):
        cvode_with_preconditioning.run_example(with_plots=False)
    
    def test_dasp3_basic(self):
        print("Currently not running test_dasp3_basic. Numerically unstable problem.")
        #dasp3_basic.run_example(with_plots=False)
    
    def test_cvode_gyro(self):
        cvode_gyro.run_example(with_plots=False)
    
    def test_cvode_basic(self):
        cvode_basic.run_example(with_plots=False)

    def test_cvode_stability(self):
        cvode_stability.run_example(with_plots=False)
        
    def test_cvode_with_disc(self):
        cvode_with_disc.run_example(with_plots=False)
    
    def test_cvode_with_initial_sensitivity(self):
        cvode_with_initial_sensitivity.run_example(with_plots=False)
    
    def test_cvode_with_jac(self):
        cvode_with_jac.run_example(with_plots=False)
    
    def test_cvode_with_jac_spgmr(self):
        cvode_with_jac_spgmr.run_example(with_plots=False)
        
    def test_ida_with_jac_spgmr(self):
        ida_with_jac_spgmr.run_example(with_plots=False)
    
    def test_cvode_with_parameters(self):
        cvode_with_parameters.run_example(with_plots=False)
    
    def test_cvode_with_parameters_fcn(self):
        cvode_with_parameters_fcn.run_example(with_plots=False)
        
    def test_cvode_with_parameters_modified(self):
        cvode_with_parameters_modified.run_example(with_plots=False)

    def test_euler_basic(self):
        euler_basic.run_example(with_plots=False)
        
    def test_euler_with_disc(self):
        euler_with_disc.run_example(with_plots=False)
        
    def test_rungekutta4_basic(self):
        rungekutta4_basic.run_example(with_plots=False)
        
    def test_rungekutta34_basic(self):
        rungekutta34_basic.run_example(with_plots=False)
        
    def test_rungekutta34_with_disc(self):
        rungekutta34_with_disc.run_example(with_plots=False)
        
    def test_ida_with_disc(self):
        ida_with_disc.run_example(with_plots=False)
    
    def test_ida_with_initial_sensitivity(self):
        ida_with_initial_sensitivity.run_example(with_plots=False)
        
    def test_ida_with_jac(self):
        ida_with_jac.run_example(with_plots=False)
        
    def test_ida_with_parameters(self):
        ida_with_parameters.run_example(with_plots=False)
        
    def test_radau5ode_vanderpol_c(self):
        radau5ode_vanderpol.run_example(with_plots=False)
    
    def test_radau5ode_vanderpol_f(self):
        radau5ode_vanderpol.run_example(with_plots=False)
        
    def test_radau5ode_with_disc_c(self):
        radau5ode_with_disc.run_example(with_plots=False)

    def test_radau5ode_with_disc_f(self):
        radau5ode_with_disc.run_example(with_plots=False)

    def test_radau5ode_with_disc_sparse(self):
        radau5ode_with_disc_sparse.run_example(with_plots=False)

    def test_radau5ode_with_jac_sparse_c(self):
        radau5ode_with_jac_sparse.run_example(with_plots=False)

    def test_radau5dae_vanderpol_f(self):
        radau5dae_vanderpol.run_example(with_plots=False)
        
    def test_dopri5_basic(self):
        dopri5_basic.run_example(with_plots=False)
        
    def test_dopri5_with_disc(self):
        dopri5_with_disc.run_example(with_plots=False)
        
    def test_rodasode_vanderpol(self):
        rodasode_vanderpol.run_example(with_plots=False)
                
    def test_mech_system_pendulum1(self):
        """
        This tests the class Mechanical_system together with ind1 and ida
        """
        mech_system_pendulum.run_example('ind1',with_plots=False,with_test=True)
 
    def test_mech_system_pendulum2(self):
        """
        This tests the class Mechanical_system together with ind2 and ida
        """
        mech_system_pendulum.run_example('ind2',with_plots=False,with_test=True)
        
    @pytest.mark.skipif(get_sundials_version() >= (4,), 
                        reason = "Needs fixing for modern SUNDIALS versions")
    def test_mech_system_pendulum3(self):
        """
        This tests the class Mechanical_system together with ind3 and ida
        """
        mech_system_pendulum.run_example('ind3',with_plots=False,with_test=True)
        
    def test_mech_system_pendulum_ggl2(self):
        """
        This tests the class Mechanical_system together with ggl2 and ida
        """
        mech_system_pendulum.run_example('ggl2',with_plots=False,with_test=True)
    
    def test_mech_system_pendulum_ovstab2(self):
        """
        This tests the class Mechanical_system together with ovstab2 and odassl
        """
        mech_system_pendulum.run_example('ovstab2',with_plots=False,with_test=True)
            
    def test_mech_system_pendulum_ovstab1(self):
        """
        This tests the class Mechanical_system together with ovstab1 and odassl
        """
        mech_system_pendulum.run_example('ovstab1',with_plots=False,with_test=True)
    
    def test_lsodar_vanderpol(self):
        lsodar_vanderpol.run_example(with_plots=False)
        
    def test_lsodar_with_disc(self):
        lsodar_with_disc.run_example(with_plots=False)

    def test_lsodar_bouncing_ball(self):
        lsodar_bouncing_ball.run_example(with_plots=False)
        
    def test_euler_vanderpol(self):
        euler_vanderpol.run_example(with_plots=False)
        
    def test_cvode_basic_backward(self):
        cvode_basic_backward.run_example(with_plots=False)
        
    def test_ida_basic_backward(self):
        ida_basic_backward.run_example(with_plots=False)

    def test_glimda_vanderpol(self):
        glimda_vanderpol.run_example(with_plots=False)

    def test_radar_basic(self):
        radar_basic.run_example()
