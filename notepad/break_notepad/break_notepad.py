# -*- coding: utf-8 -*-
from notepad.break_notepad.generate_frequency_dict import generate_list_for_frequency_analyse, generate_frequency_dict
from notepad.main import encrypt


def break_notepad(txt) -> str:
    lst = generate_list_for_frequency_analyse()
    lst_from_txt = generate_list_for_frequency_analyse(generate_frequency_dict(txt))

    notepad = generate_notepad_from_two_lists(lst, lst_from_txt)

    return encrypt(txt, notepad)


def generate_notepad_from_two_lists(lst1, lst2) -> dict:
    d = {}

    print(lst1)
    print(lst2)

    for k, v in zip(lst1, lst2):
        d[v] = k

    print(d)

    return d

print(break_notepad(''''''))