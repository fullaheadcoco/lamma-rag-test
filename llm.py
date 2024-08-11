import transformers
import torch
from huggingface_hub import login

def generate_response_lamma3_1(query, documents):
    context = "\n\n".join(documents)
    print(context)

    login("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")

    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=256,
    )
    
    return outputs[0]["generated_text"][-1]
    



def generate_response_opennAI(query, documents):
    """OpenAI API를 통해 응답 생성"""
    context = "\n\n".join(documents)
    print(context)
    
    # 대화형 메시지 형식으로 업데이트
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()