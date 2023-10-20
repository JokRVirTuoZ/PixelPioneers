from GestionCliquage import GestionCliquage as e
from pynput.mouse import Listener

def exemple():
   m = e

   with Listener(on_click=m.on_click) as listener:
       listener.join()
       listener.stop()

if __name__ == '__main__':
    exemple()