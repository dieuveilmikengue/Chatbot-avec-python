from nltk.chat.util import Chat,reflections

pairs=[
    ["(.*)Mon nom est (.*)", ["Salut %1"]],
    ["(.*)m'appel (.*)", ["Salut %2"]],
    ["(.*)créer une application(.*)|(.*)creer une application(.*)", ["Une application oui oui"]],
    ["(bonjour|salut|coucou)", ["Salut toi", "Hello", "En quoi je peux vous etes utile ?"]],
    ["Je veux une (.*) de taille (.*)", ["Ok je vais vous preparer une %1 de taille %2"]],
    ["(.*)(ville|adresse)", ["On est à Brazzaville, Talangai"]],
    ["(.*)merci(.*)", ["Je vous en prie, a très bientot"]],
    ["(.*)", ["svp veillez reformuler votre phrase je n'ai pas bien compris"]]
    
]

chat = Chat(pairs, reflections)
chat.converse()