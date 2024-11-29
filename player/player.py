import arcade


class Player(arcade.Sprite):
    PLAYER_BULLET_SPEED = 8
    PLAYER_SPEED = 5
    PLAYER_COLOR = 24, 255, 24

    def __init__(self, image_asset, scale=1):
        super().__init__()
        self.texture = arcade.load_texture(image_asset)
        self.scale = scale
        self.center_x = 600
        self.center_y = 60
        self.color = self.PLAYER_COLOR
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_stopped = True

    def move_left(self):
        self.center_x -= self.PLAYER_SPEED
        self.is_moving_left = True
        self.is_stopped = False

    def move_right(self):
        self.center_x += self.PLAYER_SPEED
        self.is_moving_right = True
        self.is_stopped = False

    def stop(self):
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_stopped = True

