from g4f.client import Client
from tqdm import tqdm
import json
import re
client = Client()

data = []

import sys

index = int(sys.argv[1])
with open(f"doc_{index}.jsonl", "r") as f:
    for line in f:
        data.append(line)


for line in tqdm(data):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content":"""Bạn là một chuyên gia trong việc đặt câu hỏi từ kiến thức được cung cấp. từ đoạn văn sau, hãy đặt 4 câu hỏi liên quan đến hệ thống thông tin quản lý (MIS). các câu hỏi có liên quan đến kiến thức được nói đến trong đoạn văn, các câu hỏi phải được trả lời bằng tiếng Việt.
        Lưu ý:
        - Người trả lời câu hỏi không được cung cấp văn bản, vì vậy chỉ hỏi câu hỏi liên quan đến kiến thức chứ không phải là câu hỏi về thông tin cụ thể trong văn bản.
        - Bạn phải trả ra theo format sau:
        {
            "question": "Câu hỏi 1"
        }
        {
            "question": "Câu hỏi 2"
        }
        {
            "question": "Câu hỏi 3" 
        }"
        - Nếu đoạn văn được cung cấp không có thông tin liên quan đến hệ thống thông tin quản lý, hãy trả lời:
        {
            "question": "None"
        }
        """},
            {"role": "user", "content": line}
            ],
    )
            
            
    json_objects = re.findall(r'{.*?}', response.choices[0].message.content, re.DOTALL)

    # Convert each JSON object into Python dictionaries
    questions_list = [json.loads(obj) for obj in json_objects]

    # Write the list to a JSONL file
    file_path = f"questions_converted_{index}.jsonl"
    with open(file_path, 'a', encoding='utf-8') as file:
        for question in questions_list:
            file.write(json.dumps(question, ensure_ascii=False) + "\n")