

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import *
import numpy as np
from matplotlib.font_manager import FontProperties

"""
@ uses: This file is created to create the graph for comparision of balanced and imbalanced dataset
"""


#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""


#========================RQ1 =============================================#
# Comparsion of classifier on balanced and imbalanced dataset  (catch-BLOCKS)
#==========================================================================#
#               LF                                                        #     
#=========================================================================#
plt.close()

#J48=(82.57,73.27)
#RF  = ( 83.34, 71.41)
#SVM = (83.77, 76.09)

BAL = (82.57, 83.34, 83.77)
IMBAL = (73.27, 71.41, 76.09 )

ind = np.arange(3)
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(ind, BAL, width,color ='#000000')
rects2 = ax.bar(ind+width, IMBAL, width, color ='#bebebe')


plt.rcParams.update({'font.size': 18})
# add some text for labels, title and axes ticks
ax.set_ylabel('Average LF (%)')
ax.set_title('Catch-Blocks')
ax.set_xticks(ind + width)
ax.set_xticklabels(('J48', 'RF', 'SVM'))

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
ax.legend((rects1[0], rects2[0] ), ('Balanced', 'Imbalanced' ), prop = fontP)

ylim(0,110)
plt.tight_layout()
#plt.show()

plt.savefig(path+"rq1-lf-catch.pdf")




#========================RQ1 ==============================================#
# Comparsion of classifier on balanced and imbalanced dataset (CATCH -BLOCKS)
#==========================================================================#
#               ACC                                                        #     
#==========================================================================#
plt.close()

#J48=(82.44,85.4)
#RF  = (83.57,86.4)
#SVM = (83.58, 86.7)

BAL = (82.44, 83.57, 83.58)
IMBAL = (85.4,86.4, 86.7)

ind = np.arange(3)
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(ind, BAL, width,color ='#000000')
rects2 = ax.bar(ind+width, IMBAL, width, color ='#bebebe')

plt.rcParams.update({'font.size': 18})
# add some text for labels, title and axes ticks
ax.set_ylabel('Average ACC (%)')
ax.set_title('Catch-Blocks')
ax.set_xticks(ind + width)
ax.set_xticklabels(('J48', 'RF', 'SVM'))

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
ax.legend((rects1[0], rects2[0] ), ('Balanced', 'Imbalanced' ), prop = fontP)

ylim(0,110)
plt.tight_layout()
#plt.show()

plt.savefig(path+"rq1-acc-catch.pdf")



#========================RQ1 =============================================#
# Comparsion of classifier on balanced and imbalanced dataset  (IF-BLOCKS)
#==========================================================================#
#               LF                                                        #     
#=========================================================================#
plt.close()

#J48=(78.65, 50.18)
#RF  = (80.10, 47.34 )
#SVM = (79.87, 43.16)

BAL = (78.65,  80.10, 79.87)
IMBAL = (50.18, 47.34, 43.16 )

ind = np.arange(3)
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(ind, BAL, width,color ='#000000')
rects2 = ax.bar(ind+width, IMBAL, width, color ='#bebebe')


plt.rcParams.update({'font.size': 18})
# add some text for labels, title and axes ticks
ax.set_ylabel('Average LF (%)')
ax.set_title('If-Blocks')
ax.set_xticks(ind + width)
ax.set_xticklabels(('J48', 'RF', 'SVM'))

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
ax.legend((rects1[0], rects2[0] ), ('Balanced', 'Imbalanced' ), prop = fontP)

ylim(0,110)
plt.tight_layout()
#plt.show()

plt.savefig(path+"rq1-lf-if.pdf")




#========================RQ1 ==============================================#
# Comparsion of classifier on balanced and imbalanced dataset (IF -BLOCKS)
#==========================================================================#
#               ACC                                                        #     
#==========================================================================#
plt.close()

#J48=(78.33, 92.32)
#RF  = (80.85, 92.99)
#SVM = (79.49, 92.17)


BAL = (78.33, 80.85, 79.49)
IMBAL = (92.32, 92.99, 92.17)

ind = np.arange(3)
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(ind, BAL, width,color ='#000000')
rects2 = ax.bar(ind+width, IMBAL, width, color ='#bebebe')

plt.rcParams.update({'font.size': 18})
# add some text for labels, title and axes ticks
ax.set_ylabel('Average ACC (%)')
ax.set_title('If-Blocks')
ax.set_xticks(ind + width)
ax.set_xticklabels(('J48', 'RF', 'SVM'))

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
ax.legend((rects1[0], rects2[0] ), ('Balanced', 'Imbalanced' ), prop = fontP)

ylim(0,110)
plt.tight_layout()
#plt.show()

plt.savefig(path+"rq1-acc-if.pdf")


