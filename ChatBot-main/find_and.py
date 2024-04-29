import subprocess
from time import sleep
import g4f
import re
import pickle
from train_bot import messages
from result_genrator import ask_and_get_info





Product_list = ["product_id","product_name","product_discount","product_actual_price","product_brand","ram_size","maximum_ram","storage","maximum_storage","keyboard_details","battery_details","display_details","processor_details","gpu_details","image_url"]




# messages = []

# Initialize an empty list to store conversation history
messages_history = []


def save_message(role, content):
    messages_history.append({"role": role, "content": content})
    with open("conversation_history.pkl", "wb") as file:
        pickle.dump(messages_history, file)


def get_previous_sessions():
    try:
        with open("conversation_history.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def clear_previous_sessions():
    messages_history.clear()
    with open("conversation_history.pkl", "wb") as file:
        pickle.dump(messages_history, file)



def GPT(*args):
    global messages_history
    assert args != ()

    message = ""
    for i in args:
        message += i

    messages.append({"role": "user", "content": message})

    save_message("user", message)
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="gpt-4-turbo",
        # provider=g4f.Provider.FlowGpt,
        # model=g4f.models.mixtral_8x7b,
        messages=messages,
        # stream=True,
    )

    # ms = response.choices[0].message.content
    ms=''
    for i in response:
        ms+=  i
    messages.append({'role':'assistent','content': ms})

    save_message("assistant", ms)
    return ms




def find_code(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    
    
    if matches:
        code = matches[0].strip()
        return code
    else:
        # print("no code found for")
        return ""


def codePy(Query):
    response = GPT(Query)
    python_code = find_code(response)
    # print("`--------------------------------------------------------`")
    # print(python_code)
    # print(module_name)
    # print("`--------------------------------------------------------`")
    if python_code != "":
        if False : 
            # print(response)
            print("`--------------------------------------------------------`")
            print(python_code)
            print("`--------------------------------------------------------`")
        else:
            try:
                exec(python_code)
                response = response[: response.index("`")]
                print(response)
                return response
            except ModuleNotFoundError:
                exec(python_code)
                response = response[: response.index("`")]
                print(response)
                # speakBot(response)
                return response
            except Exception as e:
                response = e
                # print(response)
            sleep(4)
    else:
        return(response)

# print(codePy("how me some laptop with discount of more than 10%"))

# def codePy(Query):
#     response = GPT(Query)
#     return (response)
