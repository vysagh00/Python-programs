import requests

url = "https://currencyapi.net/api/v1/rates?key=AZcoollxIoPSPU9G5GeS6rs0tf9odRYRATKw"
response = requests.get(url)
# print(response)

data = response.json()
print(response)

for x in data.keys():
    if x == "rates":
        currency_data = data['rates']
        for d in currency_data.keys():
            if d == 'INR':
                # print("{} : {}".format(d, currency_data[d]))

                inr = currency_data[d]
                break

user_input = int(input("enter the dollars: "))
k = user_input*inr
print("The dollars when converted in indian rupees will be equal to: {}".format(K))