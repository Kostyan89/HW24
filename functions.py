import re
from typing import Iterator

"""
def build_query(it: Iterator, f: str, query: str) -> Iterator:
    query_items = query.split("|")
    res = map(lambda x: x.strip(), f)
    for item in query_items:
        split_item = item.split(":")
        cmd = split_item[0]
        if cmd == "filter":
            arg = split_item[1]
            res = filter(lambda v, txt=arg: txt in v, res)
        if cmd == "map":
            arg = int(split_item[1])
            res = map(lambda v, idx=arg: v.split(" ")[idx], res)
        if cmd == "unique":
            res = set(list(res))
        if cmd == "sort":
            arg = split_item[1]
            if arg == "desc":
                reverse = True
            else:
                reverse = False
            res = sorted(res, reverse=reverse)
        if cmd == "limit":
            arg = int(split_item[1])
            res = list(res)[:arg]
        if cmd == "regex":
            pass
    return res"""


def get_command(it: Iterator, cmd: str, value: str) -> Iterator:
    if cmd == "filter":
        return filter(lambda v: value in v, it )
    if cmd == "map":
        arg = int(value)
        return map(lambda v: v.split(" ")[arg], it)
    if cmd == "unique":
        return iter(set(it))
    if cmd == "sort":
        if value == "desc":
            reverse = True
        else:
            reverse = False
        return iter(sorted(it, reverse=reverse))
    if cmd == "limit":
        arg = int(value)
        return limitation(it, arg)
    if cmd == "regex":
        regex = re.compile(value)
        return filter(lambda v: regex.search(v), it)

    return it


def limitation(it: Iterator, limit: int) -> Iterator:
    i = 0
    for item in it:
        if i < limit:
            yield item
        else:
            break
        i += 1


def build_query(it: Iterator, cmd1: str, value1: str, cmd2: str, value2: str) -> Iterator:
    res: Iterator = map(lambda x: x.strip(), it)
    res = get_command(it, cmd1, value1)
    return get_command(res, cmd2, value2)
