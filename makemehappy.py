import PIL
from PIL import Image
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "98bbbc50-6a6a-11eb-af95-9dddbf0595b865341999-8a4e-40c4-ba6f-1c8a82dc1e47"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

stuff = input("What do you want to tell me ? : ")
recognized = classify(stuff)
label = recognized["class_name"]

if label == "Kind_Things":
  print("You're so nice!")
  url = "https://st.depositphotos.com/1001911/1222/v/950/depositphotos_12221489-stock-illustration-big-smile-emoticon.jpg"
  img = Image.open(requests.get(url,stream = True).raw)
  img.show()
else:
  print("You're so mean !")
  url = "http://www.mccrystalopticians.com/wp-content/uploads/2020/03/8-82835_sad-face-emoji-png-sad-face-emoji-transparent.png"
  img = Image.open(requests.get(url,stream = True).raw)
  img.show()