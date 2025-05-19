#---- visualization line graph----

# importing matplotlibpyplot 
import matplotlib.pyplot as plt
# importing numpy
import numpy as np
# creating student array
students = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# creating avarage mark of students array
avgmarks = np.array([50, 60, 70, 11, 22, 54, 49, 51]) 
# visualising as a bar plot
plt.bar(students,avgmarks)