import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

class MazeDayGame:
    
    def __init__(self):

        pygame.init()

        pygame.mixer.init()

        pygame.display.set_caption("To The Middle!")

        self.screen = pygame.display.set_mode((640,480),0,32)

        self.screen.fill([0, 240, 100])

    def winner(self, player_one_count, player_two_count):

        self.screen.fill([255, 255, 255])

        win_font = pygame.font.SysFont('arial', 30)

        if player_one_count > player_two_count:
            win = win_font.render("Player One Wins!", True, (0, 0, 0), (0, 208, 255))
            self.screen.blit(win, (210, 250))
            print "Player One Wins!"
        elif player_two_count > player_one_count:
            win = win_font.render("Player Two Wins!", True, (0, 0, 0), (255, 185, 0))
            self.screen.blit(win, (210, 250))
            print "Player Two Wins!"
        
        pygame.display.flip()

        pygame.time.delay(2000)

    def run(self):

        player_one_count = 0

        player_two_count = 0
        
        count = 0

        pressed_keys = 0

        beat_sound = pygame.mixer.Sound("Blop.ogg")

        player_one = pygame.image.load("icon-zoom-blurry2.jpg").convert_alpha()      
        player_two = pygame.image.load("icon-zoom-blurry.jpg").convert_alpha()
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        font = pygame.font.SysFont('impact', 50)

        text = font.render("To The Middle!", True, (0, 0, 0), (0, 250, 100))

        self.screen.blit(text, (250, 230))

        pygame.display.flip()

        pygame.time.delay(1000)

        self.screen.fill([255, 255, 255])

        font = pygame.font.SysFont('arial', 30)

        text = font.render("Start!", True, (0, 0, 0), (250, 250, 250))

        self.screen.blit(text, (270, 250))

        pygame.display.flip() 

        player1_higher = True
        player2_higher = True
        
        player1_image = Images(25, player_one)
        player2_image = Images(500, player_two)

        while True:

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                print 'quit'
                break

            if event.type == pygame.KEYDOWN:
                pressed_keys = event.key
                continue

            if event.type != pygame.USEREVENT:
                continue

            print 'timer', count
            print player_one_count

            if count == 3 or count == 8 or count == 17 or count == 29 or count == 46:
                
                Sounds().high_beat(beat_sound)

                print player1_image.position

                player1_image.CloseToCenterFor(self.screen)
                player2_image.CloseToCenterBack(self.screen)
            
                if(pressed_keys == K_f):

                    player1_higher = True
                    player2_higher = False
                    
                elif(pressed_keys == K_j):
                    
                    player1_higher = False
                    player2_higher = True

            elif count == 5 or count == 11 or count == 12 or count == 20 or count == 21 or count == 24 or count == 30 or count == 36 or count == 40 or count == 45:
                pressed_keys = 0
                Sounds().medium_beat(beat_sound)

                player2_image.MoveForward(self.screen)
                player1_image.MoveBackward(self.screen)

                count += 1

            elif count == 14 or count == 22 or count == 27 or count == 34 or count == 38 or count == 41:
                pressed_keys = 0
                Sounds().medium_high_beat(beat_sound)

                player2_image.MoveForward(self.screen)
                player1_image.MoveBackward(self.screen)

                count += 1

            else:
                pressed_keys = 0
                Sounds().low_beat(beat_sound)

                player1_image.MoveForward(self.screen)
                player2_image.MoveBackward(self.screen)

                count += 1

            if player1_higher == True and player2_higher == False:
                
                player_one_count += 1
                self.screen.fill([255, 255, 255])
                
                player1_image.GotPoint(self.screen)
                player2_image.NoPointTwo(self.screen)

                player2_higher = True
                    
                pygame.display.flip()

                pygame.time.delay(1000)

                player1_image.Reset(25)
                player2_image.Reset(500)

                pressed_keys = 0

                count += 1
                
            elif player2_higher == True and player1_higher == False:

                player_two_count += 1
                self.screen.fill([255, 255, 255])

                player2_image.GotPoint(self.screen)
                player1_image.NoPointOne(self.screen)

                player1_higher = True

                pygame.display.flip()

                pygame.time.delay(1000)

                player1_image.Reset(25)
                player2_image.Reset(500)

                pressed_keys = 0

                count += 1

            elif player1_higher == False and player2_higher == False:

                player1_higher = True
                player2_higher = True

                pygame.display.flip()

                pygame.time.delay(1000)

                player1_image.Reset(25)
                player2_image.Reset(500)

                pressed_keys = 0

                count += 1
                
            if count == 47:

                break

            if count == 4:

                pygame.time.set_timer(pygame.USEREVENT, 750)

            if count == 9:

                pygame.time.set_timer(pygame.USEREVENT, 500)

            if count == 18:

                pygame.time.set_timer(pygame.USEREVENT, 250)

            if count == 30:

                pygame.time.set_timer(pygame.USEREVENT, 190)

            pygame.display.flip()
            
            self.screen.fill([255, 255, 255])
            
        self.winner(player_one_count, player_two_count)

        beat_sound.play()
        pygame.quit()

class Images(object):

    def __init__(self, pos, sprite):
        self.position = pos
        self.sprite = sprite

    def MoveForward(self, screen):
        self.position += 50
        screen.blit(self.sprite, (self.position, 150))

    def MoveBackward(self, screen):
        self.position -= 50
        screen.blit(self.sprite, (self.position, 150))

    def CloseToCenterFor(self, screen):
        self.position += 25
        screen.blit(self.sprite, (self.position, 50))

    def CloseToCenterBack(self, screen):
        self.position -= 25
        screen.blit(self.sprite, (self.position, 50))

    def GotPoint(self, screen): 
        screen.blit(self.sprite, (250, 52))

    def NoPointOne(self, screen):
        self.MoveBackward(screen)

    def NoPointTwo(self, screen):
        self.MoveForward(screen)

    def Reset(self, pos):
        self.position = pos

class Sounds:

    def __init__(self):

         pass

    def low_beat(self, beat_sound):
        beat_sound.set_volume(0.28)
        beat_sound.play()

    def high_beat(self, beat_sound):

        beat_sound.set_volume(1.0)
        beat_sound.play()
        
    def medium_beat(self, beat_sound):
        beat_sound.set_volume(0.55)
        beat_sound.play()

    def medium_high_beat(self, beat_sound):

        beat_sound.set_volume(0.72)
        beat_sound.play()

if __name__ == '__main__':

    MazeDayGame().run()
