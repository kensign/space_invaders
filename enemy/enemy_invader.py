import asyncio
import os

import arcade


class EnemyInvader(arcade.Sprite):
    BULLET_SPEED = 5
    ENEMY_SPEED = 1.5
    ENEMY_EXPLOSION_COLOR = 128, 0, 0
    # How many pixels to move the enemy down when reversing
    ENEMY_MOVE_DOWN_AMOUNT = 30

    def __init__(self, texture_1, texture_2, loop):
        super().__init__()
        self.loop = loop
        self.texture_1 = texture_1
        self.texture_2 = texture_2
        self.time = 0
        self.last_time = 0
        self.dead = False
        self.score = 0
        self.playing_sound = False
        self.texture = self.texture_1
        self.background_audio = []

        for i in range(1, 5):
            self.background_audio.append(arcade.load_sound(os.path.abspath(f"assets/audio/bg{i}.wav")))

        arcade.play_sound(self.background_audio[0])
        # asyncio.create_task(self.play_background(None))

    def on_update(self, dt):
        self.time += dt
        if self.dead:
            if self.time >= 0.5:
                self.remove_from_sprite_lists()
            return

        t = int(self.time * 2)
        t2 = t % 2
        if t2 == 0:
            self.texture = self.texture_1
        elif t2 == 1:
            self.texture = self.texture_2

        if not self.playing_sound:
            self.playing_sound = True
            asyncio.run_coroutine_threadsafe(self.play_background(t), self.loop)

    async def play_background(self, time):
        current_second = int(time * 2)
        current_note = current_second % 4
        if current_second > self.last_time:
            arcade.play_sound(self.background_audio[current_note])
            await asyncio.sleep(self.background_audio[current_note].get_length())
            self.playing_sound = False
            print(self.last_time, current_second)
            self.last_time = current_second

    def explode(self):
        self.texture = arcade.load_texture('./assets/images/enemy_explosion.png')
        self.dead = True
        self.time = 0
        self.color = self.ENEMY_EXPLOSION_COLOR
