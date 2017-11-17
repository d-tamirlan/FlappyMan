import PyQt5.QtWidgets as qt
from Character import Character
from Obstacle import Obstacle


class Window(qt.QMainWindow):
    obstacles_list = []
    obstacles_couple_count = 5
    obstacles_step = 300

    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.setWindowTitle('Flappy Man')
        self.showMaximized()
        self.setObjectName('ManiWindow')
        self.setStyleSheet("#ManiWindow {border-image: url(img/background.png);}")
        self.character = Character(self, 'img/character.png')
        self.generate_obstacles()

    def generate_obstacles(self):
        x_coordinate = 300

        for _ in range(self.obstacles_couple_count):
            # Top obstacles
            obstacle_top = Obstacle(self, 'img/obstacle_top.png', self.screen_size)
            obstacle_top.locate(x_coordinate, position='Top')
            # print('top obs', obstacle.height())
            self.obstacles_list.append(obstacle_top)
            # =============
            # Bottom obstacles
            obstacle_bottom = Obstacle(self, 'img/obstacle_bottom.png', self.screen_size)
            obstacle_bottom.locate(x_coordinate, position='Bottom', obstacle_top=obstacle_top)
            # print('bottom_obs', obstacle.height())
            # self.obstacles_list.append(obstacle)

            x_coordinate += self.obstacles_step


    def keyPressEvent(self, event):
        self.character.character_move(event)