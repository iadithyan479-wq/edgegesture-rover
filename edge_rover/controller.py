from dataclasses import dataclass
import time
COMMANDS={'thumb_up':'FORWARD','palm':'STOP','two_fingers':'TURN_LEFT','fist':'BACKWARD'}
@dataclass
class Rover: linear: float=0.0; angular: float=0.0
class GestureController:
    def __init__(self, rover=None, timeout=1.0): self.rover=rover or Rover(); self.timeout=timeout; self.last_seen=0.0
    def update(self, gesture, now=None):
        now=time.monotonic() if now is None else now; self.last_seen=now; cmd=COMMANDS.get(gesture,'STOP')
        self.rover.linear, self.rover.angular={'FORWARD':(1.0,0.0),'BACKWARD':(-0.6,0.0),'TURN_LEFT':(0.0,0.8),'STOP':(0.0,0.0)}[cmd]; return cmd
    def tick(self, now=None):
        now=time.monotonic() if now is None else now
        if now-self.last_seen>self.timeout: self.rover.linear=self.rover.angular=0.0
        return self.rover
