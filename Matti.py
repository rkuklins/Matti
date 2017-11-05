import pygame, sys

# Metoda init laduje moduly pyGame odpowiedzialne
# m.in. za dzwiek czy grafike i jest podstawa kazdej aplikacji korzystajacej z tej biblioteki.
pygame.init()

# stworzenie okna w odpowiedzniej rozdzielczosci
screen = pygame.display.set_mode((1280, 720))
box = pygame.Rect(615, 335, 40, 40)
pox = pygame.Rect(615, 335, 40, 40)

# Wydrukowanie wersji pythona (zadnego celu to nie ma)
print(pygame.__version__)
clock = pygame.time.Clock()

delta = 0.0

# Gra w nieskonczonsc bedzie trwac ....
while True:
    # Ta linia czeka na zdarzenia
    for event in pygame.event.get():
        # Jesli zdarzeniem jest zdarzenie quit (czyli na przyklad zamkniecie okna) to wychodzi z programy
        if event.type == pygame.QUIT:
            sys.exit(0)
        # Podobnie jesli uzytkowni wcisnie klawisz i bedzie to klawisz ESCAPE - wychodzimy
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    #ticking - ta linia niczemu nie sluzy (jest zbedna) wylicza teoretycznie czas od poprzedniego obrotu petli ale
    # na nic potem nie wplywa. Tej delty mozna by pozniej uzyc do odpowiedniego przesunecia boxa (w zaleznosci od tego
    # ile uplynelo czasu - moznaby przesunac odpowiednio kwadrat
    delta += clock.tick()/1000.0

    # playing - tutaj juz zbierasz wcisniecia i przesuwasz kwadrat. jakbys 10 przemnozyl przez delta to
    # bedzie jakis wplyw czasu ktory uplynal
    keys = pygame.key.get_pressed()
    if keys [pygame.K_RIGHT]:
        box.x +=10
    if keys[pygame.K_LEFT]:
        box.x -=10
    if keys[pygame.K_DOWN]:
        box.y +=10
    if keys[pygame.K_UP]:
        box.y -=10
    if keys [pygame.K_d]:
        pox.x +=10
    if keys[pygame.K_a]:
        pox.x -=10
    if keys[pygame.K_s]:
        pox.y +=10
    if keys[pygame.K_w]:
        pox.y -=10

    # rendering - tutaj masz wlascie odmalowywanie kwadratow wraz z
    screen.fill ((0,0,23))
    pygame.draw.rect(screen, (255, 255, 255), box)
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pox)
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1270, 250, 30, 240))
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 250, 10, 240))
    pygame.display.flip()

