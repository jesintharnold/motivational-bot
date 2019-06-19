import bot_sarah
import requests
import json
import time
bot=bot_sarah.sarah_jesinth()
update_id=None
#functions for calling on below if-else statements
def send_msg():
    message="Hi,what a lovely day"
    return message
def send_msg1():
    message="sorry, I can't able to respond to the curent text I am still a prototype by jesintharnold "
    return message
def quote_update():
        r = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
        read = json.loads(r.content)
        read_quote = read["quoteText"]
        write_author = read["quoteAuthor"]
        return "Quote: \n{}\n- by {}".format(read_quote, write_author)

def love_reply():
    time.sleep(3)
    message_love ="Will you marry me ???"
    return message_love

update_id=7072816

while True:
    updates=bot.get_update(offset=update_id)
    updates=updates["result"]
    if updates:
        for items in updates:
            update_id=items["update_id"]
            print(update_id)
            try:
                message=items["message"]["text"]
                print(".......")
                print(message)
                print(".......")
                # type your own reply id
                reply_id = xxxxxxxxxx
                # import your  package for messaging or type your own if-else statements here.
                if message=="motivate me":
                     quote_reply=quote_update()
                     bot.send_message(quote_reply, reply_id)
                elif message=="Motivate me":
                     quote_reply=quote_update()
                     bot.send_message(quote_reply, reply_id)
                elif message=="bomb it up":
                    for i in range(5):
                        print(i)
                        quote_reply=quote_update()
                        bot.send_message(quote_reply, reply_id)
                elif message=="Bomb it up":
                    for i in range(5):
                        print(i)
                        quote_reply=quote_update()
                        bot.send_message(quote_reply, reply_id)
                elif message=="I love you":
                    love_reply=love_reply()
                    bot.send_message(love_reply,reply_id)
                elif message == "hi":
                    msg_reply = send_msg()
                    bot.send_message(msg_reply, reply_id)
                elif message == "hello":
                    msg_reply = send_msg()
                    bot.send_message(msg_reply, reply_id)
                elif message == "Hi":
                    msg_reply = send_msg()
                    bot.send_message(msg_reply, reply_id)
                elif message == "Hello":
                    msg_reply = send_msg()
                    bot.send_message(msg_reply, reply_id)
                else:
                    msg_reply1= send_msg1()
                    bot.send_message(msg_reply1, reply_id)


                last_update_id=update_id

            except:
                print("......")