from django.views.generic import TemplateView
import google.generativeai as genai
from django.http import JsonResponse
from django.shortcuts import render




# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings)

convo = model.start_chat(history=[])


class AiRecruiterView(TemplateView):
    template_name = 'main.html'


def mensagem_request(request):

    if request.GET:
        data = {
            'mensagem': None,
        }
        convo.send_message(request.GET.get('mensagem'))
        data['mensagem'] = convo.last.text
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'mensagem': ''}, status=404)
