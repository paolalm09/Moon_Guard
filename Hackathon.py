
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MOONGUARD — Protect Your Post</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Patrick+Hand&display=swap"
    rel="stylesheet"
  />
  <style>
    :root {
      --space-bg: #0b0e17;
      --paper-bg: #fcfaf2;
      --paper-line: #e4e0d5;
      --ink-dark: #25242c;
      --purple-banner: #b6b1ff;
      --lime-btn: #c8eb78;
      --lime-btn-hover: #d7f590;
    }

    * {
      box-sizing: border-box;
      user-select: none;
    }

    html,
    body {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: var(--space-bg);
      font-family: 'Patrick Hand', cursive, sans-serif;
    }

    .screen-view {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
    }

    .hidden-view {
      display: none !important;
    }

    #cutsceneCanvas {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
      z-index: 1;
    }

    .letterbox-bar {
      position: fixed;
      left: 0;
      width: 100%;
      height: 28px;
      background: #06080e;
      z-index: 20;
      pointer-events: none;
    }

    @media (min-width: 640px) {
      .letterbox-bar {
        height: 36px;
      }
    }

    .letterbox-top {
      top: 0;
      border-bottom: 1.5px solid rgba(255, 255, 255, 0.08);
    }

    .letterbox-bottom {
      bottom: 0;
      border-top: 1.5px solid rgba(255, 255, 255, 0.08);
    }

    .notebook-sheet {
      background-color: var(--paper-bg);
      background-image: repeating-linear-gradient(
        to bottom,
        transparent 0px,
        transparent 25px,
        var(--paper-line) 26px
      );
      border: 3px solid var(--ink-dark);
      border-radius: 7px 9px 7px 9px;
      box-shadow: 9px 11px 0px #151722;
      position: relative;
    }

    .tape-strip {
      position: absolute;
      top: -14px;
      left: 50%;
      transform: translateX(-50%) rotate(-1.5deg);
      width: 96px;
      height: 25px;
      background: rgba(251, 217, 152, 0.9);
      border: 1.5px solid rgba(212, 174, 106, 0.55);
      border-radius: 3px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.14);
      z-index: 15;
    }

    .comic-title {
      font-family: 'Fredoka', sans-serif;
      font-weight: 700;
      color: var(--ink-dark);
      text-shadow: 0 0 10px rgba(255, 224, 102, 0.8), 2px 2px 0px #ffe066;
    }

    .purple-tag {
      background-color: var(--purple-banner);
      border: 2.5px solid var(--ink-dark);
      box-shadow: 3px 3px 0px var(--ink-dark);
      border-radius: 4px;
      font-family: 'Fredoka', sans-serif;
      font-weight: 600;
      letter-spacing: 0.07em;
    }

    .doodle-btn {
      background-color: var(--lime-btn);
      border: 2.5px solid var(--ink-dark);
      box-shadow: 4px 4px 0px var(--ink-dark);
      border-radius: 6px;
      font-family: 'Fredoka', sans-serif;
      font-weight: 700;
      color: var(--ink-dark);
      transition: transform 0.12s ease, box-shadow 0.12s ease, background-color 0.15s ease;
      cursor: pointer;
    }

    .doodle-btn:hover {
      background-color: var(--lime-btn-hover);
      transform: translate(-1px, -1px);
      box-shadow: 5px 5px 0px var(--ink-dark);
    }

    .doodle-btn:active {
      transform: translate(3px, 3px);
      box-shadow: 1px 1px 0px var(--ink-dark);
    }

    .hud-pill {
      background: rgba(15, 19, 32, 0.84);
      border: 2px solid rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(6px);
      font-family: 'Fredoka', sans-serif;
    }

    @keyframes stampSlam {
      0% {
        opacity: 0;
        transform: scale(2.4) rotate(-14deg);
      }
      65% {
        opacity: 1;
        transform: scale(0.92) rotate(-5deg);
      }
      100% {
        opacity: 1;
        transform: scale(1) rotate(-6deg);
      }
    }

    .stamp-active {
      animation: stampSlam 0.42s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }
  </style>
