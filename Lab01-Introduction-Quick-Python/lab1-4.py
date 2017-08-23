def get_pattem(chars):
    size = len(chars)
    for i in range(-size +1, size):
        print('.'.join(chars[-1:abs(i):-1] + chars[abs(i):]).center(4*size -3, '.'))

get_pattem("WXYZ") 
