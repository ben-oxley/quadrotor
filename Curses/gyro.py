import curses

myscreen = curses.initscr()
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
#myscreen.addstr(23, 2,"       :sso-` `-+os/         .-.` .-:/:`..`                 `o+:                  ``..//::`         ")
#myscreen.addstr(24, 2,"         `:+s/ys/.                     ``  ```              `+/:               ```  ````            ")
#myscreen.addstr(25, 2,"       `:-+oo:oo+//:..`                  ````` ```          `+/:           ```  ````                ")
#myscreen.addstr(26, 2,"     `./+oo:::--oooo:----`             ``.`.` ````          `o/:           ````     ```````         ")
#myscreen.addstr(27, 2,"  `......:+/:////--..-:::-.`           `````````           .-o+/.                    ......         ")
#myscreen.addstr(28, 2," `--.-o+/:.- `:-//+/::-:::.`..`                            `+oo+`                                   ")
#myscreen.addstr(29, 2," `- -`.`/sy+/.-.`.:/::-:::--...                              //                                     ")
#myscreen.addstr(30, 2,"  .`-   ``-/+o--..-:/-/--..--.`                                                                     ")
#myscreen.addstr(31, 2,"    ````   ``..::``..``.-.``..`                                                                     ")
#myscreen.addstr(32, 2,"        ```   `..-`.--.``..`                                       //---`:`-.:.-..-.:.:`.:: -.      ")
#myscreen.addstr(33, 2,"            ```. : . `..`                                         `:-::--::-::-:.:-.:-:`./- ..      ")
#myscreen.addstr(34, 2,"..:.---..----  ``-`..`                                                                              ")

myscreen.refresh()
myscreen.getch()

curses.endwin()
                     -+syhdddhyyo/-` -/oyyhhdhys+-                    
                  `sNMMNhsoo+osymMMMNMMho/:---:+smd+`                 
                 :NMMy:      `/yNNhsyhNMh+`      `+md-                
                .NMN:     `/hmms/`.dN:`-sdms-      -mm-               
                sMM/    .omms:`  .yMMd-  `:ymh:     :Nh               
              `:dMm   .sNd+.      `NN/      -yNh-    dN-:`            
               oMMd.`oNm+-.-:.     Nm/     --./dNo` -yMm+             
                yMmydNy::--.`      Nd/      `.-:oNd-+mMs              
                .dyNd:--``-`       md/        `--/mNs:o`     `.:`     
         :/+o+.:ymMNh`    ```      ..++::::-....  .hMdsyo. `++:.      
         ``.-:..hMddms.   ``  -+++oysssysooo/oo/ `.hMMNy/....`        
        `.-...-yMy://+/:--//: -::////:s+:-.-/sy+:/sh+dMs-.```..``     
      `-....`.+Mm-.-..``-yhs/.``-:/+//++o:/:--+hh..-:/mM+-.......-    
       ``     dM/       hy` `.::+::/-//::+o+.` :N:    :MN-`-//+++:-`  
             .MN`       do    -so+``:-.:oo`   `sd`     yMs ``````     
             /Md``      :h+.  :yoo:--:/+ys- .oys.      :MN`           
  .--.``     sMNs`       `/yooyhs/-...-+yhs::/-`      .:MM/      ``.-.
   `.--...``omMm.     `.---..:hy++++ssooyh/ `.--.``    sNMs. ``...-.``
    ..`..-..:oN/``...--.`    :yo.---....+y-     `.--.```dMN+-..-.:.   
   `.  `-//+ysyyhho.`        /:`...//-.` --         `-oohdyss-`   ..  
       /:. .+yyo.:-.`              Nm/               `.--yhho.    .`  
      `..``    ---.`--.`           mm/           `...``.-.`     `..   
     ```-----.--.:..-..--`         Nd/         ......:-`........`     
     ```````    ++++o/::`         `mm/          .`    `.:ssso+        
      `````                      `yNNd-                  `````        
                                  `yd.                                
                                    `                                 
myscreen.addstr(1, 2,"                     -+syhdddhyyo/-` -/oyyhhdhys+-                    ")
myscreen.addstr(2, 2,"                  `sNMMNhsoo+osymMMMNMMho/:---:+smd+`                 ")
myscreen.addstr(3, 2,"                 :NMMy:      `/yNNhsyhNMh+`      `+md-                ")
myscreen.addstr(4, 2,"                .NMN:     `/hmms/`.dN:`-sdms-      -mm-               ")
myscreen.addstr(5, 2,"                sMM/    .omms:`  .yMMd-  `:ymh:     :Nh               ")
myscreen.addstr(6, 2,"              `:dMm   .sNd+.      `NN/      -yNh-    dN-:`            ")
myscreen.addstr(7, 2,"               oMMd.`oNm+-.-:.     Nm/     --./dNo` -yMm+             ")
myscreen.addstr(8, 2,"                yMmydNy::--.`      Nd/      `.-:oNd-+mMs              ")
myscreen.addstr(9, 2,"                .dyNd:--``-`       md/        `--/mNs:o`     `.:`     ")
myscreen.addstr(10, 2,"         :/+o+.:ymMNh`    ```      ..++::::-....  .hMdsyo. `++:.      ")
myscreen.addstr(11, 2,"         ``.-:..hMddms.   ``  -+++oysssysooo/oo/ `.hMMNy/....`        ")
myscreen.addstr(12, 2,"        `.-...-yMy://+/:--//: -::////:s+:-.-/sy+:/sh+dMs-.```..``     ")
myscreen.addstr(13, 2,"      `-....`.+Mm-.-..``-yhs/.``-:/+//++o:/:--+hh..-:/mM+-.......-    ")
myscreen.addstr(14, 2,"       ``     dM/       hy` `.::+::/-//::+o+.` :N:    :MN-`-//+++:-`  ")
myscreen.addstr(15, 2,"             .MN`       do    -so+``:-.:oo`   `sd`     yMs ``````     ")
myscreen.addstr(16, 2,"             /Md``      :h+.  :yoo:--:/+ys- .oys.      :MN`           ")
myscreen.addstr(17, 2,"   __ oo-__      .o-    `/::.`````.:/.    `/+`      .oo.             ")
myscreen.addstr(18, 2," \\\  .oo.. //     .+/.  `::....```.:-:  .oo:         +o/             ")
myscreen.addstr(19, 2,"  \\\ -ooo.//        .//+///.    ``.:o+:```         `:+oo         ````")
myscreen.addstr(20, 2,"`` \\\ooo-//     `````   :::::::::::-::`  `````      -oos.    ``````  ")
myscreen.addstr(21, 2,"`` ``\+:/   `````      `:-``````  `.-:       `````   :oo+.`` ```     ")
myscreen.addstr(22, 2,"`-`---\///:-`          .- ````..``   -           ``:-:o/.--`         ")