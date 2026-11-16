
"""
MOONGUARD — Standalone Python Cutscene (Pygame)
-----------------------------------------------
Plays the 20-second Earth-to-Moon vertical launch and Lunar Outpost
mission briefing cutscene directly in Python using Pygame, then segues
to your game loop once finished.

Installation:
  pip install pygame

Run:
  python cutscene.py
"""

import math
import random
import sys
import pygame

# Screen & Timing Constants
WIDTH, HEIGHT = 1024, 680
FPS = 60
TOTAL_DURATION = 20.0

# Palette matching the hand-drawn MOONGUARD aesthetic
SPACE_BG = (11, 14, 23)
LETTERBOX_BG = (6, 8, 14)
PAPER_BG = (252, 250, 242)
PAPER_LINE = (228, 224, 213)
INK_DARK = (37, 36, 44)
SHADOW_DARK = (21, 23, 34)
TAPE_COLOR = (251, 217, 152)
PURPLE_BANNER = (182, 177, 255)
LIME_BTN = (200, 235, 120)
YELLOW_GLOW = (255, 224, 102)
SKY_BLUE = (56, 189, 248)
OCEAN_BLUE = (37, 150, 243)
LAND_GREEN = (132, 204, 22)
MOON_LIGHT = (241, 245, 249)
MOON_MID = (203, 213, 225)
MOON_SHADOW = (148, 163, 184)
ALERT_RED = (252, 165, 165)
STAMP_GREEN_BG = (220, 252, 231)
STAMP_GREEN_INK = (21, 128, 61)

OBJECTIVES = [
    "01. LAUNCH FROM EARTH TO LUNAR ORBIT",
    "02. DEPLOY SHIELD OVER LUNAR OUTPOST",
    "03. PROTECT THE POST AT ALL COSTS",
]


def draw_rounded_rect_with_shadow(surface, rect, fill_color, border_color=INK_DARK, radius=10, shadow_offset=(6, 6), border_width=3):
    """Draws a comic/notebook card with an offset drop shadow and crisp ink outline."""
    shadow_rect = rect.move(shadow_offset[0], shadow_offset[1])
    pygame.draw.rect(surface, SHADOW_DARK, shadow_rect, border_radius=radius)
    pygame.draw.rect(surface, fill_color, rect, border_radius=radius)
    if border_width > 0:
        pygame.draw.rect(surface, border_color, rect, width=border_width, border_radius=radius)


def draw_notebook_card(surface, rect, with_tape=True):
    """Draws a lined notebook sheet with masking tape at the top center."""
    draw_rounded_rect_with_shadow(surface, rect, PAPER_BG, INK_DARK, radius=10, shadow_offset=(8, 10), border_width=3)

    # Horizontal notebook lines clipped inside the sheet
    clip_prev = surface.get_clip()
    surface.set_clip(rect.inflate(-6, -6))
    for y in range(rect.top + 24, rect.bottom - 8, 24):
        pygame.draw.line(surface, PAPER_LINE, (rect.left + 8, y), (rect.right - 8, y), 1)
    surface.set_clip(clip_prev)

    if with_tape:
        tape_rect = pygame.Rect(rect.centerx - 45, rect.top - 11, 90, 22)
        pygame.draw.rect(surface, TAPE_COLOR, tape_rect, border_radius=3)
        pygame.draw.rect(surface, (212, 174, 106), tape_rect, width=1, border_radius=3)


