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


def excel2csv(excel_file):
    xlsx = pd.ExcelFile(excel_file)
    for sheet_name in xlsx.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        csv_path = "data/P6/" + sheet_name + ".csv"
        df.to_csv(csv_path, index=False)
        print(f"工作表 '{sheet_name}' 已保存为 CSV 文件 '{csv_path}'")
    return
