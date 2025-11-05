This is a simple mod loader experiment made in Python.  
If this is of any help to anyone I'd be happy :).  
### At the start of a mod:
```py
api=__import__('MainAPI')
if __name__=='__main__':api.SYS.exit()
```
## MainAPI functions: (the documentation is not complete)
`@api.extend()`: Extend an existing function. (Requires the extending function to be a generator, use `yield`.)  
```py
# EXAMPLE:
@api.extend('main')
def _():
  print('this will run at the start of "main()"')
  yield
  print('this will run at the end of "main()"')
```
`@api.on()`: Registera function to run when an event fires.  
```py
# EXAMPLE:
@api.on('start')
def _():
    print('this will be ran once at the start of the game')
```
`api.exitcode(i:int|none)`: edits / returns the current exit code for the game (returns api.GAME.C if i=None else edits api.GAME.C with i).  
```py
# EXAMPLE:
api.exitcode(67)
print(api.exitcode())
```  
`api.get_modified_mixins()`: returns a list of all functions that has been edited from default.mixins.  
```py
# EXAMPLE:
print("Has 'main' been modified?", 'main' in api.get_modified_mixins())
```  
