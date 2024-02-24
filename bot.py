from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#import googletrans
#from googletrans import Translator
#translator = googletrans.Translator()

# Create a ChatBot instance
chatbot = ChatBot('Arop0t')

# Create a Trainer instance and train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # You can use other languages as well

# Get user input and get responses
while True:
    user_input = input("You: ")

    #if True:
    #    result =  str(translator.translate(user_input, src='sk', dest='en'))
        

    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)