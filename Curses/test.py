import curses

myscreen = curses.initscr()
var="    |     "
rpm="3678"
myscreen.border(2)
myscreen.addstr(1, 2, "RPM(1): "+rpm)
myscreen.addstr(1, 20, "RPM(2): "+rpm)
myscreen.addstr(1, 40, "RPM(3): "+rpm)
myscreen.addstr(1, 60, "RPM(4): "+rpm)
myscreen.addstr(5, 25, "Pitch: ["+var+"]")
myscreen.addstr(6, 25, "Yaw:   ["+var+"]")
myscreen.addstr(7, 25, "Roll:  ["+var+"]")
myscreen.refresh()
myscreen.getch()

curses.endwin()
