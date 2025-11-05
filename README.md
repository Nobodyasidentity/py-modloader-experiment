This is a simple mod loader experiment made in Python.  
Ngl I suck at Python so there will probably be a lot of wierd stuff.  
If this is of any help to anyone I'd be happy :)  
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
api=__import__('MainAPI')
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
