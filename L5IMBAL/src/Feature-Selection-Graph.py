


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
    plt.savefig(path+project+"-fs-"+classifier+"-"+type+".pdf")
    #plt.show()


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
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "CloudStack", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 69.31, 78.8, 83.08, 83.38, 84.14, 84.93, 85.22, 85.27, 85.48, 85.98]
information_gain=[ 83.79, 84.56, 85.27, 85.12, 85.31, 85.26, 85.08, 85.68, 85.12, 85.98]
oner=[82.33, 82.75, 82.6, 82.54,82.4, 83.78,84.66, 85.39, 85.65, 85.98]
relief=[83.03, 84.04,84.72, 84.74, 85.46, 85.59, 85.27, 84.8, 85.75,85.98]
symmetrical=[83.91, 84.39, 85.33, 85.07, 85.29, 85.07, 85.4, 85.32, 85.79, 85.98]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "CloudStack", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 70.32,74.39, 78.08, 79.46, 81, 82.45, 83.55, 83.88, 84.29,84.32]
information_gain=[ 76.24, 80.4, 81.16, 82.08, 82.19,82.89, 83.28, 83.79, 83.88, 84.32]
oner=[75.98, 76.73, 78.12,78.59, 79.31, 81.25, 82.39, 83.2, 84.17, 84.32]
relief=[  77.56, 79.74, 80.86, 82.39, 83.4, 83.54, 83.33, 83.43, 84.1, 84.32]
symmetrical=[76.32, 80.16, 81.21, 82.17, 82.5, 82.88, 83.37,83.92, 84.05, 84.32]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "CloudStack", "Catch")





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
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Hadoop", "Catch")


#==============================================#
#  2. RF
#----------------------------------------------#
gain_ratio=[ 48.91, 57.92, 63.36, 61.52, 60.79, 61.36, 60.43, 60.93, 60.06, 59.99]
information_gain=[63.11, 62.44, 62.17, 60.66, 61.14, 62.02, 59.46,59.99, 60.42, 59.99]
oner=[50.57, 55.54, 57.76, 59.98, 60.98, 60.97, 61.19, 60.95, 61.29, 59.99]
relief=[60.64,61.21, 61.18, 60.37, 60.56, 60.4, 60.04, 59.55, 59.72, 59.99]
symmetrical=[ 63.32,62.59,61.54, 61.37, 61.75, 62, 61.4, 60.96, 60.9, 59.99]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Hadoop", "Catch")


#==============================================#
#  3. SVM
#----------------------------------------------#
gain_ratio=[ 45.48, 54.06, 61.98, 65.63, 65.74, 66.46, 66.37, 66.64, 67.12, 67.16]
information_gain=[ 59.64, 62.6, 63.95, 65.73, 65.78, 66.41, 66.33, 66.68, 67.2, 67.16]
oner=[46.04, 49.61,53.52, 56.95, 63.09, 64.5, 64.78,66.3, 66.31, 67.16]
relief=[  50.26, 56.72, 59.32, 63.74, 64.28, 64.11, 64.36, 64.32, 66.09, 67.16]
symmetrical=[59.1, 61.84, 63.56, 65.39, 65.93, 66.42, 66.49, 66.63, 67.01, 67.16]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_catch(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Hadoop", "Catch")





#===============IF-Block===========================#
#         Tomcat                                   #
#==================================================#
#  1. J48
#----------------------------------------------#
gain_ratio=[14.65, 30.06, 33.96, 40.86, 44.83, 45.66, 45.52, 45.01, 45.74, 46.28]

information_gain=[  39.6, 41.92, 43.13, 44.26, 45.01, 45.61, 45.36, 45.6, 46.17, 46.28]
oner=[16.58,30.84, 37.05, 42.65, 43.19, 44.61, 45.08, 44.89, 46.02, 46.28]
relief=[33.7, 36.39, 39.92, 42.13,43.59, 44.76, 44.61, 45.9, 45.09, 46.28]
symmetrical=[36.64, 41.18, 42.72, 43.78, 44.55, 45.95, 44.58, 45.42, 45.89, 46.28]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Tomcat", "If")


#=============IF-Block=========================#
#  2. RF
#----------------------------------------------#
gain_ratio=[29.04, 40.37,44.05, 46.39, 44.7, 44.7, 43.43, 43.78, 44.5, 43.42]
information_gain=[ 42.13, 43.89, 43.64, 44.63, 43.93, 42.96, 43.1, 43.34, 43.25, 43.42]
oner=[32.17, 42.27, 44.72, 42.79, 43.85, 44.3, 44.12, 44.28, 44.33, 43.42]
relief=[34.25, 37.92, 40.15, 40.81, 42.15, 43.47, 42.16, 42.77, 43.34, 43.42]
symmetrical=[43.4 , 43.01, 43.84, 44.59,44.84, 43.58, 43.37, 44.2, 43.91, 43.42]
x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Tomcat", "If")


#=============IF-Block=========================#
#  3. SVM
#----------------------------------------------#

gain_ratio=[21.11, 22.08, 22.65, 23.21, 26.28, 30.77, 36.2, 38.9, 41.23, 43.03]
information_gain=[ 14.98, 19.55, 21.58, 22.41, 25.55, 32.57, 36.3, 38.07, 41.04, 43.03]
oner=[18.23, 18.3, 18.48, 18.52, 21.78, 30.43, 34.23, 38.08, 42.4,43.03]
relief=[0.51, 2.2, 5.27, 12.67, 27.19, 30.78, 34.15, 37.7, 41.45, 43.03]
symmetrical=[16.48, 20.79,21.98, 22.92, 26.1, 32.22, 36.37, 38.23, 41.07, 43.03]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Tomcat", "If")



#===============IF-Block===========================#
#         CloudStack                                 #
#==================================================#
#  1. J48
#----------------------------------------------#
gain_ratio=[40.82, 52.5, 56.36,58.01, 61.19, 61.21, 62.39, 63.11, 62.95, 62.79]
information_gain=[ 59.28, 61, 61.74, 62.32, 62.62, 62.52, 63.04,63.5, 63.07, 62.79]
oner=[43.58, 54.37, 57.79, 61.45, 62.56, 63.13, 63.45, 63.1,62.72, 62.79]
relief=[56.45, 59.04, 60.34, 61.21, 62.57, 62.53, 62.62, 62.75, 62.65, 62.79]
symmetrical=[ 57.82, 60.89, 61.48, 61.9, 62.42, 62.69, 62.89, 63.43, 63.54, 62.79]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "CloudStack", "If")


