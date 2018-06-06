#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# Knihovny Numpy a matplotlib
#
# - Lorenzův atraktor

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# funkce pro výpočet dalšího bodu Lorenzova atraktoru
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# krok (změna času)
dt = 0.01

# celkový počet vypočtených bodů na Lorenzově atraktoru
n = 10000

# prozatím prázdné pole připravené pro výpočet
x = np.zeros((n,))
y = np.zeros((n,))
z = np.zeros((n,))

# počáteční hodnoty
x[0], y[0], z[0] = (0., 1., 1.05)

# vlastní výpočet atraktoru
for i in range(n-1):
    x_dot, y_dot, z_dot = lorenz(x[i], y[i], z[i])
    x[i+1] = x[i] + x_dot * dt
    y[i+1] = y[i] + y_dot * dt
    z[i+1] = z[i] + z_dot * dt

fig = plt.figure()
ax = fig.gca(projection='3d')

# vykreslení grafu
ax.plot(x, y, z)

# zobrazení grafu
plt.show()

