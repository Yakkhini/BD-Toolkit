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


def revit_formatted_to_p6(formatted_file_path, p6_file_path):
    revit_formatted = pd.read_csv(formatted_file_path)
    p6_taskrsrc = pd.read_excel(p6_file_path, sheet_name="TASKRSRC").iloc[:1]
    pd.concat([p6_taskrsrc, revit_formatted]).reset_index().to_excel(
        "out/p6.xlsx", sheet_name="TASKRSRC"
    )

    print(pd.read_excel("out/p6.xlsx", sheet_name="TASKRSRC"))

    return
