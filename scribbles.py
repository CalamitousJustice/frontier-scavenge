#actor.drop(), line 94
        def drop(self):
            self.clear()
            if not null in self.drop:
                selfdrop = MAPITEM(self.drop, self.x, self.y, '?', libtcod.purple)
            actors.remove(self)
            
#actor.bark(), line 103
        def bark(self):
            #for each self.allegiance, check list of pre-written barks, print out one at random
            if self.allegiance == 'Survivors'   
                barklist = open('.//barks/survivors.txt')
                lines = barklist.readlines()
                ranbark = math.random(1, barklist.len())
                print str(self.name) + ': ' + str(lines[ranbark])

#actor.find_closest(), line ~94
        def find_closest(self):
            #determine the closest enemy, set to self.currTarget
            targets = list()
            if facing == 'up':
                for object in actors:
                    if object.y < self.y and object.allegiance != self.allegiance:
                        targets.append(object)
            if facing == 'down':
                for object in actors:
                    if object.y > self.y and object.allegiance != self.allegiance:
                        targets.append(object)
            if facing == 'left':
                    for object in actors:
                        if object.x < self.x and object.allegiance != self.allegiance:
                            targets.append(object)
            if facing == 'right':
                for object in actors:
                    if object.x > self.x and object.allegiance != self.allegiance:
                        targets.append(object)
            target_diff = [self.hnd1.dist, self.hnd1.dist]
            for object in targets:
                object.dist_from_original = [abs(object.x - self.x), abs(object.y - self.y)]
                if object.dist_from_original[1] <= target_diff[1] and object.dist_from_original[2] <= target_diff[2]:
                    self.currTarget = object 


#actor.move_toward(target), line 112
        def move_toward(self, target):
            mx = 0
            my = 0
            #Calc path to target, take step to decrease distance between
            if target.x > self.x:
                mx += 1
            if target.y > self.y:
                my += 1
            if target.x < self.x:
                mx -= 1
            if target.y < self.y:
                my -= 1
            if mx > 0:
                self.face = 'right'
            if mx < 0:
                self.face = 'left'
            if my > 0:
                self.face = 'down'
            if my < 0:
                self.face = 'up'
            self.move(mx, my)

#actor.move_away(target), line 125
        def move_away(self, target):
            mx = 0
            my = 0
            #Calc path to target, take step to decrease distance between
            if target.x > self.x:
                mx -= 1
            if target.y > self.y:
                my -= 1
            if target.x < self.x:
                mx += 1
            if target.y < self.y:
                my += 1
            if mx > 0:
                self.face = 'right'
            if mx < 0:
                self.face = 'left'
            if my > 0:
                self.face = 'down'
            if my < 0:
                self.face = 'up'
            self.move(mx, my)
