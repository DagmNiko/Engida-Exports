from openai import OpenAI
from .API_KEY import key
client = OpenAI(api_key=key())


# assistant = client.beta.assistants.retrieve(assistant_id='asst_bfiYsMKXt9X5O1Mx9YzfhkgO')


# thread = 'thread_ddRan35kEmJQ5EJNVaxPwSpI'

assistant = client.beta.assistants.retrieve(assistant_id='asst_gSjc3AZ94ZOWzsEIlrQ11biU')

# runs = client.beta.threads.runs.list(thread_id=thread)
# retrieve = client.beta.threads.runs
# print(f'messages: \n    {messages}\n\nruns:\n\n    {runs}')



threads = ['thread_ddRan35kEmJQ5EJNVaxPwSpI']

def new_thread():
    new_th = client.beta.threads.create()
    print(f'new thread created: {new_th.id}')
    return new_th

def new_message(thread_id, msg):
    new_msg = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=msg
    )
    return new_msg

def new_runs(thread_id, additional="when you retrieve data from files, you must read the specified Excel file into a Pandas DataFrame using python and panda's library"):
    new_run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id,
        additional_instructions=additional
    )

    return new_run

import asyncio

def get_message(thread_id):

    if messages[0].content != []:
        message = messages[0]
        if message.role == 'assistant':
            print(f'{message.role}: {message.content[0].text.value}')
        else:
            print(message.content[0].text.value)
        return message
    else:
        return None
import time
def main():
    thread1 = new_thread()
    while True:
        user_input = input('user: ')
        if user_input != '' and user_input != 'exit':
            msg = new_message(thread1.id, user_input)
            run = new_runs(thread1.id)
            message = client.beta.threads.messages.list(thread1.id).data[0]
            while True:
                print('...', end=' ')
                time.sleep(3)
                message = client.beta.threads.messages.list(thread1.id).data[0]
                if message.role == 'assistant' and len(message.content) > 0:
                    break
            print(f'{message.role}: {message.content[0].text.value}')
            # print(message)

        elif user_input == 'exit':
            print("Good Bye! Rate our AI assistant and we hope to see you again.😊")
            break
        elif user_input == '':
            print('It looks like you sent an empty message accidentally! Please write some message...')