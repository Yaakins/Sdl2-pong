import sdl2, sys
import sdl2.ext as ext

class Vector():
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)
    
    def __mul__(self, n):
        return Vector(self.x*n, self.y * n)

    def __sub__(self, o):
        return Vector(self.x-o.x, self.y-o.y)

    def __repr__(self):
        return f"<Vector ({self.x}, {self.y})>"

class Ball():
    def __init__(self, master, pos):
        self.master = master
        self.pos = pos
        self.radius = 10

        self.velocity = Vector(1, 1)
    
    def update(self):
        touched_wall = False
        if (self.pos + self.velocity).y > self.master.size.y or (self.pos + self.velocity).y < 0:
            self.pos += self.velocity
            self.velocity.y *= -1
            touched_wall = True
        if (self.pos + self.velocity).x > self.master.size.x or (self.pos + self.velocity).x < 0:
            self.pos += self.velocity
            self.velocity.x *= -1
            touched_wall = True
        if not touched_wall:
            self.pos += self.velocity
        
    
    def render(self, surface):
        ext.draw.fill(surface, ext.Color(255, 255, 255), (self.pos.x - self.radius, self.pos.y - self.radius, self.radius*2, self.radius * 2))

class Game():
    def __init__(self):
        ext.init()

        self.size = Vector(800, 600)        

        flags = (sdl2.SDL_WINDOW_SHOWN)
        self.window = ext.Window("test", (self.size.x, self.size.y), flags = flags)
        self.screen = self.window.get_surface()
    
        self.ball = Ball(self, Vector(self.size.x/2, self.size.y/2))
    
    def render(self):
        ext.fill(self.screen, ext.Color(0, 0, 0))
        ext.draw.fill(self.screen, ext.Color(255, 255, 255), (20, max(ext.mouse_coords()[1]-75, 0), 20, 150))

        self.ball.render(self.screen)

    def run(self):
        self.window.show()
        while True:
            for event in ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    self.window.close()
                    ext.quit()
                    sys.exit()
            self.ball.update()        
            
            self.render()
            self.window.refresh()

if __name__ == "__main__":
    game = Game()
    game.run()
    sys.exit()