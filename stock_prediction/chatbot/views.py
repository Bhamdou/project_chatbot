# from django.shortcuts import render
# from .chatbot import chatbot_response

# def chatbot_view(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = chatbot_response(message)
#         return render(request, 'chatbot.html', {'response': response})
#     return render(request, 'chatbot.html')


from django.shortcuts import render
from .chatbot import chatbot_response
from .forms import ChatbotForm

def chatbot_view(request):
    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            response = chatbot_response(message)
            return render(request, 'chatbot.html', {'form': form, 'response': response})
    else:
        form = ChatbotForm()
    return render(request, 'chatbot.html', {'form': form})
