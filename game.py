#Rehan Javaid rj3dxu #Danish Chauhan dic2fx

# Rehan Javaid rj3dxu #Danish Chauhan dic2fx

# Game Title: Secret Agent Man
# Description: The camera angle of the game is top-down. You are a secret agent who has just finished their task of extracting a package. Now, you have to ESCAPE
# the evil lair with the package otherwise you will FAIL the mission. The lair is a maze. You need to be careful because throughout the lair there are guards waiting to
# stop you at any cost. If a guard sees you, they will chase you. Also you need to be quick because otherwise the helicopter outside the lair will leave without you. Luckily,
# there are tools scattered throughout the level for you to get multiple chances against these pesky guards. The goal of the game is to get to the exit without running out of lives
# lives or time.
# Optional Features
# Health bar: There are a set number of lives that decreases upon getting touched by one of the guards.
# Two-player: This game is a two-player game. Both agents need to reach the end for you to win.
# Enemies: The guards are the enemies in this game. When the agent gets into the line of sight of the guards, the guards will chase the agent. If the guard
# touches the agent, the agent loses a life
# Collectibles: The collectibles include lives that also increase your total score if you collect them.
# Timer: There is a set time for which the agent is able to get out of the maze. If the agent does not escape by that time, the game ends.
import pygame
import gamebox

game_on = False
camera = gamebox.Camera(800, 600)
pass_wall_1 = False
pass_wall_2 = False
pass_wall_3 = False
pass_wall_4 = False
pass_wall_5 = False
pass_wall_6 = False
c2passwall1 = False
c2passwall2 = False
c2passwall3 = False
c2passwall4 = False
c2passwall5 = False
c2passwall6 = False
count = 900
character = gamebox.from_image(680, 10, 'secretagent1.png')
character.scale_by(0.015)
character2 = gamebox.from_image(710, 10, 'secretagent4.png')
character2.scale_by(0.015)
enemy1 = gamebox.from_image(85, 150, "robber1.png")
enemy1.scale_by(.055)
enemy2 = gamebox.from_image(700, 150, "robber1.png")
enemy2.scale_by(.055)
enemy3 = gamebox.from_image(85, 250, "robber1.png")
enemy3.scale_by(.055)
enemy4 = gamebox.from_image(330, 450, "robber1.png")
enemy4.scale_by(.055)
enemy5 = gamebox.from_image(730, 320, "robber1.png")
enemy5.scale_by(.055)
enemy6 = gamebox.from_image(71, 493, "robber1.png")
enemy6.scale_by(.055)
enemy7 = gamebox.from_image(71, 529, "robber1.png")
enemy7.scale_by(.055)
wall1 = gamebox.from_color(400, 550, "black", 700, 10)
wall2 = gamebox.from_color(50, 205, "black", 10, 700)
wall3 = gamebox.from_color(350, 5, "black", 600, 10)
wall4 = gamebox.from_color(750, 100, "black", 10, 640)
wall5 = gamebox.from_color(450, 100, "black", 600, 10)
wall6 = gamebox.from_color(350, 200, "black", 600, 10)
wall7 = gamebox.from_color(450, 300, "black", 600, 10)
wall8 = gamebox.from_color(155, 350, "black", 10, 100)
wall9 = gamebox.from_color(200, 475, "black", 300, 10)
wall10 = gamebox.from_color(350, 423, "black", 10, 115)
wall11 = gamebox.from_color(383, 370, "black", 75, 10)
wall12 = gamebox.from_color(655, 420, "black", 200, 10)
wall13 = gamebox.from_color(475, 475, "black", 10, 150)
trigger1 = gamebox.from_color(200, 52, "dark green", 1, 70)
trigger2 = gamebox.from_color(600, 150, "dark green", 1, 85)
trigger3 = gamebox.from_color(200, 250, "dark green", 1, 80)
trigger4 = gamebox.from_color(200, 400, "dark green", 1, 140)
trigger5 = gamebox.from_color(490, 360, "dark green", 1, 100)
trigger6 = gamebox.from_color(200, 515, "dark green", 1, 50)
collectible = gamebox.from_circle(150, 510, "red", 10)
collectible2 = gamebox.from_circle(650, 370, 'red', 10)
helicopter = gamebox.from_image(700, 490, 'helicpopter1.png')
helicopter.scale_by(0.15)
obstacles = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13]
lives = 3
life_box1 = gamebox.from_circle(725, 570, 'red', 8)
life_box2 = gamebox.from_circle(742, 570, 'red', 8)
life_box3 = gamebox.from_circle(759, 570, 'red', 8)
life_box4 = gamebox.from_circle(776, 570, 'red', 8)
life_box5 = gamebox.from_circle(793, 570, 'red', 8)

