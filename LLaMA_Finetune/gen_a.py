import json
from g4f.client import Client
from tqdm import tqdm
import json
import re
client = Client()

import sys

index = int(sys.argv[1])
questions = []
with open(f'questions/question_{index}.jsonl', 'r') as f:
    for line in f:
        questions.append(json.loads(line))   

for question in tqdm(questions):
    response = client.chat.completions.create(
    model="gpt-4o",
    
    messages=[
        {"role": "system", "content": "Bạn là một chatbot hỗ trợ các vấn đề về hệ thống thông tin quản lý. Chỉ được phép trả lời các câu hỏi liên quan đến hệ thống thông tin quản lý. Các câu khác hãy trả lời: tôi không biết. Chỉ cần tập trung trả lời câu hỏi một cách chi tiết và chính xác nhất có thể."},
        {"role": "user", "content": question["question"]}
        ],
    )

    with open(f'qa_final/data_{index}.jsonl', 'a', encoding='utf-8') as file:
        file.write(json.dumps({"question": question["question"], "answer": response.choices[0].message.content}, ensure_ascii=False) + "\n")