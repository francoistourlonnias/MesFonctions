from mblock import event
import time

null = 0

@event.keypressed('a')
def on_keypressed():
    global null
    v = sprite.get_variable('vitesse')
    sprite.set_variable('vitesse', v + 10)

@event.keypressed('z')
def on_keypressed1():
    global null
    v = sprite.get_variable('vitesse')
    sprite.set_variable('vitesse', v + -10)

@event.keypressed('c')
def on_keypressed2():
    global null
    sprite.say(sprite.get_variable('celcius'), 2)

@event.keypressed('space')
def on_keypressed3():
    global null
    if sprite.get_variable('light') == 0:
        sprite.set_variable('light', 1)

    else:
        sprite.set_variable('light', 0)

@event.keypressed('up arrow')
def on_keypressed4():
    global null
    sprite.set_variable('FHaut', 1)

def ControlMotion():
    global null
    if False:
        sprite.set_variable('AutorisationBouger', 0)
        sprite.set_variable('temporaire', sprite.get_variable('R'))
        sprite.set_variable('R', 60)

    else:
        sprite.set_variable('AutorisationBouger', 1)
        sprite.set_variable('R', sprite.get_variable('temporaire'))
        sprite.set_variable('temporaire', 0)

    sprite.set_variable('V', sprite.get_variable('V'))
    sprite.set_variable('B', sprite.get_variable('B'))

@event.keypressed('down arrow')
def on_keypressed5():
    global null
    sprite.set_variable('FBas', 1)

@event.keypressed('left arrow')
def on_keypressed6():
    global null
    sprite.set_variable('FGauche', 1)

@event.keypressed('right arrow')
def on_keypressed7():
    global null
    sprite.set_variable('FDroit', 1)

@event.greenflag
def on_greenflag():
    global null
    sprite.set_variable('R', 0)
    sprite.set_variable('V', 0)
    sprite.set_variable('B', 0)
    sprite.set_variable('vitesse', 200)
    sprite.set_variable('light', 0)
    sprite.set_variable('prem', 0)
    sprite.set_variable('temporaire', 0)
    sprite.set_variable('tempotouches', 0.5)
    while True:
        sprite.set_variable('compens', 0)
        sprite.set_variable('luminosité', 0)
        sprite.set_variable('celcius', 0)
        sprite.set_variable('distance', 0)
        sprite.set_variable('x', 0)
        sprite.set_variable('y', 0)
        sprite.set_variable('z', 0)
        ControlMotion()
        if sprite.get_variable('light') == 1:
            compesLum()

        if sprite.get_variable('FHaut') == 1:
            Mouvement_N_S(sprite.get_variable('vitesse'), 'A')
            time.sleep(float(sprite.get_variable('tempotouches')))
            sprite.set_variable('FHaut', 0)

        else:
            Mouvement_N_S(0, 'A')

        if sprite.get_variable('FBas') == 1:
            Mouvement_N_S(sprite.get_variable('vitesse'), 'R')
            time.sleep(float(sprite.get_variable('tempotouches')))
            sprite.set_variable('FBas', 0)

        else:
            Mouvement_N_S(0, 'R')

        if sprite.get_variable('FDroit') == 1:
            Mouvement_N_S(sprite.get_variable('vitesse'), 'D')
            time.sleep(float(sprite.get_variable('tempotouches')))
            sprite.set_variable('FDroit', 0)

        else:
            Mouvement_N_S(0, 'D')

        if sprite.get_variable('FGauche') == 1:
            Mouvement_N_S(sprite.get_variable('vitesse'), 'G')
            time.sleep(float(sprite.get_variable('tempotouches')))
            sprite.set_variable('FGauche', 0)

        else:
            Mouvement_N_S(0, 'G')

def Mouvement_N_S(speed, dir2):
    global null
    ControlMotion()
    if dir == 'A':
        if sprite.get_variable('AutorisationBouger') == 1:
            pass


    if dir == 'R':
        if sprite.get_variable('AutorisationBouger') == 1:
            pass


    if dir == 'G':
        if sprite.get_variable('AutorisationBouger') == 1:
            pass


    if dir == 'D':
        if sprite.get_variable('AutorisationBouger') == 1:
            pass


    ControlMotion()

def compesLum():
    global null
    if sprite.get_variable('luminosité') < 50:
        sprite.set_variable('compens', ((-5.1 * sprite.get_variable('luminosité') + 255)))
        if sprite.get_variable('compens') > ' 255 ':
            sprite.set_variable('compens', 255)

        sprite.set_variable('compens', 60)

sprite.set_variable('R', 0)
sprite.set_variable('V', 0)
sprite.set_variable('B', 0)
sprite.set_variable('FHaut', 0)
sprite.set_variable('FBas', 0)
sprite.set_variable('FGauche', 0)
sprite.set_variable('FDroit', 0)

compesLum()

if False:
    sprite.set_variable('vitesse', (sprite.get_variable('vitesse') == sprite.get_variable('vitesse') / 20))
    v = sprite.get_variable('prem')
    sprite.set_variable('prem', v + 1)
    sprite.set_variable('R', 20)
    sprite.set_variable('V', 20)
    sprite.set_variable('B', 20)
    sprite.set_variable('vitesse', (sprite.get_variable('vitesse') == sprite.get_variable('vitesse') * 20))

else:
    sprite.set_variable('prem', 0)
