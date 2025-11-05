This is a simple mod loader experiment made in Python.  
Ngl I suck at Python so there will probably be a lot of wierd stuff.  
If this is of any help to anyone I'd be happy :)  
## Update:  
Added `api.c.clear` to clear the terminal  
Added the main game's `fire()` to `api` as `api.fire()`  
__________________________________________  
ALL MODS MUST BE LOCATED INSIDE OF `mods/` AND END WITH `.py`.  
```
mygame.exe      # just the modloader.py
mods/           # the folder for all mods 
├─ MainAPI.py   # included mod, very usefull for modding
└─ mymod.py     # some mod, be creative!
```  
### At the start of a mod:
```py
import MainAPI as api # or `api=__import__('MainAPI')`
if __name__=='__main__':api.SYS.exit()
```
## MainAPI functions: (this documentation is not complete yet)
`@api.extend()`: Extend an existing function. (Requires the extending function to be a generator, use `yield`).  
```py
# EXAMPLE:
@api.extend('main')
def _():
  print('this will run at the start of "main()"')
  yield
  print('this will run at the end of "main()"')
```
`@api.on()`: Register a function to run when an event fires.  
```py
# EXAMPLE:
@api.on('start')
def _():
    print('this will be ran once at the start of the game')
```
`api.exitcode()`: Edit / returns the current exit code for the game (returns api.GAME.C if i=None else edits api.GAME.C to i).  
```py
# EXAMPLE:
api.exitcode(67)
print(api.exitcode())
```  
`api.get_modified_mixins()`: Returns a list of all functions that has been edited from their default.  
```py
# EXAMPLE:
print("Has 'main' been modified?", 'main' in api.get_modified_mixins())
```  
`api.c.clear`: Type = property, clears the terminal from all text.  
```py
# EXAMPLE:
print(api.c.clear+'This is now the only text in the terminal.')
```
`api.fire()`: Fires an event like "start", "exit" or "tick".
```py
# EXAMPLE:
@api.on('tick')
def _():print('Another tick!')

api.fire('tick')
```
`api.register()`: Overrides a function to let you make your own custom version.
```py
# EXAMPLE:
@api.register('main')
def _():print('This will replace the normal "main()" function')
```  
## examples:  
`mods/guess_the_number.py` (Can be found in `examples` folder): The terminal will prompt you to guess a random number (1 to 10) and every attempt will tell you if the correct number is smaller or bigger than your input  
```py
import MainAPI as api
if __name__=='__main__':api.SYS.exit()

def _intinput(s):
    """an input that only accepts integers"""
    while 1:
        a=input(s)
        try:return int(a)
        except:print(f"'{a}' is not an integer")
from random import randint
def Game(min,max,a=None):
    r=randint(min,max)# a random number from 1 to 10
    while a!=r:
        a=_intinput(f'Guess a number {min} to {max}: 'if a==None else 'Try again: ')
        print(f'Wrong, the number is '+('higher'if a<r else'lower')+f' than {a}.'if a!=r else'')
        api.fire('tick')
    print(f'Correct, the answer was {r}!')
    api.fire('tick')

@api.on('start')
def _():
    print(api.c.clear+'Guess the number mod!')
@api.register('main')
def _():
    Game(1,10)
    api.exitcode(1)
    api.fire('exit')
```  
