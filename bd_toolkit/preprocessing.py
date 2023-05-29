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


def combine_revit_files(path_prefix, file_name_list):
    result = pd.DataFrame()
    for file_name in file_name_list:
        file = pd.read_csv(path_prefix + file_name + ".csv", encoding="utf_16_le")
        match file_name:
            case "WINDOW":
                file["数量"] = file["var1"] / 10.0
            case "DOOR":
                file["数量"] = file["var1"] / 10.0
            case "WALL":
                for i in range(len(file)):
                    if file.loc[i, "清单计量编码"] == 11209204:
                        file.loc[i, "体积"] = file.loc[i, "面积"] / 10.0
            case "REBAR":
                for i in range(len(file)):
                    file.loc[i, "数量"] = (
                        file.loc[i, "总钢筋长度"]
                        * file.loc[i, "合计"]
                        * file.loc[i, "var1"]
                        / 1000000
                    )  # mm -> m & kg -> t
                    file.loc[i, "var1"] = file.loc[i, "族与类型"].lstrip("钢筋").lstrip(": ")
        if "体积" in file.columns:
            file = file.rename({"体积": "数量"}, axis=1)
        result = pd.concat(
            [
                result,
                file.loc[:, ["数量", "作业名称", "清单计量编码", "var1"]],
            ],
            ignore_index=True,
        )
    result["数量"] = result["数量"].fillna(0)
    result["var1"] = result["var1"].fillna("none")

    return result


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
    pd.read_excel(excel_file, sheet_name="USERDATA").to_excel(
        "out/p6.xlsx", sheet_name="USERDATA"
    )
    return


def revit_raw_file_merge(csv_file_path):
    csv_file = pd.read_csv(csv_file_path).loc[:, ["作业名称", "清单计量编码", "数量", "var1"]]
    result = (
        csv_file.groupby(["作业名称", "清单计量编码", "var1"]).agg({"数量": "sum"}).reset_index()
    )
    result.清单计量编码 = result.清单计量编码.astype(int)

    return result
