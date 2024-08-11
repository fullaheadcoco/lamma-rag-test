import rag
import time

# 시작 시간 기록
start_time = time.time()

pdf_files = ['/Users/gary/Documents/sample.pdf']
query = "who is 이경재?"
response = rag.answer_query_from_pdfs(query, pdf_files)

print("Question:", query)
print("Answer:", response)

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time
print(f"코드 실행 시간: {execution_time} 초")