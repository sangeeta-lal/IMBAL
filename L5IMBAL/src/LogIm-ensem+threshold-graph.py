
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

def draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,classifier, project, type):
        
    print "Draw line graph", classifier

    plt.close()
    ax= plt.subplot()
    ax.plot( x_axis, gain_ratio, 'rs-', label = "GR")
    ax.plot( x_axis, information_gain, 'bo-', label ="IG")    
    ax.plot( x_axis, oner, 'g^-', label = "OR")
    ax.plot( x_axis, relief, 'b*-', label ="RL")    
    ax.plot( x_axis, symmetrical, 'ro-', label = "SM")
    
    
    plt.xlabel("Percentage of Features", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project+"-"+classifier.upper()+" ("+type+"-Block)", fontsize=20)
    plt.axis([ 10, 100, 10, 115],fontsize=30)
    
    
    # Now add the legend with some customizations.
    plt.rcParams.update({'font.size': 15})
    legend = plt.legend(loc='lower right', shadow=False)
    
    
    # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.99')
    
    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('small')
    
    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
    
    type = type.lower()
    
    plt.show()


#==================   line graph for if ======================================#
def draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,classifier, project, type):
        
    print "Draw line graph", classifier

    plt.close()
    ax= plt.subplot()
    ax.plot( x_axis, gain_ratio, 'rs-', label = "GR")
    ax.plot( x_axis, information_gain, 'bo-', label ="IG")    
    ax.plot( x_axis, oner, 'g^-', label = "OR")
    ax.plot( x_axis, relief, 'b*-', label ="RL")    
    ax.plot( x_axis, symmetrical, 'ro-', label = "SM")
    
    
    plt.xlabel("Percentage of Features", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project+"-"+classifier.upper()+" ("+type+"-Block)", fontsize=20)
    plt.axis([ 10, 100, 10, 115],fontsize=30)
    
    
    # Now add the legend with some customizations.
    plt.rcParams.update({'font.size': 15})
    legend = plt.legend(loc='upper right', shadow=False)
    
    
    # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.99')
    
    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('small')
    
    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
    
    type = type.lower()
    
    plt.show()



#==============================================#
# Tomcat #
#==============================================#
#  1. J48
#----------------------------------------------#

gain_ratio=[58.9, 66.33, 71.12, 71.1, 71.43, 71.1, 72, 71.26, 70.97, 71.03]
information_gain=[ 68.02, 69.3, 70.46,71.4,71.66, 71.21, 71.24, 70.87, 71.13, 71.03]
oner=[62.15, 65.11, 64.91, 68.24, 69.45, 69.72, 70.36, 70.66, 71.32, 71.03]
relief=[66.23, 67.26, 68.4, 69.59, 69.69, 69.29, 70.08, 70.1, 71.27, 71.03]
symmetrical=[67.3, 69.38, 70.86, 71.53,71.2,71.15, 71.18, 71.4,71.04,71.03]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Tomcat", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 61.69 ,69.34, 68.98, 69.07, 69.16, 69.1, 68.58, 66.23, 67.43, 68.25]
information_gain=[ 67.82, 69.51, 69.08, 69.18, 68.34, 69.06, 69.08,68.19,69.2, 68.25]
oner=[64.95, 66.74, 67.74, 69.79, 69.96, 69.71, 69.34, 68.87, 70.76, 68.25]
relief=[65.95, 67.11, 67.87, 69.24, 68.64, 69.01, 68.62, 67.95, 68.55, 68.25]
symmetrical=[67.79, 68.51, 68.94, 68.16, 68.39, 68.18, 68.33, 70.25, 68.68, 68.25]
x_axis = [10, 20, 30, 40, 50, 60, 70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Tomcat", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 62.19, 70.4, 73.47, 74.03, 74.6, 75.54, 75.87, 76.05, 75.8, 76.79]
information_gain=[ 68.41, 72.73, 73.63, 74.49, 75.02, 75.55, 75.66, 75.79, 75.8, 76.79] 
oner=[64.37, 66.09, 68.31, 71.76, 74.17, 74.68, 76.03, 75.33,75.99, 76.79]
relief=[ 64.97, 66.72, 70.03, 71.96, 73.33, 74.41, 74.51, 75.54, 75.54, 76.79]
symmetrical=[68.69, 72.6, 73.43, 73.73, 74.63, 75.45, 75.55, 75.88, 75.73, 76.79]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Tomcat", "Catch")

