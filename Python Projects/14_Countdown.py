# -*- coding: utf-8 -*-
"""
This program displays a digital timer that
counts down to zero.

"""
import datetime
import time

# returns a seven-segment representation of any number number as a string

def getSevSegStr(number, width):
    
    digits=list(str(number))
    pad=width-len(digits) 
    if pad<0: pad=0
    
    digits=pad*['0'] + digits
    
    rows=['','','']
    
    for i, digit in enumerate(digits):
        
        if digit=='0':
            
            rows[0]+=' __ '
            rows[1]+='|  |'
            rows[2]+='|__|'
            
        if digit=='1':
                
            rows[0]+='    '
            rows[1]+='   |'
            rows[2]+='   |'
            
        if digit=='2':
            
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+='|__ '
            
        if digit=='3':
            
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+=' __|'
            
        if digit=='4':
            
            rows[0]+='    '
            rows[1]+='|__|'
            rows[2]+='   |'
            
        if digit=='5':
            
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+=' __|'
            
        if digit=='6':
            
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+='|__|'
            
        if digit=='7':
                
            rows[0]+=' __ '
            rows[1]+='   |'
            rows[2]+='   |'
            
        if digit=='8':
            
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+='|__|'
            
        if digit=='9':
            
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+=' __|'
            
        if i!=len(digits):
            rows[0]+='  '
            rows[1]+='  '
            rows[2]+='  '
            
    return '\n'.join(rows)

# given a sequence of two digits numbers, returns a string representantion of the numbers
# separated by '*'

def getString(*args):
    
    rows=['','','']
    
    for i, number in enumerate(args):
        parsed=getSevSegStr(number, 2).split('\n')
        rows[0]+=parsed[0]
        rows[1]+=parsed[1]
        rows[2]+=parsed[2]
        
        if i < len(args)-1:            
            rows[0]+='  '
            rows[1]+='* '
            rows[2]+='* '
        
    return '\n'.join(rows)

# makes the magic happen        

def countdown(h,m,s):
    
    clock=datetime.datetime(year=2000,month=12,day=1,hour=h, minute=m, second=s)
    second=datetime.timedelta(seconds=1)
    
    while clock.hour!=0 or clock.minute != 0 or clock.second != 0:
        print('\n'*20)
        print(getString(clock.hour,clock.minute,clock.second))
        time.sleep(1)
        clock=clock-second
    
if __name__=='__main__':
    countdown(12,1,10)
    

