# AI-GM-Engine (v6.3) -- 支持中文

A rule set and a small Python helper that turn a chat AI into a Game Master
that keeps track of things.
English-designed, multilingual gameplay, model-independent AI Game Master.

一套规则加一个小型 Python 辅助程序，让聊天 AI 变成一个会记账的游戏主持人（GM）。
英文设计，支持多语言游玩，不依赖特定模型的 AI 游戏主持人。

**[English ↓](#english) · [中文说明 ↓](#中文说明)**

---

## English

## Starting a game

You need a model that can run code, because the dice and math go through the
Python helper.

1. Open a new chat.
2. Attach `NEW_ENGINE_v6_3.md`, `AI_RULES_v6_3.md`, `SAVE_TEMPLATE_v6_3.md`,
   `engine_math_v6_3.py` and **one** background from `written_background/`.
   If you're using a Project, put the files in the project's knowledge instead
   of the chat. The helper only needs to be there for the AI to run; it doesn't
   need to read it. The background template is only for making your own world,
   and the changelog only for old saves.
3. Send:

   > Load the engine files, start <background name>.

Only attach one background. The engine is about 91 KB and each background is
40–100 KB, so this already takes a big bite out of the context window. Bigger
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
- Assassin's Creed Syndicate: London 1868
- Assassin's Creed Syndicate: The Wrong Hands
- The Sheet Anchor (India, 1991)

大多数实际上我都加入了中文翻译，但是文件主体还是英文，中文固定了名字和名词所以不容易出现每次翻译不一样。

### Making your own world

Play one of the written backgrounds first so you know what a finished one looks
like. Then attach `BACKGROUND_TEMPLATE_v6_3.md` with the engine files, tell the
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
| `NEW_ENGINE_v6_3.md` | The rules. Part 0 runs every turn, Part 1 sections open when something triggers them, Part 2 modules are on unless a background turns one off. |
| `BACKGROUND_TEMPLATE_v6_3.md` | Template for a world: setting, character, and everything that exists before Round 1. |
| `SAVE_TEMPLATE_v6_3.md` | Save format: a readable save plus a hidden capsule. |
| `AI_RULES_v6_3.md` | How the AI should run the engine in a chat. No game rules here, just discipline. |
| `engine_math_v6_3.py` | Dice, arithmetic, record merge and checks. It calculates; it never decides. |
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
## Language support

AI-GM-Engine supports playing in Chinese as well as English.

You can play in:
- Simplified Chinese (简体中文)
- English

The engine rules and technical files are currently written in English. However, the AI can run the campaign, narrate events, handle dialogue, and communicate with the player in Chinese.

To play in Chinese, add this instruction when starting a game:

> Run the entire campaign in Simplified Chinese. All narration, dialogue, descriptions, notifications, and player-facing output must be in Simplified Chinese. Keep the engine rules and internal state consistent. Do not translate proper nouns or technical terms inconsistently.

For Traditional Chinese, replace Simplified Chinese with Traditional Chinese.

## License

MIT. Fork it, change it, sell what you make with it. Your worlds belong to you.

---

## 中文说明

### 这是什么

一套规则加一个小型 Python 辅助程序，让聊天 AI 变成一个会记账的游戏主持人（GM）。世界会自己运转，不确定的行动用真实的骰子决定，游戏状态以 AI 无法悄悄修改的形式记录下来。玩上几百回合，那个店员还是同一个店员，那把刀还在你的背包里。

这不是剧本，也不是角色提示词，而是底层引擎：你带来一个世界，引擎负责运行它。MIT 协议，免费使用，你用它做出来的东西都归你。

### 开始游戏

你需要一个能运行代码的模型，因为骰子和计算都由 Python 辅助程序完成。

1. 新开一个对话。
2. 上传 `NEW_ENGINE_v6_3.md`、`AI_RULES_v6_3.md`、`SAVE_TEMPLATE_v6_3.md`、`engine_math_v6_3.py`，再加 `written_background/` 里的**一个**背景文件。如果你用的是 Project，就把文件放进 Project 的知识库，而不是对话里。辅助程序只需要存在，让 AI 能运行，AI 不需要阅读它。背景模板只在自己做世界时才用，更新日志只用于旧存档。
3. 发送：

   > Load the engine files, start <背景名称>.

只上传一个背景。引擎约 91 KB，每个背景 40–100 KB，这已经占用了不少上下文窗口。上下文越大的模型表现越好。

### 继续战役

新开一个对话，上传：

- 引擎文件（如果已经在 Project 里就不用）
- 你的存档文件
- 这个存档所属的背景

发送：

> Continue from this save.

背景必须上传，因为存档只记录第 0 回合之后发生的变化。如果存档或背景来自旧版本，还要上传 `CHANGELOG_NEW_ENGINE.md`，GM 会在开始前用它把旧文件更新到当前版本。

### 游戏中

- **存档。** GM 每 10 回合自动存档，你要求时也会存。它直接存，不会先问你。如果存档失败，你可以选 `retry`（重试）或 `continue unsaved`（不存档继续）。不存档会让你多玩一回合，然后再试一次。
- **章节。** 如果背景有章节分段，你会得到选择：**按原样继续**，或**延伸**到新章节。选择延伸时，GM 会先告诉你哪些内容将被收尾，然后才开始写。
- **完整或精简。** 第 0 回合时 GM 会问你要完整（full）还是精简（lite）输出。精简只是文字更短，其他一切不变：同样的状态、同样的掷骰、同样的存档。之后可以随时切换。
- **物品点数（Item points）。** 如果 GM 跳过了一段时间，你没机会买绳子或给门卫小费，可以花物品点数补上：绳子一直在你包里，或者你昨晚已经给过小费。点数多少取决于你的角色身份（普通上班族有 60 点），每次在安全的地方好好睡一晚会恢复一些。不能超过 Tier 2。
- **场外发言。** 消息以 `ps` 开头，就是在跟 GM 说话，而不是在游戏里行动。

### 用中文玩

引擎规则和技术文件是英文的，但 AI 可以全程用中文主持、叙述和对话。开始游戏时加上这句：

> 整个战役使用简体中文进行。所有叙述、对话、描写、提示和面向玩家的输出都必须使用简体中文。保持引擎规则和内部状态一致。专有名词和术语的翻译要前后一致。

想用繁体中文，把"简体中文"换成"繁體中文"即可。