def draw_astronaut(surface, x, y, time_sec, scale=1.0):
    """Draws the cute waving doodle astronaut."""
    s = scale
    # Backpack
    bp = pygame.Rect(int(x - 20 * s), int(y - 10 * s), int(40 * s), int(30 * s))
    pygame.draw.rect(surface, MOON_MID, bp, border_radius=int(6 * s))
    pygame.draw.rect(surface, INK_DARK, bp, width=2, border_radius=int(6 * s))

    # Legs & Blue Boots
    for leg_dx in (-13, 3):
        leg = pygame.Rect(int(x + leg_dx * s), int(y + 16 * s), int(11 * s), int(18 * s))
        pygame.draw.rect(surface, (248, 250, 252), leg, border_radius=int(4 * s))
        pygame.draw.rect(surface, INK_DARK, leg, width=2, border_radius=int(4 * s))

        boot = pygame.Rect(int(x + (leg_dx - 1) * s), int(y + 30 * s), int(13 * s), int(7 * s))
        pygame.draw.rect(surface, (147, 197, 253), boot, border_radius=int(3 * s))
        pygame.draw.rect(surface, INK_DARK, boot, width=2, border_radius=int(3 * s))

    # Torso
    torso = pygame.Rect(int(x - 15 * s), int(y - 5 * s), int(30 * s), int(25 * s))
    pygame.draw.rect(surface, (255, 255, 255), torso, border_radius=int(8 * s))
    pygame.draw.rect(surface, INK_DARK, torso, width=2, border_radius=int(8 * s))

    # Chest Pack
    pack = pygame.Rect(int(x - 8 * s), int(y + 1 * s), int(16 * s), int(11 * s))
    pygame.draw.rect(surface, (219, 234, 254), pack, border_radius=int(3 * s))
    pygame.draw.circle(surface, SKY_BLUE, (int(x - 3 * s), int(y + 6 * s)), max(2, int(2.5 * s)))

    # Waving Right Arm
    wave_angle = -0.6 + math.sin(time_sec * 9.0) * 0.4
    arm_end_x = x + 16 * s + math.sin(wave_angle) * 16 * s
    arm_end_y = y - math.cos(wave_angle) * 16 * s
    pygame.draw.line(surface, INK_DARK, (int(x + 14 * s), int(y + 2 * s)), (int(arm_end_x), int(arm_end_y)), max(4, int(9 * s)))
    pygame.draw.line(surface, (255, 255, 255), (int(x + 14 * s), int(y + 2 * s)), (int(arm_end_x), int(arm_end_y)), max(2, int(5 * s)))

    # Helmet & Blue Visor
    pygame.draw.circle(surface, (255, 255, 255), (int(x), int(y - 18 * s)), int(16 * s))
    pygame.draw.circle(surface, INK_DARK, (int(x), int(y - 18 * s)), int(16 * s), width=2)
    visor = pygame.Rect(int(x - 11 * s), int(y - 25 * s), int(22 * s), int(14 * s))
    pygame.draw.rect(surface, (2, 132, 199), visor, border_radius=int(6 * s))


