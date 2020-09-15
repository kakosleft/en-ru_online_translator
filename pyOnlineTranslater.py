from googletrans import Translator
import sqlite3


def check_in_db(word):
    response=db_action(f'SELECT * FROM translate where en=\'{word}\'')
    if type(response) == type(None):
        get_from_google(word)
    elif isinstance(response,tuple):
        print('ofline_mode')
        print(response)
    else:
        print("хз че происходит")

def get_from_google(word_en):
    word_ru=Translator().translate(word_en,src="en",dest="ru").text
    response=db_action(f'INSERT INTO translate VALUES ( \'{word_en}\' , \'{word_ru}\')')
    print('online_mode')
    print(f'(\'{word_en}\' , \'{word_ru}\')')

def db_action(request):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute(request)
    result=c.fetchone()
    conn.commit()
    conn.close()
    return result


mode = input("select mode: \n 1-writing \n 2-reading \n 3-learning \n : ")
if mode=='1':
    print('to exti from writing mode enter \'_stop\'.')
    while True:
        val=input("enter your word\n: ")
        if val=='_stop':
            break
        check_in_db(val)
elif mode=='2':
    db_action('select * from translate')
elif mode=='3':
    pass
    # TODO:
else:
    print("exit")
