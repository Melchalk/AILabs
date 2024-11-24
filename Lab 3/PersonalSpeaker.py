import datetime
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr

def talk(words):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.5)
    engine.say(words)
    engine.runAndWait()

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите !")
        talk("Говорите !")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="ru-RU").lower()

        print("Вы сказали: " + task)
        talk("Вы сказали... "+ task)
        r.pause_threshold = 1

    except sr.UnknownValueError:
        talk("Не понимаю Вас!")
        task = get_command()
    return task

def time_to_text():
    dict_hours = {1: 'час', 2: 'часа', 3: 'часа', 4: 'часа', 5: 'часов', 6: 'часов',
              7: 'часов', 8: 'часов', 9: 'часов', 10: 'часов', 11: 'часов', 12: 'часов',
              13: 'часов', 14: 'часов', 15: 'часов', 16: 'часов', 17: 'часов', 18: 'часов',
              19: 'часов', 20: 'часов', 21: 'час', 22: 'часа', 23: 'часа', 0: 'часов'}
    dict_minutes = {
            'минута': [1, 21, 31, 41, 51],
            'минуты': [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54],
            'минут': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29,
                      30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59] }
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    str_time = str(h) + dict_hours[h] + ' ... '
    for minutes in dict_minutes:
        if m in dict_minutes[minutes]:
            str_time += str(m) + ' ' + minutes
            break
    return str_time

def parse_task(task):
    if 'открой почту' in task:
        talk('Хорошо, ОТКРЫВАЮ ПОЧТУ!')
        URL='https://mail.ru'
        webbrowser.open(URL)
    elif ('сколько времени' in task) or ('который час' in task) or ('сколько время' in task)  :
        talk(time_to_text())
    elif 'кто ты' in task:
        talk('Я голосовой помощник! А ты?')
    elif 'стоп' in task:
        talk('Хорошо, заканчиваем разговор... До встречи !')
        sys.exit()

talk('Привет, я голосовой помощник! Давай поговорим!')

while True:
    parse_task(get_command())
    talk("Поговорим еще?")