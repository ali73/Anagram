from database import get_word




def get_anagram(word):
    word = list(word)
    result = get_word(''.join(sorted(list(word)))).all()
    for ouput in result:
        print(ouput.word)


word = input("کلمه‌ی مورد نظر را وارد کنید:")
