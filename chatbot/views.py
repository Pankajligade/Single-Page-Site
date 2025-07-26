from django.shortcuts import render
from .models import ChatMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def chatbot_reply(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name", "User")
        msg = data.get("message", "")

        if "hi" in msg.lower():
            response = "Hello! How can I assist you today?"
        else:
            response = "Thank you! I'll forward your message to Pankaj."

        ChatMessage.objects.create(name=name, message=msg)
        return JsonResponse({"reply": response})
