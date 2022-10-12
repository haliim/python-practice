def mutate_string(string, position, character):
    list_string = list(string)
    list_string(position) = character
    string = ''.join(list_string)
    print(string)
    return

if __name__ == '__main__':
    s = input("please write custome string")
    i, c = input("choose character number").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)