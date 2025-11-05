import MainAPI as api
if __name__=='__main__':api.SYS.exit()


def _intinput(s):
    while 1:
        a=input(s)
        try:return int(a)
        except:print(f"'{a}' is not an integer")
from random import randint
@api.on('start')
def _():
    print(api.c.clear+'Guess the mumber mod!')
@api.register('main')
def _():
    def Game(min=1,max=10,a=None):
        r=randint(min,max)
        while a!=r:
            a=_intinput(f'Guess a number {min} to {max}: 'if a==None else 'Try again: ')
            print(f'Wrong, the number is '+('higher'if a<r else'lower')+f' than {a}.'if a!=r else'')
        print(f'Correct, the answer was {r}!')
    Game()
    api.exitcode(1)
