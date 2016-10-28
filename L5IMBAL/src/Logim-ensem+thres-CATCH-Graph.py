
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""

plt.figure(1)                # the first figure

thres = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

lav_tom= [69.89, 76.92, 77.79, 78.6, 77.17, 72.67, 67.29, 58.73, 38.01]
lav_cloud = [81.12, 85.94, 87.2, 87.8,87.86, 85.77,82.72, 78.02,61.68]
lav_hd =[63.18, 70.07, 71.18, 71.33, 68.9, 63.56, 58.05, 46.51, 26.31]
ax1 =plt.subplot(5,2,1)             # the first subplot in the first figure
ax1.plot( thres, lav_tom, 'ks--', color ='0.55', label = "TC")
ax1.plot( thres, lav_cloud, 'ko--', label ="CS")
ax1.plot( thres, lav_hd, 'k*-', color='0.75', label ="HD")    
ax1.set_ylim(0,100)
ax1.set_xlim(0.1, 0.9)
ax1.xaxis.set_visible(False)
ax1.set_ylabel("LF (%)")

ax1.set_title("(a) LAV")
fontP = FontProperties()
fontP.set_size('small')
plt.legend(bbox_to_anchor=(0.6, 1.00, 0.8, .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
#plt.legend(  loc= 'upper left', bbox_to_anchor = (0.54,0.02), ncol=3)

lmv_tom = [76.79, 76.95, 77.31, 77.02, 76.81, 77.01, 76.81, 77.38, 77.19]
lmv_cloud = [87.81, 87.79, 87.75, 87.66, 87.8, 87.67, 87.88, 87.67, 87.9]
lmv_hd = [68.51, 68.81, 68.86, 68.6, 68.59, 68.68, 68.86, 68.6, 68.94]
ax2 =plt.subplot(5,2,2)             # the second subplot in the first figure
ax2.plot( thres, lmv_tom, 'ks--', color='0.55',label = "TC")
ax2.plot( thres, lmv_cloud, 'ko--', label ="CS")
ax2.plot( thres, lmv_hd, 'k*-', color='0.75',label ="HD")    
ax2.set_ylim(0,100)
ax2.set_xlim(0.1, 0.9)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_title("(b) LMV")


lmxv_tom = [65, 70.98, 76.91,77.51, 74.81, 67.22, 58.17, 41.28, 26.22]
lmxv_cloud = [78.15, 81.89, 85.76, 87.12,86.35,82.97,78.36,65.04,49]
lmxv_hd = [57.62,65.19,70.05,70.46,67.57,58.57,46.93,31.4,16.82]
ax3 =plt.subplot(5,2,3)             # the second subplot in the first figure
ax3.plot( thres, lmxv_tom, 'ks--', color='0.55',label = "TC")
ax3.plot( thres, lmxv_cloud, 'ko--', label ="CS")
ax3.plot( thres, lmxv_hd, 'k*-', color='0.75',label ="HD")    
ax3.set_ylim(0,100)
ax3.set_xlim(0.1, 0.9)
ax3.xaxis.set_visible(False)
ax3.title.set_text("(c) LMXV")
ax3.set_ylabel("LF (%)")


lst_tom = [74.37,78.94,79.12,79.15,78.23,76.14,72.5,66.4,51.74]
lst_cloud = [85.35,87.91,88.67,88.55,88.14,87.47,86.13,83.09,75.7]
lst_hd = [65.78,72.24,72.94,72.36,70.83,68.24,64.04,56.07,39.9]
ax4 =plt.subplot(5,2,4)             # the second subplot in the first figure
ax4.plot( thres, lst_tom, 'ks--', color='0.55', label = "TC")
ax4.plot( thres, lst_cloud, 'ko--', label ="CS")
ax4.plot( thres, lst_hd, 'k*-', color='0.75',label ="HD")    
ax4.set_ylim(0,100)
ax4.set_xlim(0.1, 0.9)
ax4.xaxis.set_visible(False)
ax4.yaxis.set_visible(False)
ax4.set_title("(d) LST")


lbaj_tom = [68.77, 75.09, 77.32, 77.35,75.16,71.34,64.44,53.98,36.31]
lbaj_cloud = [81.93, 84.95, 86.85,87.66,87.82,86.77,83.25,75.87,61.37]
lbaj_hd = [62.52,69,71.72,71.13,67.96,62.56,54.28,42.67,27.54]
ax5 =plt.subplot(5,2,5)             # the second subplot in the first figure
ax5.plot( thres, lbaj_tom, 'ks--', color='0.55',label = "TC")
ax5.plot( thres, lbaj_cloud, 'ko--', label ="CS")
ax5.plot( thres, lbaj_hd, 'k*-',color='0.75', label ="HD")    
ax5.set_ylim(0,100)
ax5.set_xlim(0.1, 0.9)
ax5.xaxis.set_visible(False)
ax5.set_title("(e) LBAJ")
ax5.set_ylabel("LF (%)")

lbar_tom = [59.57, 70.75, 79.14, 78.58, 72.41, 61.55, 44.85, 26.47, 10.73]
lbar_cloud = [74.82, 80.22, 84.76, 88.13, 88.83,85.95,76.89,57.21,26.42]
lbar_hd = [54.85, 67.9,73.97,72.4,63,48.47,33.16, 21.57, 11.55]
ax6 =plt.subplot(5,2,6)             # the second subplot in the first figure
ax6.plot( thres, lbar_tom, 'ks--',color='0.55', label = "TC")
ax6.plot( thres, lbar_cloud, 'ko--', label ="CS")
ax6.plot( thres, lbar_hd, 'k*-',color='0.75', label ="HD")    
ax6.set_ylim(0,100)
ax6.set_xlim(0.1, 0.9)
ax6.xaxis.set_visible(False)
ax6.yaxis.set_visible(False)
ax6.set_title("(f) LBAR")


lbas_tom = [71.81, 75.35, 77.05, 77.94,77, 75.47,72.31,67.81,58.83]
lbas_cloud = [82.77, 84.7,85.41,85.36,84.87,83.68,80.9,76.92,68.91]
lbas_hd = [63.17,67.15,68.64,68.67,67.88,65.54,61.24,54.55,43.83]
ax7 =plt.subplot(5,2,7)             # the second subplot in the first figure
ax7.plot( thres, lbas_tom, 'ks--', color='0.55',label = "TC")
ax7.plot( thres, lbas_cloud, 'ko--', label ="CS")
ax7.plot( thres, lbas_hd, 'k*-', color='0.75',label ="HD")    
ax7.set_ylim(0,100)
ax7.set_xlim(0.1, 0.9)
ax7.xaxis.set_visible(False)
ax7.set_title("(g) LBAS")
ax7.set_ylabel("LF (%)")



lboj_tom = [78.73,78.35, 78.31, 78.15, 78.25, 77.99, 77.82, 77.6, 77.18]
lboj_cloud = [88.66, 88.68, 88.6, 88.55,88.53, 88.43,88.41, 88.34, 88.26]
lboj_hd = [72.96, 72.86, 72.65, 72.33, 72.2, 71.86, 71.68,71.32, 70.87]
ax8 =plt.subplot(5,2,8)             # the second subplot in the first figure
ax8.plot( thres, lboj_tom, 'ks--',color='0.55', label = "TC")
ax8.plot( thres, lboj_cloud, 'ko--', label ="CS")
ax8.plot( thres, lboj_hd, 'k*-', color='0.75',label ="HD")    
ax8.set_ylim(0,100)
ax8.set_xlim(0.1, 0.9)
ax8.xaxis.set_visible(False)
ax8.yaxis.set_visible(False)
ax8.set_title("(h)LBOJ")


lbor_tom = [76.32,76.07,75.72,75.36,75.29,75.03,74.61,74.17,73.64]
lbor_cloud = [89.42,89.4,89.35,89.41,89.4,89.35,89.33,89.28,89.27]
lbor_hd = [70.43, 70.15, 69.98, 69.83, 69.64, 69.56, 69.31, 69.02,68.57]
ax9 =plt.subplot(5,2,9)             # the second subplot in the first figure
ax9.plot( thres, lbor_tom, 'ks--', color='0.55',label = "TC")
ax9.plot( thres, lbor_cloud, 'ko--', label ="CS")
ax9.plot( thres, lbor_hd, 'k*-', color='0.75',label ="HD")    
ax9.set_ylim(0,100)
ax9.set_xlim(0.1, 0.9)
ax9.set_title("(i)LBOR")
ax9.set_xlabel("Threshold")
ax9.set_ylabel("LF (%)")



lbos_tom = [74.63, 74.76, 74.56, 74.39, 74.37, 74.51, 74.47, 74.41, 74.2]
lbos_cloud = [83.29, 83.1, 83.04, 82.98, 82.84, 82.75, 82.62, 82.52, 82.31]
lbos_hd = [65.67, 65.6, 65.35, 65.28, 65.03, 64.9, 64.45, 63.93, 63.09]
ax10 =plt.subplot(5,2,10)             # the second subplot in the first figure
ax10.plot( thres, lbos_tom, 'ks--', color='0.55',label = "TC")
ax10.plot( thres, lbos_cloud, 'ko--', label ="CS")
ax10.plot( thres, lbos_hd, 'k*-',color='0.75', label ="HD")    
ax10.set_ylim(0,100)
ax10.set_xlim(0.1, 0.9)
ax10.yaxis.set_visible(False)
ax10.set_title("(j) LBOS")
ax10.set_xlabel("Threshold")




#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2, borderaxespad=0.)

plt.rcParams.update({'font.size': 10})
plt.tight_layout()
plt.suptitle("Catch-Blocks",  fontsize=14)
plt.subplots_adjust(top=0.89)

plt.savefig(path+"\\logim-ensem-thres-catch.pdf")
plt.show()