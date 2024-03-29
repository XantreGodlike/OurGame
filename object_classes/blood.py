import settings
import pygame
from object_classes.temp_object import TemporaryObject

class Blood(TemporaryObject):
    blood_color = (152, 0, 2)
    def __init__(self, cord, Worker = None):
        super().__init__(cord, settings.blood_size, color = self.blood_color, Worker=Worker)
    
    def run(self, *args):
        super().run(*args)
        self.off_frame = True if self.timer > 15 else False
