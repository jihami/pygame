import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hippo Game") #게임이름

#배경이미지 불러오기
backgroung = pygame.image.load("D:/game/pygame_basic/backgroung.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/game/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 가져옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치 가로크기
character_y_pos = screen_height-character_height #화면 세로 크기 가장 아래 있는 곳에 위치 세로크기

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트(X누르는거)가 발생하였는가?
            running = False #게임이 진행중이 아님

    screen.blit(backgroung,(0,0)) # 배경그리기 0,0은 시작하는 곳의 좌표 맨왼쪽 위가 (0,0)
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    # screen.fill((0, 0, 255)) #rgb 컬러로 백그라운드 색이채워짐

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종
pygame.quit()
