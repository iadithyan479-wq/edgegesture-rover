import argparse,time
from .controller import GestureController
p=argparse.ArgumentParser(); p.add_argument('--demo',action='store_true'); a=p.parse_args()
if a.demo:
    c=GestureController(timeout=1.0)
    for i,g in enumerate(['thumb_up','thumb_up','two_fingers','palm']): print(i,g,c.update(g,now=i*0.4),c.rover)
    print('after timeout:',c.tick(now=3.0))
