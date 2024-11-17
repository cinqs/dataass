import os
from openai import OpenAI
import properties

__client = OpenAI(
        api_key=properties.get("OPENAI_KEY"), 
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

def complete(prompt: str):
    global __client

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

    completion = __client.chat.completions.create(
        model="qwen-plus",
        messages=[{'role': 'system', 'content': 'You are a master in DB real time analysis'},
                    {'role': 'user', 'content': prompt}]
        )
    return completion.choices[0]