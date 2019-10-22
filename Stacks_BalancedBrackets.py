def isBalanced(s):
    stack = []
    match = True
    quest = list(s)
    dic = {'(':')', '[':']', '{':'}'}
    result = {True:'YES', False:'NO'}
    while quest != [] and match:
        qp = quest.pop()
        if qp in (')', ']', '}'):
            stack.append(qp)
        elif stack != []:
            match = (stack.pop() == dic[qp])
        else:
            match = False
    return result[match and (stack == [])]