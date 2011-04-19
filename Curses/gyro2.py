import curses

myscreen = curses.initscr()
var="    |     "
rpm="3678"
myscreen.border(0)




myscreen.addstr(1, 2,"                     -+syhdddhyyo/-` -/oyyhhdhys+-                    ")
myscreen.addstr(2, 2,"                  `sNMMNhsoo+osymMMMNMMho/:---:+smd+`Pitch Forward    ")
myscreen.addstr(3, 2,"     Roll Left   :NMMy:      `/yNNhsyhNMh+`      `+md-                ")
myscreen.addstr(4, 2,"                .NMN:     `/hmms/`.dN:`-sdms-      -mm-               ")
myscreen.addstr(5, 2,"                sMM/    .omms:`  .yMMd-  `:ymh:     :Nh               ")
myscreen.addstr(6, 2,"              `:dMm   .sNd+.                -yNh-    dN-:`            ")
myscreen.addstr(7, 2,"               oMMd.`oNm+-.-:.      /\     --./dNo` -yMm+             ")
myscreen.addstr(8, 2,"                yMmydNy::--.`      //\\\     `.-:oNd-+mMs              ")
myscreen.addstr(9, 2,"                .dyNd:--``-`   Throttle Up    `--/mNs:o`     `.:`     ")
myscreen.addstr(10, 2,"         :/+o+.:ymMNh`    ```      ..++::::-....  .hMdsyo. `++:.      ")
myscreen.addstr(11, 2,"         ``.-:..hMddms.   ``  -+++oysssysooo/oo/ `.hMMNy/....`        ")
myscreen.addstr(12, 2,"        `.-...-yMy://+/:--//: -::////:s+:-.-/sy+:/sh+dMs-.```..``     ")
myscreen.addstr(13, 2,"      `-....`.+Mm-.-..``-yhs/.``-:/+//++o:/:--+hh..-:/mM+-.......-    ")
myscreen.addstr(14, 2,"       ``     dM/       hy` `.::+::/-//::+o+.` :N:    :MN-`-//+++:-`  ")
myscreen.addstr(15, 2,"             .MN`       do    -so+``:-.:oo`   `sd`     yMs ``````     ")
myscreen.addstr(16, 2,"             /Md``      :h+.  :yoo:--:/+ys- .oys.      :MN`           ")
myscreen.addstr(17, 2,"  .--.``     sMNs`       `/yooyhs/-...-+yhs::/-`      .:MM/      ``.-.")
myscreen.addstr(18, 2,"   `.--...``omMm.     `.---..:hy++++ssooyh/ `.--.``    sNMs. ``...-.``")
myscreen.addstr(19, 2,"    ..`..-\\\:oNN//...--.`    :yo.---....+y-     `.--.```dMN+-..-.:.   ")
myscreen.addstr(20, 2,"   `.  `---\\\Ny//ho.`        /:`...//-.` --         `-oohdyss-`   ..  ")
myscreen.addstr(21, 2,"       /:. .\\\//.:-.`         Throttle Down          `.--yhho.    .`  ")
myscreen.addstr(22, 2,"      `.-.Pitch Back`--.`          \mm/           `.Roll Right..''.   ")

myscreen.refresh()
myscreen.getch()

curses.endwin()   # End curses mode		  
