def decodeHuff(root, s):
    cur = root
    dec = ''
    for i in s:
        if i == '1':
            cur = cur.right
        else:
            cur = cur.left
        if (cur.left == None) and (cur.right == None):
            dec += cur.data
            cur = root
    print(dec)