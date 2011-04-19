import curses



def setscr():
	myscreen = curses.initscr()
	curses.start_color()
	var="    |     "
	rpm="3678"
	myscreen.border(0)
	myscreen.addstr(1, 2,"              `-:://+////::-.   `.-:/://///::.                       ")
	myscreen.addstr(2, 2,"            :+oooo+::::-/+oooo+oso+/:-....--:oo/.                    ")
	myscreen.addstr(3, 2,"          .oooo:.        .:oso+/ooo:.        `-+o/                   ")
	myscreen.addstr(4, 2,"         .ooo/`       -/+/+:. // .:+o/:`        /o+`                 ")
	myscreen.addstr(5, 2,"         +oo/      .://:-`  `+oo+`  `-///.       /o/                 ")
	myscreen.addstr(6, 2,"        `oo+     .///:`     .-oo/-     .:++.     `oo`                ")
	myscreen.addstr(7, 2,"       :/oo:   .+o+-  `      `o+:        .+o/`    /o::-              ")
	myscreen.addstr(8, 2,"        +oo/.`/o+.``````     `+/:      ````-oo: `-/oo:               ")
	myscreen.addstr(9, 2,"        `oo+/oo:`````        `+/:        ````/o+`-+o/                ")
	myscreen.addstr(10, 2,"         .:/o/````           `o+:           ``-oo-`-        `..      ")
	myscreen.addstr(11, 2,"`--.--` ::oo/:                ``---..-.``      `+o/---.  `::.`       ")
	myscreen.addstr(12, 2,"     ````oo+//-          -.-::::/:::::--.::-`  `-soo/-```            ")
	myscreen.addstr(13, 2," ```   `oo-`..--.`   `` .::.`.-.`--.``.-//:. `--:-oo:``   ```        ")
	myscreen.addstr(14, 2,"` ```` /o/ ````  ``/o+-   ``-`...-:-```  `:o/`````.oo-  ```` ```     ")
	myscreen.addstr(15, 2,"`     .oo`       `+/```````.--- ..`...--`` `o/     -oo.  ```.....`   ")
	myscreen.addstr(16, 2,"      +o/        :o`     .--```..`.`..`     o+      +o+  ``````      ")
	myscreen.addstr(17, 2,"   __ oo-__      .o-    `/::.`````.:/.    `/+`      .oo.             ")
	myscreen.addstr(18, 2," \\\  .oo.. //     .+/.  `::....```.:-:  .oo:         +o/             ")
	myscreen.addstr(19, 2,"  \\\ -ooo.//        .//+///.    ``.:o+:```         `:+oo         ````")
	myscreen.addstr(20, 2,"`` \\\ooo-//     `````   :::::::::::-::`  `````      -oos.    ``````  ")
	myscreen.addstr(21, 2,"`` ``\+:/   `````      `:-``````  `.-:       `````   :oo+.`` ```     ")
	myscreen.addstr(22, 2,"`-`---\///:-`          .- ````..``   -           ``:-:o/.--`         ")
	myscreen.refresh()
	myscreen.getch()
	


setscr()
curses.endwin()