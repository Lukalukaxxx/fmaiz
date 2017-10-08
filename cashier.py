#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pickle
from datetime import datetime

class Things(object):
    '''A product info recoder:
    [product ID] [product name] [price]'''

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return str('￥'+str("%4d "%self.price)+self.name)

if __name__ == "__main__":
    print()
    print("="*40)
    print("#"+" "*5+"Welcome to Casher System v1.0"+" "*4+"#")
    print("#"+" "*5+"Author: Sky"+" "*22+"#")
    print("#"+" "*5+"Release Date: 10-8"+" "*15+"#")
    print("="*40) 
    print()

product_list = {}
try:
    f = open(".pdlist", 'rb')
except FileNotFoundError:
    f = open(".pdlist", "wb")
    f.close()
    f = open(".pdlist", "rb")
try:
    product_list = pickle.load(f)
except EOFError:
    print(">>>>>>>>>> WARNNING WARNNING <<<<<<<<<<")
    print(" "*10+"System is EMPTY now.")
    print(" "*10+"Please ADD products.")
    print()
f.close()
del f

def print_help():
    print("~~~~~~~~~~~~ Instructions ~~~~~~~~~~~~")
    print("     [name] | [description]")
    print("       add  | add/update a product to system")
    print("    rm/del  | del a product from system")
    print("       cal  | begin to account")
    print("    ls/dis  | display all products")
    print("    q/exit  | quit")
    print("     (input 'help [name]' for details) \n")

def save():
    with open(".pdlist_tmp", "wb") as f:
        pickle.dump(product_list, f)
    os.remove('.pdlist')
    os.rename('.pdlist_tmp', '.pdlist')

def add(ID, name, price):
    '''You can add info of a product by input:
    add [ID] [name] [price] ([ID] [price] must be numbers)
    [ID] is unique, so if you input an existing ID, other info \
    will be updated'''
    try:
        ID = int(ID)
        price = int(price)
    except ValueError:
        print("-----[ID] [price] must be numbers-----")
        return
    if ID in product_list.keys():
        print('-'*10+"ID[{0}] has already marked".format(ID), end=' ')
        print(product_list[ID])
        jud = input('-'*10+"Are you sure to change it?(y/n)")
        while(not jud in ['y','n','']):
            jud = input("-----Please input 'y' or 'n' to change the info or not.(y/n)")
        if jud != 'n':
            product_list[ID] = Things(name, price)
        else: return
    else:
        product_list[ID] = Things(name, price)
    save()

def rm(ID):
    '''You can remove a info of a product by input:
    rm [ID] (must be [ID], because name is not unique!)'''
    try:
        ID = int(ID)
    except ValueError:
        print("-----[ID] [price] must be numbers-----")
        return
    if ID in product_list.keys():
        del product_list[ID]
        save()
    else:
        print('-'*10+'No such product, delete failed')

def dis():
    '''To print all products' info. 
    No any parameter needed'''
    cnt = 0
    print('\n'+' '*12+"[ID]  |  [price] [name]")
    for i in product_list:
        cnt += 1
        print('%16d'%i,end='  |  ')
        print(product_list[i])
    print('\n'+' '*18+'total:', cnt)
    
def invalid():
    print('-'*5+"Invalid instruction. TRY 'help'"+'-'*5)

def print_list(order):
    sum = 0
    print('\n'+' '*12+'{Shopping Bag}')
    for i in order:
        sum += product_list[i].price
        print('%16d'%i,end='  |  ')
        print(product_list[i])
    print('\n'+' '*18+'total: ￥', sum)

def print_receipt(order):
    T = datetime.now()
    receiptfile = str(T.year)+'-'+str(T.month)+'-'+str(T.day)
    receiptfile += '_[{0}-{1}-{2}].txt'.format(T.hour,T.minute,T.second)
    with open(receiptfile, "w") as f:
        tmp = f.write("Record time: "+str(T)+'\n\n')
        tmp = f.write(" Shopping list:")
        sum = 0
        for i in order:
            sum += product_list[i].price
            tmp = f.write('%16d'%i,end='  |  ')
            f.write(product_list[i]+'\n')
        f.write('\n'+' '*18+'total: ￥ '+str(sum))
    print(" Successfully print your receipt to ["+receiptfile+']')