background = (gamebox.from_image(452, 490, 'secret_agent.jpg'))
background.scale_by(2)
camera.draw(background)
camera.draw("TWO PLAYERS REQUIRED", 50, "red", 400, 540)
camera.draw("*Collect Lives for Bonus Score*", 40, "red", 400, 580)
camera.display()


def tick(keys):
    global game_on
    global life_box
    global lives
    reset = False
    win = False
    win2 = False
    if pygame.K_SPACE in keys:
        game_on = True
    if game_on == True:
        global pass_wall_1
        global pass_wall_2
        global pass_wall_3
        global pass_wall_4
        global pass_wall_5
        global pass_wall_6
        global c2passwall1
        global c2passwall2
        global c2passwall3
        global c2passwall4
        global c2passwall5
        global c2passwall6
        global count
        camera.clear("dark green")
        camera.draw(character)
        camera.draw(character2)
        camera.draw("LIVES:", 20, 'black', 690, 570)
        for obst in obstacles:
            character2.move_to_stop_overlapping(obst)
            character.move_to_stop_overlapping(obst)
            enemy1.move_to_stop_overlapping(obst)
            enemy2.move_to_stop_overlapping(obst)
            enemy3.move_to_stop_overlapping(obst)
            enemy4.move_to_stop_overlapping(obst)
            enemy5.move_to_stop_overlapping(obst)
            enemy6.move_to_stop_overlapping(obst)
            enemy7.move_to_stop_overlapping(obst)
            camera.draw(obst)
        camera.draw(enemy1)
        camera.draw(enemy2)
        camera.draw(enemy3)
        camera.draw(enemy4)
        camera.draw(enemy5)
        camera.draw(enemy6)
        camera.draw(enemy7)
        camera.draw(trigger1)
        camera.draw(trigger2)
        camera.draw(trigger3)
        camera.draw(trigger4)
        camera.draw(trigger5)
        camera.draw(trigger6)
        camera.draw(collectible)
        camera.draw(collectible2)
        camera.draw(helicopter)

        if count > 0:
            count -=.5
        camera.draw(str(count), 50, "blue", 200, 50)

        if lives == 3:
            camera.draw(life_box1)
            camera.draw(life_box2)
            camera.draw(life_box3)
        elif lives == 4:
            camera.draw(life_box1)
            camera.draw(life_box2)
            camera.draw(life_box3)
            camera.draw(life_box4)
        elif lives == 5:
            camera.draw(life_box1)
            camera.draw(life_box2)
            camera.draw(life_box3)
            camera.draw(life_box4)
            camera.draw(life_box5)

        elif lives == 2:
            camera.draw(life_box1)
            camera.draw(life_box2)
        elif lives == 1:
            camera.draw(life_box1)
        camera.display()

        # character controls
        if pygame.K_RIGHT in keys:
            character.x += 10
        if pygame.K_LEFT in keys:
            character.x -= 10
        if pygame.K_UP in keys:
            character.y -= 10
        if pygame.K_DOWN in keys:
            character.y += 10
        if pygame.K_d in keys:
            character2.x += 10
        if pygame.K_a in keys:
            character2.x -= 10
        if pygame.K_w in keys:
            character2.y -= 10
        if pygame.K_s in keys:
            character2.y += 10



        # enemyfollowing
        if character.left_touches(trigger1):
            pass_wall_1 = True
        if character2.left_touches(trigger1):
            c2passwall1 = True
        if pass_wall_1 == True and c2passwall1 == False:
            if character.x < enemy1.x:
                enemy1.x -= 2.5
            elif character.x > enemy1.x:
                enemy1.x += 2.5
            if character.y < enemy1.y:
                enemy1.y -= 2.5
            elif character.y > enemy1.y:
                enemy1.y += 2.5
        if pass_wall_1 == True and c2passwall1 == True:
            if character.x < enemy1.x:
                enemy1.x -= 2.5
            elif character.x > enemy1.x:
                enemy1.x += 2.5
            if character.y < enemy1.y:
                enemy1.y -= 2.5
            elif character.y > enemy1.y:
                enemy1.y += 2.5
        if pass_wall_1 == False and c2passwall1 == True:
            if character2.x < enemy1.x:
                enemy1.x -= 2.5
            elif character2.x > enemy1.x:
                enemy1.x += 2.5
            if character2.y < enemy1.y:
                enemy1.y -= 2.5
            elif character2.y > enemy1.y:
                enemy1.y += 2.5

        if character.left_touches(trigger2):
            pass_wall_2 = True
        if character2.left_touches(trigger2):
            c2passwall2 = True
        if pass_wall_2 == True and c2passwall2 == False:
            if character.x < enemy2.x:
                enemy2.x -= 2.5
            elif character.x > enemy2.x:
                enemy2.x += 2.5
            if character.y < enemy2.y:
                enemy2.y -= 2.5
            elif character.y > enemy2.y:
                enemy2.y += 2.5
        if pass_wall_2  == True and c2passwall2 == True:
            if character2.x < enemy2.x:
                enemy2.x -= 2.5
            elif character2.x > enemy2.x:
                enemy2.x += 2.5
            if character2.y < enemy2.y:
                enemy2.y -= 2.5
            elif character2.y > enemy2.y:
                enemy2.y += 2.5
        if pass_wall_2 == False and c2passwall2 == True:
            if character2.x < enemy2.x:
                enemy2.x -= 2.5
            elif character2.x > enemy2.x:
                enemy2.x += 2.5
            if character2.y < enemy2.y:
                enemy2.y -= 2.5
            elif character2.y > enemy2.y:
                enemy2.y += 2.5

        if character.left_touches(trigger3):
            pass_wall_3 = True
        if character2.left_touches(trigger3):
            c2passwall3 = True
        if pass_wall_3 == True and c2passwall3 == False:
            if character.x < enemy3.x:
                enemy3.x -= 2.5
            elif character.x > enemy3.x:
                enemy3.x += 2.5
            if character.y < enemy3.y:
                enemy3.y -= 2.5
            elif character.y > enemy3.y:
                enemy3.y += 2.5
        if pass_wall_3 == False and c2passwall3 == True:
            if character2.x < enemy3.x:
                enemy3.x -= 2.5
            elif character2.x > enemy3.x:
                enemy3.x += 2.5
            if character2.y < enemy3.y:
                enemy3.y -= 2.5
            elif character2.y > enemy3.y:
                enemy3.y += 2.5
        if pass_wall_3 == True and c2passwall3 == True:
            if character.x < enemy3.x:
                enemy3.x -= 2.5
            elif character.x > enemy3.x:
                enemy3.x += 2.5
            if character.y < enemy3.y:
                enemy3.y -= 2.5
            elif character.y > enemy3.y:
                enemy3.y += 2.5

        if character.left_touches(trigger4):
            pass_wall_4 = True
        if character2.left_touches(trigger4):
            c2passwall4 = True
        if pass_wall_4 == True and c2passwall4 == False:
            if character.x < enemy4.x:
                enemy4.x -= 2.5
            elif character.x > enemy4.x:
                enemy4.x += 2.5
            if character.y < enemy4.y:
                enemy4.y -= 2.5
            elif character.y > enemy4.y:
                enemy4.y += 2.5
        if pass_wall_4 == False and c2passwall4 == True:
            if character2.x < enemy4.x:
                enemy4.x -= 2.5
            elif character2.x > enemy4.x:
                enemy4.x += 2.5
            if character2.y < enemy4.y:
                enemy4.y -= 2.5
            elif character2.y > enemy4.y:
                enemy4.y += 2.5
        if pass_wall_4 == True and c2passwall4 == True:
            if character2.x < enemy4.x:
                enemy4.x -= 2.5
            elif character2.x > enemy4.x:
                enemy4.x += 2.5
            if character2.y < enemy4.y:
                enemy4.y -= 2.5
            elif character2.y > enemy4.y:
                enemy4.y += 2.5

        if character.left_touches(trigger5):
            pass_wall_5 = True
        if character2.left_touches(trigger5):
            c2passwall5 = True
        if pass_wall_5 == True and c2passwall5 == False:
            if character.x < enemy5.x:
                enemy5.x -= 2.5
            elif character.x > enemy5.x:
                enemy5.x += 2.5
            if character.y < enemy5.y:
                enemy5.y -= 2.5
            elif character.y > enemy5.y:
                enemy5.y += 2.5
        if pass_wall_5 == False and c2passwall5 == True:
            if character2.x < enemy5.x:
                enemy5.x -= 2.5
            elif character2.x > enemy5.x:
                enemy5.x += 2.5
            if character2.y < enemy5.y:
                enemy5.y -= 2.5
            elif character2.y > enemy5.y:
                enemy5.y += 2.5
        if pass_wall_5 == True and c2passwall5 == True:
            if character.x < enemy5.x:
                enemy5.x -= 2.5
            elif character.x > enemy5.x:
                enemy5.x += 2.5
            if character.y < enemy5.y:
                enemy5.y -= 2.5
            elif character.y > enemy1.y:
                enemy5.y += 2.5

        if character.left_touches(trigger6):
            pass_wall_6 = True
        if character2.left_touches(trigger6):
            c2passwall6 = True
        if pass_wall_6 == True and c2passwall6 == False:
            if character.x < enemy6.x:
                enemy6.x -= 2.5
            elif character.x > enemy6.x:
                enemy6.x += 2.5
            if character.y < enemy6.y:
                enemy6.y -= 2.5
            elif character.y > enemy6.y:
                enemy6.y += 2.5
            if character.x < enemy7.x:
                enemy7.x -= 2.5
            elif character.x > enemy7.x:
                enemy7.x += 2.5
            if character.y < enemy7.y:
                enemy7.y -= 2.5
            elif character.y > enemy7.y:
                enemy7.y += 2.5
        if pass_wall_6 == False and c2passwall6 == True:
            if character2.x < enemy6.x:
                enemy6.x -= 2.5
            elif character2.x > enemy6.x:
                enemy6.x += 2.5
            if character2.y < enemy6.y:
                enemy6.y -= 2.5
            elif character2.y > enemy6.y:
                enemy6.y += 2.5
            if character2.x < enemy7.x:
                enemy7.x -= 2.5
            elif character2.x > enemy7.x:
                enemy7.x += 2.5
            if character2.y < enemy7.y:
                enemy7.y -= 2.5
            elif character2.y > enemy7.y:
                enemy7.y += 2.5

        if pass_wall_6 == True and c2passwall6 == True:
            if character2.x < enemy6.x:
                enemy6.x -= 2.5
            elif character2.x > enemy6.x:
                enemy6.x += 2.5
            if character2.y < enemy6.y:
                enemy6.y -= 2.5
            elif character2.y > enemy6.y:
                enemy6.y += 2.5
            if character2.x < enemy7.x:
                enemy7.x -= 2.5
            elif character2.x > enemy7.x:
                enemy7.x += 2.5
            if character2.y < enemy7.y:
                enemy7.y -= 2.5
            elif character2.y > enemy7.y:
                enemy7.y += 2.5


        if character.touches(enemy1) or character.touches(enemy2) or character.touches(enemy3) or character.touches(
                enemy4) or character.touches(enemy5) or character.touches(enemy6) or character.touches(enemy7):
            lives -= 1
            character.x = 680
            character.y = 10
            character.speedx = 0
            character.speedy = 0
        if character2.touches(enemy1) or character2.touches(enemy2) or character2.touches(enemy3) or character2.touches(
                enemy4) or character2.touches(enemy5) or character2.touches(enemy6) or character2.touches(enemy7):
            lives -= 1
            character2.x = 710
            character2.y = 10
            character2.speedx = 0
            character2.speedy = 0
        if character.touches(collectible) or character2.touches(collectible):
            lives = lives + 1
            collectible.x = 1000
            collectible.y = 1000
        if character.touches(collectible2) or character2.touches(collectible2):
            lives = lives + 1
            collectible2.x = 1000
            collectible2.y = 1000

        if character.touches(helicopter):
            win = True
            enemy1.x = 3000
            enemy1.y = 3000
            enemy3.x = 3000
            enemy3.y = 3000
            enemy5.x = 3000
            enemy5.y = 3000
        if character2.touches(helicopter):
            win2 = True
            enemy2.x = 3000
            enemy2.y = 3000
            enemy4.x = 3000
            enemy4.y = 3000
            enemy6.x = 3000
            enemy6.y = 3000
            enemy7.x = 3000
            enemy7.y = 3000

        if lives == 0 or count == 0:
            reset = True

    if reset == True:
        camera.clear("black")
        camera.draw("You lose!", 100, "red", 400, 300)
        camera.display()

    if win == True and win2 == True:
        camera.clear("white")
        if lives == 5:
            camera.draw("You win! Score: 1250", 50, "green", 400, 300)
        elif lives == 4:
            camera.draw("You win! Score: 1000", 50, "green", 400, 300)
        elif lives == 3:
            camera.draw("You win! Score: 750", 50, "green", 400, 300)
        elif lives == 2:
            camera.draw("You win! Score: 500", 50, "green", 400, 300)
        elif lives == 1:
            camera.draw("You win! Score: 250", 50, "green", 400, 300)
        camera.display()

gamebox.timer_loop(30, tick)