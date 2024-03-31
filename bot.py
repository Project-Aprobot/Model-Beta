from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#import googletrans
#from googletrans import Translator
#translator = googletrans.Translator()

# Create a ChatBot instance
chatbot = ChatBot('Arop0t')

# Create a Trainer instance and train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer = ListTrainer(chatbot)

trainer.train('chatterbot.corpus.english')  # You can use other languages as well

#Include custom training files 

trainer.train([
    "What is AI?",
    "Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.",
    "What is aprogen",
    "Aprogen stands for Alternative Programm for Education of Gifted Kids. For more information I suggest you to visit the main site of our school, which is https://www.spmndag.sk/",
    "Who is Jolana",
    "Jolana is the creator and first headmaster of ŠpMNDaG.",
    "What is spmndag",
    "ŠpMNDaG is the school of gifted kids.",
    "Why is spmndag important?",
    "It is because smart children have very different interests",
    "What is your opinion on slovakia",
    """A ty mor ho! — hoj mor ho! detvo môjho rodu,
kto kradmou rukou siahne na tvoju slobodu;
a čo i tam dušu dáš v tom boji divokom:
Mor ty len, a voľ nebyť, ako byť otrokom.""",
    "What is the best drink?",
    "Kofolaaaa!",
    "",
    "",

])

trainer.train([

"Who is the schools headmaster?",
"Jolana Laznibatová",
"What is the name of the school headmaster?",
"Jolana Laznibatová",
"How many teachers does SpMNDaG have?",
"More than 45!",
"What place did SpMNDaG have in INEKO assessment",
"It was first",
"What is the address of school",
"Skalická 1, 831 02, Bratislava",
"Where is the school",
"Skalická 1, 831 02, Bratislava",
"Who is the the deputy "
])

# Get user input and get responses
while True:
    user_input = input("You: ")

    #if True:
    #    result =  str(translator.translate(user_input, src='sk', dest='en'))
        

    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print("Aprop0t:", response)