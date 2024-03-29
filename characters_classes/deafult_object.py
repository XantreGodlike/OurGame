class GameObject:
    def __init__(self, rect):
        self.rect = rect

    def move(self, dx, dy):
        self.rect.centerx += dx
        self.rect.centery += dy

    def left_side(self):
        return [
            self.rect.topleft, 
            self.rect.midleft, 
            self.rect.bottomleft
        ]

    def right_side(self):
        return [
            self.rect.topright, 
            self.rect.midright, 
            self.rect.bottomright
            ]
    
    def bottom_side(self):
        return [
            self.rect.bottomleft,
            self.rect.midbottom,
            self.rect.bottomright
        ]

    def top_side(self):
        return [
            self.rect.topright,
            self.rect.midtop,
            self.rect.topleft
        ]