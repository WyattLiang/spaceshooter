from curses import KEY_LEFT
import sys

import pygame

from settings import Settings
from ship import Ship

class SpaceShooter:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        
        """
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        """
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #set background color.
        self.bg_color = (230,230,230)
    

    def run_game(self):
        """start the main loop for the game."""
        while True:
            """Watch for keyboard and mouse events. """
            self._check_events()
            self.ship.update()
            self._update_screen()

            

    def _update_screen(self):
        """Update image on the screen"""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()    

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                        
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                     
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True    
        elif event.key == pygame.K_q:
            sys.exit()
              
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
                            

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = SpaceShooter()
    ai.run_game()                        