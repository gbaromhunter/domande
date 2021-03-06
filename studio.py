import random
import json

# initialize questions and messages
with open("messages.json") as file_messages:
    messages = json.load(file_messages)
with open("domande.json") as file_questions:
    questions = json.load(file_questions)


def dump_questions():
    """ dump all the questions in the question file """
    with open("domande.json", "w") as file_object:
        json.dump(questions, file_object)


def dump_messages():
    """ dump all the messages in the message file """
    with open("messages.json", "w") as messages_file:
        json.dump(messages, messages_file)


def new_question():
    """ asks if user wants a new question and return True if the user typed si, or False if anything else at all. """
    user_wants_new_question = input("Vuoi un'altra domanda? Si o no?: ")
    return user_wants_new_question.lower() == "si"


def add_subject():
    """ adds a new subject which is an empty list to the questions dictionary """
    see_subjects()
    subject = input("Inserisci il nome della materia da aggiungere: ")
    if subject not in questions:
        questions[subject] = []
        dump_questions()
    else:
        print("La materia esiste già.")


def remove_subject():
    """ remove a subject """
    see_subjects()
    subject = input("Inserisci il nome della materia da eliminare: ")
    if subject not in questions:
        print("La materia non esiste. Riprova.")
        remove_subject()
    else:
        del questions[subject]
    dump_questions()


def add_questions():
    """ adds a number of questions to specified subject """
    see_subjects()
    subject = input("Inserisci il nome della materia a cui aggiungere le domande: ")
    if subject not in questions:
        print("La materia non esiste. Riprova.")
        add_questions()
    else:
        n_questions = input("Inserisci il numero di domande da aggiungere: ")
        n_questions = int(n_questions)
        for i in range(n_questions):
            questions[subject].append(input("Inserisci la domanda: "))
            print("La domanda è stata aggiunta!")
        dump_questions()


def remove_last_questions():
    """ remove the last X questions"""
    see_subjects()
    subject = input("Inserisci il nome della materia a cui rimuovere le domande: ")
    if subject not in questions:
        print("La materia non esiste. Riprova.")
        remove_last_questions()
    else:
        n_questions = input("Inserisci il numero di domande da rimuovere: ")
        n_questions = int(n_questions)
        for i in range(n_questions):
            q = questions[subject].pop(-1)
            print(f"Ecco la domanda rimossa: {q}")
        dump_questions()


def add_message():
    """ adds some new messages to display """
    n_messages = input("Inserisci il numero di messaggi da aggiungere: ")
    n_messages = int(n_messages)
    for i in range(n_messages):
        new_message = input("Inserisci un nuovo messaggio d'incoraggiamento: ")
        messages.append(new_message)
        print("Il messaggio è stato aggiunto!")
    dump_messages()


def remove_last_messages():
    """ remove the last X messages"""
    n_messages = input("inserisci il numero di messaggi da rimuovere: ")
    n_messages = int(n_messages)
    for i in range(n_messages):
        m = messages.pop(-1)
        print(f"Ecco il messaggio rimosso: {m}")
    dump_messages()


def see_subjects():
    """ see all the subjects """
    subject_list = [key for key in questions]
    print(f"Ecco la lista delle materie: "
          f"\n{subject_list}")


def see_questions():
    """ see all the questions of a subject"""
    see_subjects()
    subject = input(f"Inserisci la materia di cui vedere le domande: ")
    if subject not in questions:
        print("La materia non esiste. Riprova.")
        see_questions()
    else:
        print(f"Ecco le domande: ")
        for question in questions[subject]:
            print(question)


def see_messages():
    """ sees all the messages"""
    print("Ecco tutti i messaggi: ")
    for message in messages:
        print(message)


def interrogation():
    """ starts the loop of the interrogation, asking if random or linear order, running the loops """
    see_subjects()
    subject = input("Quale materia vuoi ripetere?: ")
    if subject not in questions:
        print("La materia non esiste. Riprova.")
        interrogation()
    else:
        interrogation_type = input(f"Vuoi le domande in ordine sparso oppure ordinato? Digita sparso/ordinato: ").lower()
        while True:
            questions_session = questions[subject][:] if interrogation_type == "ordinato" else random.sample(
                questions[subject],
                len(questions[subject]))
            while True:
                q = questions_session.pop(0)
                print(f"Eccoti la domanda: {q}")
                print(f"{random.choice(messages)}")
                if not new_question() or len(questions_session) == 0:
                    break
            if not input("Le domande sono finite. Vuoi ricominciare?: ").lower() == "si":
                break


option_list = {"1": "Fatti interrogare",
               "2": "Aggiungi una materia",
               "3": "Rimuovi una materia",
               "4": "Guarda le domande",
               "5": "Aggiungi domande",
               "6": "Rimuovi ultime domande",
               "7": "Aggiungi messaggi",
               "8": "Rimuovi messaggi",
               "9": "Vedi tutti i messaggi",
               "0": "Esci"}

func_list = [interrogation,
             add_subject,
             remove_subject,
             see_questions,
             add_questions,
             remove_last_questions,
             add_message,
             remove_last_messages,
             see_messages]


def print_menu():
    print("\n #######################")
    for key in option_list.keys():
        print(key, '--', option_list[key])
    print("####################### \n")


def program():
    while (True):
        print_menu()
        option = int(input('Scegli: '))
        if option == 1:
            func_list[0]()
        elif option == 2:
            func_list[1]()
        elif option == 3:
            func_list[2]()
        elif option == 4:
            func_list[3]()
        elif option == 5:
            func_list[4]()
        elif option == 6:
            func_list[5]()
        elif option == 7:
            func_list[6]()
        elif option == 8:
            func_list[7]()
        elif option == 9:
            func_list[8]()
        elif option == 0:
            print("Grazie per aver ripetuto con me!")
            exit()
        else:
            print('Opzione non riconosciuta!')


program()
