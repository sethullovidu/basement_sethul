#---- visualization line graph----

# importing matplotlibpyplot 
import matplotlib.pyplot as plt
# importing numpy
import numpy as np
# creating student array
students = np.array(['sethul', 'nimal', 'kamal', 'ravidu', 'saman', 'kapila', 'janaka'])
# creating avarage mark of students array
avgmarks = np.array([50, 60, 70, 11, 22, 54, 49])
# visualising as a bar plot
plt.bar(students, avgmarks)
# displaying output
plt.show()

#---- visualization scatter graph----
