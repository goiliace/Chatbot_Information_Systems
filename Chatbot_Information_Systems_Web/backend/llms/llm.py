from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from config.setting import settings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



llm_mis = ChatOpenAI(model='suzii/Llama-3.2-3B-MIS', temperature=0, base_url='http://localhost:8000/v1',openai_api_key="token-abc123")

llm_mis_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Bạn là một chatbot hỗ trợ các vấn đề về hệ thống thông tin quản lý. Chỉ được phép trả lời các câu hỏi liên quan đến hệ thống thông tin quản lý. Các câu khác hãy trả lời: tôi không biết. Chỉ cần tập trung trả lời câu hỏi một cách chi tiết và chính xác nhất có thể."),
        MessagesPlaceholder("history"),
        ("user", "{question}"),
    ]
)

generator_mis_pipeline = llm_mis_prompt | llm_mis