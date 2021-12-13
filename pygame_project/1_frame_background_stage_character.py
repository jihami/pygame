import os

import pygame
#############################################
#기본초기화(반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 640 #가로 크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Pang Pang")

#FPS - Frame per Second - 초당 프레임수
clock = pygame.time.Clock()
#############################################

#1.사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# current_path = os.path.dirname(__file__) #현재파일 위치 반환
current_path = os.getcwd() #현재 작업 폴더 얻기
image_path = os.path.join(current_path,"images")#이미지 폴더 위치 반환

#배경생성
background = pygame.image.load(os.path.join(image_path, "backgound.png"))
#스테이지 생성
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 두기 위해 사용
#캐릭터 생성
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #보통은 30사용
    #2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #3.게임 캐릭터 위치 정의

    #4.충돌처리

    #5.화면 그리기기
    screen.blit(background,(0,0))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종료
pygame.quit()
