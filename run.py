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

import bd_toolkit as bd

revit_file_name_list = ["KZGZ", "KL", "LB", "WALL", "DOOR", "WINDOW"]
revit_file_path = "data/Revit_"

bd.preprocessing.combine_revit_files(revit_file_path, revit_file_name_list).to_csv(
    "data/revit/RAW.csv", index=False
)

p6_excel_file = "data/P6BD.xlsx"
bd.preprocessing.excel2csv(p6_excel_file)
bd.preprocessing.p6_work_list_extract("data/P6/TASK.csv").to_csv(
    "data/P6/work_list.csv", index=False
)

revit_raw_file = "data/revit/RAW.csv"
bd.preprocessing.revit_raw_file_merge(revit_raw_file).to_csv(
    "data/revit/merged.csv", index=False
)

revit_merged_file = "data/revit/KZGZ.csv"
bd.workload.revit_workload_cal(revit_merged_file).to_csv(
    "data/revit/KZGZ_caled.csv", index=False
)

revit_caled_file = "data/revit/KZGZ_caled.csv"
work_list_file = "data/P6/work_list.csv"
bd.formation.worker_load_format(revit_caled_file, work_list_file).to_csv(
    "data/revit/KZGZ_caled_formatted.csv", index=False
)
