def choose(text):
    objects = []
    current = ""
    for c in range(len(text)):
        append = True
        if c < len(text)-3:
            if text[c] == 'o' and text[c+1] == 'r' and text[c+2] == ' ':
                objects.append(current)
                current = ""
                append = False
            elif text[c] == 'r' and text[c-1] == 'o' and text[c+1] == ' ':
                current = ""
                append = False
        if text[c] == ',' or text[c] == '?':
            objects.append(current)
            current = ""
        else:
            if append:
                current += text[c]
    return [o.lstrip() for o in objects]
