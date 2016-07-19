


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
path
"""

def draw_line_graph(j48,rf, svm, x_axis, project):
    print "Draw something"

    plt.clear()
    plt.plot( x_axis, j48, 'rs-', label = "J48")
    plt.plot( x_axis, rf, 'bo-', label ="RF")    
    plt.plot( x_axis, svm, 'g^-', label = "SVM")
    
    plt.xlabel("Threshold", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project, fontsize=20)
    plt.axis([ 0.1, 0.9, 10, 110],fontsize=30)
    
    
    # Now add the legend with some customizations.
    plt.rcParams.update({'font.size': 15})
    legend = plt.legend(loc='upper right', shadow=True)

    # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.99')
    
    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('medium')
    
    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
    
    
    plt.savefig(path+project+"-thres.pdf")
    #plt.show()


#==============================================#
# Tomcat #
#==============================================#
j48=[71.45, 71.27, 71.27, 71.03, 71.03, 70.97, 70.48,68.72, 60.97]
rf=[66.79, 71.9, 74.39, 72.75, 68.25,60.11, 48.12, 48.12, 33.78]
svm=[76.79, 76.79, 76.79, 76.79, 76.79, 76.79, 76.79, 76.79, 76.79]
x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Tomcat")



#==============================================#
# CloudStack                                   #
#==============================================#
j48=[]
rf=[]
svm=[]
x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph(j48, rf, svm, x_axis, "Tomcat")
