from random import choice
import pygame
from random import randint, randrange

TEXT_JUSTIFY_LEFT = 0
TEXT_JUSTIFY_CENTER = 1
TEXT_JUSTIFY_RIGHT = 2
TEXT_JUSTIFY_CENTER_Y = 3
TEXT_JUSTIFY_CENTER_X = 4


class Game:

    def __init__(self):
        self.COLOR_BLACK = (0, 0, 0)
        pygame.init()
        pygame.mixer.init()
        self.COLOR_FILL = 255, 255, 255
        self.CORRECT_SOUND = pygame.mixer.Sound('right.mp3')
        self.WRONG_SOUND = pygame.mixer.Sound('wrong.mp3')
        self.COLOR_GREEN = (21, 207, 123)
        self.COLOR_RED = (217, 9, 9)
        self.NICE_COLORS = [(19, 150, 107), (77, 38, 171), (210, 72, 40)]
        self.score = 0
        self.time_left = 60
        self.lives = 3
        self.time_left_color = self.COLOR_GREEN
        self.answer = ''
        self.question = ''
        self.question_color = None
        self.correct_answer = ''
        self.is_playing = True
        self.window = pygame.display.set_mode([500, 500])

        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, 1000)
        self.clock = pygame.time.Clock()
        self.start_game()

    def welcome(self):
        message = ['MATH GAME', 'I\'ll generate a random Math question', 'and it is you job to get the correct answer',
                   'Press space to continue...']
        while True:
            self.clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
            self.window.fill(self.COLOR_FILL)
            shift = 0
            for line in message:
                shift += self.write_text(line, self.window.get_width() // 2, shift + 100, 20, choice(self.NICE_COLORS),
                                         justify=TEXT_JUSTIFY_CENTER_X).height
            self.write_text('TURN ON YOUR SOUND FOR A BETTER EXPERIENCE', self.window.get_width(),
                            self.window.get_height() - 15, 15,
                            self.COLOR_BLACK, justify=TEXT_JUSTIFY_RIGHT)
            pygame.display.flip()

    def generate_question(self):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        sign = randint(0, 3)
        if sign == 0:
            sign = '-'
        elif sign == 1:
            num2 = randint(1, 50)
            num1 = randrange(0, 101, step=num2)
            sign = '//'
        elif sign == 2:
            sign = '*'
        else:
            sign = '+'
        self.question = f'{num1} {sign} {num2}'
        self.correct_answer = str(eval(self.question))
        self.question_color = choice(self.NICE_COLORS)
        self.reset_time()

    def end_game(self):
        shift = 0
        self.window.fill(self.COLOR_FILL)
        shift += self.write_text("GAME OVER!!!", self.window.get_width() // 2, self.window.get_height() // 2, 20,
                                 self.COLOR_RED, justify=TEXT_JUSTIFY_CENTER).height
        shift += self.write_text(f'You scored {self.score}',
                                 self.window.get_width() // 2, (self.window.get_height() // 2) + shift, 20,
                                 self.COLOR_GREEN,
                                 justify=TEXT_JUSTIFY_CENTER).height
        self.write_text('Press space to exit...', self.window.get_width() // 2, (self.window.get_height() // 2) + shift,
                        20,
                        self.COLOR_GREEN, justify=TEXT_JUSTIFY_CENTER)
        pygame.display.flip()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
        pygame.quit()
        exit(0)

    def write_text(self, string, coord_x, coord_y, font_size, color, justify=TEXT_JUSTIFY_LEFT):
        # set the font to write with
        font = pygame.font.Font('freesansbold.ttf', font_size)
        # set color to write with
        text = font.render(string, True, color)
        # get the rect of the text
        # set the position of the text
        if justify == TEXT_JUSTIFY_LEFT:
            text_rect = text.get_rect(left=coord_x, top=coord_y)
        elif justify == TEXT_JUSTIFY_CENTER_X:
            text_rect = text.get_rect(centerx=coord_x, top=coord_y)
        elif justify == TEXT_JUSTIFY_CENTER:
            text_rect = text.get_rect(center=(coord_x, coord_y))
        else:  # justify == TEXT_JUSTIFY_RIGHT:
            text_rect = text.get_rect(right=coord_x, top=coord_y)
        # add text to window
        self.window.blit(text, text_rect)
        return text_rect

    def reset_time(self):
        self.time_left = 10

    def next_frame(self):
        self.clock.tick(60)
        self.window.fill(self.COLOR_FILL)
        self.write_text(f'Score: {self.score}', 0, 10, 15, self.NICE_COLORS[0], justify=TEXT_JUSTIFY_LEFT)
        self.write_text(f'Time left: {self.time_left}', self.window.get_width(), 10, 15, self.time_left_color,
                        justify=TEXT_JUSTIFY_RIGHT)
        self.write_text(f'{self.question} = {self.answer}', self.window.get_width() // 2,
                        self.window.get_height() // 2,
                        25, self.question_color, justify=TEXT_JUSTIFY_CENTER)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.is_playing = False
                elif event.key == pygame.K_n:
                    self.generate_question()
                elif event.key == pygame.K_0:
                    self.answer += '0'
                elif event.key == pygame.K_1:
                    self.answer += '1'
                elif event.key == pygame.K_2:
                    self.answer += '2'
                elif event.key == pygame.K_3:
                    self.answer += '3'
                elif event.key == pygame.K_4:
                    self.answer += '4'
                elif event.key == pygame.K_5:
                    self.answer += '5'
                elif event.key == pygame.K_6:
                    self.answer += '6'
                elif event.key == pygame.K_7:
                    self.answer += '7'
                elif event.key == pygame.K_8:
                    self.answer += '8'
                elif event.key == pygame.K_9:
                    self.answer += '9'
                elif event.key == pygame.K_MINUS:
                    if not self.answer:
                        self.answer += '-'
                elif event.key == pygame.K_BACKSPACE:
                    self.answer = self.answer[:-1]
                if self.answer == self.correct_answer:
                    self.CORRECT_SOUND.play()
                    self.answer = ''
                    self.score += self.time_left * 10
                    self.generate_question()
                elif self.answer != self.correct_answer and len(self.answer) == len(self.correct_answer):
                    self.WRONG_SOUND.play()
                    self.answer = ''
                    self.generate_question()
                    self.end_game()
            if event.type == self.TIMER_EVENT:
                self.time_left -= 1
                if self.time_left == 0:
                    self.end_game()
                elif self.time_left <= 3:
                    self.time_left_color = self.COLOR_RED
                else:
                    self.time_left_color = self.COLOR_GREEN
        pygame.display.flip()

    def start_game(self):
        self.welcome()
        self.generate_question()
        while self.is_playing:
            self.next_frame()


if __name__ == '__main__':
    game = Game()
