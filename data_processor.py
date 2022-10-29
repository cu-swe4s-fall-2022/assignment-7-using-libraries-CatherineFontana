#import libraries
import numpy as np
import time
import pandas as pd

def get_random_matrix(num_rows, num_columns): #N = rows, #M = columns 
    np.array([0,1]) #define the array start + end points
    my_arr = np.array # turn array into a variable
    print(np.random.choice(my_arr, 10, N > 0, M > 0)) #return 10 random values that fall within the array we've defined

def get_file_dimensions(file_name):
    iris_df = pd.read_csv('iris.data', 'r', sep = ',') #sets imported data as a data frame, reads the file, tells comp. that the original file is separated by a comma
    print(iris_df.shape) #prints the number of rows and columns of a data drame 

def write_matrix_to_file(num_rows, num_columns, file_name):
    np.array([0,1]) #define the array start + end points
    my_arr = np.array # turn array into a variable
    print(np.random.choice(my_arr, 10, N > 0, M > 0)) #return 10 random values that fall within the array we've defined
    np.savetxt('np_my_arr_df.csv', my_arr, sep = ',') #save this new array as comma delimiited
    my_arr_df.to_csv('pd_my_arr_df.csv', sep = ',') #write this new data frame to a CSV file
