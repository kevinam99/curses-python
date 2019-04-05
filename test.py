import curses
from time import sleep
stdscr = curses.initscr()
'''
curses.curs_set(0)
curses.noecho() #doesn't display enetered chars. eg: entering password for sudo
curses.cbreak() #doesn't wait for enter key to be pressed for accepting an input
stdscr.keypad(True)
'''

def main(stdscr):
    
    stdscr.addstr(5, 15, "Hello") #y, x "text"
    curses.curs_set(0)
    stdscr.refresh()
    sleep(3)


curses.wrapper(main)
# Undo everything before program ends
'''curses.curs_set(0)
curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
'''