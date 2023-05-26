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

import openai

secret = open("tokens").read()
worklist = open("data/P6/work_list.csv").read()
taskrsc = open("data/revit/formatted.csv").read()
std_mat = open("stdfile/TY0131_2019_CaiLiao.csv").read()

openai.api_key = secret

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "你的任务是通过分析工程建设各个任务的材料消耗等信息给出每个任务合适的持续天数。接下来你会收到三个 csv 格式的表格，第一个表格内容是工作任务列表，第二个表格内容是任务资源分配计划，第三个表格是资源代号与资源名称的对应关系。你需要直接给出每项任务适合的持续天数（格式：任务代号 - 天数，如 A1000-1），不必描述计算分析过程",
        },
        {"role": "user", "content": worklist},
        {"role": "user", "content": taskrsc},
        {"role": "user", "content": std_mat},
    ],
    temperature=0,
)

# print the chat completion
print(chat_completion.choices[0].message.content)
