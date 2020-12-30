import curses
import time

from com.alexstarc.dpad.adb_commands import execute_adb_cmd_restart, \
    execute_adb_cmd_keyevent

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '


def main(screen):
    curses.curs_set(1)
    curses.noecho()

    while True:
        screen.clear()
        screen.addstr('For exit press q, to restart adb r\n')
        c = screen.getch()
        curses.echo()
        if c == 113:
            screen.addstr('Abort!\n')
            break
        if c == 114:
            screen.addstr('Restart adb\n')
            execute_adb_cmd_restart()
        elif c == 260:
            screen.addstr('Left arrow ←\n')
            execute_adb_cmd_keyevent(21)
        elif c == 261:
            screen.addstr('Right arrow →\n')
            execute_adb_cmd_keyevent(22)
        elif c == 258:
            screen.addstr('Down arrow ↓\n')
            execute_adb_cmd_keyevent(20)
        elif c == 259:
            screen.addstr('Up arrow ↑\n')
            execute_adb_cmd_keyevent(19)
        elif c == 10:
            screen.addstr('Enter ↵\n')
            execute_adb_cmd_keyevent(23)
        elif c == 263:
            screen.addstr('Back ⟵\n')
            execute_adb_cmd_keyevent(4)
        else:
            screen.addstr('Invalid input: ' + str(c) + '\n')

        screen.refresh()
        time.sleep(1)


curses.wrapper(main)
