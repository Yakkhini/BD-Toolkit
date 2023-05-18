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

import pandas as pd


def p6_work_list_extract(file_path):
    p6_work_sheet = pd.read_csv(file_path)
    p6_work_sheet.columns = p6_work_sheet.iloc[0]
    p6_work_sheet = p6_work_sheet.drop(index=[0])
    work_list = p6_work_sheet.loc[:, ["作业代码", "作业状态", "作业名称"]]
    return work_list


def excel2csv(excel_file):
    xlsx = pd.ExcelFile(excel_file)
    for sheet_name in xlsx.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        csv_path = "data/P6/" + sheet_name + ".csv"
        df.to_csv(csv_path, index=False)
        print(f"工作表 '{sheet_name}' 已保存为 CSV 文件 '{csv_path}'")
    return


def revit_raw_file_merge(csv_file_path):
    csv_file = pd.read_csv(csv_file_path).loc[:, ["作业名称", "清单计量编码", "体积"]]
    result = csv_file.groupby(["作业名称", "清单计量编码"]).agg({"体积": "sum"}).reset_index()

    return result
