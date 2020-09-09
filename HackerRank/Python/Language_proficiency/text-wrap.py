import textwrap

def wrap(string, max_width):
    # r = ""
    # for i in range(0, len(string), max_width):
    #     r += string[i:i+max_width] + '\n'
    # return r
    return "\n".join((textwrap.TextWrapper(max_width)).wrap(string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)