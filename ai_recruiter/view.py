from django.views.generic import TemplateView
from django.http import JsonResponse
from ai_recruiter.settings import model

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
