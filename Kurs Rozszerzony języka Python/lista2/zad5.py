from text_downloader import download_text

def compress(text):
    compressed_text = []
    count = 1
    for i in range(len(text) - 1):
        ch = text[i]
        next = text[i + 1]
        if ch == next:
            count += 1
        else:
            compressed_text.append((count, ch))
            count = 1
    
    compressed_text.append((count, next))

    return compressed_text

def decompress(compressed_text):
    text = ''
    for pair in compressed_text:
        for _ in range(pair[0]):
            text += pair[1]
    return text

url = 'https://pl.wikipedia.org/wiki/Python'
print(decompress(compress(download_text(url))))
