import random
import math

def get_insanity(n, max_n, rise_power=15.0, fall_power=15.0):
    t = n / max(1, max_n - 1)  # 0..1
    if t <= 0.5:
        u = t / 0.5
        return u ** rise_power      # slow then sharp rise
    else:
        u = (t - 0.5) / 0.5
        return (1 - u) ** fall_power  # quick drop


def get_text(insanity):
    text = "All work and no play makes Jack a dull boy"
    out_text = text
    for char in text:
        if random.random() < (0.3*insanity):
            out_text = out_text.replace(char, char.upper(), 1)
    text = out_text
    for char in text:
        if random.random() < (0.3*insanity):
            out_text = out_text.replace(char, char + char, 1)
    text = out_text
    for char in text:
        if random.random() < (0.1*insanity):
            special_chars = "!@#%&*;:,?   "
            rand_char = random.choice(special_chars)
            out_text = out_text.replace(char, rand_char, 1)
    text = out_text
    if insanity > 0.5:
        for char in text:
            if random.random() < (0.5*insanity):
                zalgo_chars = (
                    "\u0300\u0301\u0302\u0303\u0304\u0305\u0306\u0307\u0308\u0309"
                    "\u030A\u030B\u030C\u030D\u030E\u030F\u0310\u0311\u0312\u0313"
                    "\u0314\u0315\u0316\u0317\u0318\u0319\u031A\u031B\u031C\u031D"
                    "\u031E\u031F\u0320\u0321\u0322\u0323\u0324\u0325\u0326\u0327"
                    "\u0328\u0329\u032A\u032B\u032C\u032D\u032E\u032F\u0330\u0331"
                    "\u0332\u0333\u0334\u0335\u0336\u0337\u0338\u0339\u033A\u033B"
                    "\u033C\u033D\u033E\u033F\u0340\u0341\u0342\u0343\u0344\u0345"
                    "\u0346\u0347\u0348\u0349\u034A\u034B\u034C\u034D\u034E\u034F"
                    "\u0350\u0351\u0352\u0353\u0354\u0355\u0356\u0357\u0358\u0359"
                    "\u035A\u035B\u035C\u035D\u035E\u035F\u0360\u0361\u0362\u0363"
                    "\u0364\u0365\u0366\u0367\u0368\u0369\u036A\u036B\u036C\u036D"
                    "\u036E\u036F"
                )
                rand_char = random.choice(zalgo_chars)
                out_text = out_text.replace(char, char + rand_char, 1)
    text = out_text
    for char in text:
        if random.random() < (0.01*insanity):
            out_text = out_text.replace(char, "\n", 1)
    text = out_text

    text = text + "."
    if random.random() > insanity:
        text = text + "\n"
    return text


num_lines = 100000
with open("data.txt", "w", encoding="utf-8") as file:
    for n in range(num_lines):
        file.write(get_text(get_insanity(n, num_lines)))
        if n == 45970:
            file.write("My name is Jack Torrance, I am the caretaker of the Overlook Hotel in the Colorado Rockies.")
        if n == 48010:
            file.write("I killed my wife Wendy.")
        if n == 50230:
            file.write("And I also got Danny.")
        if n == 51030:
            file.write("I used my axe and hid it behind the house in a hole I dug next to the cabin.")
        if n == 52500:
            file.write("I escaped to my secret vacation home in Timberline Lodge in Oregon.")