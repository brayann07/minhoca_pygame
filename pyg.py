import pygame as pyGM
import random

# importantes
pyGM.init()
screen = pyGM.display.set_mode((1280,720))
clock = pyGM.time.Clock()
dt = 0
pyGM.display.set_caption("teste fisica")

screen_width = screen.get_width()
screen_height = screen.get_height()

# mouse variaveis
is_mouse_on_screen = False

# principal
running = True

# circles 
current_circles = []

# random
random_velocity = [10,30]
colors = ['red','white','purple','green','yellow']
random_dir = ['left','down','up','right']
# mouse old positions
mouse_positions = []

# font
font = pyGM.font.SysFont(None,30)


while running:
    for event in pyGM.event.get(): # EVENTOS GERAIS
        if event.type == pyGM.QUIT:
            running = False
        elif event.type == pyGM.WINDOWENTER:
            is_mouse_on_screen = True

            for i in range(len(current_circles)):
                current_circles[i]["velocity"] = random.choice(random_velocity)

        elif event.type == pyGM.WINDOWLEAVE:
            is_mouse_on_screen = False
        elif event.type == pyGM.MOUSEBUTTONDOWN:
            new_circle = {"pos" : pyGM.mouse.get_pos(), "color" : random.choice(colors), "direction" : random.choice(random_dir), "velocity" : random.choice(random_velocity), "direction_extra" : random.choice(random_dir)}
            if len(current_circles) >= 100:
                current_circles.pop(0)
            current_circles.append(new_circle)

    # tela cor
    screen.fill("magenta")    

    # bola 
    if len(current_circles) > 0:
        for circle in current_circles:
            pyGM.draw.circle(screen, circle["color"] , circle["pos"], 30)

    if is_mouse_on_screen:
        # mouse logic
        if len(mouse_positions) > 100: 
            mouse_positions.pop(0)
        mouse_positions.append(pyGM.mouse.get_pos())

        for i in range(len(current_circles)):
            target_pos = mouse_positions[-(i + 1)]
            current_circles[i]["pos"] = pyGM.Vector2(target_pos)
    else:
        for i in range(len(current_circles)):
            current_vel = current_circles[i]["velocity"]
            current_dir = current_circles[i]["direction"]
            current_pos = current_circles[i]["pos"]
        
            if current_vel > 0:
                if current_dir == "left":
                    current_circles[i]["pos"].x -= current_vel
                 
                elif current_dir == "down":
                    current_circles[i]["pos"].y += current_vel
                   
                elif current_dir == "up":
                    current_circles[i]["pos"].y -= current_vel
                   
                elif current_dir == "right":
                    current_circles[i]["pos"].x += current_vel
                


            if current_pos.x <= 0:
                current_circles[i]["direction"] = "right"
                current_circles[i]["velocity"] -= random.randint(1,2)
                current_circles[i]["color"] = random.choice(colors)
            elif current_pos.x >= screen_width:
                current_circles[i]["direction"] = "left"
                current_circles[i]["velocity"] -= random.randint(1,2)
                current_circles[i]["color"] = random.choice(colors)
            if current_pos.y <= 0:
                current_circles[i]["direction"] = "down"
                current_circles[i]["velocity"] -= random.randint(1,2)
                current_circles[i]["color"] = random.choice(colors)
            elif current_pos.y >= screen_height:
                current_circles[i]["direction"] = "up"
                current_circles[i]["velocity"] -= random.randint(1,2)
                current_circles[i]["color"] = random.choice(colors)
                
            if current_circles[i]["velocity"] > 0:
                current_circles[i]["velocity"] -= 5 * dt

    # draw len texto
    text_surface = font.render(f"NUM CIRCULOS:{len(current_circles)}", True, (255,255,255))
    screen.blit(text_surface,(screen_width / 2, 50))

    # DELTA TIME E REFRESH DA TELA
    pyGM.display.flip()
    dt = clock.tick(60) / 1000

pyGM.quit()