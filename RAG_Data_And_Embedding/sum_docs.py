from g4f.client import Client
import json
import sys
from tqdm import tqdm

client = Client()

name_file = int(sys.argv[1])

docs  = []
with open(f"docs_chunk_1/output_{name_file}.jsonl") as f:
    for line in f:
        docs.append(json.loads(line))
        

for doc in tqdm(docs):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        messages=[
            {"role": "system", "content": """Bạn là một chuyên gia trong ngành hệ thống thông tin quản lý,  
            Bạn được cung cấp 1 văn bản với nội dung liên quan đến ngành hệ thống thông tin quản lý.
            Bạn cần đọc kỹ, phân tích và đưa ra kiến thức hệ thống thông tin quản lý trong văn bản đó sao cho khi hỏi khi có người hỏi các câu hỏi về kiến thức đó, có thể dùng văn bản của bạn để đưa ra câu trả lời
            Bạn phải trình bày kiến thức một cách rõ ràng, đầy đủ ý. 
            Luôn sử dụng tiếng Việt Nam (vietnamese) để trả lời.
            Hãy viết thành các đoạn, không được sử dụng markdown, hãy sử dụng văn bản thuần túy
            Hãy chú ý các số liệu, các số liệu phải được trình bày, và đảm bảo số liệu đúng và chính xác
            Nếu đoạn văn bản không có kiến thức nào liên quan đến ngành hệ thống thông tin quản lý, hãy trả về: 'No relevant MIS'."""},
            {"role": "user", "content": "Văn bản: \n" + doc},
        ],
        max_tokens=8192
    )
    with open(f'docs_gen_1/doc_{name_file}.jsonl', '+a') as f:
        f.write(json.dumps(response.choices[0].message.content, ensure_ascii=False) + "\n")