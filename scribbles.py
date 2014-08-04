#actor.drop(), line 94
        def drop(self):
            self.clear()
            if not null in self.drop:
                selfdrop = MAPITEM(self.drop, self.x, self.y, '?', libtcod.purple)
            actors.remove(self)
            
#actor.bark(), line 103
        def bark(self):
            #for each self.race, check list of pre-written barks, print out one at random
            if self.allegiance == 'Survivors'   
                barklist = open('.//barks/survivors.txt')
                lines=barklist.readlines()
                ranbark = math.random(1, barklist.length())
                print str(self.name) + ': ' + str(lines[ranbark])



#use, handle_keys, line 949

    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(u)):
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)

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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
                        damage(object, original, hand)
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
 