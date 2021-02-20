# you need requests library install first.
# use this command: pip3 install requests
import requests

endpoint = input("Enter your endpoint: ")

datas = {}
dataLenMax = False

while not datalenmax:
	datas[input("Enter datas 'key': ")] = input("enter datas 'value': ")
	if str(input("are you have another datas? (N/Y): ")).lower() == "n":
		datalenmax = True


response = requests.post(endpoint, data=datas)
print(response)