
system_prompt_1 = """Hướng dẫn: Bạn sẽ nhận được một câu hỏi và câu trả lời từ chatbot liên quan đến ngành Hệ thống thông tin quản lý (MIS). Nhiệm vụ của bạn là đánh giá độ chính xác của câu trả lời dựa trên thông tin được cung cấp.

Tiêu chí Đánh giá:
Độ Chính Xác (0-10):

Điểm 0:
Câu trả lời hoàn toàn sai, không liên quan đến câu hỏi hoặc cung cấp thông tin sai lệch nghiêm trọng. Không thể xác định được thông tin chính xác nào từ câu trả lời.

Điểm 1:
Câu trả lời có một số thông tin đúng, nhưng thiếu sót lớn và không trả lời đúng câu hỏi. Các thông tin đưa ra không rõ ràng hoặc có nhiều sai sót nghiêm trọng. Cần sửa chữa hoặc cung cấp thêm thông tin cơ bản để có thể hiểu được câu trả lời.

Điểm 2:
Câu trả lời có thông tin đúng nhưng thiếu sót lớn, không trả lời đầy đủ câu hỏi. Có một số phần đúng, nhưng thiếu chi tiết quan trọng hoặc có nhiều phần thông tin không chính xác hoặc không đủ rõ ràng.

Điểm 3:
Câu trả lời đúng nhưng thiếu một số chi tiết quan trọng. Mặc dù cung cấp thông tin cơ bản chính xác, nhưng chưa đủ để làm rõ câu hỏi hoặc thiếu ví dụ, lý do, hoặc các yếu tố bổ trợ cần thiết.

Điểm 4:
Câu trả lời đúng, có đầy đủ thông tin cơ bản và cung cấp một số chi tiết rõ ràng, nhưng thiếu một vài yếu tố phụ hoặc ví dụ minh họa. Mặc dù trả lời chính xác, nhưng cần thêm một số yếu tố để câu trả lời trở nên thuyết phục và dễ hiểu hơn.

Điểm 5:
Câu trả lời chính xác, đầy đủ và rõ ràng, nhưng vẫn có thể bổ sung thêm một số chi tiết nhỏ để tăng tính thuyết phục hoặc dễ hiểu. Mặc dù cung cấp thông tin chính xác, nhưng vẫn có thể cải thiện bằng cách giải thích thêm hoặc sử dụng ví dụ.

Điểm 6:
Câu trả lời đầy đủ và chính xác, cung cấp thông tin cần thiết và rõ ràng. Tuy nhiên, câu trả lời vẫn thiếu một chút thông tin bổ sung để trở nên hoàn toàn chi tiết hoặc có thể mở rộng với một vài ví dụ cụ thể để tăng tính áp dụng thực tế.

Điểm 7:
Câu trả lời rất chi tiết và chính xác, giải thích rõ ràng mọi khía cạnh của câu hỏi. Tuy nhiên, vẫn thiếu một số chi tiết nhỏ hoặc có thể bổ sung thêm một vài ví dụ thực tế để làm rõ hơn. Câu trả lời dễ hiểu và đúng đắn, nhưng có thể thêm thông tin để tăng cường tính ứng dụng.

Điểm 8:
Câu trả lời đầy đủ và chi tiết, cung cấp tất cả thông tin cần thiết với các giải thích rõ ràng. Tuy nhiên, có thể bổ sung thêm một vài yếu tố nhỏ hoặc ví dụ thực tế để nâng cao sự hoàn thiện và áp dụng vào các tình huống cụ thể hơn.

Điểm 9:
Câu trả lời rất chi tiết, rõ ràng và chính xác. Đưa ra đầy đủ thông tin và giải thích rõ ràng mọi khía cạnh của câu hỏi, bao gồm ví dụ, lý do và thông tin bổ sung. Tuy nhiên, vẫn có thể có một số điểm có thể mở rộng thêm hoặc áp dụng vào những trường hợp đặc biệt.

Điểm 10:
Câu trả lời hoàn toàn chính xác, đầy đủ và chi tiết. Mọi khía cạnh của câu hỏi được giải thích rõ ràng, cung cấp thông tin sâu sắc, ví dụ cụ thể và các yếu tố bổ trợ. Câu trả lời hoàn hảo, không thiếu sót và dễ hiểu với mức độ thông tin cao, phù hợp với câu hỏi và tình huống.

Các bước thực hiện:
Đọc kỹ câu hỏi và câu trả lời.
Đánh giá độ chính xác của câu trả lời dựa trên mức độ đúng đắn và đầy đủ của thông tin được cung cấp.
Cung cấp điểm số từ 0 đến 10 dựa trên các tiêu chí trên.
Hãy đánh giá một cách khó tính

Trả về kết quả dạng:
score: int  (0-10)
Không trả ra gì thêm
"""
system_prompt_2 = """Hướng dẫn: Bạn sẽ nhận được một câu hỏi và câu trả lời từ chatbot liên quan đến ngành Hệ thống thông tin quản lý (MIS). Nhiệm vụ của bạn là đánh giá mức độ chi tiết của câu trả lời, tức là câu trả lời có cung cấp đủ thông tin cần thiết hay không, có giải thích rõ ràng, đầy đủ hay chỉ đưa ra thông tin cơ bản.

Tiêu chí Đánh giá:
Mức Độ Chi Tiết (0-7):

Điểm 0:
Câu trả lời không có thông tin hoặc hoàn toàn không liên quan đến câu hỏi. Không có bất kỳ thông tin hữu ích nào được cung cấp.

Điểm 1:
Câu trả lời rất ngắn gọn, thiếu thông tin quan trọng và không cung cấp đủ chi tiết để người đọc hiểu vấn đề. Câu trả lời có thể chỉ bao gồm một câu đơn giản hoặc rất chung chung, thiếu rõ ràng.

Điểm 2:
Câu trả lời có thông tin nhưng thiếu các giải thích chi tiết hoặc còn mơ hồ. Cung cấp một số thông tin đúng nhưng chưa đủ để người đọc có thể hiểu một cách toàn diện về câu hỏi. Câu trả lời có thể thiếu các yếu tố cần thiết để thu hút sự chú ý.

Điểm 3:
Câu trả lời cung cấp thông tin tương đối đầy đủ và rõ ràng, nhưng vẫn thiếu một vài chi tiết nhỏ hoặc có phần chưa giải thích rõ. Dù thông tin chính xác, nhưng chưa thực sự hấp dẫn hoặc chưa đủ thuyết phục, làm giảm tính lôi cuốn của câu trả lời.

Điểm 4:
Câu trả lời đầy đủ và rõ ràng, cung cấp thông tin chi tiết và dễ hiểu. Tuy nhiên, câu trả lời có thể thiếu một vài yếu tố nhỏ hoặc chưa đủ lôi cuốn người đọc. Câu trả lời có thể chưa thực sự hấp dẫn hoặc sinh động, mặc dù đã đủ thông tin.

Điểm 5:
Câu trả lời rất chi tiết và dễ hiểu, trả lời rõ ràng mọi khía cạnh của câu hỏi. Tuy nhiên, có thể thiếu một số yếu tố bổ sung để làm câu trả lời thêm hấp dẫn hoặc sinh động. Câu trả lời khá tốt nhưng chưa hoàn hảo về mặt thu hút sự chú ý hoặc sự lôi cuốn.

Điểm 6:
Câu trả lời cung cấp thông tin chính xác, đầy đủ và rõ ràng, nhưng câu trả lời có thể hơi khô khan hoặc thiếu sự sáng tạo trong cách diễn đạt. Mặc dù cung cấp đủ thông tin, nhưng có thể thiếu yếu tố tạo sự hứng thú hoặc sự dễ nhớ.

Điểm 7:
Câu trả lời rất đầy đủ và chi tiết, giải thích các khía cạnh của câu hỏi một cách rõ ràng và dễ hiểu. Câu trả lời không chỉ đúng mà còn được diễn đạt một cách mạch lạc, có thể hấp dẫn người đọc với một cách tiếp cận logic và dễ tiếp thu.

Các bước thực hiện:
Đọc kỹ câu hỏi và câu trả lời.
Đánh giá mức độ chi tiết của câu trả lời, xem câu trả lời có cung cấp đầy đủ thông tin và giải thích rõ ràng, chi tiết hay không.
Cung cấp điểm số từ 0 đến 7 dựa trên các tiêu chí trên.
Hãy đánh giá một cách khó tính
Trả về kết quả dạng:
score: int (0-7)
Không trả ra gì thêm
"""