def draw_earth_launchpad(surface, offset_y, time_sec):
    """Draws the curved Earth surface, continents, clouds, launchpad gantry, and ground crew."""
    horizon_y = int(HEIGHT * 0.76 + offset_y)
    if horizon_y > HEIGHT + 140:
        return

    # Atmospheric halo
    atmo_rect = pygame.Rect(-60, horizon_y - 26, WIDTH + 120, 320)
    pygame.draw.ellipse(surface, (29, 78, 137), atmo_rect)

    # Ocean Dome
    earth_rect = pygame.Rect(-80, horizon_y - 12, WIDTH + 160, 420)
    pygame.draw.ellipse(surface, OCEAN_BLUE, earth_rect)
    pygame.draw.ellipse(surface, INK_DARK, earth_rect, width=3)

    # Green Continents
    pygame.draw.ellipse(surface, LAND_GREEN, (int(WIDTH * 0.14), horizon_y + 25, 220, 85))
    pygame.draw.ellipse(surface, LAND_GREEN, (int(WIDTH * 0.40), horizon_y + 6, 200, 65))
    pygame.draw.ellipse(surface, LAND_GREEN, (int(WIDTH * 0.68), horizon_y + 28, 240, 90))

    # Fluffy Clouds
    for cx, cy in [(WIDTH * 0.18 + math.sin(time_sec) * 8, horizon_y - 28), (WIDTH * 0.82 + math.cos(time_sec) * 8, horizon_y - 24)]:
        pygame.draw.circle(surface, (255, 255, 255), (int(cx - 14), int(cy)), 13)
        pygame.draw.circle(surface, (255, 255, 255), (int(cx), int(cy - 6)), 16)
        pygame.draw.circle(surface, (255, 255, 255), (int(cx + 15), int(cy)), 13)

    # Launchpad Deck & Gantry Tower
    pad_x = WIDTH // 2
    pad_y = horizon_y - 12
    gantry = pygame.Rect(pad_x - 56, pad_y - 68, 14, 70)
    pygame.draw.rect(surface, MOON_MID, gantry, border_radius=3)
    pygame.draw.rect(surface, INK_DARK, gantry, width=2, border_radius=3)
    pygame.draw.line(surface, INK_DARK, (pad_x - 42, pad_y - 52), (pad_x - 18, pad_y - 52), 3)

    deck = pygame.Rect(pad_x - 44, pad_y - 4, 88, 10)
    pygame.draw.rect(surface, (71, 85, 105), deck, border_radius=4)
    pygame.draw.rect(surface, INK_DARK, deck, width=2, border_radius=4)

    # Waving Ground Crew Astronauts
    draw_astronaut(surface, WIDTH * 0.30, horizon_y - 24 + math.sin(time_sec * 3.2) * 4, time_sec, 0.85)
    draw_astronaut(surface, WIDTH * 0.70, horizon_y - 22 + math.cos(time_sec * 3.0) * 4, time_sec + 1.0, 0.80)


def draw_lunar_outpost(surface, moon_y, time_sec, shield_locked):
    """Draws the cratered Moon and domed Lunar Outpost at the top-right destination."""
    if moon_y < -180:
        return

    mx = int(WIDTH * 0.75)
    my = int(moon_y)
    radius = 115

    # Cratered Moon Sphere
    pygame.draw.circle(surface, MOON_MID, (mx, my), radius)
    pygame.draw.circle(surface, INK_DARK, (mx, my), radius, width=3)

    # Craters
    pygame.draw.ellipse(surface, MOON_SHADOW, (mx - 65, my + 5, 36, 20))
    pygame.draw.ellipse(surface, MOON_LIGHT, (mx - 63, my + 4, 32, 16))
    pygame.draw.ellipse(surface, MOON_SHADOW, (mx + 25, my + 22, 42, 22))
    pygame.draw.ellipse(surface, MOON_LIGHT, (mx + 27, my + 20, 38, 18))

    # Domed Lunar Outpost on top of Moon
    post_y = my - radius + 6
    dome_rect = pygame.Rect(mx - 22, post_y - 26, 44, 44)
    pygame.draw.arc(surface, (186, 230, 253), dome_rect, 0, math.pi, 22)
    pygame.draw.arc(surface, INK_DARK, dome_rect, 0, math.pi, 3)

    base_rect = pygame.Rect(mx - 34, post_y - 6, 68, 11)
    pygame.draw.rect(surface, (71, 85, 105), base_rect, border_radius=4)
    pygame.draw.rect(surface, INK_DARK, base_rect, width=2, border_radius=4)

    # Beacon Antenna
    pygame.draw.line(surface, INK_DARK, (mx, post_y - 26), (mx, post_y - 42), 3)
    beacon_color = (74, 222, 128) if shield_locked else (248, 113, 113)
    pygame.draw.circle(surface, beacon_color, (mx, post_y - 44), 5)

    # Waving Outpost Astronaut
    draw_astronaut(surface, mx + 46, post_y - 12 + math.sin(time_sec * 3.5) * 3, time_sec, 0.58)

    # Protective Cyan Dome Shield
    if shield_locked:
        pulse = int(math.sin(time_sec * 5.0) * 3)
        shield_rect = pygame.Rect(mx - 62 - pulse, post_y - 64 - pulse, 124 + pulse * 2, 124 + pulse * 2)
        pygame.draw.arc(surface, SKY_BLUE, shield_rect, 0, math.pi, 4)


