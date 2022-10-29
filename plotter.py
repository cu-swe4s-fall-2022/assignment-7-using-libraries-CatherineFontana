#import libraries
import matplotlib.pyplot as plt
import pandas as pd

#generate code for three figures: BOX PLOT iris_boxplot.png, SCATTER petal_length_v_width_scatter.png, and MULTIPANEL multi_panel_figure.png.

#First, load in data from data file. Set header names.

iris = pd.read_csv('iris.data', header=None) #data does not have headers so we will import them in step below
iris.columns = ['sepal_width', 'sepal_length','petal_width', 'petal_length', 'species'] #accessing columns and renaming them
print(iris) #returns data in 5 columns w/designated headers

#BOX PLOT. 1 box plot for data in each column (cols #0-3).

measurement_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'] #plotting all columns for plotting
plt.boxplot(iris[measurement_names], labels = measurement_names)
plt.ylabel('cm') #To add a Y-axis label
plt.show() #this makes the plot show up 

#SCATTER PLOT. Plotting petal length vs. petal width in scatter plot for 3 iris species.

iris['species'].unique()  
for species_name in set(iris['species']): #Look for new variable species name in the column "species". "Set" does not allow for duplication, so it will limit data to by species.
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['petal_length'], iris_subset['petal_width'], label = species_name, s = 5) #note that "label" is singular, not plural ("labels") like in histogram. "s" is the size of the dot. 
plt.legend() #makes sure we can see what the colors represent
plt.ylabel('petal_width, cm')
plt.xlabel('petal_length, cm')
plt.title('Petal Length vs. Petal Width of 3 Species of Iris')
plt.show()

#HISTOGRAM. Plotting a histogram of the petal length data points originally plotted in box plot.

plt.hist(iris['petal_length'], bins = 20) #making a histogram of the data in column petal length, separates data into 20 bins/sections
plt.ylabel('count') #y-axis labeled
plt.xlabel('petal_length') #x-axis labeled
plt.title('Histogram of Iris Petal Lengths') #adding a title to the graph
plt.show() 

#MULTIPANEL PLOT. Combining previously made plots into a new multi-panel plot that is 1 row x 2 columns. Left graph = histogram; right graph = scatter plot.

fig, axes = plt.subplots(1,2) #rows, columns = defines how many rows and columns we want in multi-plot
fig.set_size_inches(10,5)
print(axes.shape) #prints out 1 x 2 grid that we've defined above

#Puts the histogram on the left side
axes[0].hist(iris['sepal_length'],bins=20)
axes[0].set_ylabel('count')
axes[0].set_xlabel('sepal_length')
plt.show() 

#Puts the scatter plot on the right side
for species_name in set(iris['species']): #Look for new variable species name in the column "species". "Set" does not allow for duplication, so it will limit data to by species.
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['petal_length'], iris_subset['petal_width'], label = species_name, s = 5) #switch out .plt for axes.
axes[1].legend() #makes sure we can see what the colors represent
axes[1].set_ylabel('petal_width')
axes[1].set_xlabel('petal_length')
plt.show()

#for each row (i)
for i in range(1):
    #for each column (j)
    for j in range(2):
        # choose to hide of show certain borders or "spines"
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        axes[i].spines['bottom'].set_visible(True)
        axes[i].spines['left'].set_visible(True)
        
plt.savefig('my_beautiful_plot.png')
plt.show()