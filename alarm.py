import winsound, sys, pygame, time
pygame.init()

#opens a pygame window blank to allow button inputs
pygame.display.set_caption('Keyboard Example')
size = [640, 480]
screen = pygame.display.set_mode(size)

#plays the alarm
def Alarm_Sound():
    for i in range(7):
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

Alarm_Sound()

#choose to press left to end or down to snooze for 7 minutes
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                time.sleep(420)
                Alarm_Sound()
                crashed = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.quit()
                sys.exit()



pygame.quit()
sys.exit
