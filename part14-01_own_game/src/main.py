# Complete your game here
import pygame
from random import randint

class Asset:
    def __init__(self, x:int, y: int, variant: str):
        self.x = x
        self.y = y
        self.img = variant
        self.width = self.img.get_width()
        self.height = self.img.get_height()

class CoinCollector:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Coin Collector")              

        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.hi_score = 0
        self.load_images()  
        self.main_loop()

    #loads the assets images into the game
    def load_images(self):
        self.images = []
        for name in ["robot", "coin", "monster"]:
            self.images.append(pygame.image.load(name + ".png"))
    
    #sets a new game
    def new_game(self):
        self.lives = 3
        self.score = 0
        self.robot = Asset(self.width/2-self.images[0].get_width() /2, self.height - self.images[0].get_height(), self.images[0])
        self.falling_objects = [] 
        self.game_state = 1       

    #runs the corresponding loop according to game state
    def main_loop(self):
        self.game_state = 0
        self.to_left = False
        self.to_right = False
        while True:
            while self.game_state == 0:
                self.start_loop()

            while self.game_state == 1:
              self.game_loop()  
            
            while self.game_state == 2:
                self.end_loop()

    #the game start loop 
    def start_loop(self):
        self.check_events()
        self.draw_window()
        self.clock.tick(60)
    
    #the main game loop
    def game_loop(self):
        self.check_events()
        self.move()
        self.falling_objects_generator()
        self.check_collision()
        self.draw_window()        
        self.clock.tick(60)
        if self.game_over():
            self.end_game()

    #the end of game loop
    def end_loop(self):
        self.check_events()
        self.draw_window()
        self.clock.tick(60)


    #returns true when lives reach 0
    def game_over(self):        
        if self.lives == 0:
            return True
    
    #handles high score and game state
    def end_game(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
        self.game_state = 2

    #generates coins and monsters up to a limit
    def falling_objects_generator(self):
        #randomizes if the generated object will be a coin or a monster
        def coin_or_monster():
            if randint(0, 100) < min(10 + self.score, 50):
                return 2
            else: 
                return 1

        if len(self.falling_objects) == 0:
            self.falling_objects.append(Asset(randint(0, self.width - self.images[1].get_width()), 10, self.images[1]))
        if len(self.falling_objects) < 5 and self.falling_objects[-1].y > 100:            
            self.falling_objects.append(Asset(randint(0, self.width - self.images[coin_or_monster()].get_width()), 10, self.images[coin_or_monster()]))      

    #checks for coin and monster collision with player robot, modifies lives and score and removes non collected items
    def check_collision(self):    
        for f_object in self.falling_objects:
            if f_object.y > self.height - self.robot.img.get_height() - f_object.img.get_height():
                if f_object.x > self.robot.x - f_object.img.get_height() and f_object.x < self.robot.x + self.robot.img.get_width():
                    self.falling_objects.remove(f_object)
                    if f_object.img == self.images[1]:    
                        self.score += 1
                    else:
                        self.lives -=1
            if f_object.y < 480 - f_object.img.get_height():
                f_object.y += 1
            else:
                self.falling_objects.remove(f_object)



    #monitors user input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_n:
                    self.new_game()  
                if event.key == pygame.K_e:
                    self.end_game()
                if event.key == pygame.K_q:
                    exit()   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
            if event.type == pygame.QUIT:
                exit()

    #handles player movement
    def move(self):
        move_unit = 2
        if self.to_left:
            if self.robot.x + move_unit > 0:
                self.robot.x -= move_unit
        if self.to_right:
            if self.robot.x + move_unit < self.width - self.robot.width:
                self.robot.x += move_unit

    
    def game_assets(self):
        self.window.blit(self.robot.img, (self.robot.x, self.robot.y))
        for f_object in self.falling_objects:
            self.window.blit(f_object.img, (f_object.x, f_object.y))

    #generates the score and lives text
    def game_text(self):
        game_font = pygame.font.SysFont("Arial", 24)
        score_text = game_font.render(f"Score: {self.score}", True, (255, 0, 0))
        hi_score_text = game_font.render(f"Hi Score: {self.hi_score}", True, (255, 0, 0))
        lives_text = game_font.render(f"Lives: {self.lives}", True, (255, 0, 0))
        self.window.blit(score_text, (280, 1))
        self.window.blit(hi_score_text, (10, 1))
        self.window.blit(lives_text, (550, 1))

    #generates the welcome and instructions text
    def start_text(self):
        welcome_font = pygame.font.SysFont("Arial", 48)
        instructions_font = pygame.font.SysFont("Arial", 24)
        welcome_text = welcome_font.render("Welcome to Coin Collector!", True, (255, 0, 0))
        instructions_text = ["N = New Game", "E = End game", "Q = Quit", "Left / Right to move"]
        for i in range(0, len(instructions_text)):
            text = instructions_font.render(instructions_text[i], True, (255, 0, 0))
            self.window.blit(text, (240, 120 + 30 * i))
        
        self.window.blit(welcome_text, (30, 50))

    #generates the end of game text
    def end_text(self):        
        over_font = pygame.font.SysFont("Arial", 48)
        instructions_font = pygame.font.SysFont("Arial", 24)
        over_text = over_font.render("GAME OVER!", True, (255, 0, 0))
        instructions_text = [f"Your Score: {self.score}",f"High Score: {self.hi_score}","", "","N = New Game", "Q = Quit",]
        for i in range(0, len(instructions_text)):
            text = instructions_font.render(instructions_text[i], True, (255, 0, 0))
            self.window.blit(text, (240, 120 + 30 * i))
        
        self.window.blit(over_text, (150, 50))

    
    #draws the corresponding text and asssest according to game state
    def draw_window(self):
        self.window.fill((120, 120, 120))
        if self.game_state == 0:
            self.start_text()        
        elif self.game_state == 1:
            self.game_text()
            self.game_assets()
        elif self.game_state == 2:
            self.end_text()

        pygame.display.flip()

if __name__ == "__main__":
    CoinCollector()