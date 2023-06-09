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


def std_workload_cal(code, load, var1, var2=0):
    std_ty0131 = pd.read_csv("stdfile/TY0131_2019.csv").set_index("code")
    result = std_ty0131.loc[code]

    result.loc["worker_load"] = np.fromstring(result.loc["worker_load"], sep=",")
    result.loc["materials_load"] = np.fromstring(result.loc["materials_load"], sep=",")
    result.loc["materials"] = np.array(result.loc["materials"].split(","))

    if var1 != "none" and str(result.loc["materials"][0]) == "var1":
        result.loc["materials"][0] = var1

    match code:
        # 钢筋
        case 10515092:
            load = load
        # 门窗幕墙
        case 10801003:
            load /= 100
        case 10805035:
            load /= 100
        case 10806041:
            load /= 100
        case 11209204:
            load /= 100
        # 混凝土矩形柱
        case _:
            load = load / 10
    return __result_series_cal(result, load)


def __result_series_cal(result, load):
    worker_load_array = np.ceil(result.loc["worker_load"] * load).astype(int)
    materials_load_array = np.ceil(result.loc["materials_load"] * load).astype(int)
    result.loc["worker_load"] = (
        np.array2string(worker_load_array, separator=",")
        .strip("[]")
        .replace(" ", "")
        .replace("\n", "")
    )
    result.loc["materials_load"] = (
        np.array2string(materials_load_array, separator=",")
        .strip("[]")
        .replace(" ", "")
        .replace("\n", "")
    )
    result.loc["materials"] = (
        np.array2string(result.loc["materials"], separator=",")
        .strip("[]")
        .replace(" ", "")
        .replace("'", "")
        .replace("\n", "")
    )
    return result