#=============IF-Block=========================#
#  2. RF
#----------------------------------------------#

gain_ratio=[46.19, 56.98, 60.26, 61.23, 62.54, 62.41, 61.65, 61.12, 61.46, 61.29]
information_gain=[ 60.82, 61.13, 60.73, 60.7, 60.94, 60.59, 61.28, 61.32, 61.62, 61.29]
oner=[49.78, 58.97,60.36, 61.23, 62.07, 62.09, 61.45, 61.71, 61.63, 61.29]
relief=[57.9, 59.25, 60.26, 59.93,60.98,61.23,61.08,61.25, 61.02, 61.29]
symmetrical=[62.56, 61.44, 61.73, 60.6, 60.81, 60.83, 60.76, 61.48, 61.34, 61.29]

x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "CloudStack", "If")


#=============IF-Block=========================#
#  3. SVM
#----------------------------------------------#

gain_ratio=[31.08, 31.68, 32.17, 39.79, 47.55, 50, 52.74, 54.71, 56.12, 56.68]
information_gain=[ 25.18, 38.52, 45.59, 47.94, 51.15, 52.32, 53.92,55.01,55.89, 56.68]
oner=[29.23, 29, 30.21, 47.51, 50.69,52.69,53.79, 54.65, 54.99, 56.68]
relief=[18.63, 38.53, 45.95, 49.14, 51.35, 52.58, 53.61, 55, 56.16, 56.68]
symmetrical=[20.76, 37.43, 44.49, 47.93, 50.51,52.36, 53.45, 55.07, 55.83, 56.68]



x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "CloudStack", "If")


#===============IF-Block===========================#
#         Hadoop                                #
#==================================================#
#  1. J48
#----------------------------------------------#

gain_ratio=[19.32, 25.93, 31.47, 36.81, 39.7, 40.77, 40.54, 41.37, 41.25, 41.28]
information_gain=[ 34.13, 36.58, 38.31, 38.84, 40.9, 39.63, 40.75, 40.77, 40.99, 41.48]
oner=[20.4, 30.36, 33.49, 38.89, 39.48, 40.68, 40.7,41.02, 40.66, 41.48]
relief=[30.82,36.03, 36.65, 38.24, 39.87, 40.81, 41.21, 41.03, 40.6, 41.48]
symmetrical=[31.82, 35.73, 36.55, 38.13, 40.06, 40.36, 40.88, 41.5, 41.04,41.48]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"j48", "Hadoop", "If")



#=============IF-Block=========================#
#  2. RF
#----------------------------------------------#

gain_ratio=[29.6, 35.89,39.87, 37.21, 37.22, 36.75,36.78, 36.97, 37.07, 37.32]
information_gain=[ 34.15, 36.16,37.17, 36.94, 36.68, 37.52, 37.62, 37.1, 36.61, 37.32]
oner=[31.43, 37.63, 39.23, 35.8, 37.12, 37.02, 36.9, 36.71, 36.84, 37.32]
relief=[31.89, 34.96, 36.25, 35.92, 35.47, 36.47, 36.51, 36.04, 37.72, 37.32]
symmetrical=[33.03, 35.9, 36.51, 37.04, 37.17, 36.85, 36.96, 36.84, 37.44, 37.32]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"rf", "Hadoop", "If")

#=============IF-Block=========================#
#  3. SVM
#----------------------------------------------#

gain_ratio=[10.95, 11.5, 11.71,11.74, 11.9, 13.89, 19.06, 23.98, 27.38, 29.78]
information_gain=[ 6.96, 9.98, 11.08, 11.58, 11.79, 13.42, 18.89, 23.65, 27.37, 29.78]
oner=[8.57,8.69, 8.69, 8.57, 8.61, 9.14, 10.13, 18.18, 24.22, 29.78]
relief=[0, 0, 0, 0, 0.06, 6.52, 13.14,21.14, 26, 29.78]
symmetrical=[7.87, 10.56, 11.31, 11.79, 11.71, 13.24, 19.2, 23.68, 27.62, 29.78]


x_axis = [10,20,30, 40,50,60,70,80,90,100]
draw_line_graph_if(gain_ratio, information_gain, oner, relief, symmetrical, x_axis,"svm", "Hadoop", "If")
