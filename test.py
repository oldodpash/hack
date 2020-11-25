import random
import time
import simpleaudio as sa
import pyautogui
import pygame
from pygame import mixer
import sys

def main():
    bomzh = ['1.png', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '9.jpg', '10.jpg', '11.jpg', '12.png',
             '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg']
    pygame.font.init()
    size = pyautogui.size()
    sc = pygame.display.set_mode(size)
    sc.fill((255, 255, 255))

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Привет! Я хацкер Олег. Сейчас начнется представление.'
                      ' архивировать твои файлы!!! Приятного просмотра!', True, (180, 0, 0))
    text2 = f1.render('Ну а пока ты будешь его смотреть я буду архивировать', True, (180, 0, 0))
    text3 = f1.render('твои файлы!!! Приятного просмотра!', True, (180, 0, 0))
    sc.blit(text1, (10, 30))
    sc.blit(text2, (10, 60))
    sc.blit(text3, (10, 90))

    pygame.display.update()

    mixer.init()
    mixer.music.load(".mp3\\zvuki-orgazm.mp3")
    mixer.music.play()
    time.sleep(7)
    stage = 0
    start_time = time.time()
    mixer.init()
    mixer.music.load(".mp3\\1.mp3")
    mixer.music.play()

    while True:
        time.sleep(0.05)
        image = pygame.image.load(f'.img\\{bomzh[random.randint(0, len(bomzh) - 1)]}').convert_alpha()
        img_size = image.get_size()
        image = pygame.transform.scale(image, (random.randint(1, 1000), random.randint(1, 1000)))
       # image = pygame.transform.rotate(image, random.randint(0, 360))

        x = random.randint(1, size[0]) - img_size[0]
        if x < 0:
            x += img_size[0]
        y = random.randint(1, size[1]) - img_size[1]
        if y < 0:
            y += img_size[1]
        sc.blit(image, (x, y))
        pygame.display.update()
        #pyautogui.moveTo(random.randint(1, size[0]), random.randint(1, size[1]))
        for i in pygame.event.get():
            pass

main()