def has_cycle(head):
    seen = {}
    seen[head.data] = True
    now = head
    while now.data not in seen and now.next:
        now = now.next
    if not now.next:
        return 0
    else:
        return 1