import re
import random
from random import randint


def get_response(user_input: str) -> str:
    """
    A rule-based chatbot that responds to specific keywords or patterns.
    """
    user_input = user_input.lower()  # Make input case-insensitive

    if user_input == "":
        return "Well, you're awfully silent..."
    elif re.search(r"oi|olá|hey", user_input):
        greetings = ["oii", "oie", "oi mo"]
        return random.choice(greetings)
    elif re.search(r"how are you", user_input):
        return "I'm doing well, thanks!"
    elif re.search(r"what's your name|who are you", user_input):
        return "I'm a simple Discord bot."
    elif re.search(r"joga o dado", user_input):
        return f"o número é: {randint(1, 6)}"
    elif re.search(r"tchau|até mais|ai tchau", user_input):
        return ["beijo mo", "tchauu", "até depois!"]
    elif re.search(r"quem é carolinna", user_input):
        return "é uma loira básica"
    elif re.search(r"quem é fernanda", user_input):
        return "kkkkkk vou nem responder"
    elif re.search(r"carlos", user_input):
        return "fora carlos"
    elif re.search(r"bate aí", user_input):
        bate_ai = ["vem fazer melhor porra",
                   "pelo menos eu bato pros outros", "a muqi só batem do lado kkkkk"]
        return random.choice(bate_ai)
    elif re.search(r"quem é eduardo dragoneti", user_input):
        return "https://images.tcdn.com.br/img/img_prod/1115696/monster_energy_lata_473ml_6_und_101_1_e71ca80ee20f42aa859e7b25df410734.jpg"
    else:
        return "mor não entendi (falta de programação da muqi)"
