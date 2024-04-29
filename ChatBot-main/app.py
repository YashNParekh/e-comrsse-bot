from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from find_and import GPT 


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

from result_genrator import ask_and_get_info




last_conver_over = True



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    last_conver_over = False
    msg = request.form["msg"]
    input = msg
    
    msg_send = GPT(input)
    # msg_send = ask_and_get_info(input)
    # last_conver_over = True

    
    return str(msg_send)
    
    





if __name__ == '__main__':
    app.run()
