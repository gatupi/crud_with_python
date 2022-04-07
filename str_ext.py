

def substr(value: str, start: int, length: int = None):
    length = len(value) if length == None else length
    if start < 0 or length < 0:
        return None   
    end = start + length - 1
    substring = ''
    count = start
    while count < len(value) and count <= end:
        substring += value[count]
        count += 1
    return substring