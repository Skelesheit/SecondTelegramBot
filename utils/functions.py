def split_message(text, max_length=4096):
    parts = []
    while len(text) > max_length:
        parts.append(text[:max_length])
        text = text[max_length:]
    parts.append(text)
    return parts