def receipt(order):
    cmd = input(' Successfully Billing. Do you want a RECEIPT?(y/n)')
    while(not cmd in ['y','n','']):
        cmd = input(" Please input 'y' or 'n' to print receipt or not.(y/n)")
    if cmd != 'n':
        print_receipt(order)
    print(" Thanks for use. You can donate to Alipay: 17733099176")

def cal():
    '''Begin to calculate the cost.
    No any parameter needed.
    When start it:
        input [ID] directly to add a product into bill
        input 'b' to remove the previous product you added
        input 'del [ID]' to remove a definite product product you added
        input 'clear' to empty the bill
        input 'q'or'done' to finish and choose to print receipt or not'''
    print("\n Begin to calculate cost:\n")
    cart = {}
    cmds = ['b', 'del', 'rm', 'clear', 'q', 'done', 'help']
    order = []
    while(True):
        cmd = input(" >>>Input:").split()
        Len = len(cmd)
        if not Len: continue
        if cmd[0] in cmds:
            if cmd[0] == 'b':
                if Len > 1:
                    invalid()
                    continue
                if len(order) < 1:
                    print('-'*10+"Your bag is empty now!"+'-'*10)
                    continue
                del order[-1]
                print_list(order)
                continue
            if cmd[0] in ['del','rm']:
                if Len > 2:
                    invalid()
                    continue
                delID = 19990801
                try:
                    delID = int(cmd[1])
                except ValueError:
                    print('-'*10+"[ID] must be numbers"+'-'*10)
                    continue
                if not delID in order:
                    print('\n'+'-'*10+"Your bag has no this!"+'-'*10+'\n')
                    print_list(order)
                    print('\n'+'-'*10+"Your bag has no this!"+'-'*10+'\n')
                    continue
                order.remove(delID)
                print_list(order)
            if cmd[0] == 'clear':
                if Len > 1:
                    invalid()
                    continue
                order = []
                print_list(order)
            if cmd[0] in ['q','done']:
                if Len > 1:
                    invalid()
                    continue
                receipt(order)
                return
            if cmd[0] == 'help':
                print(''' 
  input [ID] directly to add a product into bill
  input 'b' to remove the previous product you added
  input 'del/rm [ID]' to remove a definite product product you added
  input 'clear' to empty the bill
  input 'q'or'done' to finish and choose to print receipt or not
                ''')
                continue
        if Len > 1:
            invalid()
            continue
        addID = 19990523
        try:
            addID = int(cmd[0])
        except ValueError:
            print('-'*10+"[ID] must be numbers"+'-'*10)
        if not addID in product_list.keys():
            print('-'*10+"This is no such product [{0}]".format(addID))
            continue
        order.append(addID)
        print_list(order)

def main():
    # no output is the best !
    print_help()
    cmds = ['q', 'exit', 'add', 'del', 'rm', 'cal', 'dis', 'ls', 'help']
    while(True):
        cmd = input(">>>Input: ").split()
        if not len(cmd): continue
        if not cmd[0] in cmds:
            invalid()
            continue
        if cmd[0] in ['q','exit']: 
            if len(cmd) > 1:
                invalid()
                continue
            exit()
        if cmd[0] == cmds[2]:
            try:
                 add(*(cmd[1:]))
            except TypeError:
                invalid()
            continue
        if cmd[0] in cmds[3:5]:
            try:
                rm(*(cmd[1:]))
            except TypeError:
                invalid()
            continue
        if cmd[0] == cmds[5]:
            try:
                cal(*(cmd[1:]))
            except TypeError:
                invalid()
            continue
        if cmd[0] in cmds[6:8]:
            try:
                dis(*(cmd[1:]))
            except TypeError:
                invalid()
            continue
        if cmd[0] == cmds[8]:
            if len(cmd) == 1:
                print_help()
                continue
            if len(cmd) > 2 or not cmd[1] in cmds[2:]:
                invalid()
                continue
            if cmd[1] == 'add': help(add)
            if cmd[1] == 'cal': help(cal)
            if cmd[1] in ['del','rm']: help(rm)
            if cmd[1] in ['dis','ls']: help(dis)

if __name__ == "__main__":
    main()