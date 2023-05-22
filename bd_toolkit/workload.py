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
from . import stdcalculator


def revit_workload_cal(file_path):
    revit_raw_sheet = pd.read_csv(file_path)
    result = revit_raw_sheet.apply(__workload_row_transform, axis="columns")
    return result


def __workload_row_transform(row):
    append = stdcalculator.std_workload_cal(
        row.loc["清单计量编码"], row.loc["数量"], row.loc["var1"]
    )
    return pd.concat([row, append])
