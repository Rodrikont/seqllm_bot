from gradio_client import Client
from clients.qwen.dto.qwen_request_dto import QwenRequestDto
from clients.qwen.dto.qwen_response_dto import QwenResponseDto

client = Client("Qwen/Qwen2.5-72B-Instruct")

class QwenClient:
    def ask_question(self, data):
        try:
            result = client.predict(
                query=data + "\nЭто уравнение? Не решай. Ответь 'Да' или 'Нет'",
                history=[],
                system="You are Qwen, created by Alibaba Cloud. You are a helpful assistant.",
                api_name="/model_chat"
            )
            '''req = QwenRequestDto(
                query=data.question,
                history=[],
                system="You are Qwen, created by Alibaba Cloud. You are a helpful assistant.",
                api_name="/model_chat"
            )

            result = client.predict(req.dict())
            '''

            # resp = QwenResponseDto(**result)

            print(f"{data} - {result[-2][0][-1]}") # log

            resp = result[-2][0][-1]
        except Exception as e:
            print(e)
            return f"Ошибка: {e}"

        return resp