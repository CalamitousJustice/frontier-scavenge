import libtcodpy as libtcod
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
libtcod.console_set_custom_font ('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TC0D)
libtcod.init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Frontier:Scavenger', false)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
libtcod.sys_set_fps(LIMIT_FPS)

class actor:

    def __init__(self, name, gender, species, job, x, y, face, color, char, AI, EXPcurr, EXPspent, AGI, STR, INT, STMmax, allegiance, status, fire, drop, mobility, blades, whips, hammers, pistols, rifles, heavyw, thrown, software, hardware, leadership, medicine, pilot, xenology, suit, hnd1, hnd2, visor, shield):
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
    self.drop = drop
    
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
        if not map[self.x + dx], [self.x + dx].blockpass:
            self.x += dx
            self.y += dy
            if dx < 0:
                self.face = 'left'
                if self == 'player':
                    self.char = '◀'
            if dx > 0:
                self.face = 'right'
                if self == 'player':
                    self.char = '▶'
            if dy < 0:
                self.face = 'up'
                if self == 'player':
                    self.char = '▲'
            if dx > 0:
                self.face = 'down'
                if self == 'player':
                    self.char = '▼'
    def draw (self):
        #draws character in color to con
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
    def clear (self):
        #Clears character
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        
#Combat Functions
def damage(target, origin, hand):
    if origin.hand.skill == 'None' and origin.hand.sort == 'Melee':
    	origin_damage = (origin.STR * origin.suit.power + origin.hand.power)
	target_resist = (target.STR * target.suit.power + target.suit.protection)
	damage_dealt = origin_damage - target_resist
	if damage_dealt < 1 :
		target.HPcurr -= 1
	elif damage_dealt >= 1 :
		target.HPcurr = target.HPcurr - damage_dealt
		if target.HPcurr <= 0 :
			#target.drop()
	

#Melee Weapon Functions
def melee_atk(origin, hand, facing):
    If origin.fire != True :
        origin.hand.effect(origin, origin.facing, hand)
        origin.fire = True

def fist_attack(origin, facing, weapon):
    if facing == 'up'
	put_char(con, origin.x, origin.y - 1, '.', libtcod.BKGND_NONE)
	for object in actors:
		if object.x == origin.x and object.y == origin.y - 1:
			damage(object, origin, weapon)
			put_char(con, origin.x, origin.y - 1, ' ', libtcod.BKGND_NONE)
    if facing == 'down'
	put_char(con, origin.x, origin.y + 1, '.', libtcod.BKGND_NONE)
	for object in actors:
		if object.x == origin.x and object.y == origin.y + 1:
			damage(object, origin, weapon)
			put_char(con, origin.x, origin.y + 1, ' ', libtcod.BKGND_NONE)
    if facing == 'left'
	put_char(con, origin.x - 1, origin.y, '.', libtcod.BKGND_NONE)
	for object in actors:
		if object.x == origin.x - 1 and object.y == origin.y - 1:
			damage(object, origin, weapon)
			put_char(con, origin.x - 1, origin.y, ' ', libtcod.BKGND_NONE)
    if facing == 'right'
	put_char(con, origin.x + 1, origin.y, '.', libtcod.BKGND_NONE)
	for object in actors:
		if object.x == origin.x + 1 and object.y == origin.y:
			damage(object, origin, weapon)
			put_char(con, origin.x + 1, origin.y, ' ', libtcod.BKGND_NONE)
        
def do_nothing():
	print 'Unfortunately, this does nothing.'

#item code
def weapon:
    __init__(self, power, dist, skill, sort, hands, effect)
    self.power = power
    self.dist = dist
    self.skill = skill
    self.sort = sort
    self.hands = hands
    self.effect = effect

def suit:
    __init__(self, power, protection)
    self.power = power
    self.protection = protection
    
def visor:
    __init__(self, effect)
    self.effect = effect

def shield:
    __init__(self, powermax, powercurr = powermax, regentime)
    self.powermax = powermax
    self.regentime = regentime

#Melee weapons
weap_fist = weapon(0, 1, 'None', 'Melee', 1, fist_attack())
weap_flexiblade = weapon(15, 1, 'blades', 'Melee', 1, sword_atk())

#Ranged Weapons

#Suits
suit_skillsuit = suit(1.1, 10)

#Visors
visor_basic = visor(do_nothing())

#Shields
shield_basic = shield(50, 15)

#construct player
player = actor('name', 'gender', 'species', 'job', 0, 0, 'down', libtcod.white, '▼', 'Input', 100, 0, 50, 50, 50, 150, 'Survivors', 'Alive', False, 'drop', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, suit_skillsuit, weap_fist, weap_fist, visor_basic, shield_basic):

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
def tile:
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
    global player.x, player.y
    
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
        If player.hnd1.dist == 1 and player.fire != True:
            melee_atk (player, hnd1, player.face)
        elif player.hnd2.dist == 1 and player.fire != True:
            melee_atk (player, hnd2, player.face)
        elif player.hnd1.dist != 1 and player.hnd2.dist != 1:
            print 'No melee weapon equipped!'
            
#Ranged attack(player)
    if libtcod.console_is_key_pressed(libtcod.KEY_CHAR(r)):
        If player.hnd1.dist > 1 and player.fire != True:
            melee_atk (player, hnd1, player.face)
        elif player.hnd2.dist > 1 and player.fire != True:
            melee_atk (player, hnd2, player.face)
        elif player.hnd1.dist == 1 and player.hnd2.dist == 1:
            print 'No ranged weapon equipped!'
 
#rendering
def render_all():
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
pbag = actor('Punching Bag', 'Sand', 'Burlap', 'bag', 5, 5, 'down', libtcod.yellow, '@', 'none', 100, 0, 50, 50, 50, 150, 'Burlap', 'Alive', False, 'drop', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, suit_skillsuit, weap_fist, weap_fist, visor_basic, shield_basic):

actors = [player, pbag]

while not libtcod.is_window_closed():
render_all()
    
    libtcod.console_set_default_foreground(con, libtcod.silver)
    libtcod.console_flush()
   
    for object in actors:
        actor.clear()
        
    exit = handle_keys()
    if exit:
        break
#end main loop
