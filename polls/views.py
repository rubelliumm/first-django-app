from django.shortcuts import redirect, render
from .forms import createPollForm
from .models import Poll

def index(request):
    return render(request,'polls/index.html')

def polls(request):
    polls = Poll.objects.all()
    return render(request,'polls/polls.html',{'polls': polls})

def create(request):
    form = createPollForm()
    if request.method == "POST":
        form = createPollForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('polls')
    return render(request,'polls/create.html' , {'form': form})
def vote(request,pk):
    poll = Poll.objects.get(pk = pk)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count = poll.option_one_count + 1
            poll.save()
        elif selected_option == 'option2':
            poll.option_two_count = poll.option_two_count + 1
            poll.save()
        elif selected_option == 'option3':
            poll.option_three_count = poll.option_three_count + 1
            poll.save()
        else:
            pass
        return redirect('polls')
    return render(request,'polls/vote.html',{'poll': poll })

def results(request,pk):
    poll = Poll.objects.get(pk = pk )
    return render(request,'polls/results.html',{'poll': poll})

