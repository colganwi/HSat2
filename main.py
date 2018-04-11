import xlsxwriter
from sat_finder import *
from sat_maker import *

#names = ["CHRY_17109M","CHR1_11321M"]
names = ["CHR1_11321M","CHR2_17119F","CHR4_17119F","CHR5_17119F","CHR6_7340F","CHR7_17119F","CHR8n9_17119F","CHR9to12_7340F","CHR13_7340F","CHR14_17119F","CHR18_17109M","CHR21_17119F","CHR22_7340F","CHRX_7340F","CHRY_17109M"]
for name in names[10:]:
    sat_maker(name)

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
workbook = xlsxwriter.Workbook('sat_dist.xlsx')
worksheet = workbook.add_worksheet()
subfamilies = ['3B2', '3B3', '3B1', '3B4', '3B5', '2A2', '2B', '2A1', '3A3', '3A2', '3A1', '3A6', '3A5', '3A4', 'Unclassified']

for i in range(len(subfamilies)):
    worksheet.write('A'+str(i+2), subfamilies[i])

for i in range(len(names)):
    name = names[i]
    worksheet.write(alphabet[i+1]+'1', name)
    num = sat_finder(name)
    for j in range(len(num)):
        worksheet.write(alphabet[i+1]+str(j+2), str(num[j]))

workbook.close()
