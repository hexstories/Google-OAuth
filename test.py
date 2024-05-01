import requests

URL:str = "https://bible-api.com/?random=verse"
ARK_URL:str = "https://sms.arkesel.com/api/v2/sms/send"

def get_bible_verse():
    respnse = requests.get(URL)
    message = f"\t \033[1mBible Verse Of the Day!\033[0m \n \tTitle: {respnse.json()['reference']} \n \tText: {respnse.json()['text']}"
    return message

def send_text_message(message:str,recipients:list):
    headers = {
    "api-key": "cE9QRUkdjsjdfjkdsj9kdiieieififiw=",
    "Content-Type": "application/json"  
    }


    sms_payload = {
    "sender": "Hello world",
    "message": message,
    "recipients": recipients    
    }

    try:
        response = requests.post(ARK_URL, headers=headers, json=sms_payload)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(str(err))
if __name__ == "__main__":
    message = get_bible_verse()
    send_text_message(message=message,recipients=[])