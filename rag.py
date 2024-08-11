import llm
import pdf
import es 

def answer_query_from_pdfs(query, pdf_files):
    """전체 프로세스를 통합하여 질문에 답변 생성"""
    # PDF에서 텍스트 추출
    documents = []
    for pdf_file in pdf_files:
        print("Extracting text from", pdf_file)

        text = pdf.extract_text_from_pdf(pdf_file)

        print("Text:", text)
        documents.append({"text": text, "filename": pdf_file})


    # Elasticsearch에 색인
    es.index_documents(documents)

    # 질문에 대한 관련 문서 검색
    related_documents = es.search_documents(query)
    print("Related documents:")
    print(related_documents)

    response = llm.generate_response_lamma3_1(query, related_documents)
    
    return response
