

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import *
import numpy as np
from matplotlib.font_manager import FontProperties

"""==============================================================================================================================================
@ uses: This file is shows the average improvement achived by applying Logim model (ensemble based techniques + threshold) for logging prediction
@We have computed improvement with all the three but have shown the results in paper only for the best classifier
================================================================================================================================================="""


#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""



#========================RQ4 ===========================================================================================#
# Comparision of LogIm Classifies with baseline classifer (catch-BLOCKS)
# @Note:  We have computed improvement with all the three but have shown the results in paper only for the best classifier
#=======================================================================================================================#
#               LF  (j48)                                                                                               #     
#=======================================================================================================================#
plt.close()

logim_impr_in_j48=(5.99, 4.80, 5.09, 6.98, 5.69, 7.38, 4.07, 6.85, 5.45, 1.30)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 15})
ylim(0,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Improvement in J48 (Catch-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_j48, width,color ='#bebebe')


plt.tight_layout()
#plt.show()

plt.savefig(path+"logim-imp-j48-lf-catch.pdf")


#==========================================================================#
#               LF  (RF)                                                      #     
#=========================================================================#
plt.close()
logim_impr_in_rf=(7.86, 6.67, 6.96, 8.85, 7.56, 9.24, 5.93, 8.72, 7.32, 3.17)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(0,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Improvement in RF (Catch-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_rf, width,color ='#bebebe')


plt.tight_layout()
#plt.show()

plt.savefig(path+"logim-imp-rf-lf-catch.pdf")


#==========================================================================#
#               LF  (SVM)                                                      #     
#=========================================================================#
plt.close()

logim_impr_in_svm=(3.17, 1.98, 2.27, 4.16, 2.87, 4.56, 1.25, 4.03, 2.63, -1.52)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(-5,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Techniques")
ax.set_title('Improvement in SVM (Catch-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_svm, width,color ='#bebebe')
ax.plot([0., 9], [0, 0], "k-")

plt.tight_layout()
#plt.show()
plt.savefig(path+"logim-imp-svm-lf-catch.pdf")




#========================RQ1 =============================================#
# Comparsion of classifier on balanced and imbalanced dataset  (IF-BLOCKS)
#==========================================================================#
#               LF  (j48)                                                      #     
#=========================================================================#
plt.close()


logim_impr_in_j48_if=(7.85,0.11,7.62,10.06,7.54, 12.11, 1.28,10.78,8.22,-2.18)


ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(-5,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Improvement in J48 (If-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_j48_if, width,color ='#bebebe')
ax.plot([0., 9], [0, 0], "k-")

plt.tight_layout()
#plt.show()

plt.savefig(path+"logim-imp-j48-lf-if.pdf")


#==========================================================================#
#               LF  (RF)                                                      #     
#=========================================================================#
plt.close()


logim_impr_in_rf_if=(10.69,2.95, 10.46, 12.9, 10.38, 14.95, 4.12, 13.62, 11.06, 0.66)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(0,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Technique")
ax.set_title('Improvement in RF (If-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_rf_if, width,color ='#bebebe')


plt.tight_layout()
#plt.show()

plt.savefig(path+"logim-imp-rf-lf-if.pdf")


#==========================================================================#
#               LF  (SVM)                                                      #     
#=========================================================================#
plt.close()


logim_impr_in_svm_if=(14.87,7.13, 14.64, 17.08, 14.56,19.13, 8.3, 17.8,15.24, 4.84)

ind = np.arange(10)
width = 0.3

fig, ax = plt.subplots()


# add some text for labels, title and axes ticks
plt.rcParams.update({'font.size': 13})
ylim(0,20)
ax.set_ylabel('Improvement in LF (%)')
ax.set_xlabel("Ensemble Techniques")
ax.set_title('Improvement in SVM (If-Blocks)')
ax.set_xticks(ind+width)
ax.set_xticklabels(('LAV', 'LMV', 'LMXV','LST', 'LBAJ', 'LBAR', 'LBAS','LBOJ', 'LBOR', 'LBOS'), rotation = 300)

#==== Command to change font size of legend ===#
fontP = FontProperties()
fontP.set_size('small')
rects1 = ax.bar(ind, logim_impr_in_svm_if, width,color ='#bebebe')
#ax.plot([0., 9], [0, 0], "k-")

plt.tight_layout()
#plt.show()
plt.savefig(path+"logim-imp-svm-lf-if.pdf")




