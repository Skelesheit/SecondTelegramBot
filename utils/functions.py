def split_message(text, max_length=4096):
    parts = []
    while len(text) > max_length:
        parts.append(text[:max_length])
        text = text[max_length:]
    parts.append(text)
    return parts

def make_grid(n, lst):
    return [lst[start:start+n] for start in range(0, len(lst), n)]
