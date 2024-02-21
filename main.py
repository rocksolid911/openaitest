# This is a sample Python script.
from data.first_page import input_data
from intent import predict_intent


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import pandas as pd
# import openai
# import transformers
# import plotly.express as px
# import matplotlib.pyplot as plt
# import sklearn
# import torch
# import torchvision
# import scipy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Classify input data
# Example usage
user_command = "show main screen"
predicted_intent = predict_intent(user_command)
print(f"Predicted Intent: {predicted_intent}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