def draw_vertical_rocket(surface, x, y, thruster_power, shield_active, time_sec):
    """Draws the white-and-blue doodle rocket pointing straight upward."""
    rx, ry = int(x), int(y)

    # Orbital Shield Bubble
    if shield_active:
        pulse = int(math.sin(time_sec * 6.0) * 3)
        pygame.draw.circle(surface, SKY_BLUE, (rx, ry - 4), 66 + pulse, width=3)

    # Thruster Flame
    if thruster_power > 0:
        flicker = math.sin(time_sec * 35.0) * 6
        flame_h = int(24 + thruster_power * 30 + flicker)
        outer_color = SKY_BLUE if thruster_power > 1.1 else (251, 191, 36)
        pygame.draw.polygon(surface, outer_color, [(rx - 12, ry + 34), (rx, ry + 34 + flame_h), (rx + 12, ry + 34)])
        pygame.draw.polygon(surface, (254, 249, 195), [(rx - 6, ry + 34), (rx, ry + 34 + int(flame_h * 0.6)), (rx + 6, ry + 34)])

    # Swept Blue Fins
    pygame.draw.polygon(surface, (147, 197, 253), [(rx - 16, ry + 10), (rx - 34, ry + 38), (rx - 14, ry + 28)])
    pygame.draw.polygon(surface, INK_DARK, [(rx - 16, ry + 10), (rx - 34, ry + 38), (rx - 14, ry + 28)], width=2)
    pygame.draw.polygon(surface, (147, 197, 253), [(rx + 16, ry + 10), (rx + 34, ry + 38), (rx + 14, ry + 28)])
    pygame.draw.polygon(surface, INK_DARK, [(rx + 16, ry + 10), (rx + 34, ry + 38), (rx + 14, ry + 28)], width=2)

    # Rocket Nozzle
    nozzle = pygame.Rect(rx - 12, ry + 30, 24, 7)
    pygame.draw.rect(surface, (100, 116, 139), nozzle, border_radius=3)
    pygame.draw.rect(surface, INK_DARK, nozzle, width=2, border_radius=3)

    # Sleek White Rocket Hull
    hull_points = [
        (rx, ry - 48),
        (rx + 17, ry - 24),
        (rx + 21, ry + 4),
        (rx + 15, ry + 31),
        (rx - 15, ry + 31),
        (rx - 21, ry + 4),
        (rx - 17, ry - 24),
    ]
    pygame.draw.polygon(surface, (255, 255, 255), hull_points)
    pygame.draw.polygon(surface, INK_DARK, hull_points, width=3)

    # Circular Blue Porthole
    pygame.draw.circle(surface, (186, 230, 253), (rx, ry - 8), 13)
    pygame.draw.circle(surface, INK_DARK, (rx, ry - 8), 13, width=2)
    pygame.draw.circle(surface, (2, 132, 199), (rx, ry - 8), 9)
    pygame.draw.circle(surface, (255, 255, 255), (rx - 3, ry - 11), 3)


