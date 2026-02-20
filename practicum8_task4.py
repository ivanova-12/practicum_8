text = input()

if len(text) >= 3:
    for symbol in text:
        if text.count(symbol) == 3:
            print(symbol)
            break





