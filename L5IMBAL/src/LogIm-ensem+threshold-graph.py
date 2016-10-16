
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

def draw_line_graph_catch(lav,lmv,lmxv,lst,lbaj,lbar,lbas,lboj,lbor,lbos, x_axis, project, type):
        
    print "Draw line graph=", project

    plt.close()
    ax= plt.subplot()
    ax.plot( x_axis, lav, 'ks-', label = "LAV")
    ax.plot( x_axis, lmv, 'ko-', label ="LMV")    
    ax.plot( x_axis, lmxv, 'k^-', label = "LMXV")
    ax.plot( x_axis, lst, 'k*-', label ="LST")    
    ax.plot( x_axis, lbaj, 'ks--', label = "LBAJ")
    ax.plot( x_axis, lbar, 'ko--', label ="LBAR")    
    ax.plot( x_axis, lbas, 'k*--', label = "LBAS")
    ax.plot( x_axis, lboj, 'k^--', label ="LBOJ")    
    ax.plot( x_axis, lbor, 'k+-', label = "LBOR")
    ax.plot( x_axis, lbos, 'k+--', label = "LBOS")
   
        
    plt.xlabel("Threshold", fontsize= 20)
    plt.ylabel("LF(%)", fontsize=20)
    plt.title(project+"-"+" ("+type+"-Block)", fontsize=20)
    plt.axis([ 0.1, 0.9, 20, 90],fontsize=30)
    
    
    # Now add the legend with some customizations.
    plt.rcParams.update({'font.size': 15})
    legend=plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.02),
          fancybox=True, shadow=True, ncol=5)
    
    # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.99')
    
    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('small')
    
    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
    
    
    #ax.legend(bbox_to_anchor=(1.1, 1.05))

    type = type.lower()
    
    plt.savefig(path+"\\a.pdf")
    plt.show()


#==============================================#
# Tomcat #
#==============================================#
#  1. J48
#----------------------------------------------#
lav=[69.89, 76.92,77.79, 78.6, 77.17, 72.67, 67.29, 58.73, 38.01]
lmv=[76.79, 76.95, 77.31, 77.02, 76.81, 77.01, 76.81, 77.38, 77.19]
lmxv=[65, 70.98, 76.91, 77.51, 74.81, 67.22, 58.17, 41.28, 26.22]
lst=[74.37, 78.94, 79.12, 79.15, 78.23, 76.14, 72.5, 66.4, 51.74]
lbaj=[68.77, 75.09, 77.32, 77.35, 75.16, 71.34, 64.44, 53.98, 36.31]
lbar=[59.57, 70.75, 79.14, 78.58, 72.41, 61.55, 44.85, 26.47, 10.73]
lbas=[71.81, 75.35, 77.05, 77.94, 77, 75.47, 72.31, 67.81, 58.83]
lboj=[78.73,78.35, 78.31, 78.15, 78.25, 77.99, 77.82, 77.6, 77.18]
lbor=[76.32, 76.07, 75.72, 75.36, 75.29, 75.03, 74.61, 74.17, 73.64]
lbos=[74.63, 74.76, 74.56, 74.39, 74.37, 74.51, 74.47, 74.41, 74.2]

x_axis = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
draw_line_graph_catch(lav,lmv,lmxv,lst,lbaj,lbar,lbas,lboj,lbor,lbos, x_axis, "Tomcat", "Catch")

