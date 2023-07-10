from datetime import datetime
import requests
import meme as m
import api
import bs4_pic


def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi"):
        return "hey! how's it going?"
    if user_message in ("who are you", "who are you ?"):
        return "I am a bot"
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/ %y ,%H:%M:%S")
        return str(date_time)
    if user_message in ("how are you", "how are you?"):
        return "Great, thank you"
    if user_message in ("help", "helps"):
        return "if you need help! dm +66 9 8264 1974"
    if user_message in ("meme", "memes"):
        return m.get_meme()
    if user_message in ("joke", "dadjoke", "dad joke"):
        return api.dad_joke()
    if user_message in ("fact", "facts"):
        return api.fact()
    if user_message in ("morning"):
        return api.morning()
    if user_message in ("pic", "pics", "picture", "porn", "nude", "naked"):
        return bs4_pic.get_pic()
    return "sorry, i dont understand"
