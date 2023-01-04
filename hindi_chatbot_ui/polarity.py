def polarity(words):
    import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
    sys.path.insert(1, 'E:\Chatbot remastered')
    import chad

    polarity = chad.total_polarity(words)

    return polarity

