from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
#
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
# chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

chatterbot = ChatBot(**settings.CHATTERBOT)
def chat(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        # bot_response = chatbot(user_message)[0]['generated_text']
        bot_response = chatterbot.get_response(user_message)
        return JsonResponse({'bot_response': str(bot_response)})
    return render(request, "chatbot/chat.html")