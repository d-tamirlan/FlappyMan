import PyQt5.QtWidgets as qt
import random


class Obstacle(qt.QLabel):
    def __init__(self, window, obstacles_image_path, screen_size):
        super().__init__(window)
        self.screen_size = screen_size
        # print('init_height', window.height())
        self.setObjectName('obstacle')
        self.setStyleSheet('#obstacle {border-image: url(' + obstacles_image_path + ');}')
        # obstacles_image = qt_gui.QPixmap(obstacles_image_path)
        # self.setPixmap(obstacles_image)
        # self.move(100, 100)
        # self.resize(50, obstacles_image.height())
        self.slot = round(self.screen_size.height() / 4)
        # self.calc_height()
        # self.show()

    def locate(self, x_coordinate, position, obstacle_top=None):
        if position == 'Top':
            y_coordinate = random.randrange(100+self.slot, self.screen_size.height() - 100 - self.slot)
            self.calc_height(y_coordinate, position='Top')
            self.move(x_coordinate, 0)
            self.show()
        elif position == 'Bottom':
            y_coordinate = obstacle_top.height() + self.slot
            self.calc_height(y_coordinate, position='Bottom')
            self.move(x_coordinate, y_coordinate)
            self.show()
        else:
            raise Exception('Unexpected value ' + str(position) + ' choice "Top" or "Bottom"')

    def calc_height(self, y_coordinate, position):
        if position == 'Top':
            print('top_y', y_coordinate)
            self.resize(50, y_coordinate)
        elif position == 'Bottom':
            print('bottom_y', y_coordinate)
            obstacle_bottom_height = self.screen_size.height() - y_coordinate
            print('obstacle_bottom_height', obstacle_bottom_height)
            print('======================')
            self.resize(50, obstacle_bottom_height)
        # window_height = self.screen_size.height()
        # print('window_height', window_height)

        # print('slot', self.slot)
        # resize_height = (window_height - self.slot) / 2
        # print('resize_height', resize_height)

