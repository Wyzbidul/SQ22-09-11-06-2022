#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 11-06-2022
#	TITLE : SQ22-09 - (11-06-2022)
#   SUBTITLE : Iris Dataset Visualization
#	REDACTED FOR : ADV COURSE ON COMPUTER VISUALIZATION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
from numpy import *
from matplotlib.pyplot import *
from pandas import *
from pandas.plotting import parallel_coordinates, scatter_matrix
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

#Data Download
iris = read_csv('./iris.data', sep=",", header=None, names= ["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"])

#Scatter Plot Matrix
colors = array(50*['r']+50*['g']+50*['b'])
scatter_matrix(iris,c=colors,figsize=(7,7))
show()

#PCP plot
figure(figsize=(17,12))
parallel_coordinates(iris, 'Species', color=("blue", "red", "green"))
show()

print('END TESTS')
#####################################################################################################################################