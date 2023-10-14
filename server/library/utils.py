from .nlu import NLUEngine, Status
from .tts import TTS
from pprint import PrettyPrinter

speech = TTS()
printer = PrettyPrinter()
engine = NLUEngine()


def get_input():  # will change
    return input("Enter your Query: ")


def query_intent_not_found():
    return speech.resolve('INTENT_NOT_FOUND')


def query_slot_not_found(slot_name):
    return speech.resolve('SLOTS_NOT_FOUND', slot_name=slot_name)


def query_search_book(data: dict):
    if data['result']:
        print("DATA",data['result'])
        if data['result'][0]['copies']:
            print("BOOK FOUNDD.....")
            return speech.resolve(
                'BOOK_FOUND',
                book_name=data['result'][0]['title'],
                shelf=data['result'][0]['location'],
                section= None
            )
        else:
            print("BOKK NOT FOUND..")
            return speech.resolve(
                'BOOK_NOT_AVAILABLE',
                book_name=data['result'][0]['title'],
            )
    else:
        print("BOKK NOT FOUND..")
        return speech.resolve(
            'BOOK_NOT_FOUND',
            book_name=data['value']
        )


def query_summarize_book(data):
    if data['result']:
        return speech.resolve(
            'SUMMARIZE_BOOK',
            book_name=data['result']['title'],
            author_name=data['result']['author'],
            description=data['result']['description'],
        )
    else:
        return query_search_book(data)


def query_search_by_author(data: dict):
    if data['result']:
        return speech.resolve(
            'FOUND_BOOK_BY_AUTHOR',
            author_name=data['value']
        )

    else:
        return speech.resolve(
            'NOT_FOUND_BOOk_BY_AUTHOR',
            author_name=data['value'],
        )


def query_search_by_genre(data: dict):
    if data['result']:
        return speech.resolve(
            'FOUND_BOOK_BY_GENRE',
            genre=data['value']
        )

    else:
        return speech.resolve(
            'NOT_FOUND_BOOk_BY_GENRE',
            genre=data['value'],
        )


def query_successfull(data: dict):
    if data['intent'] == 'searchBook':
        return query_search_book(data)

    elif data['intent'] == 'summarizeBook':
        return query_summarize_book(data)

    elif data['intent'] == 'searchByAuthor':
        return query_search_by_author(data)

    elif data['intent'] == 'searchByGenre':
        return query_search_by_genre(data)