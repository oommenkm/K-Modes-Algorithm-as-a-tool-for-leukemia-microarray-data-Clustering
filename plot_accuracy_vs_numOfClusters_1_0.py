"""
This script will generate the plot for accuracy and number of clusters in
both pdf and png format

Author: Oommen Mathew

Date: 25th Feb 2012

"""

from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label

d = Drawing(620, 430)

lp = LinePlot()
lp.width = 520
lp.height = 320
lp.x = 70
lp.y = 80

FH = open("finalOutPut.csv", 'r')
data_lines = FH.readlines()
FH.close()

TP = 20
TN = 14
TOT = 7129

dat_dict = {}

num_clust = -1
num_clust_prev = -1

for data_row in data_lines:
    cur_dict = {}
    #print data_row
    num_clust_prev = int(num_clust)
    [num_clust, clust, aml_cnt, all_cnt] = data_row.split(",")
    cur_dict['AML_COUNT'] = int(aml_cnt)
    cur_dict['ALL_COUNT'] = int(all_cnt)
    if num_clust_prev != int(num_clust):
        cur_dict2 = {}
    cur_dict2[clust] = cur_dict
    dat_dict[int(num_clust)] = cur_dict2

#print "\n\n\n>>>>", dat_dict, "\n\n\n"

print "+---------------|-------|------|------|------|--------+"
print "|No. of Clusters|FP SUM |FP    |FN SUM|FN    |Accuracy|"
print "+---------------|-------|------|------|------|--------+"

d_keys = dat_dict.keys()
d_keys.sort()

accuracy_list = []

for num_clust in dat_dict.keys():
    fp_sum = 0
    fn_sum = 0
    for i in range(1, int(num_clust)):
        fp_sum = fp_sum + dat_dict[num_clust][str(i)]['ALL_COUNT']/float(TOT)
        fn_sum = fn_sum + dat_dict[num_clust][str(i)]['AML_COUNT']/float(TOT)
    FP = TP - fp_sum
    FN = TN - fn_sum
    accuracy = (TP + TN) / (TP + FP + TN + FN) * 100.00
    accuracy_list.append((num_clust, accuracy))
    print "| %d             | %02.2f | %02.2f | %02.2f | %02.2f | %02.2f  |" % (num_clust, round(fp_sum), round(FP), round(fn_sum), round(FN), round(accuracy))
    
print "+---------------|-------|------|------|------|--------+"

lp.data = [accuracy_list]
print lp.data

lp.joinedLines = 1
lp.lines.symbol = makeMarker('Circle')
lp.lineLabelFormat = '%2.2f'
lp.strokeColor = colors.black
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = 5
lp.xValueAxis.labelTextFormat = '%2.0f'
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 104
lp.yValueAxis.valueStep = 10

xlbl = Label()
xlbl.setText("No. of Clusters")
xlbl.setOrigin(310, 53)

xlbl1 = Label()
xlbl1.setText("No. Of Clusters Vs Accuracy")
xlbl1.setOrigin(310, 25)

ylbl = Label()
ylbl.setText("Accuracy\n      (%)")
ylbl.setOrigin(28, 260)

lp.lines[0].strokeColor = colors.purple
lp.lineLabels[0].strokeColor = colors.purple

d.add(lp)
d.add(xlbl)
d.add(xlbl1)
d.add(ylbl)
d.save(fnRoot='NoOfClustersVsAccuracy', formats=['png', 'pdf'])