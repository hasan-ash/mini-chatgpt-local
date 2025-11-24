import random

responses = {
    "selam": ["Selam!", "Merhaba!", "Naber?"],
    "nasılsın": ["İyiyim, sen?", "Harikayım!", "Bomba gibiyim!"],
    "ne yapıyorsun": ["Sana yardım ediyorum 😎", "Takılıyorum işte"],
}

print("Mini ChatGPT — çıkmak için 'exit' yaz.\n")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        break

    found = False
    for key in responses:
        if key in msg:
            print("AI:", random.choice(responses[key]), "\n")
            found = True
            break

    if not found:
        print("AI: Bunu tam anlamadım ama gelişiyorum! 😅\n")
