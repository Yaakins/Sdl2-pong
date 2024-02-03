import sdl2, sys, time
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
        self.board = Board(self, Vector(20, self.size.y/2))

        self.last_tick = sdl2.timer.SDL_GetTicks()
    
    def render(self):
        ext.fill(self.screen, ext.Color(0, 0, 0))

        self.ball.render(self.screen)
        self.board.render(self.screen)
    
    def tick(self, n):
        if sdl2.timer.SDL_GetTicks() - self.last_tick < 1000/n:
            sdl2.timer.SDL_Delay(int(self.last_tick + 1000/n - sdl2.timer.SDL_GetTicks()))

    def run(self):
        self.window.show()
        while True:
            for event in ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    self.window.close()
                    ext.quit()
                    sys.exit()

            self.board.move(Vector(self.board.pos.x, ext.mouse.mouse_coords()[1]))
            self.ball.update()        
            
            self.render()
            self.window.refresh()

            self.tick(30)

if __name__ == "__main__":
    game = Game()
    game.run()
    sys.exit()