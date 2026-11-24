# AI-GM-Engine (v6.3) -- 支持中文

A rule set and a small Python helper that turn a chat AI into a Game Master
that keeps track of things.
English-designed, multilingual gameplay, model-independent AI Game Master.

一套规则加一个小型 Python 辅助程序，让聊天 AI 变成一个能牢牢记住游戏状态的 GM。
英文设计，支持多语言游玩，不挑模型的 AI GM。

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

Most backgrounds include Chinese translations, but the main text is still in English.
The Chinese fixes names and terms, so they don't come out translated differently each time.

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
- Simplified Chinese
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

世界会自己运转，没把握的行动用真骰子决定，游戏状态都记录在案，AI 没法偷偷改动。就算玩上几百回合，店员还是原来那个店员，刀也还在你包里。

它不是剧本，也不是角色提示词，而是跑在底下的引擎：你提供世界，引擎负责运行。MIT 协议，免费使用，你用它做出来的东西都归你。

### 开始游戏

模型必须能运行代码，因为掷骰和计算都交给 Python 辅助程序。

1. 开一个新对话。
2. 上传 `NEW_ENGINE_v6_3.md`、`AI_RULES_v6_3.md`、`SAVE_TEMPLATE_v6_3.md`、`engine_math_v6_3.py`，加上 `written_background/` 里的**一个**背景。用 Project 的话，把文件放进 Project 知识库，不要放在对话里。辅助程序只要上传给 AI 运行就行，不用让它读。背景模板只有自己做世界时才用，更新日志只有读旧存档时才用。
3. 发送：

   > Load the engine files, start <背景名称>.

背景只上传一个。引擎约 91 KB，每个背景 40–100 KB，光这些就占掉不少上下文。上下文越大的模型跑得越稳。

大多数实际上我都加入了中文翻译，但是文件主体还是英文，中文固定了名字和名词所以不容易出现每次翻译不一样。

### 继续战役

开一个新对话，上传：

- 引擎文件（已经在 Project 里的可以跳过）
- 你的存档
- 这个存档对应的背景

发送：

> Continue from this save.

背景一定要上传，因为存档只记录第 0 回合之后的变化。存档或背景是旧版本的话，再加上 `CHANGELOG_NEW_ENGINE.md`，GM 会在开局前把旧文件升级到当前版本。

### 游戏中

- **存档。** GM 每 10 回合自动存档，你要求时也会存，不会先问你。存档失败时可以选 `retry`（重试）或 `continue unsaved`（不存档继续）。选不存档的话，可以再玩一回合，之后会重新尝试存档。
- **章节。** 背景如果分了章节，到时你可以选**照原样继续**，或**延伸**成新章节。如果选延伸，GM 会先列出哪些内容要收尾，再开始写新章节。
- **完整或精简。** 第 0 回合 GM 会问你要完整（full）还是精简（lite）输出。精简只是文字短一些，其他完全一样：状态、掷骰、存档都不变。之后随时可以切换。
- **物品点数（Item points）。** GM 跳过一段时间，你没来得及买绳子或给门卫塞小费？花物品点数补上就行：绳子本来就在你包里，或者小费昨晚已经给了。点数多少看你的角色身份（普通上班族 60 点），每次在安全的地方睡个好觉会回复一些。最高只能到 Tier 2。
- **场外发言。** 消息开头加 `ps`，就是在跟 GM 说话，不算游戏里的行动。

### 用中文玩

引擎规则和技术文件是英文的，但 AI 可以全程用中文跑团、叙述和对话。开局时加上这句：

> 整个战役使用简体中文进行。所有叙述、对话、描写、提示和面向玩家的输出都必须使用简体中文。保持引擎规则和内部状态一致。专有名词和术语的翻译要前后一致。

想玩繁体中文，把"简体中文"换成"繁體中文"就行。
