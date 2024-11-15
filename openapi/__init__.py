import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="${api_key}", 
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt = """
有一张 mysql 表，建表语句如下：
create table if not exists table_name (
    id bigint auto increment primary key,
    gender varchar comment "性别",
    name varchar comment "姓名",
    age int comment "年龄"
)

请你给出一条sql 语句，查询男性的平均年龄;
请记住，你仅需给出 sql 语句就好，不需要任何客套话，不需要任何对代码的解释
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[{'role': 'system', 'content': 'You are a master in DB real time analysis'},
                {'role': 'user', 'content': prompt}]
    )
print(completion.choices[0])