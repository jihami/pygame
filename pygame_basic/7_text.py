import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hippo Game") #게임이름

#FPS - Frame per Second - 초당 프레임수
clock = pygame.time.Clock()

#배경이미지 불러오기
backgroung = pygame.image.load("D:/game/pygame_basic/backgroung.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/game/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 가져옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치 가로크기
character_y_pos = screen_height-character_height #화면 세로 크기 가장 아래 있는 곳에 위치 세로크기

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#적 enemy 캐릭터
enemy = pygame.image.load("D:/game/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 가져옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width/2) - (enemy_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치 가로크기
enemy_y_pos = (screen_height/2) - (enemy_height/2) #화면 세로 크기 가장 아래 있는 곳에 위치 세로크기

# 폰트정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

#총시간
total_time = 10

#시작시간 정보
start_tick = pygame.time.get_ticks() # 현재 tick 를 받아줌

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당프레임수 설정

    #캐릭터가 100만틈 이동해야함
    # 10fps : 1초동안 10번 동작 -> 1번에 몇 만큼 이동? 10만큼 이동 10 * 10 = 100
    # 20fps : 1초동안 20번 동작 -> 1번에 5만큼 이동 5 * 20 = 100

    print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트(X누르는거)가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            if event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed
            if event.key == pygame.K_UP: #캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN : #캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0 : # 가로 화면 왼쪽밖으로 벗어날때
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 가로 화면 오른쪽밖으로 벗어날때
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0 : # 세로 화면 위쪽밖으로 벗어날때
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height: # 세로 화면 아래쪽밖으로 벗어날때
        character_y_pos = screen_height- character_height

    #충돌 처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect): #사각형 기준 충돌확인 함수
        print("충돌")
        running = False

    screen.blit(backgroung,(0,0)) # 배경그리기 0,0은 시작하는 곳의 좌표 맨왼쪽 위가 (0,0)

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    # screen.fill((0, 0, 255)) #rgb 컬러로 백그라운드 색이채워짐

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    # 경과시간(ms)을 1000으로 나누어서 초(s)단위로 표시시


    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    #출력할 글자, 무조건 True, 글자 색상
    screen.blit(timer, (10,10))

    pygame.display.update() #게임화면 다시그리기 -> 안그리면 배경 적용 x

# pygame 종
pygame.quit()
