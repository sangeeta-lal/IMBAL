

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import *
import numpy as np
from matplotlib.font_manager import FontProperties

"""==================================================================================================================
@ uses: This file is shows the average improvement achived by applying ensemble based techniques for logging prediction
======================================================================================================================"""


#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""


#========================RQ1 =============================================#
# Comparsion of classifier on balanced and imbalanced dataset  (catch-BLOCKS)
#==========================================================================#
#               LF  (j48)                                                      #     
#=========================================================================#
plt.close()

ensemble_impr_in_j48=(4.46, 4.41, 0.96, 5.42, 3.71, 1.48, 3.08, 6.39, 4.84, 0.71)


ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(0,20)
ax.set_ylabel('Average LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Catch-Blocks')
ax.set_xticks(ind+width)
ax.set_xticklabels(('AV', 'MV', 'MxV','ST', 'BA(J48)', 'BA(RF)', 'BA(SVM)','BO(J48)', 'BO(RF)', 'BO(SVM)'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, ensemble_impr_in_j48, width,color ='#bebebe')


plt.tight_layout()
#plt.show()

plt.savefig(path+"rq4-imp-j48-lf-catch.pdf")


#==========================================================================#
#               LF  (RF)                                                      #     
#=========================================================================#
plt.close()
ensemble_impr_in_rf=(6.32, 6.27, 2.82, 7.28, 5.57, 3.34, 4.94, 8.25, 6.70, 2.57)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(0,20)
ax.set_ylabel('Average LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Catch-Blocks')
ax.set_xticks(ind+width)
ax.set_xticklabels(('AV', 'MV', 'MxV','ST', 'BA(J48)', 'BA(RF)', 'BA(SVM)','BO(J48)', 'BO(RF)', 'BO(SVM)'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, ensemble_impr_in_rf, width,color ='#bebebe')


plt.tight_layout()
#plt.show()

plt.savefig(path+"rq4-imp-rf-lf-catch.pdf")


#==========================================================================#
#               LF  (SVM)                                                      #     
#=========================================================================#
plt.close()

ensemble_impr_in_svm=(1.64, 1.59, -1.86, 2.60, 0.89, -1.34, 0.26, 3.57, 2.02, -2.11)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(-5,20)
ax.set_ylabel('Average LF (%)')
ax.set_xlabel("Ensemble Techniques")
ax.set_title('Catch-Blocks')
ax.set_xticks(ind+width)
ax.set_xticklabels(('AV', 'MV', 'MxV','ST', 'BA(J48)', 'BA(RF)', 'BA(SVM)','BO(J48)', 'BO(RF)', 'BO(SVM)'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, ensemble_impr_in_svm, width,color ='#bebebe')
ax.plot([0., 9], [0, 0], "k-")

plt.tight_layout()
#plt.show()
plt.savefig(path+"rq4-imp-svm-lf-catch.pdf")



