


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

def draw_line_graph(j48,rf, svm, x_axis, project, type):
    print "Draw line graph"

    plt.close()
    ax= plt.subplot()
    ax.plot( x_axis, j48, 'rs-', label = "J48")
    ax.plot( x_axis, rf, 'bo-', label ="RF")    
    ax.plot( x_axis, svm, 'g^-', label = "SVM")
    
    plt.xlabel("Threshold", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project+" ("+type+"-Block)", fontsize=20)
    plt.axis([ 0.1, 0.9, 10, 115],fontsize=30)
    
    
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
    
    
    type =  type.lower()
    plt.savefig(path+project+"-thres-"+type+".pdf")
    #plt.show()


#==============================================#
# Tomcat #
#==============================================#
j48=[71.45, 71.27, 71.27, 71.03, 71.03, 70.97, 70.48,68.72, 60.97]
rf=[66.79, 71.9, 74.39, 72.75, 68.25,60.11, 48.12, 48.12, 33.78]
svm=[75.05, 76.3, 76.99, 77.19, 76.85, 76.43, 75.37, 73.68, 70.43]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Tomcat", "Catch")



#==============================================#
# CloudStack                                   #
#==============================================#
j48=[ 84.32, 84.75, 84.68, 84.51, 84.51, 84.51, 84.4, 84.25, 82.04]
rf=[ 80.1,83.63, 85.92, 86.98, 85.98, 81.6, 72.5, 72.5, 57.13]
svm=[83.95, 84.97, 85.08, 84.8, 84.14, 83.35, 82.24, 80.24, 76.55]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "CloudStack", "Catch")


#==============================================#
# Hadoop                                 #
#==============================================#
j48=[ 64.23, 65.09, 64.57, 64.27, 64.27, 64.26, 63.86, 62.99, 55.05]
rf=[ 62.15, 67.48, 69.32, 66.8, 59.99, 49.79, 38.63, 38.63, 26.28]
svm=[63.99, 66.98, 67.9, 67.79, 67.33, 66.01, 64.04, 60.67, 52.7]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Hadoop", "Catch")



#====== IF - Blocks ========================================#
#   Tomcat  -if                                             #
#===========================================================#
j48 = [46.34, 47.09, 46.83, 46.28, 46.28, 46.28, 45.57, 43.61, 38.48 ]
rf= [49.78, 55.83, 55.36, 51.11, 43.42, 34.99, 26.89, 26.89, 17.1]
svm=[40.45 ,46.75, 47.71, 46.91,45.66,43.13, 40.26, 35.95,27.96]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Tomcat", "If")



#====== IF - Blocks ========================================#
#   CloudStack-if                                            #
#===========================================================#
j48 = [61.59, 63.38, 63.13, 62.79, 62.79, 62.77,62.28, 61.25,55.52]
rf= [61.78, 67.56, 68.68, 66.47, 61.29,53.58,44.18, 44.18, 32.47]
svm=[53.51, 60.29, 61.15, 59.68, 57.13, 53.98, 48.9, 41.44, 26.2]


x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "CloudStack", "If")


#====== IF - Blocks ========================================#
#   Hadoop-if                                               #
#===========================================================#
j48=[42.39, 42.4, 41.82, 41.48,41.48,41.47,40.35,38.77,33.11]
rf=[45.32, 50.96, 50.05, 44.7, 37.32, 29.67, 21.31, 21.31, 13.43]
svm=[35.78, 41.8, 40.97, 37.96, 34.65, 31.35, 27.17, 22.43, 15.36]


x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Hadoop", "If")

