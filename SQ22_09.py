"""
SQ22-09
=======
MC IATRIDES
ID 82123707
"""

from numpy import *
from matplotlib.pyplot import *
from pandas import *
from pandas.plotting import parallel_coordinates, scatter_matrix

"""Scatter Plot Matrix"""

rcParams["figure.autolayout"] = True
iris = read_csv('./drive/MyDrive/Data_SQ/bezdekIris.data', sep=",")

colors = array(50*['r']+50*['g']+50*['b'])
scatter_matrix(iris,c=colors,figsize=(7,7))
show()

"""PCP plot"""

iris = read_csv('./drive/MyDrive/Data_SQ/iris.data', sep=",", header=None, names= ["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"])

figure(figsize=(17,12))
parallel_coordinates(iris, 'Species', color=("blue", "red", "green"))
show()