</head>
<body>
  <!-- ========================================================= -->
  <!-- VIEW 1: HOMEPAGE                                          -->
  <!-- ========================================================= -->
  <div id="homeView" class="screen-view flex items-center justify-center p-4">
    <div class="fixed inset-0 pointer-events-none opacity-80">
      <div class="w-1.5 h-1.5 bg-white rounded-full absolute top-[15%] left-[20%]"></div>
      <div class="w-2 h-2 bg-yellow-200 rounded-full absolute top-[25%] right-[22%]"></div>
      <div class="w-1 h-1 bg-white rounded-full absolute bottom-[30%] left-[14%]"></div>
      <div class="w-1.5 h-1.5 bg-sky-200 rounded-full absolute top-[40%] left-[78%]"></div>
      <div class="w-1 h-1 bg-white rounded-full absolute bottom-[22%] right-[18%]"></div>
    </div>

    <main class="notebook-sheet w-full max-w-[360px] px-7 pt-9 pb-8 text-center z-10">
      <div class="tape-strip"></div>

      <svg class="w-24 h-24 mx-auto mb-2" viewBox="0 0 140 140" fill="none">
        <path
          d="M72 26 C46 29, 30 53, 34 80 C38 106, 63 123, 90 118 C102 116, 112 109, 118 100 C100 104, 82 94, 76 76 C70 58, 78 39, 93 31 C87 27, 79 25, 72 26 Z"
          fill="#ffdf5d"
          stroke="#25242c"
          stroke-width="5"
          stroke-linejoin="round"
        />
        <path
          d="M44 43 C44 24, 67 16, 87 24 C101 29, 108 38, 112 45 C102 42, 92 40, 81 36 C67 32, 54 36, 44 43 Z"
          fill="#b8b3ff"
          stroke="#25242c"
          stroke-width="4.5"
          stroke-linejoin="round"
        />
        <circle cx="113" cy="47" r="8" fill="#ffdf5d" stroke="#25242c" stroke-width="4" />
        <path d="M56 66 Q63 72 70 66" stroke="#25242c" stroke-width="4.5" stroke-linecap="round" />
        <ellipse cx="56" cy="76" rx="6" ry="3.5" fill="#fda4af" />
      </svg>

      <h1 class="comic-title text-4xl tracking-wide mb-2">MOONGUARD</h1>

      <div class="purple-tag inline-block px-3.5 py-1 text-xs text-[#25242c] mb-7">
        PROTECT YOUR POST
      </div>

      <button
        id="homePlayBtn"
        type="button"
        class="doodle-btn block w-full py-3.5 px-6 text-2xl tracking-wide"
      >
        ▶ PLAY
      </button>
    </main>

    <div
      class="fixed -bottom-24 left-[-10%] right-[-10%] h-44 bg-[#cbd5e1] border-t-4 border-[#25242c] rounded-t-[100%] pointer-events-none"
    ></div>
  </div>

  <!-- ========================================================= -->
  <!-- VIEW 2: 20-SECOND INTRO CUTSCENE                          -->
  <!-- ========================================================= -->
  <div id="cutsceneView" class="screen-view hidden-view">
    <div class="letterbox-bar letterbox-top"></div>
    <div class="letterbox-bar letterbox-bottom"></div>

    <canvas id="cutsceneCanvas"></canvas>

    <header
      class="fixed top-9 sm:top-11 left-0 right-0 z-30 px-3 sm:px-6 flex items-center justify-between gap-2 pointer-events-none"
    >
      <div class="hud-pill rounded-full px-3.5 py-1.5 flex items-center gap-2.5 sm:gap-3 text-white pointer-events-auto shadow-lg">
        <span class="flex items-center gap-1.5 text-xs sm:text-sm font-semibold tracking-wide text-[#fde047]">
          <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
          <span id="sceneLabel">SCENE 01 // EARTH PAD</span>
        </span>
        <span class="text-white/30">|</span>
        <span class="text-xs sm:text-sm font-bold text-[#7dd3fc]">
          DIST: <span id="altReadout">0</span> km
        </span>
      </div>

      <div class="flex items-center gap-1.5 sm:gap-2 pointer-events-auto">
        <button
          id="muteBtn"
          type="button"
          class="hud-pill hover:bg-white/15 text-white rounded-full px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-semibold flex items-center gap-1.5 transition cursor-pointer"
        >
          <span id="muteIcon">🔇</span>
          <span id="muteText" class="hidden md:inline">SOUND OFF</span>
        </button>

        <button
          id="playPauseBtn"
          type="button"
          class="hud-pill hover:bg-white/15 text-[#fde047] rounded-full px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-semibold flex items-center gap-1 transition cursor-pointer"
        >
          <span id="playPauseIcon">⏸</span>
          <span id="playPauseText" class="hidden sm:inline">PAUSE</span>
        </button>

        <button
          id="replayBtn"
          type="button"
          class="hud-pill hover:bg-white/15 text-white rounded-full px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-semibold flex items-center gap-1 transition cursor-pointer"
        >
          <span>↺</span>
          <span class="hidden sm:inline">REPLAY</span>
        </button>

        <button
          id="skipBtn"
          type="button"
          class="hud-pill hover:bg-white/15 text-[#c8eb78] rounded-full px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-semibold flex items-center gap-1 transition cursor-pointer"
        >
          <span>SKIP</span>
          <span>⏭</span>
        </button>
      </div>
    </header>

    <!-- SCENE 1 OVERLAY -->
    <section
      id="scene1Overlay"
      class="fixed inset-x-0 top-20 sm:top-24 z-20 flex justify-center px-4 pointer-events-none transition-all duration-500"
      style="opacity: 0; transform: translateY(-28px);"
    >
      <div class="notebook-sheet w-full max-w-[375px] sm:max-w-[420px] px-5 pt-5 pb-4 text-center">
        <div class="tape-strip"></div>

        <div class="flex items-center justify-center gap-2 mb-1.5">
          <svg class="w-8 h-8" viewBox="0 0 64 64" fill="none">
            <path
              d="M34 10 C20 12, 12 24, 14 38 C16 51, 29 59, 43 56 C49 55, 54 51, 57 47 C48 49, 39 44, 36 35 C33 26, 37 16, 45 12 C42 10, 38 9, 34 10 Z"
              fill="#ffdf5d"
              stroke="#25242c"
              stroke-width="3.2"
            />
            <path d="M25 31 Q29 34 32 31" stroke="#25242c" stroke-width="2.6" stroke-linecap="round" />
          </svg>
          <span
            class="text-xs sm:text-sm font-bold uppercase tracking-widest px-2.5 py-0.5 rounded bg-[#fca5a5] border-2 border-[#25242c] text-[#25242c]"
            style="font-family: 'Fredoka', sans-serif;"
          >
            📡 URGENT TRANSMISSION
          </span>
        </div>

        <p class="text-base sm:text-lg text-[#25242c] font-bold leading-tight mb-2.5">
          LUNAR OUTPOST NEEDS REINFORCEMENT — Preparing Earth launch!
        </p>

        <div
          class="inline-block px-5 py-1.5 rounded-md bg-[#b6b1ff] border-2 border-[#25242c] shadow-[3px_3px_0px_#25242c]"
        >
          <span
            id="countdownText"
            class="comic-title text-2xl sm:text-3xl tracking-wider inline-block"
          >
            T-MINUS 3...
          </span>
        </div>
      </div>
    </section>

    <!-- SCENE 3 & 4 MISSION BRIEFING OVERLAY -->
    <section
      id="briefingOverlay"
      class="fixed inset-y-0 left-0 right-0 sm:right-auto sm:left-6 md:left-12 lg:left-20 z-20 flex items-center justify-center sm:justify-start px-4 pointer-events-none transition-all duration-700"
      style="opacity: 0; transform: translateX(-45px) rotate(-1deg);"
    >
      <div
        class="notebook-sheet w-full max-w-[385px] sm:max-w-[430px] px-5 pt-6 pb-5 sm:px-6 sm:pt-7 sm:pb-6 pointer-events-auto"
      >
        <div class="tape-strip"></div>

        <div class="flex items-center justify-between border-b-2 border-dashed border-[#25242c]/30 pb-2.5 mb-3">
          <div class="flex items-center gap-2.5">
            <svg class="w-12 h-12 shrink-0" viewBox="0 0 140 140" fill="none">
              <path
                d="M72 26 C46 29, 30 53, 34 80 C38 106, 63 123, 90 118 C102 116, 112 109, 118 100 C100 104, 82 94, 76 76 C70 58, 78 39, 93 31 C87 27, 79 25, 72 26 Z"
                fill="#ffdf5d"
                stroke="#25242c"
                stroke-width="5"
                stroke-linejoin="round"
              />
              <path
                d="M44 43 C44 24, 67 16, 87 24 C101 29, 108 38, 112 45 C102 42, 92 40, 81 36 C67 32, 54 36, 44 43 Z"
                fill="#b8b3ff"
                stroke="#25242c"
                stroke-width="4.5"
                stroke-linejoin="round"
              />
              <circle cx="113" cy="47" r="8" fill="#ffdf5d" stroke="#25242c" stroke-width="4" />
              <path d="M56 66 Q63 72 70 66" stroke="#25242c" stroke-width="4.5" stroke-linecap="round" />
              <ellipse cx="56" cy="76" rx="6" ry="3.5" fill="#fda4af" />
            </svg>

            <div>
              <h1 class="comic-title text-2xl sm:text-[28px] leading-none tracking-wide">
                MOONGUARD
              </h1>
              <div class="purple-tag inline-block px-2.5 py-0.5 text-[11px] sm:text-xs text-[#25242c] mt-1">
                PROTECT YOUR POST
              </div>
            </div>
          </div>

          <svg class="w-8 h-8 shrink-0" viewBox="0 0 44 44" fill="none">
            <path
              d="M22 4 L27 16 L40 17 L30 25 L33 38 L22 31 L11 38 L14 25 L4 17 L17 16 Z"
              fill="#fde047"
              stroke="#25242c"
              stroke-width="3"
              stroke-linejoin="round"
            />
          </svg>
        </div>

        <div class="flex items-center justify-between mb-2.5">
          <span
            class="text-xs sm:text-sm font-bold uppercase tracking-wider text-[#25242c] bg-[#fde047]/80 px-2 py-0.5 rounded border border-[#25242c]"
            style="font-family: 'Fredoka', sans-serif;"
          >
            📋 MISSION BRIEFING
          </span>
          <span class="text-xs font-bold text-[#4f46e5]" style="font-family: 'Fredoka', sans-serif;">
            EARTH ➔ LUNAR POST
          </span>
        </div>

        <ul class="space-y-2 text-left mb-3.5">
          <li
            id="objRow1"
            class="flex items-start gap-2.5 bg-white/80 p-2 rounded border-2 border-[#25242c]/20 transition-all duration-300 opacity-35"
          >
            <div
              id="check1"
              class="w-6 h-6 mt-0.5 rounded border-2 border-[#25242c] bg-white flex items-center justify-center shrink-0 font-bold text-sm text-[#16a34a]"
            ></div>
            <div class="flex-1 min-h-[34px]">
              <p id="objText1" class="text-[15px] sm:text-[16px] leading-snug text-[#25242c] font-bold"></p>
            </div>
          </li>

          <li
            id="objRow2"
            class="flex items-start gap-2.5 bg-white/80 p-2 rounded border-2 border-[#25242c]/20 transition-all duration-300 opacity-35"
          >
            <div
              id="check2"
              class="w-6 h-6 mt-0.5 rounded border-2 border-[#25242c] bg-white flex items-center justify-center shrink-0 font-bold text-sm text-[#16a34a]"
            ></div>
            <div class="flex-1 min-h-[34px]">
              <p id="objText2" class="text-[15px] sm:text-[16px] leading-snug text-[#25242c] font-bold"></p>
            </div>
          </li>

          <li
            id="objRow3"
            class="flex items-start gap-2.5 bg-white/80 p-2 rounded border-2 border-[#25242c]/20 transition-all duration-300 opacity-35"
          >
            <div
              id="check3"
              class="w-6 h-6 mt-0.5 rounded border-2 border-[#25242c] bg-white flex items-center justify-center shrink-0 font-bold text-sm text-[#16a34a]"
            ></div>
            <div class="flex-1 min-h-[34px]">
              <p id="objText3" class="text-[15px] sm:text-[16px] leading-snug text-[#25242c] font-bold"></p>
            </div>
          </li>
        </ul>

        <div class="relative pt-1 flex flex-col items-center">
          <div
            id="missionStamp"
            class="hidden mb-3 px-4 py-1 rounded border-[3px] border-[#16a34a] bg-[#dcfce7] text-[#15803d] font-extrabold text-sm sm:text-base tracking-wider uppercase shadow-[3px_3px_0px_#15803d]"
            style="font-family: 'Fredoka', sans-serif;"
          >
            ✔ MISSION ACTIVE
          </div>

          <div id="finalActionGroup" class="hidden w-full flex flex-col sm:flex-row gap-2.5">
            <button
              id="startMissionBtn"
              type="button"
              class="doodle-btn flex-1 py-2.5 px-4 text-base sm:text-lg flex items-center justify-center gap-2"
            >
              <span>🚀</span>
              <span>START MISSION</span>
            </button>
            <button
              id="replayBottomBtn"
              type="button"
              class="doodle-btn py-2.5 px-4 text-base sm:text-lg flex items-center justify-center gap-1.5"
              style="background-color: #b6b1ff;"
            >
              <span>↺</span>
              <span>REPLAY</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <footer
      class="fixed bottom-9 sm:bottom-11 left-1/2 -translate-x-1/2 z-30 w-[92%] max-w-[700px] pointer-events-auto"
    >
      <div class="hud-pill rounded-full px-4 py-2 flex items-center gap-3 shadow-xl">
        <span
          id="timeCode"
          class="text-xs font-bold text-white/90 tabular-nums shrink-0"
        >
          00:00 / 00:20
        </span>

        <div
          id="timelineTrack"
          class="relative flex-1 h-2.5 bg-white/15 rounded-full overflow-hidden cursor-pointer"
        >
          <div class="absolute top-0 bottom-0 w-[2px] bg-white/35 z-10" style="left: 20%;"></div>
          <div class="absolute top-0 bottom-0 w-[2px] bg-white/35 z-10" style="left: 47.5%;"></div>
          <div class="absolute top-0 bottom-0 w-[2px] bg-white/35 z-10" style="left: 82.5%;"></div>

          <div
            id="timelineFill"
            class="h-full bg-gradient-to-r from-[#fde047] via-[#c8eb78] to-[#7dd3fc] rounded-full transition-none"
            style="width: 0%;"
          ></div>
        </div>

        <span
          id="chapterBadge"
          class="text-[11px] font-bold uppercase tracking-wider text-[#c8eb78] shrink-0 hidden sm:inline"
        >
          ACT I
        </span>
      </div>
    </footer>
  </div>

  <!-- ========================================================= -->
  <!-- VIEW 3: GAME SCREEN (SEGUES HERE AFTER CUTSCENE)          -->
  <!-- ========================================================= -->
  <div id="gameView" class="screen-view hidden-view flex items-center justify-center p-4">
    <div class="notebook-sheet max-w-md w-full px-7 pt-9 pb-7 text-center">
      <div class="tape-strip"></div>

      <div class="text-5xl mb-3">🛡️🌙</div>
      <h1
        class="text-3xl font-bold text-[#25242c] mb-2"
        style="font-family: 'Fredoka', sans-serif;"
      >
        LUNAR OUTPOST REACHED!
      </h1>

      <p class="text-lg text-[#25242c] font-bold mb-6">
        Cutscene complete! Drop your game canvas and logic inside <code>#gameView</code>.
      </p>

      <button
        id="backHomeBtn"
        type="button"
        class="doodle-btn w-full py-2.5 px-4 text-base"
      >
        ← Back to Homepage
      </button>
    </div>
  </div>

  <script>
    (function () {
      // View Containers
      const homeView = document.getElementById('homeView');
      const cutsceneView = document.getElementById('cutsceneView');
      const gameView = document.getElementById('gameView');

      const homePlayBtn = document.getElementById('homePlayBtn');
      const backHomeBtn = document.getElementById('backHomeBtn');

      // Cutscene Elements
      const canvas = document.getElementById('cutsceneCanvas');
      const ctx = canvas.getContext('2d');

      const sceneLabel = document.getElementById('sceneLabel');
      const altReadout = document.getElementById('altReadout');
      const timeCode = document.getElementById('timeCode');
      const timelineTrack = document.getElementById('timelineTrack');
      const timelineFill = document.getElementById('timelineFill');
      const chapterBadge = document.getElementById('chapterBadge');

      const scene1Overlay = document.getElementById('scene1Overlay');
      const countdownText = document.getElementById('countdownText');

      const briefingOverlay = document.getElementById('briefingOverlay');
      const objRow1 = document.getElementById('objRow1');
      const objRow2 = document.getElementById('objRow2');
      const objRow3 = document.getElementById('objRow3');
      const objText1 = document.getElementById('objText1');
      const objText2 = document.getElementById('objText2');
      const objText3 = document.getElementById('objText3');
      const check1 = document.getElementById('check1');
      const check2 = document.getElementById('check2');
      const check3 = document.getElementById('check3');

      const missionStamp = document.getElementById('missionStamp');
      const finalActionGroup = document.getElementById('finalActionGroup');

      const muteBtn = document.getElementById('muteBtn');
      const muteIcon = document.getElementById('muteIcon');
      const muteText = document.getElementById('muteText');
      const playPauseBtn = document.getElementById('playPauseBtn');
      const playPauseIcon = document.getElementById('playPauseIcon');
      const playPauseText = document.getElementById('playPauseText');
      const replayBtn = document.getElementById('replayBtn');
      const skipBtn = document.getElementById('skipBtn');
      const startMissionBtn = document.getElementById('startMissionBtn');
      const replayBottomBtn = document.getElementById('replayBottomBtn');

      const OBJECTIVES = [
        '01. LAUNCH FROM EARTH TO LUNAR ORBIT',
        '02. DEPLOY SHIELD OVER LUNAR OUTPOST',
        '03. PROTECT THE POST AT ALL COSTS'
      ];

      const TOTAL_DURATION = 20.0;
      let currentScreen = 'home';
      let elapsed = 0;
      let isPlaying = false;
      let isScrubbing = false;
      let postCutsceneFreeFlight = false;
      let lastTimestamp = 0;
      let autoSegueTimer = null;

      let milestones = {
        beep3: false,
        beep2: false,
        beep1: false,
        ignition: false,
        briefingSlide: false,
        check1: false,
        check2: false,
        check3: false,
        shieldHum: false,
        stampSlam: false
      };

      let width = 0;
      let height = 0;
      let dpr = Math.min(window.devicePixelRatio || 1, 2);

      let stars = [];
      let shootingStars = [];
      let smokePuffs = [];
      let shieldPulses = [];

      let distanceKm = 0;
      let lastTypeSoundTime = 0;

      let audioCtx = null;
      let isMuted = true;

      // Screen Router
      function showScreen(screenName) {
        currentScreen = screenName;
        if (autoSegueTimer) {
          clearTimeout(autoSegueTimer);
          autoSegueTimer = null;
        }

        homeView.classList.add('hidden-view');
        cutsceneView.classList.add('hidden-view');
        gameView.classList.add('hidden-view');

        if (screenName === 'home') {
          isPlaying = false;
          homeView.classList.remove('hidden-view');
        } else if (screenName === 'cutscene') {
          cutsceneView.classList.remove('hidden-view');
          resizeCanvas();
          resetCutscene(false);
        } else if (screenName === 'game') {
          isPlaying = false;
          gameView.classList.remove('hidden-view');
        }
      }

      homePlayBtn.addEventListener('click', () => {
        ensureAudioContext();
        showScreen('cutscene');
      });

      backHomeBtn.addEventListener('click', () => {
        showScreen('home');
      });

      function ensureAudioContext() {
        if (!audioCtx) {
          const AudioContextClass = window.AudioContext || window.webkitAudioContext;
          if (AudioContextClass) {
            audioCtx = new AudioContextClass();
          }
        }
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
      }

      function playTone(freq, duration, type = 'sine', volume = 0.12, slideFreq = null) {
        if (isMuted || !audioCtx) return;
        try {
          const now = audioCtx.currentTime;
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, now);
          if (slideFreq) {
            osc.frequency.exponentialRampToValueAtTime(slideFreq, now + duration);
          }
          gain.gain.setValueAtTime(volume, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + duration);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now);
          osc.stop(now + duration);
        } catch (e) {}
      }

      function playIgnitionRumble() {
        if (isMuted || !audioCtx) return;
        try {
          const now = audioCtx.currentTime;
          const bufferSize = audioCtx.sampleRate * 1.5;
          const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
          const data = buffer.getChannelData(0);
          for (let i = 0; i < bufferSize; i++) {
            data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.75));
          }
          const noise = audioCtx.createBufferSource();
          noise.buffer = buffer;

          const filter = audioCtx.createBiquadFilter();
          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(195, now);
          filter.frequency.exponentialRampToValueAtTime(70, now + 1.5);

          const gain = audioCtx.createGain();
          gain.gain.setValueAtTime(0.24, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 1.5);

          noise.connect(filter);
          filter.connect(gain);
          gain.connect(audioCtx.destination);
          noise.start(now);
        } catch (e) {}
      }

      function playShieldHum() {
        if (isMuted || !audioCtx) return;
        try {
          const now = audioCtx.currentTime;
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(160, now);
          osc.frequency.exponentialRampToValueAtTime(360, now + 0.65);
          gain.gain.setValueAtTime(0.001, now);
          gain.gain.linearRampToValueAtTime(0.11, now + 0.15);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.85);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(now);
          osc.stop(now + 0.85);
        } catch (e) {}
      }

      function toggleMute() {
        isMuted = !isMuted;
        if (!isMuted) {
          ensureAudioContext();
          muteIcon.textContent = '🔊';
          muteText.textContent = 'SOUND ON';
          playTone(587.33, 0.12, 'triangle', 0.12);
        } else {
          muteIcon.textContent = '🔇';
          muteText.textContent = 'SOUND OFF';
        }
      }

      function updatePlayPauseUI() {
        if (isPlaying) {
          playPauseIcon.textContent = '⏸';
          playPauseText.textContent = 'PAUSE';
        } else {
          playPauseIcon.textContent = '▶';
          playPauseText.textContent = 'PLAY';
        }
      }

      function togglePlayPause() {
        ensureAudioContext();
        if (elapsed >= TOTAL_DURATION) {
          resetCutscene(false);
          return;
        }
        isPlaying = !isPlaying;
        updatePlayPauseUI();
        playTone(isPlaying ? 523.25 : 392.0, 0.1, 'triangle', 0.1);
      }

      muteBtn.addEventListener('click', toggleMute);
      playPauseBtn.addEventListener('click', togglePlayPause);

      function resizeCanvas() {
        width = window.innerWidth;
        height = window.innerHeight;
        dpr = Math.min(window.devicePixelRatio || 1, 2);

        canvas.width = Math.floor(width * dpr);
        canvas.height = Math.floor(height * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        generateStars();
      }

      function generateStars() {
        const count = Math.floor((width * height) / 7200);
        stars = [];
        for (let i = 0; i < count; i++) {
          stars.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2.2 + 0.8,
            isFourPoint: Math.random() < 0.24,
            parallax: 0.15 + Math.random() * 0.45,
            phase: Math.random() * Math.PI * 2,
            speed: 1.2 + Math.random() * 2.2
          });
        }
      }

      function spawnShootingStar() {
        shootingStars.push({
          x: Math.random() * (width * 0.55) + width * 0.05,
          y: Math.random() * (height * 0.35) + 45,
          vx: 290 + Math.random() * 140,
          vy: -80 - Math.random() * 45,
          length: 105 + Math.random() * 45,
          life: 1.0
        });
      }

      function spawnSmoke(x, y, spreadX, vyBase, sizeBase) {
        smokePuffs.push({
          x: x + (Math.random() - 0.5) * spreadX,
          y: y + (Math.random() - 0.5) * 8,
          vx: (Math.random() - 0.5) * 38,
          vy: vyBase + Math.random() * 22,
          radius: sizeBase + Math.random() * 11,
          grow: 18 + Math.random() * 14,
          alpha: 0.52 + Math.random() * 0.16
        });
      }

      function resetCutscene(jumpToEnd = false) {
        if (autoSegueTimer) {
          clearTimeout(autoSegueTimer);
          autoSegueTimer = null;
        }
        elapsed = jumpToEnd ? TOTAL_DURATION : 0;
        isPlaying = !jumpToEnd;
        postCutsceneFreeFlight = jumpToEnd;
        updatePlayPauseUI();

        smokePuffs = [];
        shootingStars = [];
        shieldPulses = [];

        milestones = {
          beep3: jumpToEnd,
          beep2: jumpToEnd,
          beep1: jumpToEnd,
          ignition: jumpToEnd,
          briefingSlide: jumpToEnd,
          check1: jumpToEnd,
          check2: jumpToEnd,
          check3: jumpToEnd,
          shieldHum: jumpToEnd,
          stampSlam: jumpToEnd
        };

        scene1Overlay.style.opacity = '0';
        scene1Overlay.style.transform = 'translateY(-28px)';

        if (jumpToEnd) {
          briefingOverlay.style.opacity = '1';
          briefingOverlay.style.transform = 'translateX(0px) rotate(-0.6deg)';
          objRow1.style.opacity = '1';
          objRow2.style.opacity = '1';
          objRow3.style.opacity = '1';
          objText1.textContent = OBJECTIVES[0];
          objText2.textContent = OBJECTIVES[1];
          objText3.textContent = OBJECTIVES[2];
          check1.textContent = '✓';
          check2.textContent = '✓';
          check3.textContent = '✓';
          missionStamp.classList.remove('hidden');
          missionStamp.classList.add('stamp-active');
          finalActionGroup.classList.remove('hidden');
        } else {
          briefingOverlay.style.opacity = '0';
          briefingOverlay.style.transform = 'translateX(-45px) rotate(-1deg)';
          objRow1.style.opacity = '0.35';
          objRow2.style.opacity = '0.35';
          objRow3.style.opacity = '0.35';
          objText1.textContent = '';
          objText2.textContent = '';
          objText3.textContent = '';
          check1.textContent = '';
          check2.textContent = '';
          check3.textContent = '';
          missionStamp.classList.add('hidden');
          missionStamp.classList.remove('stamp-active');
          finalActionGroup.classList.add('hidden');
        }
      }

      replayBtn.addEventListener('click', () => {
        ensureAudioContext();
        playTone(523.25, 0.14, 'triangle', 0.12);
        resetCutscene(false);
      });

      replayBottomBtn.addEventListener('click', () => {
        ensureAudioContext();
        playTone(523.25, 0.14, 'triangle', 0.12);
        resetCutscene(false);
      });

      skipBtn.addEventListener('click', () => {
        ensureAudioContext();
        playTone(659.25, 0.14, 'triangle', 0.12);
        resetCutscene(true);
      });

      startMissionBtn.addEventListener('click', () => {
        ensureAudioContext();
        playTone(880, 0.2, 'triangle', 0.15);
        showScreen('game');
      });

      function scrubToClientX(clientX) {
        const rect = timelineTrack.getBoundingClientRect();
        const ratio = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
        const targetTime = ratio * TOTAL_DURATION;
        const wasPlaying = isPlaying;
        resetCutscene(false);
        elapsed = targetTime;
        if (elapsed >= TOTAL_DURATION) {
          resetCutscene(true);
        } else {
          isPlaying = wasPlaying;
          updatePlayPauseUI();
        }
      }

      timelineTrack.addEventListener('pointerdown', (e) => {
        isScrubbing = true;
        timelineTrack.setPointerCapture(e.pointerId);
        scrubToClientX(e.clientX);
      });

      timelineTrack.addEventListener('pointermove', (e) => {
        if (!isScrubbing) return;
        scrubToClientX(e.clientX);
      });

      timelineTrack.addEventListener('pointerup', (e) => {
        if (!isScrubbing) return;
        isScrubbing = false;
        timelineTrack.releasePointerCapture(e.pointerId);
      });

      canvas.addEventListener('click', (e) => {
        const rect = canvas.getBoundingClientRect();
        shieldPulses.push({
          x: e.clientX - rect.left,
          y: e.clientY - rect.top,
          radius: 12,
          alpha: 0.85,
          color: '#7dd3fc'
        });
        playTone(440, 0.18, 'sine', 0.08, 660);
      });

      function getRocketScreenX() {
        const centerX = width * 0.5;
        if (elapsed < 9.5) {
          return centerX;
        } else {
          const transition = Math.min(1, (elapsed - 9.5) / 1.4);
          const ease = 1 - Math.pow(1 - transition, 3);
          const targetX = width < 640 ? width * 0.82 : Math.min(width * 0.76, width / 2 + 265);
          return centerX + (targetX - centerX) * ease;
        }
      }

      function getRocketScreenY() {
        const earthPadY = height * 0.75;
        if (elapsed < 4.0) {
          return earthPadY - 46;
        } else if (elapsed < 9.5) {
          const t = (elapsed - 4.0) / 5.5;
          const easeOut = 1 - Math.pow(1 - t, 2.1);
          return (earthPadY - 46) - easeOut * (height * 0.25);
        } else if (elapsed < 16.5) {
          return height * 0.5 + Math.sin((elapsed - 9.5) * 2.4) * 8;
        } else {
          const targetY = width < 640 ? height * 0.36 : height * 0.43;
          const transition = Math.min(1, (elapsed - 16.5) / 1.3);
          const ease = 1 - Math.pow(1 - transition, 3);
          return height * 0.5 + (targetY - height * 0.5) * ease + Math.sin(elapsed * 2.6) * 6;
        }
      }

      function getTypedString(fullText, progress, nowSec) {
        const clamped = Math.max(0, Math.min(1, progress));
        const charCount = Math.floor(fullText.length * clamped);
        if (clamped > 0 && clamped < 1 && isPlaying && nowSec - lastTypeSoundTime > 0.085) {
          lastTypeSoundTime = nowSec;
          playTone(880, 0.025, 'square', 0.03);
        }
        const slice = fullText.slice(0, charCount);
        return clamped < 1 && clamped > 0 ? slice + '▍' : slice;
      }

      function drawSpaceAndStars(timeSec, scrollOffset) {
        ctx.fillStyle = '#0b0e17';
        ctx.fillRect(0, 0, width, height);

        ctx.save();
        const grad = ctx.createLinearGradient(0, height * 0.1, width, height * 0.85);
        grad.addColorStop(0, 'rgba(32, 28, 58, 0.38)');
        grad.addColorStop(0.5, 'rgba(19, 25, 48, 0.24)');
        grad.addColorStop(1, 'rgba(42, 32, 68, 0.36)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.moveTo(0, height * 0.18);
        ctx.bezierCurveTo(width * 0.35, height * 0.08, width * 0.65, height * 0.42, width, height * 0.28);
        ctx.lineTo(width, height * 0.75);
        ctx.bezierCurveTo(width * 0.65, height * 0.86, width * 0.3, height * 0.55, 0, height * 0.68);
        ctx.closePath();
        ctx.fill();
        ctx.restore();

        for (const s of stars) {
          const twinkle = 0.55 + 0.45 * Math.sin(timeSec * s.speed + s.phase);
          const wrappedY = ((s.y + scrollOffset * s.parallax) % height + height) % height;

          ctx.save();
          ctx.globalAlpha = twinkle * 0.9;
          ctx.fillStyle = '#e2e8f0';

          if (s.isFourPoint) {
            const r = s.radius * 2.2;
            ctx.beginPath();
            ctx.moveTo(s.x, wrappedY - r);
            ctx.quadraticCurveTo(s.x, wrappedY, s.x + r, wrappedY);
            ctx.quadraticCurveTo(s.x, wrappedY, s.x, wrappedY + r);
            ctx.quadraticCurveTo(s.x, wrappedY, s.x - r, wrappedY);
            ctx.quadraticCurveTo(s.x, wrappedY, s.x, wrappedY - r);
            ctx.fill();
          } else {
            ctx.beginPath();
            ctx.arc(s.x, wrappedY, s.radius, 0, Math.PI * 2);
            ctx.fill();
          }
          ctx.restore();
        }
      }

      function drawShootingStars() {
        for (const st of shootingStars) {
          ctx.save();
          ctx.globalAlpha = st.life;
          const tailX = st.x - (st.vx / 310) * st.length;
          const tailY = st.y - (st.vy / 310) * st.length;
          const grad = ctx.createLinearGradient(st.x, st.y, tailX, tailY);
          grad.addColorStop(0, '#93c5fd');
          grad.addColorStop(0.4, 'rgba(59, 130, 246, 0.5)');
          grad.addColorStop(1, 'rgba(59, 130, 246, 0)');

          ctx.strokeStyle = grad;
          ctx.lineWidth = 5;
          ctx.lineCap = 'round';
          ctx.beginPath();
          ctx.moveTo(st.x, st.y);
          ctx.lineTo(tailX, tailY);
          ctx.stroke();

          ctx.fillStyle = '#dbeafe';
          ctx.beginPath();
          ctx.arc(st.x, st.y, 4.5, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }
      }

      function drawEarthLaunchpadSurface(verticalOffset, timeSec) {
        const horizonY = height * 0.75 + verticalOffset;
        if (horizonY > height + 160) return;

        ctx.save();

        const atmoGrad = ctx.createLinearGradient(0, horizonY - 75, 0, horizonY + 45);
        atmoGrad.addColorStop(0, 'rgba(56, 189, 248, 0)');
        atmoGrad.addColorStop(0.55, 'rgba(56, 189, 248, 0.28)');
        atmoGrad.addColorStop(1, 'rgba(37, 150, 243, 0.55)');
        ctx.fillStyle = atmoGrad;
        ctx.beginPath();
        ctx.moveTo(-40, horizonY + 60);
        ctx.lineTo(-40, horizonY - 12);
        ctx.quadraticCurveTo(width * 0.5, horizonY - 82, width + 40, horizonY - 12);
        ctx.lineTo(width + 40, horizonY + 60);
        ctx.closePath();
        ctx.fill();

        const oceanGrad = ctx.createLinearGradient(0, horizonY - 36, 0, horizonY + height * 0.38);
        oceanGrad.addColorStop(0, '#38bdf8');
        oceanGrad.addColorStop(0.35, '#2596f3');
        oceanGrad.addColorStop(1, '#1d4ed8');

        ctx.fillStyle = oceanGrad;
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(-40, horizonY + height * 0.45);
        ctx.lineTo(-40, horizonY + 34);
        ctx.quadraticCurveTo(width * 0.5, horizonY - 38, width + 40, horizonY + 34);
        ctx.lineTo(width + 40, horizonY + height * 0.45);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.save();
        ctx.clip();

        ctx.fillStyle = '#84cc16';
        ctx.strokeStyle = '#3f6212';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.ellipse(width * 0.22, horizonY + 55, Math.max(110, width * 0.16), 58, -0.15, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#a3e635';
        ctx.beginPath();
        ctx.ellipse(width * 0.5, horizonY + 28, Math.max(120, width * 0.15), 42, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#84cc16';
        ctx.beginPath();
        ctx.ellipse(width * 0.8, horizonY + 62, Math.max(120, width * 0.18), 64, 0.18, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
        ctx.restore();

        function drawDoodleCloud(cx, cy, scale) {
          ctx.save();
          ctx.translate(cx, cy);
          ctx.scale(scale, scale);
          ctx.fillStyle = '#ffffff';
          ctx.strokeStyle = '#25242c';
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.arc(-22, 4, 14, Math.PI * 0.5, Math.PI * 1.5);
          ctx.arc(-6, -6, 18, Math.PI, Math.PI * 2);
          ctx.arc(16, -2, 15, Math.PI * 1.1, Math.PI * 0.2);
          ctx.arc(24, 6, 12, Math.PI * 1.5, Math.PI * 0.5);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
          ctx.restore();
        }

        drawDoodleCloud(width * 0.15 + Math.sin(timeSec * 0.8) * 8, horizonY - 26, 0.85);
        drawDoodleCloud(width * 0.84 + Math.cos(timeSec * 0.7) * 8, horizonY - 22, 0.9);

        const padX = width * 0.5;
        const padY = horizonY - 8;

        ctx.strokeStyle = '#334155';
        ctx.fillStyle = '#cbd5e1';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.roundRect(padX - 58, padY - 68, 14, 72, 3);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(padX - 58, padY - 52);
        ctx.lineTo(padX - 44, padY - 36);
        ctx.moveTo(padX - 44, padY - 52);
        ctx.lineTo(padX - 58, padY - 36);
        ctx.moveTo(padX - 44, padY - 54);
        ctx.lineTo(padX - 18, padY - 54);
        ctx.stroke();

        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 5;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(padX - 38, padY + 4);
        ctx.lineTo(padX - 48, padY + 18);
        ctx.moveTo(padX + 38, padY + 4);
        ctx.lineTo(padX + 48, padY + 18);
        ctx.stroke();

        ctx.fillStyle = '#475569';
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.roundRect(padX - 46, padY - 4, 92, 10, 4);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fde047';
        ctx.fillRect(padX - 32, padY - 2, 12, 6);
        ctx.fillRect(padX - 6, padY - 2, 12, 6);
        ctx.fillRect(padX + 20, padY - 2, 12, 6);

        const astroLeftX = width < 640 ? width * 0.18 : width * 0.28;
        const astroRightX = width < 640 ? width * 0.82 : width * 0.72;
        drawWavingAstronaut(astroLeftX, horizonY - 24 + Math.sin(timeSec * 3.4) * 5, timeSec, 0.82);
        drawWavingAstronaut(astroRightX, horizonY - 22 + Math.cos(timeSec * 3.1) * 5, timeSec + 1.2, 0.76);

        ctx.restore();
      }

      function drawLunarOutpostDestination(moonDropY, timeSec, shieldLocked) {
        if (moonDropY < -180) return;

        const moonCenterX = width < 640 ? width * 0.82 : Math.min(width * 0.76, width / 2 + 265);
        const moonCenterY = moonDropY;
        const moonRadius = width < 640 ? 92 : 128;

        ctx.save();

        const glow = ctx.createRadialGradient(
          moonCenterX,
          moonCenterY,
          moonRadius * 0.85,
          moonCenterX,
          moonCenterY,
          moonRadius * 1.45
        );
        glow.addColorStop(0, 'rgba(226, 232, 240, 0.25)');
        glow.addColorStop(1, 'rgba(226, 232, 240, 0)');
        ctx.fillStyle = glow;
        ctx.beginPath();
        ctx.arc(moonCenterX, moonCenterY, moonRadius * 1.45, 0, Math.PI * 2);
        ctx.fill();

        const moonGrad = ctx.createRadialGradient(
          moonCenterX - moonRadius * 0.3,
          moonCenterY - moonRadius * 0.3,
          10,
          moonCenterX,
          moonCenterY,
          moonRadius
        );
        moonGrad.addColorStop(0, '#f1f5f9');
        moonGrad.addColorStop(0.55, '#cbd5e1');
        moonGrad.addColorStop(1, '#94a3b8');

        ctx.fillStyle = moonGrad;
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.arc(moonCenterX, moonCenterY, moonRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        function drawMiniCrater(cx, cy, rx, ry) {
          ctx.save();
          ctx.translate(cx, cy);
          ctx.fillStyle = '#94a3b8';
          ctx.beginPath();
          ctx.ellipse(0, 2, rx * 1.12, ry * 1.18, 0, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = '#e2e8f0';
          ctx.beginPath();
          ctx.ellipse(0, 0, rx, ry, 0, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = '#64748b';
          ctx.beginPath();
          ctx.ellipse(0, 1, rx * 0.72, ry * 0.65, 0, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }

        drawMiniCrater(moonCenterX - moonRadius * 0.42, moonCenterY + moonRadius * 0.15, 18, 10);
        drawMiniCrater(moonCenterX + moonRadius * 0.38, moonCenterY + moonRadius * 0.25, 22, 12);
        drawMiniCrater(moonCenterX - moonRadius * 0.1, moonCenterY + moonRadius * 0.48, 25, 13);

        const postX = moonCenterX;
        const postY = moonCenterY - moonRadius + 6;

        ctx.fillStyle = '#475569';
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.roundRect(postX - 36, postY - 6, 72, 12, 5);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#bae6fd';
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(postX, postY - 6, 24, Math.PI, 0);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = 'rgba(255,255,255,0.65)';
        ctx.beginPath();
        ctx.ellipse(postX - 8, postY - 18, 7, 3.5, -0.4, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(postX, postY - 30);
        ctx.lineTo(postX, postY - 44);
        ctx.stroke();

        ctx.fillStyle = shieldLocked ? '#4ade80' : '#f87171';
        ctx.beginPath();
        ctx.arc(postX, postY - 46, 4.5, 0, Math.PI * 2);
        ctx.fill();

        drawWavingAstronaut(postX + 44, postY - 12 + Math.sin(timeSec * 3.5) * 3, timeSec, 0.56);

        if (shieldLocked) {
          const pulse = 1 + Math.sin(timeSec * 5) * 0.03;
          ctx.save();
          ctx.strokeStyle = 'rgba(56, 189, 248, 0.9)';
          ctx.fillStyle = 'rgba(125, 211, 252, 0.18)';
          ctx.lineWidth = 3.5;
          ctx.setLineDash([10, 6]);
          ctx.beginPath();
          ctx.arc(postX, postY - 10, 66 * pulse, Math.PI * 1.05, Math.PI * 1.95);
          ctx.stroke();
          ctx.setLineDash([]);
          ctx.beginPath();
          ctx.arc(postX, postY - 10, 60 * pulse, Math.PI, 0);
          ctx.fill();
          ctx.restore();
        }

        ctx.restore();
      }

      function drawWavingAstronaut(x, y, timeSec, scaleMult = 0.85) {
        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(-0.14 + Math.sin(timeSec * 2.5) * 0.05);
        const s = (width < 640 ? 0.72 : 0.9) * scaleMult;
        ctx.scale(s, s);

        ctx.fillStyle = '#cbd5e1';
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.roundRect(-24, -12, 48, 36, 8);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#f8fafc';
        ctx.beginPath();
        ctx.roundRect(-16, 20, 13, 22, 6);
        ctx.roundRect(4, 20, 13, 22, 6);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#93c5fd';
        ctx.beginPath();
        ctx.roundRect(-18, 37, 16, 8, 4);
        ctx.roundRect(3, 37, 16, 8, 4);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.roundRect(-18, -6, 36, 30, 10);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#dbeafe';
        ctx.beginPath();
        ctx.roundRect(-10, 1, 20, 14, 4);
        ctx.fill();
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(-4, 8, 2.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#f8fafc';
        ctx.beginPath();
        ctx.roundRect(-27, -2, 11, 20, 5);
        ctx.fill();
        ctx.stroke();

        ctx.save();
        ctx.translate(18, 0);
        ctx.rotate(-0.7 + Math.sin(timeSec * 9) * 0.35);
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.roundRect(0, -18, 11, 22, 5);
        ctx.fill();
        ctx.stroke();
        ctx.restore();

        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(0, -22, 20, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.roundRect(-14, -31, 28, 18, 8);
        ctx.fill();

        ctx.fillStyle = 'rgba(255,255,255,0.55)';
        ctx.beginPath();
        ctx.roundRect(-10, -28, 12, 4, 2);
        ctx.fill();

        ctx.restore();
      }

      function drawSmokePuffs() {
        for (const p of smokePuffs) {
          ctx.save();
          ctx.globalAlpha = Math.max(0, p.alpha);
          ctx.fillStyle = '#f1f5f9';
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }
      }

      function drawVerticalRocket(x, y, tilt, scale, thrusterLevel, shieldActive) {
        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(tilt);
        ctx.scale(scale, scale);

        if (shieldActive) {
          const pulse = 1 + Math.sin(performance.now() * 0.01) * 0.05;
          ctx.save();
          ctx.strokeStyle = 'rgba(125, 211, 252, 0.85)';
          ctx.fillStyle = 'rgba(125, 211, 252, 0.14)';
          ctx.lineWidth = 4;
          ctx.beginPath();
          ctx.arc(0, -4, 68 * pulse, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();
          ctx.restore();
        }

        if (thrusterLevel > 0) {
          const flicker = Math.sin(performance.now() * 0.04) * 6;
          const flameH = (26 + thrusterLevel * 32) + flicker;

          ctx.beginPath();
          ctx.moveTo(-12, 35);
          ctx.quadraticCurveTo(0, 35 + flameH, 12, 35);
          ctx.closePath();
          ctx.fillStyle = thrusterLevel > 1.1 ? '#38bdf8' : '#fbbf24';
          ctx.fill();

          ctx.beginPath();
          ctx.moveTo(-6, 35);
          ctx.quadraticCurveTo(0, 35 + flameH * 0.62, 6, 35);
          ctx.closePath();
          ctx.fillStyle = '#fef9c3';
          ctx.fill();
        }

        ctx.fillStyle = '#93c5fd';
        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 2.8;
        ctx.beginPath();
        ctx.moveTo(-18, 10);
        ctx.quadraticCurveTo(-36, 22, -31, 40);
        ctx.quadraticCurveTo(-20, 35, -14, 28);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(18, 10);
        ctx.quadraticCurveTo(36, 22, 31, 40);
        ctx.quadraticCurveTo(20, 35, 14, 28);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#64748b';
        ctx.beginPath();
        ctx.roundRect(-12, 31, 24, 7, 3);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.moveTo(0, -48);
        ctx.bezierCurveTo(22, -32, 25, 8, 16, 33);
        ctx.lineTo(-16, 33);
        ctx.bezierCurveTo(-25, 8, -22, -32, 0, -48);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#e2e8f0';
        ctx.beginPath();
        ctx.moveTo(0, -48);
        ctx.bezierCurveTo(22, -32, 25, 8, 16, 33);
        ctx.lineTo(5, 33);
        ctx.bezierCurveTo(12, 8, 10, -28, 0, -48);
        ctx.closePath();
        ctx.fill();

        ctx.strokeStyle = '#25242c';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(0, -48);
        ctx.bezierCurveTo(22, -32, 25, 8, 16, 33);
        ctx.lineTo(-16, 33);
        ctx.bezierCurveTo(-25, 8, -22, -32, 0, -48);
        ctx.closePath();
        ctx.stroke();

        ctx.fillStyle = '#bae6fd';
        ctx.beginPath();
        ctx.arc(0, -8, 13.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(0, -8, 9.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = 'rgba(255, 255, 255, 0.55)';
        ctx.beginPath();
        ctx.ellipse(-3.5, -11.5, 3.5, 2, -0.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.restore();
      }

      function drawShieldPulses() {
        for (const sp of shieldPulses) {
          ctx.save();
          ctx.strokeStyle = sp.color || '#7dd3fc';
          ctx.globalAlpha = sp.alpha;
          ctx.lineWidth = 3.5;
          ctx.beginPath();
          ctx.arc(sp.x, sp.y, sp.radius, 0, Math.PI * 2);
          ctx.stroke();
          ctx.restore();
        }
      }

      let smokeAccumulator = 0;
      let starScroll = 0;
      let shootingTimer = 1.5;

      function updateAndRender(timestamp) {
        if (!lastTimestamp) lastTimestamp = timestamp;
        const dt = Math.min((timestamp - lastTimestamp) / 1000, 0.05);
        lastTimestamp = timestamp;

        if (currentScreen !== 'cutscene') {
          requestAnimationFrame(updateAndRender);
          return;
        }

        const timeSec = timestamp / 1000;

        if (isPlaying) {
          elapsed += dt;
          if (elapsed >= TOTAL_DURATION) {
            elapsed = TOTAL_DURATION;
            isPlaying = false;
            postCutsceneFreeFlight = true;
            updatePlayPauseUI();

            // Automatically segue over to the game screen 1.5s after finishing
            autoSegueTimer = setTimeout(() => {
              showScreen('game');
            }, 1500);
          }
        }

        const pct = Math.min(100, (elapsed / TOTAL_DURATION) * 100);
        timelineFill.style.width = `${pct}%`;
        const secFormatted = Math.floor(elapsed).toString().padStart(2, '0');
        timeCode.textContent = `00:${secFormatted} / 00:20`;

        let cameraShakeX = 0;
        let cameraShakeY = 0;
        let earthVerticalOffset = 0;
        let moonDestinationY = -280;
        let thrusterPower = 0;
        let rocketScale = width < 640 ? 0.8 : 1.0;
        let rocketTilt = 0;
        let rocketShieldActive = false;
        let postShieldLocked = false;

        if (elapsed < 4.0) {
          sceneLabel.textContent = 'SCENE 01 // EARTH PAD';
          chapterBadge.textContent = 'ACT I';
          distanceKm = 0;

          if (elapsed > 0.25) {
            scene1Overlay.style.opacity = '1';
            scene1Overlay.style.transform = 'translateY(0px)';
          }

          if (elapsed < 1.1) {
            countdownText.textContent = 'T-MINUS 3...';
            countdownText.style.color = '#25242c';
            if (!milestones.beep3) {
              milestones.beep3 = true;
              playTone(440, 0.14, 'square', 0.08);
            }
          } else if (elapsed < 2.1) {
            countdownText.textContent = 'T-MINUS 2...';
            if (!milestones.beep2) {
              milestones.beep2 = true;
              playTone(440, 0.14, 'square', 0.08);
            }
          } else if (elapsed < 3.1) {
            countdownText.textContent = 'T-MINUS 1...';
            if (!milestones.beep1) {
              milestones.beep1 = true;
              playTone(440, 0.14, 'square', 0.08);
            }
          } else {
            countdownText.textContent = '🔥 IGNITION! 🔥';
            countdownText.style.color = '#dc2626';
            thrusterPower = 0.85;
            cameraShakeX = (Math.random() - 0.5) * 6;
            cameraShakeY = (Math.random() - 0.5) * 6;

            if (!milestones.ignition) {
              milestones.ignition = true;
              playTone(660, 0.35, 'sawtooth', 0.12, 880);
              playIgnitionRumble();
            }
          }

          if (elapsed > 2.4 && isPlaying) {
            smokeAccumulator += dt;
            if (smokeAccumulator > 0.06) {
              smokeAccumulator = 0;
              spawnSmoke(width * 0.5, height * 0.75 - 10, 52, -14, 14);
            }
          }
        } else if (elapsed < 9.5) {
          sceneLabel.textContent = 'SCENE 02 // EARTH LIFTOFF';
          chapterBadge.textContent = 'ACT II';

          scene1Overlay.style.opacity = '0';
          scene1Overlay.style.transform = 'translateY(-32px)';
          countdownText.style.color = '#25242c';

          const t2 = (elapsed - 4.0) / 5.5;
          thrusterPower = 1.35;

          if (t2 < 0.28) {
            const shakeMag = (1 - t2 / 0.28) * 7.5;
            cameraShakeX = (Math.random() - 0.5) * shakeMag;
            cameraShakeY = (Math.random() - 0.5) * shakeMag;
          }

          earthVerticalOffset = Math.pow(t2, 1.35) * (height * 0.85);
          if (isPlaying) {
            starScroll += (200 + t2 * 360) * dt;
          }
          distanceKm = Math.floor(Math.pow(t2, 1.4) * 140000);
          rocketTilt = Math.sin(elapsed * 6) * 0.02;

          if (isPlaying) {
            smokeAccumulator += dt;
            if (smokeAccumulator > 0.04) {
              smokeAccumulator = 0;
              spawnSmoke(getRocketScreenX(), getRocketScreenY() + 38 * rocketScale, 18, 105, 16);
            }
          }
        } else if (elapsed < 16.5) {
          sceneLabel.textContent = 'SCENE 03 // MISSION BRIEFING';
          chapterBadge.textContent = 'ACT III';

          earthVerticalOffset = height + 250;
          const t3 = elapsed - 9.5;
          thrusterPower = 1.05;
          if (isPlaying) starScroll += 310 * dt;
          distanceKm = Math.floor(140000 + (t3 / 7.0) * 200000);
          rocketTilt = Math.sin(elapsed * 3.2) * 0.025;

          if (!milestones.briefingSlide) {
            milestones.briefingSlide = true;
            playTone(523.25, 0.14, 'triangle', 0.11);
          }
          briefingOverlay.style.opacity = '1';
          briefingOverlay.style.transform = 'translateX(0px) rotate(-0.6deg)';

          if (t3 >= 0.4) {
            objRow1.style.opacity = '1';
            const p1 = (t3 - 0.4) / 1.6;
            objText1.textContent = getTypedString(OBJECTIVES[0], p1, timeSec);
            if (p1 >= 1 && !milestones.check1) {
              milestones.check1 = true;
              check1.textContent = '✓';
              playTone(659.25, 0.1, 'triangle', 0.1);
            }
          }

          if (t3 >= 2.4) {
            objRow2.style.opacity = '1';
            const p2 = (t3 - 2.4) / 1.6;
            objText2.textContent = getTypedString(OBJECTIVES[1], p2, timeSec);
            if (p2 >= 1 && !milestones.check2) {
              milestones.check2 = true;
              check2.textContent = '✓';
              playTone(783.99, 0.1, 'triangle', 0.1);
            }
          }

          if (t3 >= 4.4) {
            objRow3.style.opacity = '1';
            const p3 = (t3 - 4.4) / 1.6;
            objText3.textContent = getTypedString(OBJECTIVES[2], p3, timeSec);
            if (p3 >= 1 && !milestones.check3) {
              milestones.check3 = true;
              check3.textContent = '✓';
              playTone(880, 0.14, 'triangle', 0.12);
            }
          }

          if (isPlaying) {
            smokeAccumulator += dt;
            if (smokeAccumulator > 0.055) {
              smokeAccumulator = 0;
              spawnSmoke(getRocketScreenX(), getRocketScreenY() + 38 * rocketScale, 14, 85, 14);
            }
          }
        } else {
          sceneLabel.textContent = 'SCENE 04 // LUNAR OUTPOST';
          chapterBadge.textContent = 'READY';

          earthVerticalOffset = height + 250;
          const t4 = Math.min(3.5, elapsed - 16.5);
          const arrivalEase = Math.min(1, t4 / 1.3);
          const targetMoonY = width < 640 ? height * 0.18 : height * 0.22;
          moonDestinationY = -200 + (1 - Math.pow(1 - arrivalEase, 3)) * (targetMoonY + 200);

          thrusterPower = postCutsceneFreeFlight ? 0.95 : 0.65;
          if (isPlaying || postCutsceneFreeFlight) {
            starScroll += (postCutsceneFreeFlight ? 180 : 120) * dt;
          }
          distanceKm = Math.min(384400, Math.floor(340000 + (t4 / 1.3) * 44400));
          rocketTilt = Math.cos(timeSec * 2.8) * 0.03;
          rocketShieldActive = true;
          postShieldLocked = t4 >= 0.9;

          briefingOverlay.style.opacity = '1';
          briefingOverlay.style.transform = 'translateX(0px) rotate(-0.6deg)';
          objRow1.style.opacity = '1';
          objRow2.style.opacity = '1';
          objRow3.style.opacity = '1';
          objText1.textContent = OBJECTIVES[0];
          objText2.textContent = OBJECTIVES[1];
          objText3.textContent = OBJECTIVES[2];
          check1.textContent = '✓';
          check2.textContent = '✓';
          check3.textContent = '✓';

          if (postShieldLocked && !milestones.shieldHum) {
            milestones.shieldHum = true;
            playShieldHum();
          }

          if (t4 >= 1.2 && !milestones.stampSlam) {
            milestones.stampSlam = true;
            missionStamp.classList.remove('hidden');
            missionStamp.classList.add('stamp-active');
            finalActionGroup.classList.remove('hidden');

            playTone(523.25, 0.12, 'triangle', 0.13);
            setTimeout(() => playTone(659.25, 0.12, 'triangle', 0.13), 110);
            setTimeout(() => playTone(1046.5, 0.28, 'triangle', 0.15), 220);

            shieldPulses.push({
              x: getRocketScreenX(),
              y: moonDestinationY,
              radius: 30,
              alpha: 0.95,
              color: '#38bdf8'
            });
          }

          if (isPlaying || postCutsceneFreeFlight) {
            smokeAccumulator += dt;
            if (smokeAccumulator > 0.07) {
              smokeAccumulator = 0;
              spawnSmoke(getRocketScreenX(), getRocketScreenY() + 38 * rocketScale, 12, 55, 12);
            }
          }
        }

        altReadout.textContent = distanceKm.toLocaleString();

        if (isPlaying || postCutsceneFreeFlight) {
          shootingTimer -= dt;
          if (shootingTimer <= 0) {
            spawnShootingStar();
            shootingTimer = 3.2 + Math.random() * 2.5;
          }

          for (let i = shootingStars.length - 1; i >= 0; i--) {
            const st = shootingStars[i];
            st.x += st.vx * dt;
            st.y += st.vy * dt;
            st.life -= 0.72 * dt;
            if (st.life <= 0) shootingStars.splice(i, 1);
          }

          for (let i = smokePuffs.length - 1; i >= 0; i--) {
            const p = smokePuffs[i];
            p.x += p.vx * dt;
            p.y += p.vy * dt;
            p.radius += p.grow * dt;
            p.alpha -= 0.32 * dt;
            if (p.alpha <= 0) smokePuffs.splice(i, 1);
          }

          for (let i = shieldPulses.length - 1; i >= 0; i--) {
            const sp = shieldPulses[i];
            sp.radius += 210 * dt;
            sp.alpha -= 1.3 * dt;
            if (sp.alpha <= 0) shieldPulses.splice(i, 1);
          }
        }

        ctx.save();
        ctx.translate(cameraShakeX, cameraShakeY);

        drawSpaceAndStars(timeSec, starScroll);
        drawShootingStars();
        drawEarthLaunchpadSurface(earthVerticalOffset, timeSec);
        drawLunarOutpostDestination(moonDestinationY, timeSec, postShieldLocked);
        drawSmokePuffs();
        drawVerticalRocket(
          getRocketScreenX(),
          getRocketScreenY(),
          rocketTilt,
          rocketScale,
          thrusterPower,
          rocketShieldActive
        );
        drawShieldPulses();

        ctx.restore();

        requestAnimationFrame(updateAndRender);
      }

      window.addEventListener('resize', () => {
        if (currentScreen === 'cutscene') resizeCanvas();
      });

      window.onload = function () {
        resizeCanvas();
        spawnShootingStar();
        requestAnimationFrame(updateAndRender);
      };
    })();
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    """Renders the complete single-file MOONGUARD homepage, cutscene, and game screen."""
    return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
