C=0
try:
    if __name__=='__main__':
        from glob import glob,sys,os;sys.dont_write_bytecode=True
        import atexit,signal
        def get_base_path():return os.path.dirname(sys.executable) if getattr(sys,"frozen",False) else os.path.dirname(__file__)
        dir=get_base_path().replace('\\','/')
        print(f'Got "{dir}" as base path')
    sys.modules['modloader']=sys.modules[__name__]
    def fire(event_name, *a, **kw):
        funcs=EVENTS.get(event_name,[])
        for fn in funcs:
            try:fn(*a, **kw)
            except Exception as e:print(f"[event:{event_name}] error in {fn.__name__}: {e}")
        if event_name=='exit':sys.exit()
    class default:
        @staticmethod
        def main():
            print('main function!')
        
        mixins={'main':main}
    MIXINS=dict(default.mixins)
    EVENTS={"start":[],"exit":[],"tick":[]}
    
    if __name__=='__main__':
        def on_exit():
            global C
            input(f"Game exited with code: '{C}'...")
        def _sigint_exit(*_):global C;C=-2;sys.exit()
        atexit.register(on_exit)
        signal.signal(signal.SIGINT,_sigint_exit)
        try:
            sys.path.append(dir+'/mods')
            mods=[f[len(dir)+6:len(f)-3] for f in glob(f'{dir}/mods/*.py')]
            print(f'found {len(mods)} mod{"s"if len(mods)!=1 else""}: {mods}')
        except Exception as e:print(f"Unable to find 'mods': {e}");mods=[]
        try:
            for i in mods:__import__(i)
        except Exception as e:print(f'Error occurred while loading "{i}": {e}')
        sys.path.append(dir)
        fire("start")
        while 1:MIXINS['main']()
        fire("exit")
except Exception as e:print(f'Error: {e}');C=-1
