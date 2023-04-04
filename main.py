import nltk
from nltk.chat.util import Chat, reflections

import wikipedia

pairs = [
  ['hi', ['Hello!', 'Hi there!', 'Hey!']],
  ['hello', ['Hi there!', 'Hello!', 'Hey!']],
  [
    'what is your name?',
    ['My name is Chatbot.', 'I am Chatbot.', 'You can call me Chatbot.']
  ],
  [
    'how are you?',
    ['I am fine, thank you.', 'I am doing great!', 'I am good.']
  ],
  [
    'what can you do?',
    ['I can answer questions based on my knowledge. Try asking me something.']
  ], ['quit', ['Bye!', 'Goodbye!', 'Have a nice day!']]
]


def extract_keyword(sentence):
  words = nltk.word_tokenize(sentence)
  tagged = nltk.pos_tag(words)
  keyword = None
  for word, pos in tagged:
    if pos in ['NN', 'NNS']:
      keyword = word
      break
  return keyword


def get_wikipedia_summary(keyword):
  summary = None
  try:
    summary = wikipedia.summary(keyword, sentences=2)
  except:
    pass
    return summary


def chatbot_response(input_text):
  keyword = extract_keyword(input_text)
  if keyword:
    summary = get_wikipedia_summary(keyword)
    if summary:
      return summary
      chatbot = Chat(pairs, reflections)
      response = chatbot.respond(input_text)
  return response


print("Welcome to Chatbot! Ask me something.")
while True:
  user_input = input("You: ")
  response = chatbot_response(user_input)
  print("Chatbot:", response)
  if response in ['Bye!', 'Goodbye!', 'Have a nice day!']:
    break
