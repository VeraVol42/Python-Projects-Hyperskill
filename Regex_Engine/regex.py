import sys
sys.setrecursionlimit(10000)


def match_char(regex, string):

    if not regex or not string and regex == "$":
        return True

    if regex[0] == '\\':
        regex = regex[1:]
        
    if regex and not string:
        return False

        
    elif len(regex) > 1 and regex[1] == "?":
        return match_char(regex.replace("?", ""), string) or match_char(regex[2:], string)
    elif len(regex) > 1 and regex[1] == "*":
        return match_char(regex[2:], string) or match_char(regex, string[1:])
    elif len(regex) > 1 and regex[1] == "+":
        return match_char(regex, string[1:]) or match_char(regex.replace("+", ""), string)
    elif regex[0] == string[0] or regex[0] == ".":
        return match_char(regex[1:], string[1:])
    return False
        
def match(regex, string):
    if match_char(regex, string):
        return True
    elif regex and regex[0] == "^":
        return match_char(regex[1:], string)
    elif string:
        return match(regex, string[1:])
    return False

print(match(*input().split('|')))