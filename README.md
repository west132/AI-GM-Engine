# AI-GM-Engine (v6)

A rule set and a small Python helper that turn a chat AI into a Game Master
that keeps track of things.

---

## Starting a game

You need a model that can run code, because the dice and math go through the
Python helper.

1. Open a new chat.
2. Attach `NEW_ENGINE_v6_0.md`, `AI_RULES_v6_0.md`, `SAVE_TEMPLATE_v6_0.md`,
   `engine_math_v6_0.py` and **one** background from `written_background/`.
   If you're using a Project, put the files in the project's knowledge instead
   of the chat. The helper only needs to be there for the AI to run; it doesn't
   need to read it. The background template is only for making your own world,
   and the changelog only for old saves.
3. Send:

   > Load the engine files, start <background name>.

Only attach one background. The engine is about 87 KB and each background is
60–95 KB, so this already takes a big bite out of the context window. Bigger
context models handle it better.

### Written backgrounds

- TWWH
- Call of Cthulhu: Shanghai Tides
- Ashfall Hunter
- Cyberpunk RED: South Night City
- Last Scion: Boundary
- Last Train to Somewhere
- SCP: Omega-99
- SCP: Lambda-12
- Tarnstead (low fantasy)
- Skyrim: Dragonborn

### Making your own world

Play one of the written backgrounds first so you know what a finished one looks
like. Then attach `BACKGROUND_TEMPLATE_v6_0.md` with the engine files, tell the
AI the basics (genre, tone, who you play, what the story is about), and ask it
to check its own design at least twice before you start.

### Continuing a campaign

New chat, then attach:

- the engine files (skip if they're already in your Project)
- your save file
- the background that save belongs to

Send:

> Continue from this save.

The background is required. A save only holds what has changed since Round 0.

If the save or background is from an older version, also attach
`CHANGELOG_NEW_ENGINE.md`. The GM uses it to bring the old file up to date
before play starts.

---

## During play

- **Saving.** The GM saves every 10 rounds and whenever you ask. It just does
  it, it won't ask first. If a save fails you can pick `retry` or
  `continue unsaved`. Unsaved gives you one more round, then it tries again.
- **Chapters.** If the background has chapter breaks, you'll get a choice:
  **continue as is** or **extend** into a new chapter. If you extend, the GM
  shows you what's being retired before it writes anything.
- **Full or lite.** At Round 0 the GM asks whether you want full or lite
  output. Lite is shorter prose, nothing else changes: same state, same rolls,
  same saves. You can switch later.
- **Item points.** If the GM skipped ahead and you didn't get the chance to
  buy rope or tip the doorman, spend item points: the rope was in your pack all
  along, or you tipped him last night. Your pool depends on who your character
  is (an ordinary working adult has 60) and refills a bit after each good
  night's rest somewhere safe. Nothing above Tier 2.
- **Out of character.** Start a message with `ps` to talk to the GM instead of
  acting in the game.

---

## What this is

The world moves on its own, uncertain actions are settled with real dice, and
the game state is written down in a form the AI can't quietly change. You can
play hundreds of rounds and the clerk is still the same clerk, and the knife is
still in your pack.

This isn't a campaign or a character prompt. It's the layer underneath: you
bring a world, the engine runs it.

Free under MIT. Whatever you build with it is yours.

---

## Files

All files share one version number. Don't mix versions.

| File | Purpose |
|---|---|
| `NEW_ENGINE_v6_0.md` | The rules. Part 0 runs every turn, Part 1 sections open when something triggers them, Part 2 modules are on unless a background turns one off. |
| `BACKGROUND_TEMPLATE_v6_0.md` | Template for a world: setting, character, and everything that exists before Round 1. |
| `SAVE_TEMPLATE_v6_0.md` | Save format: a readable save plus a hidden capsule. |
| `AI_RULES_v6_0.md` | How the AI should run the engine in a chat. No game rules here, just discipline. |
| `engine_math_v6_0.py` | Dice, arithmetic, record merge and checks. It calculates; it never decides. |
| `CHANGELOG_NEW_ENGINE.md` | What changed over time, and how old saves and backgrounds are brought forward. Only needed for older files. |
| `written_background/` | Ready-to-play worlds (list above). |

---

## Reviewing the rules instead of playing

If you want an AI to review the spec, say so up front:

> Don't play. Review this as a spec.

The rules file opens with "I SIMULATE THE WORLD…", and without that line some
models just start playing. It's not an engine rule, just a tip.

---

## Tested on

| Model | Setting |
|---|---|
| DeepSeek | Deep Thinking |
| ChatGPT | 5.6, High |
| Claude | Opus 5.5, Medium |

These are the ones I've run real campaigns on. Other models should work.

Use your strongest model for the first session, chapter rebases (§16.8), and
fixing GM mistakes (§16.7). A smaller one is fine for normal play after that.

---

## How it's designed

Everything comes back to three ideas:

- **The world doesn't revolve around the player.** Things can be found,
  avoided, changed, missed, or lost for good. Nothing is guaranteed to reach
  you, and no storyline is protected.
- **Cause comes first.** Any hidden cause is decided before anything depends on
  it. The GM never makes up a reason after you've already found the clue.
- **Narration can't change the state.** The text describes what's already
  true. Saying something doesn't make it true.

If any rule goes against these three, the rule loses.

---

## License

MIT. Fork it, change it, sell what you make with it. Your worlds belong to you.
