import turtle
import time
import random
import pygame
import os

HEIGHT = 650
WIDTH = 800
TOTAL_ROUNDS = 5

COLORS = [
    "red", "blue", "green", "yellow", "purple",
    "orange", "pink", "brown", "cyan", "magenta"
]

# --- FILE---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# --- AUDIO ---


def init_audio():
    """Fires up the pygame audio engine so we can play sounds."""
    try:
        pygame.mixer.init()
        return True
    except Exception as e:
        print(f"Audio system could not initialize. Error: {e}")
        return False


def play_bg_music():
    """Loads our background music, sets the volume, and plays it on a glorious, endless loop."""
    try:
        pygame.mixer.stop()
        music_path = os.path.join(SCRIPT_DIR, "race_music.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Could not load background music. Error: {e}")


def play_victory_sound():
    try:
        # Important: stop the main music track first.
        pygame.mixer.music.stop()
        victory_path = os.path.join(SCRIPT_DIR, "victory.mp3")
        victory_sound = pygame.mixer.Sound(victory_path)
        victory_sound.play()
    except Exception as e:
        print(f"Could not play victory sound. Error: {e}")

# --- CLASSES ---


class Racer:
    def __init__(self, color, x_pos, y_pos):
        self.color = color
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.t.color(color)
        self.t.left(90)
        self.t.penup()
        self.t.goto(x_pos, y_pos)

        self.finished = False
        self.finish_time = 0.0

        self.base_speed = random.uniform(0.25, 0.45)
        self.current_speed = self.base_speed
        self.effect_timer = 0
        self.x_pos = x_pos

    def move(self):
        if self.finished:
            return

        if self.effect_timer > 0:
            self.effect_timer -= 1
        else:
            self.current_speed = self.base_speed

        step = self.current_speed + random.uniform(0, 0.15)
        self.t.forward(step)

    def apply_effect(self, effect_type):
        if effect_type == "mud":
            self.current_speed = self.base_speed * 0.2
            self.effect_timer = 60
        elif effect_type == "potion":
            self.current_speed = self.base_speed * 3.0
            self.effect_timer = 50


class Item:
    def __init__(self, item_type, x, y):
        self.type = item_type
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(x, y)
        if self.type == "mud":
            self.t.shape('square')
            self.t.color('saddlebrown')
            self.t.shapesize(0.8, 0.8)
        else:
            self.t.shape('circle')
            self.t.color('gold')
            self.t.shapesize(0.6, 0.6)

    def hide(self):
        self.t.hideturtle()
        self.t.goto(1000, 1000)


def setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Ultimate Turtle Racing: Chaos Edition!")
    return screen


