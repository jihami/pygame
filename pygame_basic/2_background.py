import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_high = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_high))

#화면 타이틀 설정
pygame.display.set_caption("Hippo Game") #게임이름

#배경이미지 불러오기
backgroung = pygame.image.load("D:/game/pygame_basic/backgroung.png")

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트(X누르는거)가 발생하였는가?
            running = False #게임이 진행중이 아님

    screen.blit(backgroung,(0,0)) # 배경그리기 0,0은 시작하는 곳의 좌표 맨왼쪽 위가 (0,0)

    # screen.fill((0, 0, 255)) #rgb 컬러로 백그라운드 색이채워짐

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종
pygame.quit()
