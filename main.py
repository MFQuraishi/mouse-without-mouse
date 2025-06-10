import keyboard
import mouse

COMBINATION = "ctrl+alt+shift"
COORDINATE_BASE_VAL = 10
SCROLL_BASE_VAL = 2

def moveMouse(x, y):
    mouse.move(y, x, False)

def registerHotKeys(combination, func):
    keyboard.add_hotkey(COMBINATION + "+" + combination, lambda: func(), suppress=True)

print("=========================================")
print("mouse without mouse program started...")
print("=========================================")


# simple motions
registerHotKeys("up", lambda: moveMouse(COORDINATE_BASE_VAL*-1, 0))
registerHotKeys("down", lambda: moveMouse(COORDINATE_BASE_VAL, 0))
registerHotKeys("left", lambda: moveMouse(0, COORDINATE_BASE_VAL*-1))
registerHotKeys("right", lambda: moveMouse(0, COORDINATE_BASE_VAL))

# diagonal movements
registerHotKeys("up+right", lambda: moveMouse(COORDINATE_BASE_VAL*-1, COORDINATE_BASE_VAL))
registerHotKeys("up+left", lambda: moveMouse(COORDINATE_BASE_VAL*-1, COORDINATE_BASE_VAL*-1))

registerHotKeys("down+right", lambda: moveMouse(COORDINATE_BASE_VAL, COORDINATE_BASE_VAL))
registerHotKeys("down+left", lambda: moveMouse(COORDINATE_BASE_VAL, COORDINATE_BASE_VAL*-1))

registerHotKeys("left+up", lambda: moveMouse(COORDINATE_BASE_VAL*-1, COORDINATE_BASE_VAL*-1))
registerHotKeys("left+down", lambda: moveMouse(COORDINATE_BASE_VAL, COORDINATE_BASE_VAL*-1))

registerHotKeys("right+up", lambda: moveMouse(COORDINATE_BASE_VAL*-1, COORDINATE_BASE_VAL))
registerHotKeys("right+down", lambda: moveMouse(COORDINATE_BASE_VAL, COORDINATE_BASE_VAL))

# keyboard mappings with mouse actions
registerHotKeys("del", lambda: mouse.click())
registerHotKeys("end", lambda: mouse.right_click())
registerHotKeys("insert", lambda: mouse.double_click())

registerHotKeys("page up", lambda: mouse.wheel(SCROLL_BASE_VAL))
registerHotKeys("page down", lambda: mouse.wheel(-SCROLL_BASE_VAL))

keyboard.wait()