#Aimed atk, combat functions, line 104
def aimed_atk(target, original, weapon):
    player.fire = True
    if weapon.effect.str() == 'pulse_attack()':
        for sx, sy, sd in range(1, weapon.dist + 1):
            if map[(original.x + sx)][original.y + sy].blockpass:
                break
            if sd > weapon.dist:
                break
            if target.x < original.x:
                sx -= 1
            if target.y < original.y:
                sy -= 1
            if target.x > original.x:
                sx += 1
            if target.y > original.y:
                sy += 1                         
            libtcod.console_put_char(con, player.x + sx, player.y + sy, '*', libtcod.pink, libtcod.BKGND_NONE)
            if collision(original.x + sx, original.y + sy):
                damage(target, original, weapon)
                libtcod.console_put_char(con, original.x + sx, original.y + sy, ' ', libtcod.BKGND_NONE)  
                break                                     
            libtcod.console_put_char(con, original.x + sx, original.y + sy, ' ', libtcod.BKGND_NONE)
            sd + 1
    if weapon.effect.str() == 'line_attack()':            
        lineatks = list()
        for sx, sy, sd in range(1, weapon.dist + 1):
            if map[(original.x + sx)][original.y + sy].blockpass:
                for object in lineatks:
                    lineatks.remove(object)
                    object.drop()
                break
            if sd > weapon.dist:
                for object in lineatks:
                    lineatks.remove(object)
                    object.drop()
                break
            if target.x < original.x:
                sx -= 1
            if target.y < original.y:
                sy -= 1
            if target.x > original.x:
                sx += 1
            if target.y > original.y:
                sy += 1                         
            lineatk = ANIMATION(original.x + sx, original.y + sy, '*', libtcod.pink)
            lineatk.draw()
            lineatks.append(lineatk)
            for object in actors:
                if collision(object, original.x, original.y - ly):
                    damage(object, original, weapon)
            sd + 1
    if weapon.effect.str() == 'beam_attack()':            
        beamatks = list()
        for sx, sy, sd in range(1, weapon.dist + 1):
            if map[(original.x + sx)][original.y + sy].blockpass:
                for object in beamatks:
                    beamatks.remove(object)
                    object.drop()
                break
            if sd > weapon.dist:
                for object in beamatks:
                    beamatks.remove(object)
                    object.drop()
                break
            if target.x < original.x:
                sx -= 1
            if target.y < original.y:
                sy -= 1
            if target.x > original.x:
                sx += 1
            if target.y > original.y:
                sy += 1                         
            beamatk = ANIMATION(original.x + sx, original.y + sy, ' ', libtcod.yellow)
            beamatk.draw()
            beamatks.append(beamatk)
            for object in actors:
                if collision(object, original.x, original.y - ly):
                    damage(object, original, weapon)
            sd + 1

            
#use, aim, break_aim, handle_keys, line 949
    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(x)) and game_state == 'playing':
       player.currTarget = 'None'
       player.aimWeap = 'None'
        
    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(f)) and game_state == 'playing':
        if player.currTarget = 'None':
            targets = list()
            for object in actors:
                object.dist_from_original = [abs(object.x - original.x), abs(object.y - original.y)]
                target_diff = [weapon.dist, weapon.dist]
                if object.allegiance != player.allegiance and not object.dist_from_original[1] <= target_diff[1] and object.dist_from_original[2] <= target_diff[2]:
                    targets.append(object)
            targetmenu = True
