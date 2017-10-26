# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:06:18 2017

@author: dacrands
"""
import pandas as pd
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['patch.force_edgecolor'] = True

xlsfile = pd.ExcelFile(r'../substance_copy.xlsx')
dframe = xlsfile.parse('main')
dframe_text = open("drugage_dframe.txt", "w")
dframe_text.write(str(dframe.head()))



print(sum(dframe['Admissions']))
print(min(dframe['Admissions']))
admissions = str(sum(dframe['Admissions']))

plt.rcParams['axes.facecolor'] = '#3b3b49'
age_graph = sb.factorplot(
        y="Admissions", x="age_num", data=dframe,
        size=7, aspect=1.6, capsize=0.1,
        hue="Substance", legend=None,
        palette=sb.color_palette(['#4286f4',
                                    '#f4d442',
                                    '#cb42f4',
                                    '#42f498',
                                    '#f4426b'])
)

sb.despine(left=True)
sb.set_style("whitegrid")

plt.title("NY State Chemical Dependence\nTreatment Program Admissions 2007-2015",
          fontsize=24, color="black", fontweight="heavy", y=1.04)

legend = plt.legend(
                    bbox_to_anchor=(.01, 0.98), loc='upper left',
                    ncol=1, fontsize=14,
                    frameon=True, shadow=True
                    )

frame = legend.get_frame()

plt.ylabel("Annual average\nper country", fontweight="bold", fontsize=20)
plt.xlabel("Age", fontweight="bold", fontsize=22)
plt.text(-0.23, 115, "Total Admissions = {0},{1},{2}".format(admissions[:1], 
                                                             admissions[0:3], 
                                                             admissions[3:6], 
                                                             admissions[0:3]),
        fontsize=14, color="white", fontweight="medium", fontstyle="italic")

plt.xticks([0, 1, 2, 3, 4, 5],
           ['<18', '18-24', '25-34', '35-44', '45-54', '55+'],
           fontsize=16, fontweight='bold')
plt.yticks(fontsize=16, fontweight='bold')

age_graph.savefig('agegraph.png')
