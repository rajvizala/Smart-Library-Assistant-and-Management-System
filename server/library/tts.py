
import random


class Reply():
    INTENT_NOT_FOUND = [
        "Sorry didn't understood what you have said",
        "I am sorry, can you repeat your request?",
        "Sorry, I didn't understand what you said.",
        "I'm not sure I follow, could you explain that another way?"

    ]
    SLOTS_NOT_FOUND = [
        "Sorry, unable to recognise the {slot_name}",
        "Sorry, I didn't quite catch the {slot_name} you mentioned.",
        "I'm sorry, I didn't recognize the {slot_name} you provided.",
        "I'm having trouble understanding the {slot_name} you mentioned. Can you please speak them more clearly?",
    ]
    BOOK_FOUND = [
        "You can Find {book_name} at shelf {shelf} {section}",
        "Your Book {book_name} is at shelf {shelf} {section}",
        "The book {book_name} is located on shelf {shelf}, section {section}.",
        "Shelf {shelf}, section {section} holds the book {book_name}."
    ]
    BOOK_NOT_AVAILABLE = [
        "I'm sorry, but {book_name} is currently unavailable in the library.",
        "Sorry Your Requested Book {book_name} is not currently available",
        "Unfortunately, {book_name} is not currently in our collection.",
        "Sorry, but {book_name} is not in the library's collection right now.",
        "I regret to inform you that {book_name} is not currently accessible in the library."
    ]
    BOOK_NOT_FOUND = [
        "We Don't Have {book_name} in our Library",
        "I'm sorry, but we could not find {book_name} in the library.",
        "We searched our database, but we could not find {book_name}.",
        "The book you're looking for, {book_name}, is not present in our library's collection "
    ]
    FOUND_BOOK_BY_AUTHOR = [
        "Here are some books related to author {author_name}",
        "I found some books by {author_name}.",
        "I have a list of books written by {author_name}.",
    ]
    NOT_FOUND_BOOk_BY_AUTHOR = [
        "Sorry no books found related to author {author_name}"
    ]
    FOUND_BOOK_BY_GENRE = [
        "Here are some Books of {genre} catagory you will like"
    ]
    NOT_FOUND_BOOk_BY_GENRE = [
        "Sorry No books of {genre} catagory found"
    ]
    SUMMARIZE_BOOK = [
        "Book Name {book_name}, Authored By {author_name}, Synopsis {description}"
    ]


class TTS(Reply):

    def resolve(self, resolve, **kwargs):
        sentence = random.choice(getattr(self, resolve))
        return sentence.format(**kwargs)

    def resolve_and_say(self, resolve, **kwargs):
        self.speak(self.resolve(resolve, **kwargs))