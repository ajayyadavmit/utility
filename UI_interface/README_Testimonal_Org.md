#  testimonial marquee + animated org chart https://paperclip.ing/

A single-file, dependency-free page (HTML + CSS + a little JavaScript) with two sections:

1. **Testimonial marquee**: two rows of cards. Row 1 scrolls **left → right**, row 2 scrolls **right → left**. Speed is adjustable and hovering pauses the row.
2. **Organisation chart**: pill-shaped role cards. "Active" roles get a **green light that travels around the border**, and green dashes **flow along the connector lines**.

The look is inspired by modern dark landing pages. All names, quotes and roles are **placeholders**. Replace them with your own (and get permission before publishing real people's quotes).

## Quick start

```text
builders-page/
├── testimonal.html   ← the whole page
└── README.md
```


## Speed adjustment

| Where | What to change | Effect |
|---|---|---|
| On the page | The two **speed sliders** | 0.2× (slow) to 4× (fast), live and smooth |
| CSS | `animation: slide 60s linear infinite` on `.track` | **Base** speed: one full loop takes 60 s at 1×. Lower the number to make it faster |
| JS | `input[data-row]` handler | Uses `updatePlaybackRate()` so speed changes do not jump |
| Default per row | Add `value="1.5"` to a slider, then call `anim.updatePlaybackRate(1.5)` on load | Start one row faster than the other |

**Direction:** row 1 uses `animation-direction: reverse` (left → right). Remove that line to make it right → left.

**Pause on hover:** `.marquee:hover .track { animation-play-state: paused }`. Delete it to keep scrolling.

## Editing content

Everything lives at the top of the `<script>` block.

- **Testimonials:** edit the `PEOPLE` array: `[name, handle, quote, avatar colour]`. The first 5 go in row 1, the rest in row 2. Add more entries for a longer loop.
- **Org chart:** edit the `NODES` array. Each node has `t` (title), `a` (agent or person), `i` (icon), `x`/`y` (position on the 900 × 420 stage) and `on:1` for the green **Active** state.
- **Connector lines:** the `<svg class="lines">` paths use the same coordinates. The grey `.base` paths are the tree. The green `.flow` paths animate. If you move a node, adjust its path.

## Colours and styling

- **Accent colour:** change `--accent` in `:root`, or use the colour picker on the page.
- **Card size:** `.card { width: 380px; height: 200px }`.
- **Flow speed:** `.flow { animation: flow 1s … }` (smaller = faster).
- **Border light speed:** `.node.active { animation: spin 3s … }`.

## How it works (short version)

- **Seamless marquee:** each row's cards are rendered twice, and the track slides by exactly `-50%` and repeats.
- **Moving border light:** a `conic-gradient` border whose start angle is animated with a registered CSS property (`@property --a`).
- **Flowing line:** `stroke-dasharray` plus an animated `stroke-dashoffset`.
- **Responsive chart:** the 900 px stage is scaled down with `transform: scale()` on small screens.

