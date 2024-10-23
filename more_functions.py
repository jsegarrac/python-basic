def freq1(string):

    words = []
    words = string.split()
    print (words)
    Dict = {}

    for key in words:
        Dict[key] = words.count(key)

    print("Frecuencia de palabrases:", Dict)

def freq2(string, passedkey):

    words = []
    words = string.split()
    print (words)
    Dict = {}

    for key in words:
        if (key == passedkey):
            Dict[key] = words.count(key)
            
    print("Frecuencia de passed:", Dict)


freq1("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


freq2("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")