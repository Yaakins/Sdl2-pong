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
    
class Board():
    def __init__(self, master, pos):
        self.master = master
        self.pos =pos

        self.height = 150

    def move(self, npos):
        if npos.y >=  self.master.size.y - self.height/2:
            npos.y = self.master.size.y - self.height/2
        elif npos.y <= self.height/2:
            npos.y = self.height/2
        self.pos = npos
    
    def render(self, surface):
        ext.draw.fill(surface, ext.Color(255, 255, 255), (self.pos.x - 10, self.pos.y - self.height/2, 20, self.height))

class Ball():
    def __init__(self, master, pos):
        self.master = master
        self.pos = pos
        self.radius = 10

        self.velocity = Vector(1, 1)
        self.moving = False
    
    def update(self):
        if self.moving:
            touched_wall = False
            if (self.pos + self.velocity).y > self.master.size.y or (self.pos + self.velocity).y < 0:
                self.pos += self.velocity
                self.velocity.y *= -1
                touched_wall = True
            if (self.pos + self.velocity).x > self.master.size.x:
                self.master.game_over("left")
                touched_wall = True
            elif  (self.pos + self.velocity).x < 0:
                self.master.game_over("right")
                touched_wall = True
            for board in self.master.boards:
                if board.pos.x - 10 < (self.pos + self.velocity).x < board.pos.x + 10 and board.pos.y - board.height/2 < (self.pos + self.velocity).y < board.pos.y + board.height/2:
                    touched_wall = True
                    self.velocity.x *= -1
            if not touched_wall:
                self.pos += self.velocity
        
    
    def render(self, surface):
        ext.draw.fill(surface, ext.Color(255, 255, 255), (self.pos.x - self.radius, self.pos.y - self.radius, self.radius*2, self.radius * 2))
