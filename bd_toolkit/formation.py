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
import numpy as np


def worker_load_format(file_path):
    revit_caled_sheet = pd.read_csv(file_path).loc[:, ["作业名称", "worker_load"]]
    revit_caled_sheet.insert(0, "rsrc_id", "Labor,Mechanic,Technician")
    revit_caled_sheet = revit_caled_sheet.apply(__string_to_list, axis="columns")
    revit_caled_sheet = (
        revit_caled_sheet.explode(["rsrc_id", "worker_load"])
        .reset_index()
        .drop(columns=["index"])
    )
    return revit_caled_sheet


def __string_to_list(row):
    row.loc["rsrc_id"] = row.loc["rsrc_id"].split(",")
    row.loc["worker_load"] = np.fromstring(row.loc["worker_load"], sep=",").tolist()
    return row