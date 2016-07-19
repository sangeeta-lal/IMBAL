


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""======================================================================
@ Note 
1.This file is used to create the threshold graph for the catch blocks
2. This graph uses FMEASURE for drawing the graphs
========================================================================"""

#"""
path = "F:\\Research\\L5IMBAL\\result-70-30\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result-70-30\\"
"""

def draw_line_graph(j48,rf, svm, x_axis, project, type):
    print "Draw something"

    plt.close()
    ax= plt.subplot()
    ax.plot( x_axis, j48, 'rs-', label = "J48")
    ax.plot( x_axis, rf, 'bo-', label ="RF")    
    ax.plot( x_axis, svm, 'g^-', label = "SVM")
    
    plt.xlabel("Threshold", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project, fontsize=20)
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
    
    
    plt.savefig(path+project+"-thres-"+type+".pdf")
    #plt.show()


#==============================================#
# Tomcat #
#==============================================#
j48=[71.45, 71.27, 71.27, 71.03, 71.03, 70.97, 70.48,68.72, 60.97]
rf=[66.79, 71.9, 74.39, 72.75, 68.25,60.11, 48.12, 48.12, 33.78]
svm=[75.05, 76.3, 76.99, 77.19, 76.85, 76.43, 75.37, 73.68, 70.43]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Tomcat", "catch")



#==============================================#
# CloudStack                                   #
#==============================================#
j48=[ 84.32, 84.75, 84.68, 84.51, 84.51, 84.51, 84.4, 84.25, 82.04]
rf=[ 80.1,83.63, 85.92, 86.98, 85.98, 81.6, 72.5, 72.5, 57.13]
svm=j48
x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "CloudStack", "catch")


#==============================================#
# Hadoop                                 #
#==============================================#
j48=[ 64.23, 65.09, 64.57, 64.27, 64.27, 64.26, 63.86, 62.99, 55.05]
rf=[ 62.15, 67.48, 69.32, 66.8, 59.99, 49.79, 38.63, 38.63, 26.28]

svm=j48
x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Hadoop", type)


