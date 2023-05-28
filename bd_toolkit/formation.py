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


def worker_load_format(worker_load_path, work_list_path):
    work_list_sheet = pd.read_csv(work_list_path).rename(
        columns={
            "作业名称": "task__task_name",
            "作业代码": "task_id",
            "作业状态": "TASK__status_code",
        }
    )
    revit_caled_sheet = pd.read_csv(worker_load_path)
    revit_worker_caled_sheet = revit_caled_sheet.loc[:, ["作业名称", "worker_load"]]
    revit_worker_caled_sheet.insert(0, "rsrc_id", "Labor,Mechanic,Technician")
    revit_worker_caled_sheet = revit_worker_caled_sheet.rename(
        columns={"worker_load": "target_qty"}
    ).apply(__string_to_list, axis="columns")
    revit_worker_caled_sheet = (
        revit_worker_caled_sheet.explode(["rsrc_id", "target_qty"])
        .reset_index()
        .drop(columns=["index"])
    ).rename(columns={"作业名称": "task__task_name"})

    revit_mat_caled_sheet = revit_caled_sheet.loc[
        :, ["作业名称", "materials", "materials_load"]
    ].rename(columns={"materials": "rsrc_id"})
    revit_mat_caled_sheet = revit_mat_caled_sheet.rename(
        columns={"materials_load": "target_qty"}
    ).apply(__string_to_list, axis="columns")
    revit_mat_caled_sheet = (
        revit_mat_caled_sheet.explode(["rsrc_id", "target_qty"])
        .reset_index()
        .drop(columns=["index"])
    ).rename(columns={"作业名称": "task__task_name"})

    revit_caled_sheet = pd.concat([revit_worker_caled_sheet, revit_mat_caled_sheet])

    revit_caled_sheet["role_id"] = np.nan

    revit_caled_sheet = revit_caled_sheet.merge(
        work_list_sheet, on="task__task_name"
    ).loc[
        :,
        [
            "rsrc_id",
            "task_id",
            "TASK__status_code",
            "role_id",
            "task__task_name",
            "target_qty",
        ],
    ]

    print(revit_caled_sheet)

    revit_caled_sheet = (
        revit_caled_sheet.groupby(
            ["rsrc_id", "task_id", "TASK__status_code", "task__task_name"]
        )
        .agg({"target_qty": "sum"})
        .reset_index()
    )
    print(revit_caled_sheet)
    return revit_caled_sheet


def __string_to_list(row):
    row.loc["rsrc_id"] = row.loc["rsrc_id"].split(",")
    row.loc["target_qty"] = np.fromstring(row.loc["target_qty"], sep=",").tolist()
    return row
