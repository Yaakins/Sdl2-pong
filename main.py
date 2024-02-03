import sdl2, sys, ctypes
import sdl2.ext as ext
from classes import * 


class Game():
    def __init__(self):
        ext.init()

        self.size = Vector(800, 600)        

        flags = (sdl2.SDL_WINDOW_SHOWN)
        self.window = ext.Window("test", (self.size.x, self.size.y), flags = flags)
        self.screen = self.window.get_surface()
    
        self.ball = Ball(self, Vector(self.size.x/2, self.size.y/2))
        self.boards = [Board(self, Vector(30, self.size.y/2)), Board(self, Vector(self.size.x-30, self.size.y/2))]

        self.last_tick = sdl2.timer.SDL_GetTicks()
    
    def render(self):
        ext.fill(self.screen, ext.Color(0, 0, 0))

        self.ball.render(self.screen)
        for board in self.boards:
            board.render(self.screen)
    
    def tick(self, n):
        if sdl2.timer.SDL_GetTicks() - self.last_tick < 1000/n:
            sdl2.timer.SDL_Delay(int(self.last_tick + 1000/n - sdl2.timer.SDL_GetTicks()))

    def game_over(self, team):
        print(f"{team} team won!")
        self.ball.pos = Vector(self.size.x/2, self.size.y/2)
        self.ball.moving = False

    def handle_keys(self):
        keys = sdl2.keyboard.SDL_GetKeyboardState(None)
        if keys[sdl2.SDL_SCANCODE_W]:
            self.boards[0].move(Vector(self.boards[0].pos.x, self.boards[0].pos.y - 1.5))
        if keys[sdl2.SDL_SCANCODE_S]:
            self.boards[0].move(Vector(self.boards[0].pos.x, self.boards[0].pos.y + 1.5))
        if keys[sdl2.SDL_SCANCODE_UP]:
            self.boards[1].move(Vector(self.boards[1].pos.x, self.boards[1].pos.y - 1.5))
        if keys[sdl2.SDL_SCANCODE_DOWN]:
            self.boards[1].move(Vector(self.boards[1].pos.x, self.boards[1].pos.y + 1.5))
        
        if keys[sdl2.SDL_SCANCODE_SPACE]:
            self.ball.moving = True


    def run(self):
        self.window.show()
        while True:
            for event in ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    self.window.close()
                    ext.quit()
                    sys.exit()

            self.handle_keys()
            self.ball.update()        
            
            self.render()
            self.window.refresh()

            self.tick(30)

if __name__ == "__main__":
    game = Game()
    game.run()
    sys.exit()