#Choose Your Target
            for targetmenu = True:
                if targets.len() > 0:
                     for x, object in targets:
                         print str(x) + ". " + object.name
                         x + 1
                     choose_target = raw_input('Choose a Target(#) or (N)one')
                     if choose_target == int:
                         if choose_target > targets.len() or choose_target < 1:
                             print 'Invalid target!'
                         else for x in range(1, targets.len()):
                             if choose_target = x:
                                 player.currTarget = targets[x]
                                 targetmenu = False
                     elif choose_target.upr() == 'N':
                         targetmenu = False
                     elif choose_target.upr() != 'N':
                         print "Invalid target!"
        if player.currTarget != 'None':
            if player.aimWeap == 'None':
                weapons = list(player.hnd1, player.hnd2)
                for object in weapons:
                    print str(x) + '. ' + str(weapons[x].name)
                weaponmenu = True
                for weaponmenu = True:
                    choose_weapon = raw_input('Choose a weapon to aim.')
                    if choose_weapon == 1:
                        player.aimWeap = player.hnd1
                        weaponmenu = False
                    elif choose_weapon == 2:
                        player.aimWeap = player.hnd2
                        weaponmenu = False
                    else print 'Invalid weapon!'
            if player.aimWeap != 'None':
                if player.currTarget.x < player.x:
                    player.face = 'left'
                    player.char = '<'
                if player.currTarget.x > player.x:
                    player.face = 'right'
                    player.char = '>'
                if player.currTarget.y < player.y:
                    player.face = 'up'
                    player.char = '^'
                if player.currTarget.y > player.y:
                    player.face = 'down'
                    player.char = 'v'
                if player.aimWeap.sort == 'Melee' and player.fire == False:
                    melee_atk (player, player.aimWeap, player.face)
                    player.fire = False
                elif player.aimWeap.sort == 'Ranged' and player.fire == False:
                    aimed_atk (player.currTarget, player, player.aimWeap)
                    player.fire = False

    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(u)) and game_state == 'playing':
        if player.face == 'up':
            for object in actors:
                if collison(object, player.x, player.y - 1):
                    object.bark()
                    break
            for object in mapitems:
                if collison(object, player.x, player.y - 1):
                    item-menu = True
                    for item-menu == True:
                        lootlist = list()
                        for object in mapitems:
                            lootlist.append(object)
                        for x < lootlist.items() in lootlist:
                            print str(x) + ". " + str(lootlist[x].name)
                        lootchoice = raw_input("Take (#), (A)ll, or (N)one?")
                        if not lootchoice == int or not lootchoice.upper() == 'A' or not lootchoice.upper() == 'N':
                                print "Invalid option!"
                            if lootchoice.upper() == 'A':
                            for object in lootlist:
                                player.drops.append(object)
                                item-menu = False
                            if lootchoice.upper() == 'N':
                                item-menu = False
                            if lootchoice == int:
                                player.drops.append(lootlist[lootchoice])
                                lootlist.remove([lootchoice])
            for object in events:
                if collison(object, player.x, player.y - 1):
                    object.use()
        if player.face == 'down':
            for object in actors:
                if collison(object, player.x, player.y + 1):
                    object.bark()
                    break
            for object in mapitems:
                if collison(object, player.x, player.y + 1):
                    item-menu = True
                    for item-menu == True:
                        lootlist = list()
                        for object in mapitems:
                            lootlist.append(object)
                        for x < lootlist.items() in lootlist:
                            print str(x) + ". " + str(lootlist[x].name)
                        lootchoice = raw_input("Take (#), (A)ll, or (N)one?")
                        if not lootchoice == int or not lootchoice.upper() == 'A' or not lootchoice.upper() == 'N':
                                print "Invalid option!"
                            if lootchoice.upper() == 'A':
                            for object in lootlist:
                                player.drops.append(object)
                                item-menu = False
                            if lootchoice.upper() == 'N':
                                item-menu = False
                            if lootchoice == int:
                                player.drops.append(lootlist[lootchoice])
                                lootlist.remove([lootchoice])
            for object in events:
                if collison(object, player.x, player.y + 1):
                    object.use()
                    
        if player.face == 'left':
            for object in actors:
                if collison(object, player.x - 1, player.y):
                    object.bark()
                    break
            for object in mapitems:
                if collison(object, player.x - 1, player.y):
                    item-menu = True
                    for item-menu == True:
                        lootlist = list()
                        for object in mapitems:
                            lootlist.append(object)
                        for x < lootlist.items() in lootlist:
                            print str(x) + ". " + str(lootlist[x].name)
                        lootchoice = raw_input("Take (#), (A)ll, or (N)one?")
                        if not lootchoice == int or not lootchoice.upper() == 'A' or not lootchoice.upper() == 'N':
                                print "Invalid option!"
                            if lootchoice.upper() == 'A':
                            for object in lootlist:
                                player.drops.append(object)
                                item-menu = False
                            if lootchoice.upper() == 'N':
                                item-menu = False
                            if lootchoice == int:
                                player.drops.append(lootlist[lootchoice])
                                lootlist.remove([lootchoice])
            for object in events:
                if collison(object, player.x - 1, player.y):
                    object.use()                    
                    
        if player.face == 'right':
            for object in actors:
                if collison(object, player.x + 1, player.y):
                    object.bark()
                    break
            for object in mapitems:
                if collison(object, player.x + 1, player.y):
                    item-menu = True
                    for item-menu == True:
                        lootlist = list()
                        for object in mapitems:
                            lootlist.append(object)
                        for x < lootlist.items() in lootlist:
                            print str(x) + ". " + str(lootlist[x].name)
                        lootchoice = raw_input("Take (#), (A)ll, or (N)one?")
                        if not lootchoice == int or not lootchoice.upper() == 'A' or not lootchoice.upper() == 'N':
                                print "Invalid option!"
                            if lootchoice.upper() == 'A':
                            for object in lootlist:
                                player.drops.append(object)
                                item-menu = False
                            if lootchoice.upper() == 'N':
                                item-menu = False
                            if lootchoice == int:
                                player.drops.append(lootlist[lootchoice])
                                lootlist.remove([lootchoice])
            for object in events:
                if collison(object, player.x + 1, player.y):
                    object.use()
