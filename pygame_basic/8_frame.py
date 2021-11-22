import pygame
#############################################
#기본초기화(반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임이름")

#FPS - Frame per Second - 초당 프레임수
clock = pygame.time.Clock()
#############################################

#1.사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

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

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종료
pygame.quit()
