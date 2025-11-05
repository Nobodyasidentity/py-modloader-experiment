from glob import glob as GLOB,os as OS,sys as SYS
from functools import wraps as WRAPS
import inspect as INSPECT
if __name__=='__main__':SYS.exit(0)
SYS.dont_write_bytecode=True
SYS.modules['MainAPI']=SYS.modules[__name__]
def get_base_path():return OS.path.dirname(SYS.executable) if getattr(SYS,"frozen",False) else OS.path.dirname(__file__)
dir=get_base_path().replace('\\','/')
SYS.path.append(OS.path.dirname(dir))
GAME=SYS.modules.get('modloader')
SYS.path.append(dir)

def exitcode(i=None):
    global GAME
    if not i==None:GAME.C=i
    else:return GAME.C

class _c:
    @property
    def clear(self=None):OS.system('cls'if OS.name=='nt'else'clear');return''
c=_c()
# CHATGPT CODE {
# --- Decorator systems ---
def register(name):
    """Register a new mixin."""
    def deco(fn):
        GAME.MIXINS[name] = fn
        return fn
    return deco

def extend(name):
    """
    Extend an existing mixin.
    - Requires the extending function to be a generator (use `yield`).
    - Stacks multiple extensions automatically.
    """
    def deco(fn):
        old = getattr(GAME, "MIXINS", {}).get(name)
        if not INSPECT.isgeneratorfunction(fn):
            raise TypeError(f"Extended mixin '{name}' must be a generator (use yield)")
        @WRAPS(fn)
        def wrapper(*a, **kw):
            # Run the new layer's generator (before/after)
            gen = fn()
            try:next(gen)  # BEFORE
            except StopIteration:pass
            # Call the previous mixin in the chain
            if old:old(*a, **kw)
            try:next(gen)  # AFTER
            except StopIteration:pass
        # Update GAME.MIXINS[name] to the new stacked wrapper
        GAME.MIXINS[name]=wrapper
        return fn
    return deco


def on(event):
    """Register to run when an event fires."""
    GAME.EVENTS.setdefault(event, [])
    def deco(fn):
        GAME.EVENTS[event].append(fn)
        return fn
    return deco
def get_modified_mixins():
    """Return a list of all mixin names that were changed."""
    originals = getattr(GAME.default, "mixins", {})
    return [
        name for name, orig_fn in originals.items()
        if GAME.MIXINS.get(name) is not orig_fn
    ]
def fire(event_name, *a, **kw):
    """Call all functions registered to an event."""
    GAME.fire(event_name, *a, **kw)
# }
