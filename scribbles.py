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
            else lineatk = animation(original.x, original.y - ly, '|', libtcod.pink)
                ly -= 1            
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
            else lineatk = animation(original.x, original.y + ly, '|', libtcod.pink)
                ly += 1           
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
            else lineatk = animation(original.x - ly, original.y, '-', libtcod.pink)
                ly -= 1      
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
            else lineatk = animation(original.x + ly, original.y, '-', libtcod.pink)
                ly += 1      
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
            else lineatk = animation(original.x + ly, original.y + ly, '*', libtcod.pink)
                ly += 1      
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
            else lineatk = animation(original.x + ly, original.y - ly, '/', libtcod.pink)
                ly += 1      
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
            else lineatk = animation(original.x - ly, original.y + ly, '/', libtcod.pink)
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
            else lineatk = animation(original.x - ly, original.y - ly, '*', libtcod.pink)
                ly += 1      
                lineatks.append(lineatk)
                for object in actors:
                    if collision(object, original.x - ly, original.y - ly):
                        damage(object, original, hand)