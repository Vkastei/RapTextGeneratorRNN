import requests
import time 
url = "https://discord.com/api/v9/channels/665303411951927318/typing"

while True:
    
    requests.post(url, headers = {"Authorization" : "OTA2OTQwMjA2Mjc0NDc4MTAw.Glxtlg.ZI2CPMfCHlJ-vM9BSJLj59yinzBNm-pSFYmkVY"})
    time.sleep(1)