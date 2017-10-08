#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# version 2.0 no file no pickle (too busy recently)

from operator import itemgetter

print("="*30)
print("#"+" "*5+"Welcome to PES v1.0"+" "*4+"#")
print("#"+" "*5+"Author: Sky"+" "*12+"#")
print("#"+" "*5+"Release Date: 10-1"+" "*5+"#")
print("="*30)
print('''ENTER:
        add     -add info
        rm      -delete info
        update  -update info
        find    -find info
        display -print info
        q       -Quit

        help [instruction] -get details of instructions above
        example: help add
        !!NOT: help(add)
                ''')

def cmp1(a, b):
    if(a[1] < b[1]): return 1;
    if(a[1] > b[1]): return -1;
    return 0;

def cmp2(a, b):
    if(a[1] < b[1]): return -1;
    if(a[1] > b[1]): return 1;
    return 0;

def add(name, score):
    """use it to add a student's grades
       add [name] [score]"""
    try:
        score = int(score)
    except ValueError:
        print("please enter a correct score.(number needed)")

    if(name in dic.keys()):
        c = input("already exists, sure to update?(y/n) ")
        if(c == 'n'): return
        dic[name] = score
        print("update successfully")
        return
    dic[name] = score

def rm(name):
    """use it to remove a student's grades
       rm [name] """
    try:
        del dic[name]
    except KeyError:
        print("There is no such student originally.")
def find(name):
    """use it to inquire a student's grades
        find [name]"""
    if(name in dic.keys()): print(name+": "+str(dic[name]))
    else: print("There is no such student.")
def display(tp='none'):
    """use it to print all student's grades
        display -directl print
        display u -ascending order print
        display d -descending order print"""
    if(tp == 'none'):
        cnt = 1
        for stu in dic:
            print(str(cnt)+". "+stu+" "+str(dic[stu]))  
            cnt += 1
    else:
        if(tp == 'u'):
            dict= sorted(dic.items(), key=lambda d:d[1])
            cnt = 1
            for stu in dict:
                print(str(cnt)+". "+stu[0]+" "+str(stu[1]))  
                cnt += 1
        else:
            dict= sorted(dic.items(), key=lambda d:d[1], reverse = True)
            cnt = 1
            for stu in dict:
                print(str(cnt)+". "+stu[0]+" "+str(stu[1]))  
                cnt += 1

dic={}
while(True):
    cmd = input("Input>>> ")
    cmd = cmd.split()
    if(not len(cmd)): continue
    if(cmd[0] == "add"): 
        try:
            add(*cmd[1:])  #好用的*
        except TypeError:
            print("command error, enter help(add) for help")
    if(cmd[0] == "rm"): 
        try:
            rm(*cmd[1:])
        except TypeError:
            print("command error, enter help(rm) for help")
    if(cmd[0] == "find"): 
        try:
            find(*cmd[1:])
        except TypeError:
            print("command error, enter help(find) for help")
    if(cmd[0] == "display"): 
        try:
            display(*cmd[1:])
        except TypeError:
            print("command error, enter help(display) for help")
    if(cmd[0] == "q"): exit()
    if(cmd[0] == "help"): 
        if(cmd[1] == "add"): help(add)
        if(cmd[1] == "rm"): help(rm)
        if(cmd[1] == "find"): help(find)
        if(cmd[1] == "display"): help(display)

# 抱歉，实在是时间紧张，只能写一个最低配版本低先交上去，
# 我的水平，应该还是可以再添一些东西的