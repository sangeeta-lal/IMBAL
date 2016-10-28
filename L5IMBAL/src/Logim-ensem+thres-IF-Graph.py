
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



#"""
path = "F:\\Research\\L5IMBAL\\result\\"

"""
path = "E:\\Sangeeta\\Research\\L5IMBAL\\result\\"
"""

plt.figure(1)                # the first figure

thres = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

lav_tom= [49.71, 55.18, 53.38, 51.82, 47.88, 41.31, 34.95, 28.21, 15.66]
lav_cloud = [60.76, 68.35, 68.38, 67.21, 64.6, 59.41, 51.64, 39.82, 22.12]
lav_hd =[45.07, 50.53, 47.79, 44.84,40.69, 34.1, 25.84, 17.88, 8.49]

ax1 =plt.subplot(5,2,1)             # the first subplot in the first figure
ax1.plot( thres, lav_tom, 'ks--', color ='0.55', label = "TC")
ax1.plot( thres, lav_cloud, 'ko--', label ="CS")
ax1.plot( thres, lav_hd, 'k*-', color='0.75', label ="HD")    
ax1.set_ylim(0,100)
ax1.set_xlim(0.1, 0.9)
ax1.xaxis.set_visible(False)
ax1.set_title("(a) LAV")
ax1.set_ylabel("LF (%)")
fontP = FontProperties()
fontP.set_size('small')
plt.legend(bbox_to_anchor=(0.6, 1.00, 0.8, .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
#plt.legend(  loc= 'upper left', bbox_to_anchor = (0.54,0.02), ncol=3)

lmv_tom = [46.89, 46.89, 47.32, 46.95,47.08,47,47.29,46.9,46.95]
lmv_cloud = [63.93,64,64.13,64.03,64.05, 64.1,64.08, 63.98, 64.18]
lmv_hd = [39.33, 39.3, 39.23, 39.28, 39.39, 39.19, 39.22, 39.22, 39.36]

ax2 =plt.subplot(5,2,2)             # the second subplot in the first figure
ax2.plot( thres, lmv_tom, 'ks--', color='0.55',label = "TC")
ax2.plot( thres, lmv_cloud, 'ko--', label ="CS")
ax2.plot( thres, lmv_hd, 'k*-', color='0.75',label ="HD")    
ax2.set_ylim(0,100)
ax2.set_xlim(0.1, 0.9)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_title("(b) LMV")


lmxv_tom = [41.29, 52.05, 54.88, 52.81, 47.74, 36.59, 29.04, 19.78, 10.31]
lmxv_cloud = [52.47, 63.71, 68.21, 67.61, 63.72, 53.53, 41.74, 28.45, 13.2]
lmxv_hd = [37.52, 48.95, 50.31, 46.8, 41.2, 28.59, 19.22, 11.23, 4.87]

ax3 =plt.subplot(5,2,3)             # the second subplot in the first figure
ax3.plot( thres, lmxv_tom, 'ks--', color='0.55',label = "TC")
ax3.plot( thres, lmxv_cloud, 'ko--', label ="CS")
ax3.plot( thres, lmxv_hd, 'k*-', color='0.75',label ="HD")    
ax3.set_ylim(0,100)
ax3.set_xlim(0.1, 0.9)
ax3.xaxis.set_visible(False)
ax3.title.set_text("(c) LMXV")
ax3.set_ylabel("LF (%)")

lst_tom = [55.51, 57.55, 55.99, 53.41, 49.97, 46.51, 42.01, 36.74, 29.04]
lst_cloud = [68.52, 70.72, 70.17, 68.82, 66.61, 64.21, 60.6, 55.07, 45.65]
lst_hd = [47.22, 52.11, 49.39, 46.63, 43.36, 39.28, 33.67, 28.54, 19.94]

ax4 =plt.subplot(5,2,4)             # the second subplot in the first figure
ax4.plot( thres, lst_tom, 'ks--', color='0.55', label = "TC")
ax4.plot( thres, lst_cloud, 'ko--', label ="CS")
ax4.plot( thres, lst_hd, 'k*-', color='0.75',label ="HD")    
ax4.set_ylim(0,100)
ax4.set_xlim(0.1, 0.9)
ax4.xaxis.set_visible(False)
ax4.yaxis.set_visible(False)
ax4.set_title("(d) LST")


lbaj_tom = [49.44, 54.18, 54.12, 51.75, 46.68, 40.89, 33.98, 26.55, 16.94]
lbaj_cloud = [62.04, 67.36, 68.57, 67.84, 65.35, 60.63, 53.84, 44.56, 31.25]
lbaj_hd = [45.79, 50.31, 50.41, 47.74, 42.36, 35.25, 26.99, 18.46, 9.14]

ax5 =plt.subplot(5,2,5)             # the second subplot in the first figure
ax5.plot( thres, lbaj_tom, 'ks--', color='0.55',label = "TC")
ax5.plot( thres, lbaj_cloud, 'ko--', label ="CS")
ax5.plot( thres, lbaj_hd, 'k*-',color='0.75', label ="HD")    
ax5.set_ylim(0,100)
ax5.set_xlim(0.1, 0.9)
ax5.xaxis.set_visible(False)
ax5.set_title("(e) LBAJ")
ax5.set_ylabel("LF (%)")

lbar_tom = [49.99, 59.65, 58.52, 50.27, 40.49, 30.33, 20.93, 13.84, 5.77]

lbar_cloud = [56.79, 69.03, 71.97, 69.27, 62.65, 52.39, 40.32, 27.7, 15.79]
lbar_hd = [46.17, 55.25, 53.01, 45.53, 34.09, 23.93, 15.61, 8.95, 3.43]

ax6 =plt.subplot(5,2,6)             # the second subplot in the first figure
ax6.plot( thres, lbar_tom, 'ks--',color='0.55', label = "TC")
ax6.plot( thres, lbar_cloud, 'ko--', label ="CS")
ax6.plot( thres, lbar_hd, 'k*-',color='0.75', label ="HD")    
ax6.set_ylim(0,100)
ax6.set_xlim(0.1, 0.9)
ax6.xaxis.set_visible(False)
ax6.yaxis.set_visible(False)
ax6.set_title("(f) LBAR")


lbas_tom = [42.81, 47.58, 50.33, 47.98, 44.34, 41.09, 33.32, 26.65, 15.17]
lbas_cloud = [53.93, 60.43, 61.71, 60.34, 57.08, 52.39, 46.33, 36.61, 21.4]
lbas_hd = [37.55, 42.31, 42.91, 40.64, 36.7, 31.46, 25.83, 17.62, 5.46]

ax7 =plt.subplot(5,2,7)             # the second subplot in the first figure
ax7.plot( thres, lbas_tom, 'ks--', color='0.55',label = "TC")
ax7.plot( thres, lbas_cloud, 'ko--', label ="CS")
ax7.plot( thres, lbas_hd, 'k*-', color='0.75',label ="HD")    
ax7.set_ylim(0,100)
ax7.set_xlim(0.1, 0.9)
ax7.xaxis.set_visible(False)
ax7.set_title("(g) LBAS")
ax7.set_ylabel("LF (%)")

lboj_tom = [59.27, 59.31, 59, 58.71, 58.45,58.12,57.63, 56.74,56.41]

lboj_cloud = [71.38,71.38,71.04,70.99,70.89,70.68,70.54, 70.34, 70.17]

lboj_hd = [51, 50.63, 50.24, 49.86, 49.55, 49.22,48.94, 48.54, 47.44]

ax8 =plt.subplot(5,2,8)             # the second subplot in the first figure
ax8.plot( thres, lboj_tom, 'ks--',color='0.55', label = "TC")
ax8.plot( thres, lboj_cloud, 'ko--', label ="CS")
ax8.plot( thres, lboj_hd, 'k*-', color='0.75',label ="HD")    
ax8.set_ylim(0,100)
ax8.set_xlim(0.1, 0.9)
ax8.xaxis.set_visible(False)
ax8.yaxis.set_visible(False)
ax8.set_title("(h)LBOJ")


lbor_tom = [56.81, 56.72,56.64, 56.59, 56.58, 56.43,56.4, 56.27, 56.05]
lbor_cloud = [69.53, 69.41,69.31, 69.25, 69.18, 69.09, 69.01, 68.9, 68.71]
lbor_hd = [48.88, 48.08, 47.56, 47.23, 46.78, 46.45, 45.93, 45.36, 44.59]

ax9 =plt.subplot(5,2,9)             # the second subplot in the first figure
ax9.plot( thres, lbor_tom, 'ks--', color='0.55',label = "TC")
ax9.plot( thres, lbor_cloud, 'ko--', label ="CS")
ax9.plot( thres, lbor_hd, 'k*-', color='0.75',label ="HD")    
ax9.set_ylim(0,100)
ax9.set_xlim(0.1, 0.9)
ax9.set_title("(i)LBOR")
ax9.set_ylabel("LF (%)")
ax9.set_xlabel("Threshold") 

lbos_tom = [46.17, 46.98, 47.27 ,46.88, 46.39, 45.6, 44.62, 43.12, 40.67]
lbos_cloud = [53.45, 56.42, 57.65, 57.63, 56.56, 55.02, 52.61, 49.3, 42]
lbos_hd = [38.22, 38.44, 37.64, 36.71, 35.22, 34.06, 31.43, 28.54, 24.66]

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
plt.suptitle("If-Blocks",  fontsize=14)
plt.subplots_adjust(top=0.89)
plt.savefig(path+"\\logim-ensem-thres-if.pdf")
plt.show()