from chatterbot import ChatBot  # chatterbot is lib and chatbot is class
from chatterbot.trainers import ListTrainer
from tkinter import *


#import logging logger = logging.getLogger() logger.setLevel(logging.CRITICAL)



bot = ChatBot("My Bot")  # bot is object of class chatbot
convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Durgesh',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english'

]
trainer = ListTrainer(bot)
# training the bot with help of trainer
trainer.train(convo)
# answer=bot.get_response('what is your name?')
# print(answer)
# print("Talk to bot")
# while True:#infinte loop
#    query=input()
#   if query=='exit':#unless we write exit
#       break
#   answer=bot.get_response(query)
#  print('bot: ',answer)
main = Tk()  # object created of tk class
main.geometry("500x650")
main.title("My Chat Bot")
img = PhotoImage(file="bot1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    ans_from_bot = bot.get_response(query)
    msgs.insert(END, "you: " + query)
   # print(type(ans_from_bot))
    msgs.insert(END, "bot: " + str(ans_from_bot))
    textF.delete(0,END)


frame = Frame(main)
# main window given
bar = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)
bar.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# create text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot())
btn.pack()

main.mainloop()
