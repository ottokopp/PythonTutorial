"""
Das ist der absolute Code-Bewerbungsgespräch Klassiker:
1. Printe wieder alle Zahlen von 1 bis 100, aber mit folgenden Konditionen:
    # wenn die Zahl durch 3 teilbar ist, dann printe statt der Zahl das Wort "Fizz"
    # Wenn die Zahl durch 5 teilbar ist, dann printe statt der Zahl das Wort "Buzz"
    # Wenn die Zahl durch 3 und 5 teilbar ist, dann printe statt der Zahl das Wort "FizzBuzz"
    # Benutze hierfür if-statements und den Modulo-Operator.
    # (z.B. '15 % 5 == 0' gibt True zurück, '15 % 4 == 0' gibt False zurück)
    # (Modulo ist Mathescheiß, das musst du nicht so genau wissen wenn du nicht willst. Modulo gibt dir einfach den Rest einer Division zurück.
    # wenn der Rest 0 ist, ist die Zahl teilbar.)
"""




"""print("Stimmt es, dass 15 durch 5 teilbar ist?:", 15 % 5 == 0)
    print("Stimmt es, dass 15 durch 4 teilbar ist?:", 15 % 4 == 0)
    print("Stimmt es, dass 15 durch 3 UND 5 teilbar ist?:", (15 % 3 == 0 and 15 % 5 == 0))
    print("Stimmt es, dass 15 durch 4 UND 5 teilbar ist?:", (15 % 4 == 0 and 15 % 5 == 0))'
"""
    # Beispiel Ende

    # TODO: Ab hier kommt dein Code.

def fizz_buzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"FizzBuzz")
        elif i % 3 == 0:
            print(i,"Fizz")
        elif i % 5 == 0:
            print(i,"Buzz")
        else:
            print(i)


fizz_buzz()