def run_cutscene():
    """Plays the 20-second MOONGUARD cutscene and returns True when ready to launch the game."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MOONGUARD — Animated Mission Cutscene")
    clock = pygame.time.Clock()

    # Fonts
    font_title = pygame.font.SysFont("arialrounded", 30, bold=True)
    font_sub = pygame.font.SysFont("arialrounded", 15, bold=True)
    font_body = pygame.font.SysFont("comicsansms", 17, bold=True)
    font_hud = pygame.font.SysFont("consolas", 15, bold=True)

    # Generate background stars
    stars = [
        {
            "x": random.randint(0, WIDTH),
            "y": random.randint(0, HEIGHT),
            "r": random.choice([1, 2, 2, 3]),
            "parallax": random.uniform(0.2, 0.65),
            "phase": random.uniform(0, math.tau),
        }
        for _ in range(110)
    ]

    smoke_puffs = []
    shooting_stars = []

    elapsed = 0.0
    star_scroll = 0.0
    smoke_timer = 0.0
    shoot_timer = 1.5
    is_paused = False

    def reset_state():
        nonlocal elapsed, star_scroll, smoke_puffs, shooting_stars, is_paused
        elapsed = 0.0
        star_scroll = 0.0
        smoke_puffs = []
        shooting_stars = []
        is_paused = False

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        time_sec = pygame.time.get_ticks() / 1000.0

        # Event handling (SPACE = Pause/Play, R = Replay, S = Skip, ENTER = Start Game at end)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused
                elif event.key == pygame.K_r:
                    reset_state()
                elif event.key == pygame.K_s:
                    elapsed = TOTAL_DURATION
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and elapsed >= TOTAL_DURATION:
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if elapsed >= TOTAL_DURATION:
                    return True

        if not is_paused and elapsed < TOTAL_DURATION:
            elapsed = min(TOTAL_DURATION, elapsed + dt)

        # Scene Choreography Variables
        shake_x, shake_y = 0, 0
        earth_offset_y = 0.0
        moon_y = -250.0
        thruster_power = 0.0
        rocket_shield = False
        post_shield = False
        distance_km = 0

        # Rocket position interpolation
        rocket_x = WIDTH * 0.5
        earth_pad_y = HEIGHT * 0.76

        if elapsed < 4.0:
            # SCENE 1: Earth Launchpad & Countdown
            scene_label = "SCENE 01 // EARTH PAD"
            rocket_y = earth_pad_y - 54
            if elapsed >= 3.1:
                thruster_power = 0.85
                shake_x = random.randint(-3, 3)
                shake_y = random.randint(-3, 3)
            if elapsed > 2.4 and not is_paused:
                smoke_timer += dt
                if smoke_timer > 0.06:
                    smoke_timer = 0.0
                    smoke_puffs.append([rocket_x + random.uniform(-24, 24), earth_pad_y - 12, random.uniform(-20, 20), -18, 12, 180])

        elif elapsed < 9.5:
            # SCENE 2: Vertical Liftoff from Earth
            scene_label = "SCENE 02 // EARTH LIFTOFF"
            t2 = (elapsed - 4.0) / 5.5
            ease_out = 1.0 - (1.0 - t2) ** 2.1
            rocket_y = (earth_pad_y - 54) - ease_out * (HEIGHT * 0.26)
            earth_offset_y = (t2 ** 1.35) * (HEIGHT * 0.88)
            thruster_power = 1.35
            distance_km = int((t2 ** 1.4) * 140000)

            if t2 < 0.25:
                shake_x = random.randint(-4, 4)
                shake_y = random.randint(-4, 4)

            if not is_paused:
                star_scroll += (220 + t2 * 340) * dt
                smoke_timer += dt
                if smoke_timer > 0.045:
                    smoke_timer = 0.0
                    smoke_puffs.append([rocket_x + random.uniform(-8, 8), rocket_y + 38, random.uniform(-15, 15), 110, 14, 175])

        elif elapsed < 16.5:
            # SCENE 3: Deep Space Cruise & Mission Briefing
            scene_label = "SCENE 03 // MISSION BRIEFING"
            t3 = elapsed - 9.5
            shift = min(1.0, t3 / 1.3)
            ease = 1.0 - (1.0 - shift) ** 3
            rocket_x = WIDTH * 0.5 + (WIDTH * 0.75 - WIDTH * 0.5) * ease
            rocket_y = HEIGHT * 0.52 + math.sin(t3 * 2.5) * 7
            earth_offset_y = HEIGHT + 250
            thruster_power = 1.05
            distance_km = int(140000 + (t3 / 7.0) * 200000)

            if not is_paused:
                star_scroll += 300 * dt
                smoke_timer += dt
                if smoke_timer > 0.055:
                    smoke_timer = 0.0
                    smoke_puffs.append([rocket_x + random.uniform(-7, 7), rocket_y + 38, random.uniform(-12, 12), 90, 12, 165])

        else:
            # SCENE 4: Lunar Outpost Arrival & Mission Active
            scene_label = "SCENE 04 // LUNAR OUTPOST"
            t4 = min(3.5, elapsed - 16.5)
            arrive = min(1.0, t4 / 1.3)
            ease = 1.0 - (1.0 - arrive) ** 3
            moon_y = -200 + ease * (HEIGHT * 0.24 + 200)
            rocket_x = WIDTH * 0.75
            rocket_y = HEIGHT * 0.52 + (HEIGHT * 0.46 - HEIGHT * 0.52) * ease + math.sin(time_sec * 2.6) * 5
            earth_offset_y = HEIGHT + 250
            thruster_power = 0.75
            rocket_shield = True
            post_shield = t4 >= 0.9
            distance_km = min(384400, int(340000 + (t4 / 1.3) * 44400))

            if not is_paused:
                star_scroll += 140 * dt
                smoke_timer += dt
                if smoke_timer > 0.07:
                    smoke_timer = 0.0
                    smoke_puffs.append([rocket_x + random.uniform(-6, 6), rocket_y + 38, random.uniform(-10, 10), 60, 10, 150])

        # Update particles
        if not is_paused:
            shoot_timer -= dt
            if shoot_timer <= 0:
                shoot_timer = random.uniform(3.0, 5.0)
                shooting_stars.append([random.randint(40, WIDTH // 2), random.randint(60, HEIGHT // 3), 320.0, -85.0, 1.0])

            for st in shooting_stars[:]:
                st[0] += st[2] * dt
                st[1] += st[3] * dt
                st[4] -= 0.75 * dt
                if st[4] <= 0:
                    shooting_stars.remove(st)

            for p in smoke_puffs[:]:
                p[0] += p[2] * dt
                p[1] += p[3] * dt
                p[4] += 18 * dt
                p[5] -= 110 * dt
                if p[5] <= 0:
                    smoke_puffs.remove(p)

        # --- RENDER FRAME ---
        canvas = pygame.Surface((WIDTH, HEIGHT))
        canvas.fill(SPACE_BG)

        # Twinkling Parallax Stars
        for s in stars:
            wy = int((s["y"] + star_scroll * s["parallax"]) % HEIGHT)
            brightness = int(170 + 85 * math.sin(time_sec * 2.5 + s["phase"]))
            pygame.draw.circle(canvas, (brightness, brightness, min(255, brightness + 15)), (s["x"], wy), s["r"])

        # Shooting Stars
        for st in shooting_stars:
            tail = (int(st[0] - st[2] * 0.25), int(st[1] - st[3] * 0.25))
            pygame.draw.line(canvas, (96, 165, 250), (int(st[0]), int(st[1])), tail, 3)
            pygame.draw.circle(canvas, (219, 234, 254), (int(st[0]), int(st[1])), 4)

        # World Layers
        draw_earth_launchpad(canvas, earth_offset_y, time_sec)
        draw_lunar_outpost(canvas, moon_y, time_sec, post_shield)

        # Smoke Puffs
        for p in smoke_puffs:
            alpha = max(0, min(255, int(p[5])))
            puff_surf = pygame.Surface((int(p[4] * 2), int(p[4] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(puff_surf, (241, 245, 249, alpha), (int(p[4]), int(p[4])), int(p[4]))
            canvas.blit(puff_surf, (int(p[0] - p[4]), int(p[1] - p[4])))

        # Vertical Rocket
        draw_vertical_rocket(canvas, rocket_x, rocket_y, thruster_power, rocket_shield, time_sec)

        # --- NOTEBOOK UI OVERLAYS ---
        # Scene 1 Urgent Transmission Card
        if elapsed < 4.0:
            card = pygame.Rect(WIDTH // 2 - 210, 72, 420, 148)
            draw_notebook_card(canvas, card, with_tape=True)

            badge = pygame.Rect(card.centerx - 105, card.top + 18, 210, 26)
            pygame.draw.rect(canvas, ALERT_RED, badge, border_radius=5)
            pygame.draw.rect(canvas, INK_DARK, badge, width=2, border_radius=5)
            badge_txt = font_sub.render("URGENT TRANSMISSION", True, INK_DARK)
            canvas.blit(badge_txt, badge_txt.get_rect(center=badge.center))

            msg_txt = font_body.render("LUNAR OUTPOST NEEDS REINFORCEMENT!", True, INK_DARK)
            canvas.blit(msg_txt, msg_txt.get_rect(center=(card.centerx, card.top + 68)))

            if elapsed < 1.1:
                cd_str, cd_col = "T-MINUS 3...", INK_DARK
            elif elapsed < 2.1:
                cd_str, cd_col = "T-MINUS 2...", INK_DARK
            elif elapsed < 3.1:
                cd_str, cd_col = "T-MINUS 1...", INK_DARK
            else:
                cd_str, cd_col = "IGNITION!", (220, 38, 38)

            cd_box = pygame.Rect(card.centerx - 115, card.top + 92, 230, 42)
            draw_rounded_rect_with_shadow(canvas, cd_box, PURPLE_BANNER, INK_DARK, radius=6, shadow_offset=(3, 3), border_width=2)
            cd_txt = font_title.render(cd_str, True, cd_col)
            canvas.blit(cd_txt, cd_txt.get_rect(center=cd_box.center))

        # Scene 3 & 4 Mission Briefing Dossier
        if elapsed >= 9.5:
            slide_t = min(1.0, (elapsed - 9.5) / 0.7)
            card_x = int(-440 + (1.0 - (1.0 - slide_t) ** 3) * 485)
            card = pygame.Rect(card_x, HEIGHT // 2 - 190, 430, 380)
            draw_notebook_card(canvas, card, with_tape=True)

            # Header Title & Purple Tag
            title_surf = font_title.render("MOONGUARD", True, INK_DARK)
            canvas.blit(title_surf, (card.left + 24, card.top + 22))

            tag_rect = pygame.Rect(card.left + 24, card.top + 60, 175, 24)
            draw_rounded_rect_with_shadow(canvas, tag_rect, PURPLE_BANNER, INK_DARK, radius=4, shadow_offset=(2, 2), border_width=2)
            tag_txt = font_sub.render("PROTECT YOUR POST", True, INK_DARK)
            canvas.blit(tag_txt, tag_txt.get_rect(center=tag_rect.center))

            brief_hdr = font_sub.render("MISSION BRIEFING  //  EARTH -> LUNAR POST", True, (79, 70, 229))
            canvas.blit(brief_hdr, (card.left + 24, card.top + 102))

            # Typewriter Objectives
            t3 = elapsed - 9.5
            starts = [0.4, 2.4, 4.4]
            for idx, obj_str in enumerate(OBJECTIVES):
                row_y = card.top + 132 + idx * 54
                row_rect = pygame.Rect(card.left + 22, row_y, card.width - 44, 44)
                prog = max(0.0, min(1.0, (t3 - starts[idx]) / 1.6))

                if prog > 0:
                    pygame.draw.rect(canvas, (255, 255, 255), row_rect, border_radius=6)
                    pygame.draw.rect(canvas, INK_DARK, row_rect, width=2, border_radius=6)

                    chk_rect = pygame.Rect(row_rect.left + 10, row_rect.centery - 11, 22, 22)
                    pygame.draw.rect(canvas, (255, 255, 255), chk_rect, border_radius=4)
                    pygame.draw.rect(canvas, INK_DARK, chk_rect, width=2, border_radius=4)
                    if prog >= 1.0:
                        chk_txt = font_sub.render("OK", True, STAMP_GREEN_INK)
                        canvas.blit(chk_txt, chk_txt.get_rect(center=chk_rect.center))

                    shown_chars = int(len(obj_str) * prog)
                    typed = obj_str[:shown_chars] + ("_" if prog < 1.0 else "")
                    obj_txt = font_body.render(typed, True, INK_DARK)
                    canvas.blit(obj_txt, (chk_rect.right + 10, row_rect.centery - 11))

            # Scene 4 Stamp & Start Button
            if elapsed >= 17.7:
                stamp_rect = pygame.Rect(card.centerx - 105, card.top + 296, 210, 30)
                draw_rounded_rect_with_shadow(canvas, stamp_rect, STAMP_GREEN_BG, STAMP_GREEN_INK, radius=5, shadow_offset=(3, 3), border_width=2)
                stamp_txt = font_sub.render("MISSION ACTIVE", True, STAMP_GREEN_INK)
                canvas.blit(stamp_txt, stamp_txt.get_rect(center=stamp_rect.center))

                btn_rect = pygame.Rect(card.left + 24, card.top + 334, card.width - 48, 36)
                draw_rounded_rect_with_shadow(canvas, btn_rect, LIME_BTN, INK_DARK, radius=6, shadow_offset=(3, 3), border_width=2)
                btn_txt = font_sub.render("PRESS ENTER OR CLICK TO START GAME", True, INK_DARK)
                canvas.blit(btn_txt, btn_txt.get_rect(center=btn_rect.center))

        # Blit scene with camera shake
        screen.fill(SPACE_BG)
        screen.blit(canvas, (shake_x, shake_y))

        # Cinematic Letterbox Bars & Top/Bottom Telemetry HUD
        pygame.draw.rect(screen, LETTERBOX_BG, (0, 0, WIDTH, 34))
        pygame.draw.rect(screen, LETTERBOX_BG, (0, HEIGHT - 34, WIDTH, 34))

        hud_top = font_hud.render(f"{scene_label}   |   DIST: {distance_km:,} km", True, (253, 224, 71))
        screen.blit(hud_top, (18, 9))

        controls_hint = font_hud.render("[SPACE] Pause  [R] Replay  [S] Skip", True, (203, 213, 225))
        screen.blit(controls_hint, (WIDTH - controls_hint.get_width() - 18, 9))

        # Bottom Progress Bar
        bar_rect = pygame.Rect(140, HEIGHT - 22, WIDTH - 280, 10)
        pygame.draw.rect(screen, (40, 48, 70), bar_rect, border_radius=5)
        fill_w = int(bar_rect.width * (elapsed / TOTAL_DURATION))
        if fill_w > 0:
            pygame.draw.rect(screen, LIME_BTN, (bar_rect.left, bar_rect.top, fill_w, bar_rect.height), border_radius=5)

        time_txt = font_hud.render(f"00:{int(elapsed):02d} / 00:20", True, (255, 255, 255))
        screen.blit(time_txt, (24, HEIGHT - 25))

        pygame.display.flip()

        # Automatically segue into your game 1.5 seconds after cutscene finishes
        if elapsed >= TOTAL_DURATION and not is_paused:
            pygame.time.wait(1500)
            return True

    return False


def start_game():
    """Hook your actual Pygame game loop here once the cutscene finishes."""
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont("arialrounded", 32, bold=True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(SPACE_BG)
        msg = font.render("LUNAR OUTPOST REACHED — YOUR GAME STARTS HERE!", True, LIME_BTN)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()


if __name__ == "__main__":
    if run_cutscene():
        start_game()