#Line atks, line 774

def line_attack(original, facing, weapon):
    targets = list()
    if facing == 'up':
        for object in actors:
            if object.y < original.y and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'down':
        for object in actors:
            if object.y > original.y and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'left':
        for object in actors:
            if object.x < original.x and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'right':
        for object in actors:
            if object.x > original.x and object.allegiance != original.allegiance:
                targets.append(object)
    target_diff = [weapon.dist, weapon.dist]
    for object in targets:
        object.dist_from_original = [abs(object.x - original.x), abs(object.y - original.y)]
        if object.dist_from_original[1] <= target_diff[1] and object.dist_from_original[2] <= target_diff[2]:
            original.closest_target = object 
        #up
    lineatks = list()
    if original.closest_target.x == original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)                
            if map[original.x][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                    break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                    break
            else lineatk = ANIMATION(original.x, original.y - ly, '|', libtcod.pink)
                ly -= 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x, original.y - ly):
                        damage(object, original, weapon)
    #down
    if original.closest_target.x == original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x, original.y + ly, '|', libtcod.pink)
                ly += 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x, original.y + ly):
                        damage(object, original, weapon)
    #left
    if original.closest_target.x < original.x and original.closest_target.y == original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x - ly, original.y, '-', libtcod.pink)
                ly -= 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y):
                        damage(object, original, weapon)
    #right
    if original.closest_target.x > original.x and original.closest_target.y == original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x + ly, original.y, '-', libtcod.pink)
                ly += 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y):
                        damage(object, original, weapon)
    #diagonal right-down
    if original.closest_target.x > original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x + ly, original.y + ly, '*', libtcod.pink)
                ly += 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y + ly):
                        damage(object, original, weapon)
    #Diagonal right-up                    
    if original.closest_target.x > original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x + ly, original.y - ly, '/', libtcod.pink)
                ly += 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y - ly):
                        damage(object, original, weapon)
    #diagonal left-down
    if original.closest_target.x < original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x - ly, original.y + ly, '/', libtcod.pink)
                ly += 1
                lineatk.draw()
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y + ly):
                        damage(object, original, weapon)
    #Diagonal left-up                    
    if original.closest_target.x < original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) or abs(lx) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else lineatk = ANIMATION(original.x - ly, original.y - ly, '*', libtcod.pink)
                ly += 1      
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y - ly):
                        damage(object, original, weapon)

#Beam atks

