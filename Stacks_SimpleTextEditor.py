def editor(history, text, command, context):
    text = history[-1]
    if command == 1:
        text += context
        history.append(text)
    elif command == 2:
        text = text[0:-int(context)]
        history.append(text)
    elif command == 3:
        print(text[int(context)-1])
    else:
        history.pop()
        text = history[-1]


q = int(input())
text = ''
history = ['']
for i in range(q):
    x = input()
    if len(x) == 1:
        command = 4
        context = None
    else:
        command = x.split(' ')[0]
        context = x.split(' ')[1]
    editor(history, text, int(command), context)
