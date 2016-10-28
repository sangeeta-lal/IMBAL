
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import *
import numpy as np
from matplotlib.font_manager import FontProperties

"""==============================================================================================================================================
@ uses: This file is shows the average improvement achived by applying Logim model (ensemble based techniques + threshold) for logging prediction
================================================================================================================================================="""


#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""

#=====================================================================================#
# LogIm: Performance of all the algorithm  (If-blocks)                             #
#=====================================================================================#
logim_tomcat = (78.6, 77.38, 77.51, 79.15, 77.35, 79.14, 77.94, 78.73, 76.32, 74.76)
logim_cloudstack=(87.86, 87.9, 87.12, 88.67, 87.82, 88.83, 85.41, 88.68, 89.42, 83.29)
logim_hadoop=(71.33, 68.94, 70.46, 72.94, 71.72, 73.97, 68.67, 72.96, 70.43, 65.67)

tom_quartile=list()
cloud_quartile=list()
hadoop_quartile = list()

q1_tom= np.percentile(logim_tomcat, 25)
med_tom = np.median(logim_tomcat)
q3_tom = np.percentile(logim_tomcat, 75)
tom_quartile.append(q1_tom)
tom_quartile.append(med_tom)
tom_quartile.append(q3_tom)


q1_cloud= np.percentile(logim_cloudstack, 25)
med_cloud = np.median(logim_cloudstack)
q3_cloud = np.percentile(logim_cloudstack, 75)
cloud_quartile.append(q1_cloud)
cloud_quartile.append(med_cloud)
cloud_quartile.append(q3_cloud)


q1_hadoop= np.percentile(logim_hadoop, 25)
med_hadoop = np.median(logim_hadoop)
q3_hadoop = np.percentile(logim_hadoop, 75)
hadoop_quartile.append(q1_hadoop)
hadoop_quartile.append(med_hadoop)
hadoop_quartile.append(q3_hadoop)

data = [logim_tomcat, logim_cloudstack, logim_hadoop]
quartile_val  = [tom_quartile, cloud_quartile, hadoop_quartile]

#def plot_var(y_lim_upper, title, y_axis_label, quartile_val):

plt.figure()
box= plt.boxplot(data,0, 'bD', patch_artist=True, widths=0.35)
colors = ['#bebebe', '#bebebe', '#bebebe']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker in box['whiskers']:
    whisker.set(color='black', linewidth=1)
for cap in box['caps']:
    cap.set(color='black', linewidth=1)
for median in box['medians']:
    median.set(color='black', linewidth=1)

## change the style of fliers and their fill
colors = ['#bebebe', '#bebebe', '#bebebe']
for flier, color1 in zip(box['fliers'], colors):
    flier.set(marker='o', color=color1, alpha=0.5)
    

for line, temp_quartile in zip(box['medians'], quartile_val):
    # get position data for median line
    print "1=" ,line
    x,y = line.get_xydata()[1] # top of median line
    med=temp_quartile[1]  
    
    # overlay median value
    print "y=", y
    plt.rcParams.update({'font.size': 13})
   
    text(x+0.18, y, 'M=%.1f' % med,
         horizontalalignment='center') # draw above, centered
   
#print box.keys()    
for line in box['boxes']:
    print line


ylim(35,90) 
plt.rcParams.update({'font.size': 18})
ax = axes()
ax.set_xticklabels(['Tomcat', 'CloudStack', 'Hadoop'])
plt.suptitle("Performance of LogIm Models (Catch-Blocks)")
plt.ylabel("LF (%)")
#plt.show()
plt.savefig(path+"logim-imp-box-lf-catch.pdf")




#=====================================================================================#
# LogIm: Performance of all the algorithm  (IF-blocks)                             #
#=====================================================================================#
logim_tomcat_if = (55.18, 47.32, 54.88, 57.55, 54.18, 59.65, 50.33, 59.31, 56.81, 47.27)
logim_cloudstack_if=(68.38, 64.18, 68.21, 70.72, 68.57, 71.97, 61.71, 71.38, 69.53, 57.65)
logim_hadoop_if=(50.53, 39.39, 50.31, 52.11, 50.41, 55.25, 42.91, 51, 48.88, 38.44)


tom_quartile=list()
cloud_quartile=list()
hadoop_quartile = list()

q1_tom= np.percentile(logim_tomcat_if, 25)
med_tom = np.median(logim_tomcat_if)
q3_tom = np.percentile(logim_tomcat_if, 75)
tom_quartile.append(q1_tom)
tom_quartile.append(med_tom)
tom_quartile.append(q3_tom)


q1_cloud= np.percentile(logim_cloudstack_if, 25)
med_cloud = np.median(logim_cloudstack_if)
q3_cloud = np.percentile(logim_cloudstack_if, 75)
cloud_quartile.append(q1_cloud)
cloud_quartile.append(med_cloud)
cloud_quartile.append(q3_cloud)


q1_hadoop= np.percentile(logim_hadoop_if, 25)
med_hadoop = np.median(logim_hadoop_if)
q3_hadoop = np.percentile(logim_hadoop_if, 75)
hadoop_quartile.append(q1_hadoop)
hadoop_quartile.append(med_hadoop)
hadoop_quartile.append(q3_hadoop)

data = [logim_tomcat_if, logim_cloudstack_if, logim_hadoop_if]
quartile_val  = [tom_quartile, cloud_quartile, hadoop_quartile]

#def plot_var(y_lim_upper, title, y_axis_label, quartile_val):

plt.figure()
box= plt.boxplot(data,0, 'bD', patch_artist=True, widths=0.35)
colors = ['#bebebe', '#bebebe', '#bebebe']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker in box['whiskers']:
    whisker.set(color='black', linewidth=1)
for cap in box['caps']:
    cap.set(color='black', linewidth=1)
for median in box['medians']:
    median.set(color='black', linewidth=1)

## change the style of fliers and their fill
colors = ['#bebebe', '#bebebe', '#bebebe']
for flier, color1 in zip(box['fliers'], colors):
    flier.set(marker='o', color=color1, alpha=0.5)
    

for line, temp_quartile in zip(box['medians'], quartile_val):
    # get position data for median line
    print "1=" ,line
    x,y = line.get_xydata()[1] # top of median line
    med=temp_quartile[1]  
    
    # overlay median value
    print "y=", y
    plt.rcParams.update({'font.size': 13})
   
    text(x+0.18, y, 'M=%.1f' % med,
         horizontalalignment='center') # draw above, centered
   
#print box.keys()    
for line in box['boxes']:
    print line


ylim(35,90) 
plt.rcParams.update({'font.size': 18})
ax = axes()
ax.set_xticklabels(['Tomcat', 'CloudStack', 'Hadoop'])
plt.suptitle("Performance of LogIm Models (If-Blocks)")
plt.ylabel("LF (%)")
#plt.show()
plt.savefig(path+"logim-imp-box-lf-if.pdf")