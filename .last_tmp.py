import sys
from sys import path as syspath
syspath.append('.//libtcod-1.6.0')
import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
libtcod.console_set_custom_font ('terminal8x8_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Frontier:Scavenger', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
framecount = 0
libtcod.sys_set_fps(LIMIT_FPS)

class actor:

    def __init__(self, name, gender, species, job, x, y, face, color, char, AI, EXPcurr, EXPspent, AGI, STR, INT, STMmax, allegiance, status, fire, drops, mobility, blades, whips, hammers, pistols, rifles, heavyw, thrown, software, hardware, leadership, medicine, pilot, xenology, suit, hnd1, hnd2, visor, shield):
        self.name = name
        self.gender = gender
        self.species = species
        self.x = x
        self.color = color
        self.y = y
        self.face = face
        self.char = char
        self.AI = AI
        self.EXPcurr = EXPcurr
        self.EXPspent = EXPspent
        self.job = job
        self.AGI = AGI
        self.STR = STR
        self.INT = INT
        self.HPmax = STMmax / 2
        self.HPcurr = self.HPmax
        self.STMmax = AGI + STR + INT
        self.STMcurr = self.STMmax
        self.allegiance = allegiance
        self.status = status
        self.fire = fire
        self.drops = list(drops)
        self.movelock = False
        self.sneak = False
        self.swing = 1
        
        #skills
        self.mobility = mobility
        self.blades = blades
        self.hammers = hammers
        self.whips = whips
        self.pistols = pistols
        self.rifles = rifles
        self.heavyw = heavyw
        self.thrown = thrown
        self.software = software
        self.hardware = hardware
        self.leadership = leadership
        self.medicine = medicine
        self.pilot = pilot
        self.xenology = xenology
    
        #equipment
        self.hnd1 = hnd1
        self.hnd2 = hnd2
        self.suit = suit
        self.visor = visor
        self.shield = shield

    #functions
        def move(self, dx, dy):
            if not map[self.x + dx][self.x + dx].blockpass and self.movelock == False:
                self.x += dx
                self.y += dy
                if dx < 0:
                    self.face = 'left'
                    if self == 'player':
                        self.char = '<'
                if dx > 0:
                    self.face = 'right'
                    if self == 'player':
                        self.char = '>'
                if dy < 0:
                    self.face = 'up'
                    if self == 'player':
                        self.char = '^'
                if dx > 0:
                    self.face = 'down'
                    if self == 'player':
                        self.char = 'V'
        def draw (self):
            #draws character in color to con
            libtcod.console_set_default_foreground(con, self.color)
            libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
        def clear (self):
            #Clears character
            libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        def drop(self):
            self.clear()
            actors.remove(self)
            
#Combat Functions
def damage(target, original, hand):
    if original.hand.skill == 'None' and original.hand.sort == 'Melee':    
        original_damage = (original.STR * original.suit.power + original.hand.power)
        target_resist = (target.STR * target.suit.power + target.suit.protection)
        damage_dealt = original_damage - target_resist
        if damage_dealt < 1 :
            target.HPcurr -= 1
        elif damage_dealt >= 1 :
            target.HPcurr = target.HPcurr - damage_dealt
            if target.HPcurr <= 0 :
  		          target.drop()


def collision(target, cx, cy):
    if target.x == cx and target.y == cy:
        return True
#Melee Weapon Functions
def melee_atk(original, hand, facing):
    if original.fire == False:
        original.hand.effect(original, original.facing, hand)
        original.fire = True

def fist_attack(original, facing, weapon):
    if facing == 'up':
        libtcod.console_put_char(con, original.x, original.y - 1, '.', libtcod.BKGND_NONE)
        for object in actors:
            if collision(object, original.x, original.y - 1):
                damage(object, original, weapon)
                object.move(0,-1)
                libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
    if facing == 'down':
        libtcod.console_put_char(con, original.x, original.y + 1, '.', libtcod.BKGND_NONE)
        for object in actors:
  	        if collision(object, original.x, original.y + 1):
  		          damage(object, original, weapon)
                object.move(0,1)
                libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
        if facing == 'left':
            libtcod.console_put_char(con, original.x - 1, original.y, '.', libtcod.BKGND_NONE)
            for object in actors:
  	            if collision(object, original.x - 1, original.y):
  		              damage(object, original, weapon)
                    object.move(-1,0)
                    libtod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
        if facing == 'right':
            libtcod.console_put_char(con, original.x + 1, original.y, '.', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
    original.fire = False

def dagger_attack(original, facing, weapon):
    if facing == 'up':
        libtcod.console_put_char(con, original.x, original.y - 1, '|', libtcod.BKGND_NONE)
        for object in actors:
            if collision(object, original.x, original.y - 1):
                damage(object, original, weapon)
                object.move(0,-1)
                libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
    if facing == 'down':
        libtcod.console_put_char(con, original.x, original.y + 1, '|', libtcod.BKGND_NONE)
        for object in actors:
  	        if collision(object, original.x, original.y + 1):
  		          damage(object, original, weapon)
                object.move(0,1)
                libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
        if facing == 'left':
            libtcod.console_put_char(con, original.x - 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
  	            if collision(object, original.x - 1, original.y):
  		              damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
        if facing == 'right':
            libtcod.console_put_char(con, original.x + 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
    original.fire = False         
#Sword Attack
def sword_attack(original, facing, weapon):  

    if facing == 'up':
        if original.swing == 1:
            original.swing += 1
            libtcod.console_put_char(con, original.x + 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
              if collision(object, original.x + 1, original.y):
                damage(object, original, weapon)
                object.move(0,-1)
                libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y - 1, '/', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(0,-1)
                    libtcod.console_put_char(con, original.x + 1, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x, original.y - 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y - 1):
                    damage(object, original, weapon)
                    object.move(0,-1)
                    libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y - 1, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(0,-1)
                    libtcod.console_put_char(con, original.x - 1, original.y - 1, ' ', libtcod.BKGND_NONE)
    elif original.swing == 2:
        original.swing -= 1
        libtcod.console_put_char(con, original.x - 1, original.y, '_', libtcod.BKGND_NONE)
        for object in actors:
            if collision(object, original.x - 1, original.y):
                damage(object, original, weapon)
                object.move(0,-1)
                libtcod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
                libtcod.console_put_char(con, original.x - 1, original.y - 1, '-', libtcod.BKGND_NONE)
                for object in actors:
                    if collision(object, original.x - 1, original.y - 1):
                        damage(object, original, weapon)
                        object.move(0,-1)
                        libtcod.console_put_char(con, original.x - 1, original.y - 1, ' ', libtcod.BKGND_NONE)
                    libtcod.console_put_char(con, original.x, original.y - 1, '|', libtcod.BKGND_NONE)
                    for object in actors:
                        if collision(object, original.x, original.y - 1):
                            damage(object, original, weapon)
                            object.move(0,-1)
                            libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
                    libtcod.console_put_char(con, original.x + 1, original.y - 1, '_', libtcod.BKGND_NONE)
                    for object in actors:
                        if collision(object, original.x + 1, original.y - 1):
                            damage(object, original, weapon)
                            object.move(0,-1)
                            libtcod.console_put_char(con, original.x + 1, original.y - 1, ' ', libtcod.BKGND_NONE)

    if facing == 'down':
        if original.swing == 1:
            original.swing += 1
            libtcod.console_put_char(con, original.x - 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y):
                    damage(object, original, weapon)
                    object.move(0, 1)
                    libtcod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y + 1, '/', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x - 1, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y + 1, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x + 1, original.y + 1, ' ', libtcod.BKGND_NONE)	         
        elif original.swing == 2:
            original.swing -= 1
            libtcod.console_put_char(con, original.x + 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y + 1, '-', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x + 1, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y + 1, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(0,1)
                    libtcod.console_put_char(con, original.x + 1, original.y + 1, ' ', libtcod.BKGND_NONE)
        
    if facing == 'left':
        if original.swing == 1:
            original.swing += 1
            libtcod.console_put_char(con, original.x, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y + 1):
                    damage(object, original, weapon)
                    object.move(-1, 0)
                    libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y + 1, '/', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y - 1, '/', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y - 1, ' ', libtcod.BKGND_NONE)
        elif original.swing == 2:
            original.swing -= 1
            libtcod.console_put_char(con, original.x, original.y - 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y - 1):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y - 1, '-', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x - 1, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x - 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(-1,0)
                    libtcod.console_put_char(con, original.x - 1, original.y + 1, ' ', libtcod.BKGND_NONE)            
    if facing == 'right':
        if original.swing == 1:
            original.swing += 1
            libtcod.console_put_char(con, original.x, original.y - 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y - 1):
                    damage(object, original, weapon)
                    object.move(1, 0)
                    libtcod.console_put_char(con, original.x, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y - 1, '/', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y - 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y + 1, ' ', libtcod.BKGND_NONE)
        elif original.swing == 2:
            original.swing -= 1
            libtcod.console_put_char(con, original.x, original.y + 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x, original.y + 1):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y + 1, '-', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y + 1):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y + 1, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y, '_', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y, ' ', libtcod.BKGND_NONE)
            libtcod.console_put_char(con, original.x + 1, original.y - 1, '|', libtcod.BKGND_NONE)
            for object in actors:
                if collision(object, original.x + 1, original.y - 1):
                    damage(object, original, weapon)
                    object.move(1,0)
                    libtcod.console_put_char(con, original.x + 1, original.y - 1, ' ', libtcod.BKGND_NONE)
    original.fire = False   
#Whip Attack

#Hammer Attack

#Impact Mace Attack

#Pulse Attack(single shot)
#Script generates list of targets in ~170 degree arc, singles out the closest target within range, then the bottom loop guides the shot towards the closest target, breaking on collision with any Actor or impassable terrain.
                                     
def pulse_attack(original, facing, weapon):
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
        for sx, sy, sd in range(0, weapon.dist):
            if map[(original.x + sx)][original.y + sy].blockpass:
                break
            if sd > weapon.dist:
                break
            if original.closest_target.x < original.x:
                sx -= 1
            if original.closest_target.y < original.y:
                sy -= 1
            if original.closest_target.x > original.x:
                sx += 1
            if original.closest_target.y > original.y:
                sy += 1                         
                libtcod.console_put_char(con, original.x + sx, original.y + sy, '*', libtcod.BKGND_NONE)
                if collision(original.x + sx, original.y + sy):
                    damage(original.closest_target, hand, weapon)
                    libtcod.console_put_char(con, original.x + sx, original.y + sy, ' ', libtcod.BKGND_NONE)  
                    break                                     
                libtcod.console_put_char(con, original.x + sx, original.y + sy, ' ', libtcod.BKGND_NONE)
                sd + 1             
#Laser Attack(line)

#Blast Attack(cone)

#Beam Attack (line, background & foreground)

def do_nothing():
	print 'Unfortunately, this does nothing.'

#item code
def weapon():
    __init__(self, power, dist, skill, sort, hands, effect)
    self.power = power
    self.dist = dist
    self.skill = skill
    self.sort = sort
    self.hands = hands
    self.effect = effect

def suit():
    __init__(self, power, protection)
    self.power = power
    self.protection = protection
    
def visor():
    __init__(self, effect)
    self.effect = effect

def shield():
    __init__(self, powermax, regentime)
    self.powermax = powermax
    self.powercurr = powermax
    self.regentime = regentime

def mapitem():
    __init__(self, ident, x, y, char, color)
    self.ident = ident
    self.x = x
    self.y = y
    self.char = char
    self.color = color
    def draw (self):
        #draws character in color to con
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
    def clear (self):
        #Clears character
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
    def drop(self):
        self.clear()
        mapitems.remove(self)
        
#Melee weapons
weap_fist = weapon(0, 1, 'None', 'Melee', 1, fist_attack())

#Blades
weap_flexiblade = weapon(15, 1, 'blades', 'Melee', 1, sword_attack())
weap_dagger = weapon(5, 1, 'None', 'Blade', 1, dagger_attack())

#Whips

#Hammers

#Ranged Weapons

#Pistols

#Rifles

#Heavy_Weapons

#Suits
suit_skillsuit = suit(1.1, 10)

#Visors
visor_basic = visor(do_nothing())

#Shields
shield_basic = shield(50, 15)

#construct player
player = actor('name', 'gender', 'species', 'job', 0, 0, 'down', libtcod.white, 'V', 'Input', 100, 0, 50, 50, 50, 150, 'Survivors', 'Alive', False, 'drop', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, suit_skillsuit, weap_fist, weap_fist, visor_basic, shield_basic)

print 'Welcome to Frontier: Scavenger!'
player.name = raw_input('What is your name?')
player.gender = raw_input('What is your gender identity?')
player.x = SCREEN_WIDTH/2
player.y = SCREEN_HEIGHT/2
map_WIDTH = 80
map_HEIGHT = 45
color_dark_wall = libtcod.color(66, 33, 0)
color_dark_floor = libtcod.color(99, 0, 0)

#Tiles
def tile():
    __init__(self, blockpass, blocksight = None)
    self.blockpass = blockpass
    if blocksight is None : blocksight = blockpass
    self.blocksight = blocksight
#Map generator
def make_map():
    global map
    
    #Fill with passable tiles
    map = [[tile (False)
        for y in range(map_HEIGHT)]
            for x in range(map_WIDTH)]
    #adjust individual tiles
    map[30][22].blockpass= True
    map[30][22].blocksight = True

def handle_keys ():
    
#Fullscreen and exit keys
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
    #alt enter for fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen ())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True 
    #esc exits

#movement keys
    if libtcod.console_is_key_pressed (libtcod.KEY_CHAR(w)):
        player.move(0,-1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(s)):
        player.move(0,1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(a)):
        player.move(-1,0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(d)):
        player.move(1,0)

#melee attack(player)
    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(m)):
        if player.hnd1.dist == 1 and player.fire == False:
            melee_atk (player, hnd1, player.face)
        elif player.hnd2.dist == 1 and player.fire == False:
            melee_atk (player, hnd2, player.face)
        elif player.hnd1.dist != 1 and player.hnd2.dist != 1:
            fist_attack (player, player.face, fist)
            
#Ranged attack(player)
    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(r)):
        if player.hnd1.dist > 1 and player.fire == False:
            melee_atk (player, hnd1, player.face)
        elif player.hnd2.dist > 1 and player.fire == False:
            melee_atk (player, hnd2, player.face)
        elif player.hnd1.dist == 1 and player.hnd2.dist == 1:
            print 'No ranged weapon equipped!'
 
#rendering
def render_all():
    for object in mapitems:
        object.draw()
    for object in actors:
        object.draw()

    for y in range (map_HEIGHT):
        for x in range(map_WIDTH):
            wall = map [x][y].blocksight
            if wall:
                libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET )
            else:
                libtcod.console_set_char_background(con, x, y, color_dark_floor, libtcod.BKGND_SET )
libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# Incoming main loop 
pbag = actor('Punching Bag', 'Sand', 'Burlap', 'bag', 5, 5, 'down', libtcod.yellow, '@', 'none', 100, 0, 50, 50, 50, 150, 'Burlap', 'Alive', False, 'drop', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, suit_skillsuit, weap_fist, weap_fist, visor_basic, shield_basic)

actors = list(player, pbag)
mapitems = list ()
while not libtcod.is_window_closed():
    framecount += 1
    render_all()
    
    libtcod.console_set_default_foreground(con, libtcod.silver)
    libtcod.console_flush()
    for object in mapitems:
        object.clear()
    for object in actors:
        object.clear()
        
    exit = handle_keys()
    if exit:
        break
#end main loop