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


def std_workload_cal(code, load, var1=0, var2=0):
    std_ty0131 = pd.read_csv("stdfile/TY0131_2019.csv").set_index("code")
    result = std_ty0131.loc[code]

    match code:
        # 混凝土矩形柱
        case 10502001:
            load /= 10
    return __result_series_cal(result, load)


def __result_series_cal(result, load):
    worker_load_array = np.fromstring(result.loc["worker_load"], sep=",") * load
    materials_load_array = np.fromstring(result.loc["materials_load"], sep=",") * load
    result.loc["worker_load"] = (
        np.array2string(worker_load_array, separator=",").strip("[]").replace(" ", "")
    )
    result.loc["materials_load"] = (
        np.array2string(materials_load_array, separator=",")
        .strip("[]")
        .replace(" ", "")
    )
    return result
