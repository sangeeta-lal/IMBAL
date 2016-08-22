


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""======================================================================
@ Note 
1.This file is used to create the threshold graph for the catch blocks
2. This graph uses FMEASURE for drawing the graphs
========================================================================"""

#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""


def draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,classifier, project, type):
        
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
    plt.savefig(path+project+"-fs-"+classifier+"-"+type+".pdf")
    #plt.show()


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
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Tomcat", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 61.69 ,69.34, 68.98, 69.07, 69.16, 69.1, 68.58, 66.23, 67.43, 68.25]
information_gain=[ 67.82, 69.51, 69.08, 69.18, 68.34, 69.06, 69.08,68.19,69.2, 68.25]
oner=[64.95, 66.74, 67.74, 69.79, 69.96, 69.71, 69.34, 68.87, 70.76, 68.25]
relief=[65.95, 67.11, 67.87, 69.24, 68.64, 69.01, 68.62, 67.95, 68.55, 68.25]
symmetrical=[67.79, 68.51, 68.94, 68.16, 68.39, 68.18, 68.33, 70.25, 68.68, 68.25]
x_axis = [10, 20, 30, 40, 50, 60, 70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Tomcat", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 62.19, 70.4, 73.47, 74.03, 74.6, 75.54, 75.87, 76.05, 75.8, 76.79]
information_gain=[ 68.41, 72.73, 73.63, 74.49, 75.02, 75.55, 75.66, 75.79, 75.8, 76.79] 
oner=[64.37, 66.09, 68.31, 71.76, 74.17, 74.68, 76.03, 75.33,75.99, 76.79]
relief=[ 64.97, 66.72, 70.03, 71.96, 73.33, 74.41, 74.51, 75.54, 75.54, 76.79]
symmetrical=[68.69, 72.6, 73.43, 73.73, 74.63, 75.45, 75.55, 75.88, 75.73, 76.79]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Tomcat", "Catch")




#==============================================#
# CloudStack            #
#==============================================#
#  1. J48
#----------------------------------------------#

gain_ratio=[69.32, 76.21, 79.46, 79.52, 81.34, 82.47,84.57, 84.09, 84.59, 84.51]
information_gain=[ 81, 82.01, 83.9, 83.14, 83.31, 83.57, 84.54, 84.09, 84.31, 84.51]
oner=[ 78.87, 78.67, 79.46, 79.57, 79.28, 81.34, 82.63, 83.81, 84.65, 84.51]
relief=[ 81.4, 82.32, 83.07, 83.27, 83.12, 83.6,83.28, 82.95, 83.71, 84.51]
symmetrical=[ 80.7, 81.85, 83.46, 83.4, 83.27, 83.67, 84.36, 83.68,84.29,84.51]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "CloudStack", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 69.31, 78.8, 83.08, 83.38, 84.14, 84.93, 85.22, 85.27, 85.48, 85.98]
information_gain=[ 83.79, 84.56, 85.27, 85.12, 85.31, 85.26, 85.08, 85.68, 85.12, 85.98]
oner=[82.33, 82.75, 82.6, 82.54,82.4, 83.78,84.66, 85.39, 85.65, 85.98]
relief=[83.03, 84.04,84.72, 84.74, 85.46, 85.59, 85.27, 84.8, 85.75,85.98]
symmetrical=[83.91, 84.39, 85.33, 85.07, 85.29, 85.07, 85.4, 85.32, 85.79, 85.98]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "CloudStack", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 70.32,74.39, 78.08, 79.46, 81, 82.45, 83.55, 83.88, 84.29,84.32]
information_gain=[ 76.24, 80.4, 81.16, 82.08, 82.19,82.89, 83.28, 83.79, 83.88, 84.32]
oner=[75.98, 76.73, 78.12,78.59, 79.31, 81.25, 82.39, 83.2, 84.17, 84.32]
relief=[  77.56, 79.74, 80.86, 82.39, 83.4, 83.54, 83.33, 83.43, 84.1, 84.32]
symmetrical=[76.32, 80.16, 81.21, 82.17, 82.5, 82.88, 83.37,83.92, 84.05, 84.32]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "CloudStack", "Catch")





#==============================================#
# Hadoop          #
#==============================================#
#  1. J48
#----------------------------------------------#

gain_ratio=[ 47.92, 55.81, 61.92, 64.69, 65, 64.81, 64.19, 64.32, 64.68, 64.27]
information_gain=[ 62.99, 63.91, 63.63, 64.09, 64.65, 64.55, 64.28, 64.42, 64.4, 64.27]
oner=[ 48.26, 52.75, 56.41, 59.3, 62.78, 62.96, 64.23, 64.44, 65.22, 64.27]
relief=[ 61.99, 62.43, 62.62, 63.78, 64.51, 64.22, 64.29, 63.9, 63.51, 64.27]
symmetrical=[ 62.79, 64.06, 64.1, 64.56, 64.78, 64.49, 64.05, 64.33, 64.46, 64.27]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Hadoop", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 48.91, 57.92, 63.36, 61.52, 60.79, 61.36, 60.43, 60.93, 60.06, 59.99]
information_gain=[63.11, 62.44, 62.17, 60.66, 61.14, 62.02, 59.46,59.99, 60.42, 59.99]
oner=[50.57, 55.54, 57.76, 59.98, 60.98, 60.97, 61.19, 60.95, 61.29, 59.99]
relief=[60.64,61.21, 61.18, 60.37, 60.56, 60.4, 60.04, 59.55, 59.72, 59.99]
symmetrical=[ 63.32,62.59,61.54, 61.37, 61.75, 62, 61.4, 60.96, 60.9, 59.99]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Hadoop", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 45.48, 54.06, 61.98, 65.63, 65.74, 66.46, 66.37, 66.64, 67.12, 67.16]
information_gain=[ 59.64, 62.6, 63.95, 65.73, 65.78, 66.41, 66.33, 66.68, 67.2, 67.16]
oner=[46.04, 49.61,53.52, 56.95, 63.09, 64.5, 64.78,66.3, 66.31, 67.16]
relief=[  50.26, 56.72, 59.32, 63.74, 64.28, 64.11, 64.36, 64.32, 66.09, 67.16]
symmetrical=[59.1, 61.84, 63.56, 65.39, 65.93, 66.42, 66.49, 66.63, 67.01, 67.16]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Hadoop", "Catch")

