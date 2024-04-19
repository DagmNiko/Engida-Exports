from django.shortcuts import render
from django.http import JsonResponse
from .assistant import new_message, new_runs, new_thread
from openai import OpenAI
import time
from .API_KEY import key
client = OpenAI(api_key=key())
assistant = client.beta.assistants.retrieve(
    assistant_id="asst_gSjc3AZ94ZOWzsEIlrQ11biU"
)



def process_data(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        threadId = request.POST.get('threadId')
        print(input_data)
        print(threadId)
        # Process the data as needed
        msg = new_message(threadId, input_data)
        run = new_runs(threadId)

        
        message = client.beta.threads.messages.list(threadId).data[0]
        while True:
            print("...", end=" ")
            time.sleep(3)
            message = client.beta.threads.messages.list(threadId).data[0]
            if message.role == "assistant" and len(message.content) > 0:
                print("nope")
                response_data = {'result': f"{message.role}: {message.content[0].text.value}"}
                return JsonResponse(response_data)
    # Return a default response in case the condition in the while loop is not met
    response_data = {'result': "no buddy! it did not work"}
    return JsonResponse(response_data)





# Create your views here.
def home(request):
    return render(request, "Home.html", {})


def shop(request):
    return render(request, "shop.html", {})


# def shop(request):
#     return render(request, "pages/shop.html", {})
def contact(request):
    return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})


def test(request):
    thread1 = new_thread()
    thread = thread1.id
    return render(request, "test.html", {
        'thread': thread
    })
