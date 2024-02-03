A   py -m unittest
B   pycodestyle nazwa_pliku.py
C   do wygenerowania dokumentacji używamy modulu sphinx
    
    mkdir docs
    cd docs
    sphinx-quickstart (przeklikujemy opcje)
    cd ..

    do pliky conf.py dopisujemy 

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
    ]

    sphinx-apidoc -o docs .
    cd docs
    ./make html
    w folderze _build/html mamy index.html bedacy nasza dokumentacja

D   mypy nazwa_pliku.py
E   py -m zippapp server
    py -m zippapp client

    Nastepnie mozemy uruchomic plik 
    py nazwa_pliku.pyz
