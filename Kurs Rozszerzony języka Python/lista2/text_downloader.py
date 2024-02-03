import requests

# prosty parser HTML -> zwykly tekst
# dobry do stron z Wikipedii

def get_paragraphs(html):
    text = ''
    is_text = False
    for i in range(3, len(html)):
        ch1 = html[i - 3]
        ch2 = html[i - 2]
        ch3 = html[i - 1]
        ch4 = html[i]
        if is_text:
            text += ch4
        if ch2 == '<' and ch3 == 'p' and ch4 == '>':
            is_text = True
        if ch1 == '<' and ch2 == '/' and ch3 == 'p' and ch4 == '>':
            is_text = False
            text = text[:-4]
    return text

def remove_tags(html):
    TAGS = ['a', 'sup', 'span', 'code', 'i']
    text = ''
    is_text = True
    for i in range(len(html)):
        ch = html[i]
        if ch == '<':
            is_text = False
        if ch == '>':
            is_text = True
        elif is_text:
            text += ch
    return text

def parse_html(html):
    return remove_tags(get_paragraphs(html))

def download_text(url):
    response = requests.get(url)

    if response.status_code == 200:
        return parse_html(response.text)
    else:
        print("Nie udało się pobrać zawartości strony.")