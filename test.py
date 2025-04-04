import pygame
import sys
from Scripts.engine import Engine
from Scripts.panel  import Panel
from Scripts.text   import Text



# You can change the position of each panel without changing the absolute position by updating the offset
# But you have to always keep track of how much offset are you applying in the screen

class TestPanel(Panel):
    
    def __init__(self, size, pos, color, hoverable=False, clickable=False, parent=None):
        super().__init__(size, pos, color, hoverable, clickable, parent)

        self.subpanel = TestSubPanel((100, 30), (0, 30), (0, 255, 120), parent=self)
        self.button = ButtonPanel((100, 30), (self.size[0]//2, self.size[1]//2), (255, 0, 120),hoverable=True, clickable=True, parent=self)
        self.text = Text("This is a main panel", size=15, pos=(20, 0))

    def update(self):
        self.image.fill(self.color)

    def render(self, surf, offset = [0, 0]):
        self.update()
        self.subpanel.render(self.image)
        self.button.render(self.image)
        self.text.render(self.image)
        return super().render(surf, offset)

class TestSubPanel(Panel):
    def __init__(self, size, pos, color, hoverable=False, clickable=False, parent=None):
        super().__init__(size, pos, color, hoverable, clickable, parent)
        self.text = Text("SubPanel", size=15, pos=(0, 0))
        
    def update(self):
        self.image.fill(self.color)

    def render(self, surf, offset = [0, 0]):
        self.update()
        self.text.render(self.image)
        return super().render(surf, offset)

class ButtonPanel(Panel):

    def __init__(self, size, pos, color, hoverable=False, clickable=False, parent=None):
        super().__init__(size, pos, color, hoverable, clickable, parent)

        self.text = Text("Button", size=15, pos=(20, 0))
    
    def hover(self):
        pass

    def onclick(self):
        pass

    def update(self):
        self.image.fill(self.color)

    def render(self, surf, offset = [0, 0]):
        self.update()
        self.text.render(self.image)
        return super().render(surf, offset)

class Window(Engine):

    def __init__(self, dim, font_size):
        super().__init__(dim, font_size)
        self.main = TestPanel((200, 200), (0, 0), (0, 255, 0))
        self.click = False

    def run(self):
        
        
        while True:
            
            self.display.fill((0, 0, 0, 0))

            # Note since the display screen and the window screen scale is 2
            # We have to adjust the mouse pos to properly calculate its true position

            mpos = [pygame.mouse.get_pos()[0] // 2, pygame.mouse.get_pos()[1] // 2] 
            m_rect = pygame.Rect(*mpos, 1, 1)
            self.click = False
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        self.click = True
                
                if event.type == pygame.MOUSEBUTTONUP:

                    if event.button == 1:
                        pass
            
            if m_rect.colliderect(self.main.button.rect()):
                print("You are hovering")
                if self.click:
                    print("You clicked the button")

            self.main.render(self.display)  

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Window((1000, 800), 20).run()
                    