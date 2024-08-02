import subprocess
import re
import os
import pandas as pd
import numpy as np

with open('YHe1.txt', 'w') as file:
        file.write('omb/lG2 lG YHe yhe' + '\n' + '\n')

#Lis le fichier sBBN:
dat0 = pd.read_csv('external/bbn/sBBN_lambda_G_copy.dat', sep=' ', header=None, skiprows=2).values

for j in range(1,32): #32
  for k in range(1,50): #50
    i=k+j*51

    omega_b = dat0[i,0]
    lambda_G= dat0[i,1]
    Y_He= dat0[i,2]
    omega_b = omega_b*lambda_G**2

    #Reecris le fichier sBBN:
    dat1=np.delete(dat0,i,axis=0)
    dat1=np.insert(dat1,0,dat1[0],axis=0)
    with open('external/bbn/sBBN_lambda_G.dat', 'w') as file:
        file.write('51 33' + '\n' + '\n')
    with open('external/bbn/sBBN_lambda_G.dat', 'a') as file:
        np.savetxt(file, dat1, delimiter=' ', fmt='%.5f')

    #Supprime deux dernieres lignes:
    with open(r"test.ini", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[:-2])

    #Reecris 2 dernieres lignes:
    with open('test.ini', 'a') as file:
        file.write(f'omega_b = {omega_b}\n')
        file.write(f'lambda_G = {lambda_G}\n')

    #Execute CLASS:
    result = subprocess.run(['./class','test.ini'], stdout=subprocess.PIPE, universal_newlines=True)

    #Trouve valeur YHe:
    match = re.search(r'Y_He = ([0-9.]+)', result.stdout)
    y_he = float(match.group(1))

    #Enregistre la valeur:
    with open('YHe1.txt', 'a') as file:
        file.write(f'{omega_b/lambda_G**2:.5} {lambda_G:.2} {Y_He:.4} {y_he:.4}\n')

    print(i)
    #print("Valeur de omega_b:", omega_b/lambda_G**2)
    #print("Valeur de Y_He:", y_he)


with open('external/bbn/sBBN_lambda_G.dat', 'w') as file:
    file.write('51 33' + '\n' + '\n')
with open('external/bbn/sBBN_lambda_G.dat', 'a') as file:
    np.savetxt(file, dat0, delimiter=' ', fmt='%.5f')
