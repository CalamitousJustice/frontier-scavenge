import libtcodpy as libtcod
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
libtcod.console_set_custom_font ('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TC0D)
libtcod.init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Frontier:Scavenger', false)
libtcod.sys_set_fps(LIMIT_FPS)
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2
def handle_keys ():
    global playerx, playery
    
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
        playery -= 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(s)):
        playery += 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(a)):
        playerx -= 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR(d)):
        playerx += 1


# Incoming main loop 

while not libtcod.is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.silver)
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)
    exit = handle_keys()
    if exit:
        break

libtcod.console_flush ()

#end main loop
