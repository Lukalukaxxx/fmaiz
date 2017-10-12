#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pickle
from datetime import datetime

class Things(object):
    '''A product info recoder:
    [product name] [price]'''

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return str('$'+str("%4d "%self.price)+self.name)

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
    print("   add     add/update a product to system")
    print("   rm/del  delete a product from system")
    print("   cal     begin to account")
    print("   ls/dis  display all products in system")  
    print("   q/exit  quit the system")
    print("\nEXAMPLES:")
    print("         add 19990913 sky 999")
    print("          rm 19990913")
    print("         cal (no parameter needed)")
    print("          ls (no parameter needed)")
    print("           q (no parameter needed)")
    print("    (input just like 'help add' for details) \n")

def save():
    with open(".pdlist_tmp", "wb") as f:
        pickle.dump(product_list, f)
    os.remove('.pdlist')
    os.rename('.pdlist_tmp', '.pdlist')

def add(ID, name, price):
    '''You can add info of a product by input:
    add [ID] [name] [price] ([ID] [price] must be numbers)
    [ID] is unique, so if you input an existing ID, other info will be updated'''
    try:
        tmp = int(ID)
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
        tmp = int(ID)
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
        print('%16s'%i,end='  |  ')
        print(product_list[i])
    print('\n'+' '*18+'total:', cnt)
    
def invalid():
    print('-'*5+"Invalid instruction. TRY 'help'"+'-'*5)

def print_list(cart):
    sum = 0
    print('\n'+' '*12+'{Shopping list}')
    for i in cart:
        sum += product_list[i].price*cart[i]
        print('%16s'%i,end='  |  ')
        print(product_list[i], end='')
        if cart[i] != 1: print(" x%d"%cart[i]) 
        else: print()
    print('\n'+' '*18+'total: $', sum)

def print_receipt(cart):
    T = datetime.now()
    receiptfile = str(T.year)+'-'+str(T.month)+'-'+str(T.day)
    receiptfile += '_[{0}-{1}-{2}].txt'.format(T.hour,T.minute,T.second)
    with open(receiptfile, "w") as f:
        tmp = f.write("Record time: "+str(T)+'\n\n')
        tmp = f.write(" Shopping list:\n")
        sum = 0
        for i in cart:
            sum += product_list[i].price*cart[i]
            tmp = f.write(str('%16s'%i)+'  |  ')
            tmp = f.write(str(product_list[i]))
            if cart[i] != 1: tmp = f.write(str(" x%d"%cart[i]))
            tmp = f.write('\n')
        tmp = f.write('\n'+' '*18+'total: $ '+str(sum))
    print(" Successfully print your receipt to ["+receiptfile+']')

def receipt(cart):
    cmd = input(' Successfully Billing. Do you want a RECEIPT?(y/n)')
    print(' '+'-'*50)
    while(not cmd in ['y','n','']):
        cmd = input(" Please input 'y' or 'n' to print receipt or not.(y/n)")
    if cmd != 'n':
        print_receipt(cart)
    print(" Thanks for use. You can donate to Alipay: 17733099176")

def cal():
    '''Begin to calculate the cost.
    No any parameter needed.
    When start it, you can:

        1.input [ID] directly to add one product to cart
        2.input [ID] [numbers] to add several products to cart
        3.input 'rm [ID] [numbers] to remove products from cart
        4.input 'q' to finish to finish and choose to print receipt or not

    (If you still do not understand, input 'example' to get examples)'''

    print("\n Begin to calculate cost:")
    print("     (If you can not use it, try 'help')\n")
    cmds = ['rm', 'q', 'help', 'example']
    cart = {}
    while(True):
        cmd = input(" >>>Input:").split()
        Len = len(cmd)
        if not Len: continue
        if cmd[0] in cmds:
            if cmd[0] == 'rm':
                if Len != 3: invalid(); continue
                rm_ID = cmd[1]
                try:
                    tmp = int(rm_ID)
                    rmnum = int(cmd[2])
                except ValueError:
                    print('-'*6+"[ID] [numbers] must be numbers"+'-'*6)
                    continue
                if not rm_ID in cart.keys():
                    print('-'*10+"Your cart has no this"+'-'*10)
                    continue
                if cart[rm_ID] < rmnum:
                    print('-'*7+"Your cart has no enough this"+'-'*7)
                    continue
                cart[rm_ID] -= rmnum
                if cart[rm_ID] == 0: del cart[rm_ID]
                print_list(cart)
            elif cmd[0] == 'q':
                if Len > 1: invalid(); continue
                receipt(cart)
                return
            elif cmd[0] == 'help':
                if Len > 1: invalid(); continue
                help(cal)
            elif cmd[0] == 'example':
                if Len > 1: invalid(); continue
                print("     1.   19990523")
                print("     2.   19990801 88")
                print("     3.   rm 19990801 88")
                print("     4.   q (no parameter needed)")
        else:
            if Len > 2: invalid(); continue
            addID = cmd[0]
            try:
                tmp = int(cmd[0])
                if Len == 2: num = int(cmd[1])
                else: num = 1
            except ValueError:
                print('-'*6+"[ID] [numbers] must be numbers"+'-'*6)
                continue
            if addID in cart.keys(): cart[addID] += num
            else: cart[addID] = num
            print_list(cart)

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