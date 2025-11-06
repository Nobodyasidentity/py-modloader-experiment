import MainAPI as api
if __name__=='__main__':api.SYS.exit()

def _intinput(s,Exit=None):
    """an input that only accepts integers"""
    while 1:
        a=input(s)
        if a==Exit:return'Exit'
        try:return int(a)
        except:print(f"'{a}' is not an integer")

@api.on('tick')
def _():
    global r,a,minv,maxv
    a=_intinput(f'Guess a number {minv} to {maxv}: 'if a==None else 'Try again: ','exit')
    if a=='Exit':api.fire('exit')
    print(f'Wrong, the number is '+('higher'if a<r else'lower')+f' than {a}.'if a!=r else'')

from random import randint
def Game(lminv,lmaxv):
    global r,a,minv,maxv
    minv,maxv,a=lminv,lmaxv,None
    r=randint(minv,maxv) # a random number from 1 to 10
    while a!=r:
        api.fire('tick')
    input(f'Correct, the answer was {r}!')

@api.on('start')
def _():
    print(api.c.clear+'Guess the number mod!')
@api.register('main')
def _():
    api.c.exitcode(0)
    Game(1,100)
    api.c.exitcode(1)
    api.c.clear
