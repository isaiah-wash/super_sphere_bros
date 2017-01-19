#Super Mario Bros.!!

from visual import *

scene.range=105
scene.autoscale=False



def supermariobros():
    #mariocollisions
    def collision1(mario, block):
        if (mario.pos.x + mario.radius > block.pos.x - block.length/2.
            and mario.pos.x < block.pos.x
            and mario.pos.y - mario.radius < block.pos.y + block.height/2.
            and mario.pos.y + mario.radius > block.pos.y - block.height/2.
            ):
            return True
        else:
            return False
        
    def collision4(mario, block):
        if(mario.pos.x - mario.radius < block.pos.x + block.length/2.
             and mario.pos.x > block.pos.x
             and mario.pos.y - mario.radius < block.pos.y + block.height/2.
             and mario.pos.y + mario.radius > block.pos.y - block.height/2.
             ):
        
            return True
        else:
            return False

    def collision2(mario, block):
        if(mario.pos.y - mario.radius < block.pos.y + block.height/2.
           and mario.pos.y > block.pos.y
           and mario.pos.x >= block.pos.x - block.length/2.
           and mario.pos.x <= block.pos.x + block.length/2.
           ):
            return True
        else:
            return False

    #coincollision
    def collision3(sphere1, sphere2):
        dist=mag(sphere1.pos-sphere2.pos)
        if(dist<sphere1.radius+sphere2.radius):
            return True
        else:
            return False
    #spikecollision
    '''def collision(mario, spike):
        if mario.pos.y - mario.radius < thisspike.pos.y + 5'''

    #setting up the background
    background = box(pos=vector(0,0,-4), length=220, width=1, height=229, color=color.cyan)
    '''cloud1'''
    cloudpiece1 = box(pos=(-80,80, -2), size=(10,10,1), color=color.white)
    cloudpiece2 = box(pos=(-75, 85, -2), size=(10,10,1), color=color.white)
    cloudpiece3 = box(pos=(-70, 80, -2), size=(10,10,1), color=color.white)
    '''cloud2'''
    cloudpiece1 = box(pos=(-5,70, -2), size=(10,10,1), color=color.white)
    cloudpiece2 = box(pos=(5, 72, -2), size=(10,14,1), color=color.white)
    cloudpiece3 = box(pos=(15, 70, -2), size=(10,10,1), color=color.white)
    '''cloud3'''
    cloudpiece1 = box(pos=(80,80, -2), size=(10,10,1), color=color.white)
    cloudpiece2 = box(pos=(75, 85, -2), size=(10,10,1), color=color.white)
    cloudpiece3 = box(pos=(70, 80, -2), size=(10,10,1), color=color.white)
    '''ground'''
    ground = box(pos=(0,-95, 0), size=(215,26,1), color=color.green)

    #variables for the game
    mario = sphere(pos=(-95, -75,-2 ), radius=7, color=color.red)

    spike1 = pyramid(pos=(646,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0)) 
    spike2 = pyramid(pos=(660,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike3 = pyramid(pos=(674,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike4 = pyramid(pos=(688,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike5 = pyramid(pos=(296,31.26,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike6 = pyramid(pos=(310,31.26,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike7 = pyramid(pos=(324,31.26,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike8 = pyramid(pos=(338,31.26,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike9 = pyramid(pos=(400,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike10 = pyramid(pos=(414,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike11 = pyramid(pos=(428,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike12 = pyramid(pos=(112,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0)) 
    spike13 = pyramid(pos=(126,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike14 = pyramid(pos=(140,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))
    spike15 = pyramid(pos=(154,-82,-2), size=(12.13,14,2), color=(0.5,0.5,0.5), axis=(0,1,0))





    block16 = box(pos=(243,-62, -2), size=(90,40,2), color=color.blue)

    block1 = box(pos=(226,10.26, -2), size=(14,14,3), color=(1,0.7,0.2))
    block2 = box(pos=(240,24.26, -2), size=(14,14,3), color=(1,0.7,0.2))
    block3 = box(pos=(324,24.26, -2), size=(168,14,3), color=(1,0.7,0.2))
    block4 = box(pos=(377,-60, -2), size=(14,42,3), color=(1,0.7,0.2))
    #staircase
    block5 = box(pos=(507,-74, -2), size=(84,14,3), color=color.white)
    block6 = box(pos=(514,-60, -2), size=(70,14,3), color=color.white)
    block7 = box(pos=(521,-46, -2), size=(56,14,3), color=color.white)
    block8 = box(pos=(528,-32, -2), size=(42,14,3), color=color.white)
    block9 = box(pos=(535,-18, -2), size=(28,14,3), color=color.white)
    block10 = box(pos=(542,-4, -2), size=(14,14,3), color=color.white)

    block11 = box(pos=(605,26.26, -2), size=(56,14,3), color=(1,0.7,0.2))
    block12 = box(pos=(633, -67, -2), size=(14, 28, 3), color=color.black)
    block13 = box(pos=(703, -67, -2), size=(14, 28, 3), color=color.black)
    block14 = box(pos=(800, -60, -2), size=(56, 70, 3), color=(1,0.7,0.2))
    block15 = box(pos=(800, -18, -2), size=(84, 14, 3), color=color.green)

    coin1 = sphere(pos=(126,-55,-2), radius=5, color=color.yellow)
    coin2 = sphere(pos=(140,-55,-2), radius=5, color=color.yellow)
    coin3 = sphere(pos=(214,-35,-2), radius=5, color=color.yellow)
    coin4 = sphere(pos=(228,-35,-2), radius=5, color=color.yellow)
    coin5 = sphere(pos=(242,-35,-2), radius=5, color=color.yellow)
    coin6 = sphere(pos=(256,-35,-2), radius=5, color=color.yellow)
    coin7 = sphere(pos=(270,-35,-2), radius=5, color=color.yellow)
    coin8 = sphere(pos=(284,-35,-2), radius=5, color=color.yellow)
    coin9 = sphere(pos=(226, 26,-2), radius=5, color=color.yellow)
    coin10 = sphere(pos=(254,48,-2), radius=5, color=color.yellow)
    coin11 = sphere(pos=(254,62,-2), radius=5, color=color.yellow)
    coin12 = sphere(pos=(270,48,-2), radius=5, color=color.yellow)
    coin13 = sphere(pos=(270,62,-2), radius=5, color=color.yellow)
    coin14 = sphere(pos=(284,48,-2), radius=5, color=color.yellow)
    coin15 = sphere(pos=(284,62,-2), radius=5, color=color.yellow)
    coin16 = sphere(pos=(298,48,-2), radius=5, color=color.yellow)
    coin17 = sphere(pos=(298,62,-2), radius=5, color=color.yellow)
    coin18 = sphere(pos=(312,48,-2), radius=5, color=color.yellow)
    coin19 = sphere(pos=(312,62,-2), radius=5, color=color.yellow)
    coin20 = sphere(pos=(326,48,-2), radius=5, color=color.yellow)
    coin21 = sphere(pos=(326,62,-2), radius=5, color=color.yellow)
    coin22 = sphere(pos=(340,48,-2), radius=5, color=color.yellow)
    coin23 = sphere(pos=(340,62,-2), radius=5, color=color.yellow)
    coin24 = sphere(pos=(354,48,-2), radius=5, color=color.yellow)
    coin25 = sphere(pos=(354,62,-2), radius=5, color=color.yellow)
    coin26 = sphere(pos=(370,48,-2), radius=5, color=color.yellow)
    coin27 = sphere(pos=(370,62,-2), radius=5, color=color.yellow)
    coin28 = sphere(pos=(384,48,-2), radius=5, color=color.yellow)
    coin29 = sphere(pos=(384,62,-2), radius=5, color=color.yellow)
    coin30 = sphere(pos=(398,48,-2), radius=5, color=color.yellow)
    coin31 = sphere(pos=(398,62,-2), radius=5, color=color.yellow)
    coin32 = sphere(pos=(772,-5,-2), radius=5, color=color.yellow)
    coin33 = sphere(pos=(772,9,-2), radius=5, color=color.yellow)
    coin34 = sphere(pos=(786,-5,-2), radius=5, color=color.yellow)
    coin35 = sphere(pos=(786,9,-2), radius=5, color=color.yellow)
    coin36 = sphere(pos=(800,-5,-2), radius=5, color=color.yellow)
    coin37 = sphere(pos=(800,9,-2), radius=5, color=color.yellow)
    coin39 = sphere(pos=(814,-5,-2), radius=5, color=color.yellow)
    coin40 = sphere(pos=(814,9,-2), radius=5, color=color.yellow)
    coin41 = sphere(pos=(772,23,-2), radius=5, color=color.yellow)
    coin42 = sphere(pos=(772,37,-2), radius=5, color=color.yellow)
    coin43 = sphere(pos=(786,23,-2), radius=5, color=color.yellow)
    coin44 = sphere(pos=(786,37,-2), radius=5, color=color.yellow)
    coin45 = sphere(pos=(800,23,-2), radius=5, color=color.yellow)
    coin46 = sphere(pos=(800,37,-2), radius=5, color=color.yellow)
    coin47 = sphere(pos=(814,23,-2), radius=5, color=color.yellow)
    coin48 = sphere(pos=(814,37,-2), radius=5, color=color.yellow)

    
    pole = cylinder(pos=(910,-80,-2), axis=(0,130,0), radius=3, color=(0.5,0.5,0.5))
    goal = sphere(pos=(910, 50, -2), radius=4, color=color.yellow)


    #variable movements

    marioSpeed = 1000

    blocksList = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16]
         

    spikesList = [spike1, spike2, spike3, spike4, spike5, spike6, spike7, spike8, spike9, spike10, spike11, spike12, spike13, spike14, spike15]
    
        
    coinsList = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                 coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19,
                 coin20, coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28,
                 coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36,
                 coin37, coin39, coin40, coin41, coin42, coin43, coin44,
                 coin45, coin46, coin47, coin48]
    
    
    for thisblock in blocksList:
        thisblock.v = marioSpeed*vector(-.5,0,0)
    for thisspike in spikesList:
        thisspike.v = marioSpeed*vector(-.5,0,0)
    for thiscoin in coinsList:
        thiscoin.v = marioSpeed*vector(-.5,0,0)



    pole.v = marioSpeed*vector(-.5,0,0)
    goal.v = marioSpeed*vector(-.5,0,0)

    

    mario.v = marioSpeed*vector(.25,0,0)
    mario.a = vector(0,-60,0)



    t=0
    dt=0.01

    jumps = 0
    coins = 0


    label(pos=vector(70, 95, 0), color=color.white, text = 'SuperSphereBros.')
    coins_label = label(pos=vector(0, 95, 0), color=color.white, text = 'Coins=%s' % coins)


    #game

    '''makes mario and course move'''
    while 1:
        rate(100)
        mario.pos.y = mario.pos.y + mario.v.y*dt
        mario.v.y = mario.v.y + mario.a.y*dt
    
        if mario.pos.y < -75.:
            mario.pos.y = -75
        
        if -95 <= mario.pos.x <= 0:
            for thisblock in blocksList:
                thisblock.v = marioSpeed*vector(-.5,0,0)
            for thisspike in spikesList:
                thisspike.v = marioSpeed*vector(-.5,0,0)
            for thiscoin in coinsList:
                thiscoin.v = marioSpeed*vector(-.5,0,0)
            if scene.kb.keys:
                k=scene.kb.getkey()
                if k == "right":
                   mario.pos.x=mario.pos.x+mario.v.x*dt
                if k == "up" and jumps < 2:
                    mario.v.y = 50
                    jumps = jumps + 1
                    print jumps
                if k == "left":
                    mario.pos.x=mario.pos.x+(-1*mario.v.x)*dt

        if mario.pos.x < -95:
            for thisblock in blocksList:
                thisblock.v = marioSpeed*vector(.5,0,0)
            for thisspike in spikesList:
                thisspike.v = marioSpeed*vector(.5,0,0)
            for thiscoin in coinsList:
                thiscoin.v = marioSpeed*vector(.5,0,0)
            pole.v = marioSpeed*vector(.5,0,0)
            goal.v = marioSpeed*vector(.5,0,0)
            
            if scene.kb.keys:
                k=scene.kb.getkey()
                if k == "right":
                   mario.pos.x=mario.pos.x+mario.v.x*dt
                if k == "up" and jumps < 2:
                    mario.v.y = 50
                    jumps = jumps + 1
                    print jumps
                if k == "left":
                    for thisblock in blocksList:
                        thisblock.pos.x=thisblock.pos.x+thisblock.v.x*dt
                    for thisspike in spikesList:
                        thisspike.pos.x=thisspike.pos.x+thisspike.v.x*dt
                    for thiscoin in coinsList:
                        thiscoin.pos.x=thiscoin.pos.x+thiscoin.v.x*dt
                    pole.pos.x=pole.pos.x+pole.v.x*dt
                    goal.pos.x=goal.pos.x+goal.v.x*dt




        if scene.kb.keys:
            pole.v = marioSpeed*vector(-.5,0,0)
            goal.v = marioSpeed*vector(-.5,0,0)
            k=scene.kb.getkey()
            if k == "up" and jumps < 2:
                mario.v.y = 50
                jumps = jumps + 1
                print jumps
            if k == "left":
                mario.pos.x=mario.pos.x+(-1*mario.v.x)*dt
            if k == "right":
                for thisblock in blocksList:
                    thisblock.pos.x=thisblock.pos.x+thisblock.v.x*dt
                for thisspike in spikesList:
                    thisspike.pos.x=thisspike.pos.x+thisspike.v.x*dt
                for thiscoin in coinsList:
                    thiscoin.pos.x=thiscoin.pos.x+thiscoin.v.x*dt
                pole.pos.x=pole.pos.x+pole.v.x*dt
                goal.pos.x=goal.pos.x+goal.v.x*dt

        for thisblock in blocksList:
            if collision2(mario, thisblock):
                mario.pos.y = thisblock.pos.y + thisblock.height/2 + mario.radius
                
            if collision1(mario, thisblock):
               
                mario.pos.x = thisblock.pos.x-thisblock.length/2 - mario.radius

            if collision4(mario, thisblock):
                mario.pos.x = thisblock.pos.x+thisblock.length/2 + mario.radius

            
        for thisblock in blocksList:
            if mario.pos.y == thisblock.pos.y + thisblock.height/2 + mario.radius or mario.pos.y == -75:
                jumps = 0
    #Spikes
        for thisspike in spikesList:
            dist = (
                math.sqrt(
                    ((mario.pos.x - thisspike.pos.x)**2) + ((mario.pos.y - (thisspike.pos.y + thisspike.axis.y))**2)
                    )
                )
            
            if dist < mario.radius:
                label(pos=vector(0, 0, 0), color=color.red, text = 'GAME OVER')
                for thisblock in blocksList:
                    thisblock.v = marioSpeed*vector(0,0,0)
                for thisspike in spikesList:
                    thisspike.v = marioSpeed*vector(0,0,0)
                for thiscoin in coinsList:
                    thiscoin.v = marioSpeed*vector(0,0,0)
        
                pole.v = marioSpeed*vector(0,0,0)
                goal.v = marioSpeed*vector(0,0,0)
                mario.v = marioSpeed*vector(0,0,0)

                delete(display)
                supermariobros()


                
    #coins
        for thiscoin in coinsList:
            if collision3(mario, thiscoin):
                    thiscoin.pos=vector(0,-120,0)
                    thiscoin.v = vector(0,0,0)
                    coins = coins+1
                    coins_label.text = 'coins=%s' %coins
                    
    #endgame
        if mario.pos.x >= 0 and pole.pos.x <= 0:
            label(pos=vector(0, 0, 0), color=color.green, text = 'YOU WIN!')
            for thisblock in blocksList:
                thisblock.v = marioSpeed*vector(0,0,0)
            for thisspike in spikesList:
                thisspike.v = marioSpeed*vector(0,0,0)
            for thiscoin in coinsList:
                thiscoin.v = marioSpeed*vector(0,0,0)
    
            pole.v = marioSpeed*vector(0,0,0)
            goal.v = marioSpeed*vector(0,0,0)

    #restart 
    
            
        t=t+dt
supermariobros()