def draw_track(num_lanes):
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)

    drawer.penup()
    drawer.goto(-WIDTH//2 + 50, -HEIGHT//2)
    drawer.pendown()
    drawer.color("#333333")
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(WIDTH - 100)
        drawer.left(90)
        drawer.forward(HEIGHT)
        drawer.left(90)
    drawer.end_fill()

    drawer.color("white")
    drawer.pensize(2)
    spacing = (WIDTH - 100) / num_lanes

    for i in range(1, num_lanes):
        drawer.penup()
        x = -WIDTH//2 + 50 + (i * spacing)
        drawer.goto(x, -HEIGHT//2)
        drawer.setheading(90)

        for _ in range(HEIGHT // 20):
            drawer.pendown()
            drawer.forward(10)
            drawer.penup()
            drawer.forward(10)

    drawer.goto(-WIDTH//2 + 50, HEIGHT//2 - 60)
    drawer.setheading(0)
    drawer.pensize(8)
    drawer.color("white")
    drawer.pendown()
    drawer.forward(WIDTH - 100)

    return HEIGHT // 2 - 60


def draw_hud(hud_turtle, elapsed_time, total_score):
    hud_turtle.clear()
    hud_text = f"Score: {total_score} | Time: {elapsed_time:.2f}s"
    hud_turtle.write(hud_text, align="right", font=("Courier", 16, "bold"))


def countdown(screen):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 0)
    writer.color("white")

    for i in range(3, 0, -1):
        writer.write(str(i), align="center", font=("Courier", 60, "bold"))
        screen.update()
        time.sleep(1)
        writer.clear()

    writer.color("green")
    writer.write("GO!", align="center", font=("Courier", 60, "bold"))
    screen.update()
    time.sleep(1)
    writer.clear()


def celebrate(winner_color, winning_racer, screen):
    play_victory_sound()  # victory music!

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 50)
    writer.color(winner_color)

    writer.write(f"The {winner_color.upper()} turtle wins!",
                 align="center", font=("Courier", 30, "bold"))

    t = winning_racer.t
    t.penup()
    t.goto(0, -50)
    t.setheading(90)
    t.shapesize(3, 3)

    for _ in range(36):
        t.right(10)
        screen.update()
        time.sleep(0.02)

    time.sleep(2)
    writer.clear()


def display_leaderboard(racers, round_num, total_score, player_guess):
    board = turtle.Turtle()
    board.hideturtle()
    board.penup()

    racers.sort(key=lambda r: r.finish_time)

    start_y = 220

    board.goto(0, start_y)
    board.color("white")
    board.write(f"--- ROUND {round_num} RESULTS ---",
                align="center", font=("Courier", 24, "bold"))

    start_y -= 40
    board.goto(0, start_y)
    board.color("yellow")
    board.write(f"Your Pick: {player_guess.upper()}",
                align="center", font=("Courier", 18, "bold"))

    board.color("white")
    start_y -= 40
    for i, r in enumerate(racers):
        board.goto(0, start_y)
        board.write(f"{i+1}. {r.color.upper()} - {r.finish_time:.2f}s",
                    align="center", font=("Courier", 18, "bold"))
        start_y -= 30

    start_y -= 30
    board.goto(0, start_y)
    board.write(f"Total Score: {total_score}",
                align="center", font=("Courier", 22, "bold"))

    turtle.Screen().update()

# --- GAME LOGIC ---


def run_race(screen, racers, finish_y, current_score):
    hud_t = turtle.Turtle()
    hud_t.hideturtle()
    hud_t.penup()
    hud_t.color("white")
    hud_t.goto(WIDTH//2 - 20, HEIGHT//2 - 40)

    play_bg_music()  # Get the race music pumping right before the countdown.
    countdown(screen)

    items = []
    start_time = time.time()
    active_racers = len(racers)

    while active_racers > 0:
        current_time = time.time() - start_time
        draw_hud(hud_t, current_time, current_score)

        unfinished = [r for r in racers if not r.finished]
        unfinished.sort(key=lambda r: r.t.ycor(), reverse=True)

        if unfinished and len(items) < len(racers) * 1.5 and random.random() < 0.08:
            target = random.choice(unfinished)
            rank = unfinished.index(target)

            if len(unfinished) > 1:
                rank_factor = rank / (len(unfinished) - 1)
            else:
                rank_factor = 0.5

            mud_probability = 0.80 - (0.60 * rank_factor)

            if target.t.ycor() < finish_y - 60:
                new_item_y = target.t.ycor() + random.randint(50, 100)

                too_close = False
                for item in items:
                    if item.t.distance(target.x_pos, new_item_y) < 40:
                        too_close = True
                        break

                if not too_close:
                    if random.random() < mud_probability:
                        items.append(Item("mud", target.x_pos, new_item_y))
                    else:
                        items.append(Item("potion", target.x_pos, new_item_y))

        for r in unfinished:
            r.move()

            for item in items:
                if r.t.distance(item.t) < 18:
                    r.apply_effect(item.type)
                    item.hide()
                    items.remove(item)

            if r.t.ycor() >= finish_y:
                r.finished = True
                r.finish_time = current_time
                active_racers -= 1

        screen.update()
        time.sleep(0.015)

    return racers


def play_game():
    init_audio()  # First things first lets get the sound system ready.
    screen = setup_screen()

    screen.bgcolor("black")
    screen.update()

    num_str = screen.numinput(
        "Race Setup", "How many turtles? (2-10):", 5, 2, 10)
    num_turtles = int(num_str) if num_str else 5

    total_score = 0

    for round_num in range(1, TOTAL_ROUNDS + 1):
        screen.clearscreen()
        screen.tracer(0)
        screen.bgcolor("#2E8B57")

        random.shuffle(COLORS)
        race_colors = COLORS[:num_turtles]
        finish_y = draw_track(num_turtles)

        # A loop to make sure the player actually picks a valid turtle color.
        prompt = f"Round {round_num}/{TOTAL_ROUNDS} | Score: {total_score}\nRacers: {', '.join(race_colors)}\nWho will win?"
        guess = ""
        while guess not in race_colors:
            raw_guess = screen.textinput("Place Your Bet!", prompt)

            if raw_guess is None:  # This happens if the player hits 'Cancel' on the input box.
                prompt = f"You must pick a color!\nRacers: {', '.join(race_colors)}"
                continue

            guess = raw_guess.lower().strip()

            if guess not in race_colors:
                prompt = f"INVALID COLOR! Please choose from the roster:\n{', '.join(race_colors)}"

        racers = []
        spacing = (WIDTH - 100) / num_turtles
        for i, color in enumerate(race_colors):
            x = -WIDTH//2 + 50 + (spacing / 2) + (i * spacing)
            racers.append(Racer(color, x, -HEIGHT//2 + 30))

        screen.update()
        time.sleep(1)

        finished_racers = run_race(screen, racers, finish_y, total_score)

        finished_racers.sort(key=lambda r: r.finish_time)

        winning_racer = finished_racers[0]
        winner_color = winning_racer.color

        celebrate(winner_color, winning_racer, screen)

        if guess == winner_color:
            total_score += (10 * num_turtles)
        elif num_turtles > 2 and guess == finished_racers[1].color:
            total_score += (5 * num_turtles)

        screen.clearscreen()
        screen.tracer(0)
        screen.bgcolor("#111111")
        display_leaderboard(finished_racers, round_num, total_score, guess)

        # After the round, ask the player if they want to continue or quit.
        if round_num < TOTAL_ROUNDS:
            choice = screen.textinput(f"Round {round_num} Complete!",
                                      "Press Enter/OK to continue, or type 'exit' to quit.")
            if choice and choice.lower().strip() == 'exit':
                break

    # --- GAME OVER ---
    screen.clearscreen()
    screen.tracer(0)
    screen.bgcolor("black")
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.color("gold")
    writer.write(f"GAME OVER!\nFinal Score: {total_score}", align="center", font=(
        "Courier", 40, "bold"))
    screen.update()

    pygame.mixer.quit()  # Clean up and shut down the audio engine.
    # Give the player a moment to see their glorious final score.
    time.sleep(5)

    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    play_game()
