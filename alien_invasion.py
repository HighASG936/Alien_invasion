import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint
from time import sleep
from game_stats import GameStats
from button import Button
from button_easy import ButtonEasy
from button_middle import ButtonMiddle
from button_hard import ButtonHard
from scoreboard import Scoreboard
from sound import Sound
from game_over import GameOver
from game_pause import GamePause
from game_help import GameHelp

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game, adn create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width,
               self.settings.screen_height
             ))       
#         self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#         self.settings.screen_width = self.screen.get_rect().width
#         self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #Create an instance to store game statistics,
        #  and create a scoreboard.
        self.mode_level = 'easy'
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.button_easy = ButtonEasy(self)
        self.button_middle = ButtonMiddle(self)
        self.button_hard = ButtonHard(self)
        self.game_over = GameOver(self)
        self.game_pause = GamePause(self)
        self.game_help = GameHelp(self)
        
        self.level_is_set = False
        self.you_lose_before = False  
        self._create_fleet()
        self._draw_stars()        
        
        #Make the Play button.
        self.play_button = Button(self, "Play")
        self.sound = Sound()
        
        self.sound.play_background_song()
        self.is_paused = False
        

    def _draw_stars(self):
        """ """
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width        
        number_star_x = available_space_x // (5* star_width)        
        
        #Determine the number of rows of aliens that fit on the screen        
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * star_height)
                
        #Create the full fleet of aliens.
        for row_number in range(number_rows):
            for star_number in range(number_star_x):                        
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an alien and place it in the row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 1 * star_width * star_number * randint(1, 15)
        star.rect.x = star.x
        star.rect.y = (star_height + 1 * star.rect.height * row_number
                       * randint(1, 15))
        self.stars.add(star)       

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()                
                if self.level_is_set:
                    self._check_play_button(mouse_pos)
                else:
                    self._check_level_buttons(mouse_pos)
                    self._check_help_button(mouse_pos)
                
                    
    
    def _reset_game_settings(self):
        """Reset the game settings."""
        self.settings.initialize_dynamic_settings()            
        self.level_is_set = False
            
    def _reset_game_stats(self):
        """Reset the game statistics."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
    
    def _clean_screen(self):
        """Get rid of any remaining aliens and bullets."""
        self.aliens.empty()
        self.bullets.empty()        
 
    def _reset_fleet_and_ship(self):
        """Create a new fleet and center the ship"""
        self._create_fleet()
        self.ship.center_ship()         
    
    def _check_play_button(self, mouse_pos=None):
        """Start new game when the player clicks Play."""
        if mouse_pos:
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        else:
            button_clicked = True
        
        if button_clicked and not self.stats.game_active:            
            self._reset_game_settings()
            self._reset_game_stats()                            
            self._clean_screen()
            self._reset_fleet_and_ship()            
            #Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            
            self.sound.play_button_sound()
            self.sound.play_background_song()

    def _check_level_buttons(self, mouse_pos):
        """Set Easy mode to start game"""
        if self.button_easy.rect.collidepoint(mouse_pos):
            self.settings.ship_speed =   1
            self.settings.bullet_speed = 2
            self.settings.alien_speed =  1
            self.mode_level = 'easy'
            self.sound.play_button_sound()
            self.level_is_set = True
        elif self.button_middle.rect.collidepoint(mouse_pos):
            self.settings.ship_speed =   2
            self.settings.bullet_speed = 3
            self.settings.alien_speed =  2
            self.mode_level = 'middle'
            self.sound.play_button_sound()
            self.level_is_set = True
        elif self.button_hard.rect.collidepoint(mouse_pos):
            self.settings.ship_speed =   3
            self.settings.bullet_speed = 4
            self.settings.alien_speed =  3
            self.mode_level = 'hard'
            self.sound.play_button_sound()
            self.level_is_set = True
        self.sb.get_high_score()
        self.sb.prep_high_score()

    def _check_help_button(self, mouse_pos):
        """ """
        if (self.game_help.rect.collidepoint(mouse_pos) and
            not self.stats.game_active):
            self.sound.play_pause_sound()
            print("Help")
            
    
    def _check_pause_event(self):
        """Toggle pause status game and check actions"""
        self.is_paused = not self.is_paused            
        self.sound.play_pause_sound()
        if not self.is_paused:
            self.sound.resume_background_song()            
        

    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            self.sb.set_new_high_score()
            sys.exit()
        elif event.key == pygame.K_p:            
            if self.stats.game_active:
                self._check_pause_event()
            else:
                if self.level_is_set:
                    self._check_play_button()
            

    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False          
  
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:            
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            #Shoot sound FX
            if self.stats.game_active:
                self.sound.play_shooting_sound()
  
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
            
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets tha have hit aliens.
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_sore()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self.sound.play_level_up_sound()
            sleep(1.5)
    
    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // ( 2 * alien_width)
        
        #Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             3 * alien_height - ship_height)
        number_rows = available_space_y // (2 * alien_height)
                
        #Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):                        
                self._create_alien(alien_number, row_number)
     
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number                         
        self.aliens.add(alien)
  
    def _update_screen(self):        
        """Update images on the screen, and flip to the new screen"""        
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        
        #Draw the score information
        self.sb.show_score()
        
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        self.aliens.draw(self.screen)        
        
        #Draw the play button if the game is inactive
        if not self.stats.game_active: 
            if not self.level_is_set:            
                if not self.sound.is_busy():
                    self.button_easy.draw_button()
                    self.button_middle.draw_button()
                    self.button_hard.draw_button()
                    self.game_help.draw_button()
                
                if self.you_lose_before:
                    self.game_over.draw_game_over()                    
            else:
                self.play_button.draw_button()
        else:
            if self.is_paused:
                    self.game_pause.draw_pause()
        
        pygame.display.flip()

    def  _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()        

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #Look for aliens hitting the bottom of the scren
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #Decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
        
            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            #Pause
            self.sound.play_ship_hit_sound()
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.you_lose_before = True
            pygame.mouse.set_visible(True)
            self.sound.stop_background_song()
            self.sound.play_game_over()                        

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as us the ship got hit
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Responds appropiately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_elements_on_screen(self):
        """update ship, bullets and aliens depend to their interction"""
        if self.stats.game_active:  
            self.ship.update()
            self._update_bullets()
            self._update_aliens()                    
    
    def run_game(self):
        """Start tha main loop for the game"""        
        while True:
            self._check_events()                        
            if not self.is_paused:  
                self._update_elements_on_screen()                    
            else:
                self.sound.pause_background_song()                
            self._update_screen()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        
