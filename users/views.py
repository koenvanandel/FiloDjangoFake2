from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('chatting')
            else:
                # Display error message for invalid credentials
                messages.error(request, 'Invalid email or password. Please try again.')
        else:
            # Display error message for form errors
            messages.error(request, 'Your email or password was incorrect, please correct the errors above.')
    else:
        form = CustomAuthenticationForm()

    context = {'loginform': form}
    return render(request, 'users/login.html', context=context)

def chatting(request):
    if request.method == 'POST':
        philosopher = request.POST.get('philosopher')
        question = request.POST.get('question')
        # Code to get philosopher's response

        # Save conversation to the database
        conversation = Conversation.objects.create(
            philosopher=philosopher,
            user_message=question,
            philosopher_response=philosopher_response
        )
        conversation.save()

        # Return JSON response or redirect to another page
        return JsonResponse({'status': 'success', 'answer': philosopher_response})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
@login_required(login_url='login')
def conversations(request):
    return render(request, 'conversations.html', {'conversations': conversations})