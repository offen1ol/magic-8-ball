import random

def answer(num):
    responses = {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Yes, definitely",
        5: "You may rely on it",
        6: "As I see it, yes",
        7: "Most likely",
        8: "Outlook good",
        9: "Yes",
        10: "Signs point to yes",
        11: "Reply hazy, try again...",
        12: "Ask again later",
        13: "Better not tell you now...",
        14: "Cannot predict now",
        15: "Concentrate and ask again",
        16: "Don't count on it",
        17: "My reply is no",
        18: "My sources say no",
        19: "Outlook not so good",
        20: "Very doubtful"
    }
        
    print("Thinking...")
    print(responses[num])

def main():
    ask = str(input("What would you like to know?\n")).lower()

    while ask != "quit":
        answer(random.randrange(1,20))

        ask = str(input("What else would you like to know?\n")).lower()
    

if __name__ == '__main__':
    main()