def clean(text):
    MARKS = ['.', ',', ':', "'", '-', '.', '!', '?', ' ']
    new = ''
    for ch in text:
        if ch not in MARKS:
            new += ch
    return new.lower()


def is_palindrom(text):
    cleaned_text = clean(text)
    return cleaned_text == cleaned_text[::-1]


text1 = "Eine güldne, gute Tugend: Lüge nie!"
text2 = "Míč omočím."

print(is_palindrom(text1))
print(is_palindrom(text2))
