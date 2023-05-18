"""
Copyright (c) 2023 Yakkhini
BD-Toolkit is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""

import preprocessing, workload

p6_excel_file = "data/P6BD.xlsx"
preprocessing.excel2csv(p6_excel_file)

revit_kzgz_file = "data/KZGZ.csv"
preprocessing.revit_raw_file_merge(revit_kzgz_file).to_csv(
    "data/revit/KZGZ.csv", index=False
)

revit_merged_file = "data/revit/KZGZ.csv"
workload.revit_workload_cal(revit_merged_file).to_csv(
    "data/revit/KZGZ_caled.csv", index=False
)