def beam_attack(original, facing, weapon):
    
    targets = list()
    if facing == 'up':
        for object in actors:
            if object.y < original.y and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'down':
        for object in actors:
            if object.y > original.y and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'left':
        for object in actors:
            if object.x < original.x and object.allegiance != original.allegiance:
                targets.append(object)
    if facing == 'right':
        for object in actors:
            if object.x > original.x and object.allegiance != original.allegiance:
                targets.append(object)
    target_diff = [weapon.dist, weapon.dist]
    for object in targets:
        object.dist_from_original = [abs(object.x - original.x), abs(object.y - original.y)]
        if object.dist_from_original[1] <= target_diff[1] and object.dist_from_original[2] <= target_diff[2]:
            original.closest_target = object 
        #up
    lineatks = list()
    if original.closest_target.x == original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)                
            if map[original.x][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                    break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                    break
            else beamatk = ANIMATION(original.x, original.y - ly, ' ', libtcod.yellow)
                ly -= 1            
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x, original.y - ly):
                        damage(object, original, weapon)
    #down
    if original.closest_target.x == original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x, original.y + ly, ' ', libtcod.yellow)
                ly += 1           
                lineatks.append(beamatk)
                beamatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + ly):
                        damage(object, original, weapon)
    #left
    if original.closest_target.x < original.x and original.closest_target.y == original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x - ly, original.y, ' ', libtcod.yellow)
                ly -= 1
                beamatk.draw()
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y):
                        damage(object, original, weapon)
    #right
    if original.closest_target.x > original.x and original.closest_target.y == original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x + ly, original.y, ' ', libtcod.yellow)
                ly += 1
                beamatk.draw()
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y):
                        damage(object, original, weapon)
    #diagonal right-down
    if original.closest_target.x > original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x + ly, original.y + ly, ' ', libtcod.yellow)
                ly += 1
                beamatk.draw()
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y + ly):
                        damage(object, original, weapon)
    #Diagonal right-up                    
    if original.closest_target.x > original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)
            if map[original.x + ly][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x + ly, original.y - ly, ' ', libtcod.yellow)
                ly += 1
                beamatk.draw()
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x + ly, original.y - ly):
                        damage(object, original, weapon)
    #diagonal left-down
    if original.closest_target.x < original.x and original.closest_target.y > original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y + ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x - ly, original.y + ly, ' ', libtcod.yellow)
                ly += 1      
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y + ly):
                        damage(object, original, weapon)
    #Diagonal left-up                    
    if original.closest_target.x < original.x and original.closest_target.y < original.y:
        for ly in range(1, weapon.dist)
            if map[original.x - ly][original.y - ly].blockpass:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            if abs(ly) or abs(lx) > hand.dist:
                for object in lineatks:       
                    lineatks.remove(object)
                    object.clear()
                break
            else beamatk = ANIMATION(original.x - ly, original.y - ly, ' ', libtcod.yellow)
                ly += 1
                beamatk.draw()
                lineatks.append(beamatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y - ly):
                        damage(object, original, weapon)
