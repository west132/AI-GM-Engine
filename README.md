# NEW ENGINE

A rules specification and a stateless Python helper that let a language model
run as a Game Master — one that remembers.

The engine simulates a world independently of the player, referees uncertain
actions with real dice, and keeps canonical state in a form the model cannot
silently rewrite. A campaign can run for hundreds of rounds without the AI
forgetting who the clerk is or losing the knife in your pack.

It is not a chatbot prompt. It is not a campaign. It is the infrastructure
under one.

The engine is MIT-licensed and free. The worlds you build with it belong to you.

---

## What's in the set

Five files, all carrying the same version number:

| File | What it is |
|---|---|
| `NEW_ENGINE_v5_4.md` | The rules. Part 0 runs every turn; Part 1 sections open only when their trigger fires; Part 2 modules are opt-in. |
| `BACKGROUND_TEMPLATE_v5_4.md` | Round-0 truth — the world, the character, what already exists before play. |
| `SAVE_TEMPLATE_v5_4.md` | Persistence: a readable save plus a hidden capsule. |
| `AI_RULES_v5_4.md` | How to actually run the engine in a chat. No game rules — operational discipline. |
| `engine_math_v5_4.py` | Stateless helper: dice, arithmetic, record merge/validate. Decides nothing. |

Mixing versions breaks. Use one set.

---

## How to use

### To play

To play: start a new chat, attach the engine set + a BACKGROUND(chose 1, all will increase the tokens), then ask AI to start.
**If you had project, upload them in project resources, not the chat.

That's it. "Loading" = attaching the files to the conversation before the first message. No install, no clone, no folder.

First message to AI

Load the engine files, start <selected background>.

Without a background or wise to design your own (please try one of the written one to see what happen first):
Type in your world going to be, bones of your story e.g. fantacy, romance, fight etc.
Ask AI to check its design atleast 2 times.

Continuing a campaign
New chat → attach engine set(if there is a project lib then you dont need it) + save file + the BACKGROUND the save points to → send Continue from this save.

The BACKGROUND is required. The save only stores what differs from Round 0.


### To review the spec

Say plainly:

> **Don't play. Review this as a spec.**

Without that line, the opening directive ("I SIMULATE THE WORLD…") can pull a
model into playing the role instead of reviewing the file. One sentence
prevents it. This is not an engine rule; it's how to phrase the request.

### While playing

- The GM saves every 10 rounds and when you ask. Saves are performed, never
  offered. If one fails, you get `retry` or `continue unsaved` — one round,
  then the save is retried.
- A chapter break (when the BACKGROUND says so) gives you **continue as is** or
  **extend** into a new chapter. The extend path shows you what is about to be
  dropped before it is written.
- Output length: full by default; say `lite` at Round 0 for a shorter form.
  Same state, same rolls, same saves — only prose is compressed.

---

## Tested with

Real campaigns, real run lengths:

| Model | Mode | Tested |
|---|---|---|
| DeepSeek | Deep Thinking | yes |
| ChatGPT | 5.6 · High | yes |
| Claude | Opus 5.5 · Medium | yes |

The engine is model-agnostic; these are the ones with run logs behind them.
Use the largest model you have for the chapter rebase (§16.8), GM-error repair
(§16.7), and the first session of a campaign. Routine continuation can use a
smaller one.

---

## Design stance

Three commitments that everything else follows from:

- **The world exists independently of the player.** It can be met, avoided,
  altered, exploited, missed, or lost permanently. Nothing must reach the
  player. No arc is protected.
- **Cause before effect.** A hidden cause is committed before anything depends
  on it. No cause is invented backward from a clue the player already found.
- **Output cannot strengthen state.** Narration renders what is already true.
  It never makes something true by saying it.

If a rule contradicts one of these, the rule is void.

---

## License

MIT. Fork it, build on it, sell what you build. The worlds you create with it
are yours, not the engine's.