from g4f.client import Client
import json
from tqdm import tqdm
import sys

ctn = True
while ctn:
    client = Client()


    qar = []

    file_name = sys.argv[1]
    model = sys.argv[2]
    with open(file_name, 'r') as f:
        for line in f:
            qar.append(json.loads(line))   
    scores_old = []
    with open(f'benmark/res_mis_1500k_test_score_{model}_{file_name}.jsonl', 'r') as f:
        for line in f:
            try:
                scores_old.append(json.loads(line))
            except:
                scores_old.append("~~")
    if len(scores_old)>=1500:
        ctn = False
    try:
        for item in tqdm(qar[len(scores_old)+1:]):
            q,r = item['question'], item['respone']
            
            response_1 = client.chat.completions.create(
                model=model,
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt_1
                    },
                    {
                        "role": "user",
                        "content": """
                        cặp câu hỏi - trả lời
                        user: {question}
                        assistant: {answer}
                        """.format(question=q, answer=r)
                    }
                ]
            )
            try:
                score_1 = int(response_1.choices[0].message.content.split(":")[1])  
            except:
                score_1 = response_1.choices[0].message.content
            response_2 = client.chat.completions.create(
                model=model,
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt_2
                    },
                    {
                        "role": "user",
                        "content": """
                        cặp câu hỏi - trả lời
                        user: {question}
                        assistant: {answer}
                        """.format(question=q, answer=r)
                    }
                ]
            )
            try:
                score_2 = int(response_2.choices[0].message.content.split(":")[1])
            except:
                score_2 = response_2.choices[0].message.content
            with open(f'benmark/res_mis_1500k_test_score_{model}_{file_name}.jsonl', 'a') as f:
                f.write(json.dumps({'question': q, 'response': r, 'score_1': score_1, 'score_2': score_2}, ensure_ascii=False))
                f.write('\n')
    
    except:
        print("errror")
        continue
        