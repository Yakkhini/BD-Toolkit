'''
Copyright (c) 2023 Yakkhini
BD-Toolkit is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
'''

from tabnanny import check
import pandas as pd

revit_kzgz_sheet = pd.read_csv("data/KZGZ.csv")
p6_work_sheet = pd.read_excel("data/P6BD.xlsx").drop(index = [0])
#print(p6_work_sheet.head())

work_list = p6_work_sheet['task_name'].unique()
print(work_list)

check = input('Is work name list correct?(y/N)')

if check == 'y':
    print('Work list checking done.')
else:
    print('Work list checking error.')
    exit()