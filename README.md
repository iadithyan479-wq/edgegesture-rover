# EdgeGesture Rover

A lightweight robotics control starter that maps hand-gesture labels to safe rover commands. It includes a deterministic rover simulator, command debouncing, a dead-man timeout, and a clean adapter boundary for MediaPipe or another vision model.

## Run

```bash
python -m edge_rover --demo
```

Run tests with `python -m unittest discover -s tests`.

## Safety-first design

- Unknown gestures map to STOP.
- Commands expire unless fresh gestures arrive.
- Speed is clamped to a conservative range.
- Vision inference is separated from motion control.

To connect a camera, implement a producer that emits labels such as `thumb_up`, `palm`, `two_fingers`, and `fist`.