#evolving fist attack - line 125. Level 1 adds a hooking motion to the animation, level 3 adds an extra swing if the first hits and a movement forward, level 5 adds a third hit that can instantly kill.
def fist_attack(original, facing, weapon):
    if facing == 'up':
        if original.swing == 1:
            swing += 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x - 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x - 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
        if original.swing == 2:
            swing -= 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x + 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x + 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
            if combo == True:
                original.move(0,-1)
                fist_attack(original, facing, weapon)
            if combo2 == True:
                original.move(0,-1)
                fistatk = ANIMATION(original.x - 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x + 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                combo2 = False
    if facing == 'down':
        if original.swing == 1:
            swing += 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x + 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x + 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
        if original.swing == 2:
            swing -= 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x - 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x - 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
            if combo == True:
                original.move(0,1)
                fist_attack(original, facing, weapon)
            if combo2 == True:
                original.move(0,1)
                fistatk = ANIMATION(original.x + 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x - 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(0,1)
                        object.status = 'Deathblow'
                        fistatk.clear()
                combo2 = False
    if facing == 'left':
        if original.swing == 1:
            swing += 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y - 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x - 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x - 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
        if original.swing == 2:
            swing -= 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x - 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x - 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
            if combo == True:
                original.move(-1,0)
                fist_attack(original, facing, weapon)
            if combo2 == True:
                original.move(-1,0)
                fistatk = ANIMATION(original.x - 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x - 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x - 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x - 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(-1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                combo2 = False
    if facing == 'right':
        if original.swing == 1:
            swing += 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y + 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x + 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x + 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
        if original.swing == 2:
            swing -= 1
            if original.unarmed >= 1:
                fistatk = ANIMATION(original.x, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x, original.y - 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            combo = True
                fistatk = ANIMATION(original.x + 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False
                                if unarmed >= 5:
                                    combo2 = True
                            else combo = True
            if original.unarmed >= 0:
                fistatk = ANIMATION(original.x + 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y):
                        damage(object, original, weapon)
                        object.move(1,0)
                        fistatk.clear()
                        if unarmed >= 3:
                            if combo == True:
                                combo = False     
                            else combo = True
            if combo == True:
                original.move(1,0)
                fist_attack(original, facing, weapon)
            if combo2 == True:
                original.move(1,0)
                fistatk = ANIMATION(original.x + 1, original.y - 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x + 1, original.y, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y):
                        damage(object, original, weapon)
                        object.move(1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                fistatk = ANIMATION(original.x + 1, original.y + 1, '.', libtcod.silver)
                fistatk.draw()
                for object in actors:
                    if collision(object, original.x + 1, original.y + 1):
                        damage(object, original, weapon)
                        object.move(1,0)
                        object.status = 'Deathblow'
                        fistatk.clear()
                combo2 = False
    original.fire = False

#map code, line 893

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

color_light_wall = libtcod.Color(132, 66, 25)
color_light_floor = libtcod.Color(200, 90, 50)
color_dark_wall = libtcod.color(66, 33, 0)
color_dark_floor = libtcod.color(99, 0, 0)

fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        libtcod.map_set_properties(fov_map, x, y, not map[x][y].block_sight, not map[x][y].blocked)

class RECT:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1)
class CIRCLE:
    #a circle on the map. used to characterize a room.
    def __init__(self, x, y, r):
        self.x1 = x
        self.y1 = y
        self.x2 = x + r
        self.y2 = y + r
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1)

      
      
def create_room(room):
    global map
    #go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            map[x][y].blocked = False
            map[x][y].block_sight = False         
def create_circle(room):
    global map
    #go through the tiles in the rectangle and make them passable
    for x in range(room.center_x - r + 1, room.center_x + r):
        for y in range(room.center_y - r + 1, room.center_y + r):
            map[x][y].blocked = False
            map[x][y].block_sight = False         

def create_h_tunnel(x1, x2, y):
    global map
    #Horizontal tunnel - 2 tiles wide
    for x in range(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False
        map[x][y + 1].blocked = False
        map[x][y + 1].block_sight = False        
def create_v_tunnel(y1, y2, x):
    global map
    #vertical tunnel - 2 tiles wide
    for y in range(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False
        map[x + 1][y].blocked = False
        map[x + 1][y].block_sight = False
#Make_map, line 894
def make_map():
    global map
    rooms = []
    num_rooms = 0    
    #Fill with unpassable tiles
    map = [[TILE (True)
        for y in range(map_HEIGHT)]
            for x in range(map_WIDTH)]
        #go through all tiles, and set their background color according to the FOV
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = map[x][y].block_sight
                if not visible:
                    #it's out of the player's FOV
                    if wall:
                        libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)
                else:
                    #it's visible
                    if wall:
                        libtcod.console_set_char_background(con, x, y, color_light_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_char_background(con, x, y, color_light_ground, libtcod.BKGND_SET )
    for r in range(MAX_ROOMS):
        #random width and height
        w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        #random position without going out of the boundaries of the map
        x = libtcod.random_get_int(0, 0, MAP_WIDTH - w - 1)
        y = libtcod.random_get_int(0, 0, MAP_HEIGHT - h - 1)
        #"Rect" class makes rectangles easier to work with
        new_room = Rect(x, y, w, h)
        
        #run through the other rooms and see if they intersect with this one
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break
        if not failed:
            #this means there are no intersections, so this room is valid
            #"paint" it to the map's tiles
            create_room(new_room)
            #center coordinates of new room, will be useful later
            
            (new_x, new_y) = new_room.center()
            if num_rooms == 0:
                #this is the first room, where the player starts at
                player.x = new_x
                player.y = new_y
            else:
                #all rooms after the first:
                #connect it to the previous room with a tunnel
                #center coordinates of previous room
                (prev_x, prev_y) = rooms[num_rooms-1].center()
                #draw a coin (random number that is either 0 or 1)
                if libtcod.random_get_int(0, 0, 1) == 1:
                    #first move horizontally, then vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    #first move vertically, then horizontally
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)
            #add some contents to this room, such as monsters
            place_objects(new_room)
            #finally, append the new room to the list
            rooms.append(new_room)
            num_rooms += 1

# Field of View
FOV_ALGO = FOV_DIAMOND  #default FOV algorithm
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

#render_all , line 948
def render_all():
    global fov_map, color_dark_wall, color_light_wall
    global color_dark_floor, color_light_floor
    global fov_recompute
    
    if fov_recompute:
        #recompute FOV if needed (the player moved or something)
        fov_recompute = False
        libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)
        #go through all tiles, and set their background color according to the FOV
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = map[x][y].block_sight
                if not visible:
                    #if it's not visible right now, the player can only see it if it's explored
                    if map[x][y].explored:
                        if wall:
                            libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
                        else:
                            libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)
                else:
                    #it's visible
                    if wall:
                        libtcod.console_set_char_background(con, x, y, color_light_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_char_background(con, x, y, color_light_ground, libtcod.BKGND_SET )
                    #since it's visible, explore it
                    map[x][y].explored = True

#Monster spawning
def place_objects(room):
    #choose random number of monsters
    num_monsters = libtcod.random_get_int(0, 0, MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        #choose random spot for this monster
        x = libtcod.random_get_int(0, room.x1, room.x2)
        y = libtcod.random_get_int(0, room.y1, room.y2)
        if not is_blocked(x, y):
            if libtcod.random_get_int(0, 0, 100) < 80:  #80% chance
                 #Monster spawn
            else:
            

        actors.append(monster)

#Skills and Skill Menu, find line

def build_ability_list()
self.abilities = list()
    for key, x <= SKILLS.len() in self:
        if key == str(SKILLS[x])
            if self.key >= 1:
                self.abilities.append(SKILLS[x].ability1)
            if self.key >= 3:
                self.abilities.append(SKILLS[x].ability2)
            if self.key >= 5:
                self.abilities.append(SKILLS[x].ability3)
        x + 1
def SKILL():
    __init__(self, name, description, xp_cost, ability1, ability2, ability3, keystat)
    self.name = name
    self.description = description
    self.xp_cost = xp_cost
    self.ability1 = ability1
    self.ability2 = ability2
    self.ability3 = ability3
    self.keystat = keystat
#Weapon skills    
unarmed = SKILL('Unarmed', 'Power of Fist + 5 * skill level. DMG + 5% per skill level.', 20, hook, combo, northstarpalm, 'STR')

blades = SKILL('Blades', 'DMG + 5% per skill level.', 20, parry, dualwield, whirl, 'STR')

hammers = SKILL('Hammers', 'DMG + 5% per skill level.', 20, rush, mechanicalstrike, deathblow, 'STR')

whips = SKILL('Whips', 'DMG + 5% per skill level.', 20, disarm, swing, entangle, 'STR')

pistols = SKILL('Pistols', 'DMG + 5% per skill level.', 20, speedreload, dualfire, maelstrom, 'AGI')

rifles = SKILL('Rifles', 'DMG + 5% per skill level.', 20, takeaim, doubletap, headshot, 'AGI')

heavyw = SKILL('Heavy Weapons', 'DMG + 5% per skill level.', 20, ammosave, discharge, overclock, 'AGI')

thrown = SKILL('Thrown Weapons', 'DMG + 5% per skill level.', 15, longarm, twohand, masterblaster, 'STR')

#Accessory Skills
mobility = SKILL('Mobility', '5% chance per skill level to dodge ranged attacks.', 15, backpedal, dodgeroll, hitandrun, 'AGI')

software = SKILL('Software', 'Shield power + 10 per skill level.', 15, disengage, disable, control, 'INT')

hardware = SKILL('Hardware', 'Damage + 10% per skill level against artificial targets.', repair, turret, autoguard, 'INT')

leadership = SKILL('Leadership','Allies within range gain +10 AGI/STR per skill level.', concentratefire, retreat, entourage, 'INT')

medicine = SKILL('Medicine', 'Effectiveness of healing items + 5% per skill level.', firstaid, synthmed, synthbuffs, 'INT')

pilot = SKILL('Pilot', 'Stat bonuses +5% per skill level with any Mech equipped.', boost, abil2, trumpcard, 'INT')

xenology = SKILL('Xenology', 'Expanded information on alien foes.', language, biology, technology, 'INT' )

stealth = SKILL('Stealth', 'Increases enemy reaction times.', sneak, sneakattack, assassinate, 'AGI')

SKILLS = list(blades, hammers, whips, thrown, heavyw, rifles, pistols, mobility, unarmed, stealth, xenology, hardware, software, pilot, medicine, leadership)

#Abilities
def ABILITY():
    __init__(self, name, skill, key, cost, effect, desc)
    self.name = name
    self.skill = skill
    self.key = key
    self.cost = cost
    self.effect() = effect
    self.desc = desc
#Weapon abilities
ammosave = ABILITY('Ammo Save', heavyw, 'None', 0, do_nothing(), 'Adds 2 charges per battery per skill level.')

combo = ABILITY('Combo', unarmed, 'None', 0, do_nothing(), 'Adds additional hit upon successful unarmed attack.')

deathblow = ABILITY('Deathblow', hammers, 'None', 25, do_nothing(), 'Activate to make a hammer swing that instantly kills most enemies.' )

disarm = ABILITY('Disarm', whips, 'None', 15, do_nothing(), 'Activate to remove equipped weapon of any actor hit.')

discharge = ABILITY('Discharge', heavyw, 'None', 25, do_nothing(), 'Activate to hit all adjacent enemies with heat discharge.')

doubletap = ABILITY('Double Tap', rifles, 'None', 0, do_nothing(), 'Successful hit with any rifle weapon triggers a second shot.')

dualfire = ABILITY('Dual-Fire', pistols, 'None', 0, do_nothing(), 'Adds additional shot with two pistols equipped.')

dualwield = ABILITY('Dual-Wield', blades, 'None', 0, do_nothing(), 'Can attack with two blades per swing.')

entangle = ABILITY('Entangle', whips, 'None', 25, do_nothing(), 'Activate to stop an enemy from moving, dealing damage over time while the whip remains attached.')

headshot = ABILITY('Headshot', rifles, 'None', 0, do_nothing(), '25% chance to instantly kill most enemies.')

hook = ABILITY('Hook', unarmed, 'None', 0, do_nothing(), 'Extends reach of unarmed attacks.')

longarm = ABILITY('Long Arm', thrown, 'None', 0, do_nothing(), 'Increases range of thrown weapons by skill level.')

maelstrom = ABILITY('Maelstrom', pistols, 'None', 25, do_nothing(), 'Activate to fire at all targets in range until out of ammo.')

masterblaster = ABILITY('Master Blaster', thrown, 'None', 0, do_nothing(), 'Increases blast radius of grenade-like weapons.')

mechanicalstrike = ABILITY('Mechanical Strike', hammers, 'None', 0, do_nothing(), 'Successful attacks with hammers inflict an additional hit.')

northstarpalm = ABILITY('North Star Palm', unarmed, 'None', 0, do_nothing(), 'Adds a third hit to successful unarmed comboes. This hit can instantly kill most enemies.')

overclock = ABILITY('Overclock', heavyw, 'None', 30, do_nothing(), 'Activate to fire a shot, with the damage multiplied by the number of charges remaining on the current battery.')
                    
parry = ABILITY('Parry', blades, 'None', 0, do_nothing(), '5% * skill level chance to evade melee attacks.')

rush = ABILITY('Rush', hammers, 'None', 25, do_nothing(), 'Activate to damage and push all enemies forward up to 3 spaces.')

speedreload = ABILITY('Speed Reload', pistols, 'None', 0, do_nothing(), 'Automatically reloads when ammo reaches 0.')

swing = ABILITY('Swing', whips, 'None', 10, do_nothing(), 'Swings whip in chosen direction, if collides with wall or object, move actor to that point. Range = skill level.')

takeaim = ABILITY('Take Aim', rifles, 'None', 10, do_nothing(), 'Activate to stop movement and take aim. Damage increases depending on time spent standing still.')

twohand = ABILITY('Two Hand Throw', thrown, 'None', 0, do_nothing(), 'Throws an additional weapon if availible.')

whirl = ABILITY('Whirl', blades, 'None', 25, do_nothing(), 'Activate to hit all adjacent enemies and move forward up to 3 spaces.')
                    
                    
#Enemy AI Functions
#Just remember to duplicate this:
            if object.wait > 0:  #don't take a turn yet if still waiting
            object.wait -= 1
            return