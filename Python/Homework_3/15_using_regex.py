import re


text = 'Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных'


def my_function(text, multiplier=2):
    changed_text = re.sub('[0-9]+', lambda matchobj: str(int(matchobj.group(0)) * multiplier), text)
    return print(changed_text)


my_function(text, 2)
