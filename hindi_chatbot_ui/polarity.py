def polarity(words):
    import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
    sys.path.insert(1, r"C:\Users\kamra\Documents\AIIT\chatbot_reprise")
    import chad

    polarity = chad.total_polarity(words)

    return polarity

