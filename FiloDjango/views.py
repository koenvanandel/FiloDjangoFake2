from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ai_utils import ask_philosopher
from django.http import JsonResponse
from .forms import QuestionForm
from users.models import Conversation


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'oldsignup.html')

def password_reset(request):
    return render(request, 'password_reset.html')

def signin(request):
    return render(request, 'signin.html')

@login_required(login_url='login')
def chatting(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            philosopher = form.cleaned_data['philosopher']
            answer = ask_philosopher(question, philosopher)
            return JsonResponse({'answer': answer})
    else:
        form = QuestionForm()
    return render(request, 'chatting.html', {'form': form})

def saved_conversations(request):
    if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        conversation_data = request.POST.get('conversation_data')
        # Process and save conversation_data to your database
        # Example:
        # Conversation.objects.create(data=conversation_data)
        return JsonResponse({'message': 'Conversation saved successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)
