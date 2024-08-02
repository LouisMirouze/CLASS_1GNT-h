#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import necessary modules
# uncomment to get plots displayed in notebook
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from classy_1GNT import Class as Class_1GNT
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import math


# In[ ]:


# esthetic definitions for the plots
font = {'size'   : 16, 'family':'STIXGeneral'}
axislabelfontsize='large'
matplotlib.rc('font', **font)
matplotlib.mathtext.rcParams['legend.fontsize']='medium'
plt.rcParams["figure.figsize"] = [8.0,6.0]


# In[ ]:


lambdacdm_PR3 = {'output' : 'tCl',
                   'h':0.6724,
                   'omega_b':0.02234,
                   'omega_cdm':0.1202,
                   'A_s':2.099e-09,
                   'n_s':0.964,
                   'tau_reio':0.0543,
                   'thermodynamics_verbose':1
                   }

GNT_PR3 = {'output' : 'tCl',
                   'lambda_G':1.,
                   'h':0.669,
                   'omega_b':0.02210,
                   'omega_cdm':0.1192,
                   'A_s':2.095e-09,
                   'n_s':0.9626,
                   'tau_reio':0.0537,
                   'thermodynamics_verbose':1
                   }

##############
#
# call CLASS
#
###############
M1 = Class()
M1.set(lambdacdm_PR3)
M1.compute()
#derived = M.get_current_derived_parameters(['tau_rec','conformal_age'])
thermo1 = M1.get_thermodynamics()
print (thermo1.keys())
#print(dir(Class()))

M2 = Class_1GNT()
M2.set(GNT_PR3)
M2.compute()
thermo2 = M2.get_thermodynamics()

#tau = thermo['conf. time [Mpc]']
z1 = thermo1['z']
x_e1 = thermo1['x_e']
#g = thermo['g [Mpc^-1]']

z2 = thermo2['z']
x_e2 = thermo2['x_e']

# to make the reionisation peak visible, rescale g by 100 for late times
#g[:500] *= 100

#################
#
# start plotting
#
#################

#plt.xlim([1.e2,derived['conformal_age']])
#plt.xlim([1700,500])
plt.xlim([7500,10])

#plt.xlabel(r'$\tau \,\,\, \mathrm{[Mpc]}$')
plt.xlabel('z')

#plt.ylabel(r'$\mathrm{visibility} \,\,\, g \,\,\, [\mathrm{Mpc}^{-1}]$')
plt.ylabel(r'$X_e$')

#plt.axvline(x=derived['tau_rec'],color='k')
# The conformal time at reionisation  could be extracted from the code.
# But we know it because it is part of the standard output
# when thermodynamics_verbose=1
#plt.axvline(x=4255.316282,color='k')
#
# Print functions one by one, saving between each (for slides)
#
plt.plot(z1,x_e1,'r',label='LambdaCDM_PR3')
plt.plot(z2,x_e2,'r',label='1GNT_PR3')
plt.legend()

# In[ ]:


plt.savefig('xe_comparaison_1GNT_PR3.pdf',bbox_inches='tight')
