# Grid + animated sidebar

 Move the mouse over a **chosen area** of the page and:

- the grid lines **light up around the cursor** (spotlight),
- a **highlight pill slides** between sidebar links, with a soft glow that follows the cursor,
- icons **wiggle**, the logo squares **shuffle**, and the panel **tilts** slightly,
- the accent colour can be changed (green, red, blue, purple, orange or any custom colour).

---



### Use it in your own page

```html
<!-- Any section of your page. data-glow sets the starting colour -->
<section class="glow-area" data-glow="#e5484d">
  <div class="grid"></div>
  <!-- your sidebar, cards, text... -->
</section>

<script>
  document.querySelectorAll('.glow-area').forEach(initGlowArea);
</script>
```

Copy the `.glow-area`, `.grid` styles and the `initGlowArea()` function from the demo. You can repeat the section as many times as you like, each with its own colour.

---

## 2. Variables explained

### 2.1 CSS custom properties (colours and position)

| Variable | Set where | What it does | Example |
|---|---|---|---|
| `--glow` | `.glow-area` (or `data-glow`, or the colour picker) | **Accent colour.** Drives the spotlight grid, panel edge, logo square, hover icon colour and link glow. Change this one value to recolour everything. | `#e5484d` (red) |
| `--x`, `--y` | Updated by JavaScript on every mouse move | **Cursor position inside the area**, in pixels from the area's top-left corner. Used by the spotlight mask. Default `-999px` (off-screen), so there is no glow until the mouse enters. | `--x: 240px` |
| `--mx` | Updated by JavaScript on each nav link | Cursor's horizontal position **inside one link**. Moves the soft glow within that link. | `--mx: 60px` |
| `--c` | Inline style on each colour dot | The dot's own colour (`style="--c:#e5484d"`). Display only. | `#3b82f6` |

### 2.2 Theme tokens (page colours)

Defined in `:root`. Dark mode values replace them automatically (`prefers-color-scheme: dark`), or force it with `<html data-theme="dark">` or `"light"`.

| Variable | Meaning |
|---|---|
| `--bg` | Page and area background |
| `--line` | Normal (unlit) grid line colour and area border |
| `--fg` | Main text colour |
| `--muted` | Secondary text and idle icon colour |
| `--pill` | Colour of the sliding highlight behind the hovered link |
| `--panel` | Sidebar panel background |

### 2.3 HTML attributes

| Attribute | On | Meaning |
|---|---|---|
| `data-glow="#rrggbb"` | `.glow-area` | Starting accent colour for that area |
| `data-target="demo"` | `#colors` (the colour controls) | `id` of the area these colour buttons control |
| `data-color="#rrggbb"` | each colour button | The colour that button applies |
| `aria-pressed` | each colour button | Marks the selected colour (accessibility) |

### 2.4 CSS classes

| Class | Purpose |
|---|---|
| `.glow-area` | The container where the effect is active. **Put the effect here.** |
| `.on` | Added automatically while the mouse is inside the area. Shows the spotlight. |
| `.grid` | Layer that draws the grid. Its `::after` layer is the lit (coloured) grid revealed by the mask. |
| `.logo` | Four-square pixel logo that shuffles on hover |
| `.panel` | The sidebar card that tilts |
| `nav a` | Sidebar links (icon `span` + label) |
| `.pill` | The sliding highlight element. This is **not** the badge style from other pages. |
| `.controls` | Row of colour dots and the custom colour picker |

### 2.5 JavaScript

| Name | Where | What it does |
|---|---|---|
| `initGlowArea(area)` | global function | Sets up one area: reads `data-glow`, tracks the mouse, adds or removes `.on`, runs the pill and tilt. Call once per area. |
| `area` | inside `initGlowArea` | The `.glow-area` element being set up |
| `r` | mouse handlers | `getBoundingClientRect()` of the area, used to turn page coordinates into area coordinates |
| `nav`, `pill`, `panel` | inside `initGlowArea` | The sidebar list, the sliding highlight and the card that tilts |
| `px`, `py` | tilt handler | Cursor position as a fraction (-0.5 to 0.5) across the panel, converted to rotation |
| `controls`, `target`, `picker` | colour code | The dot row, the area it controls (found via `data-target`) and the `<input type="color">` |
| `setColor(c)` | colour code | Sets `--glow` on the target area and updates `aria-pressed` on the dots |

---

## 3. Settings you can safely tweak

| Want to change | Where | Current value |
|---|---|---|
| Spotlight size | `radial-gradient(160px circle ...)` in `.grid::after` | `160px` |
| Spotlight softness | the `70%` stop in the same gradient | `70%` |
| Grid cell size | `background-size` on `.grid` | `20px` |
| Area height | `.glow-area { height }` | `440px` |
| Link glow size | `radial-gradient(90px circle ...)` in `nav a::after` | `90px` |
| Link glow strength | `color-mix(in srgb, var(--glow) 24%, ...)` | `24%` |
| Pill slide speed | `.pill { transition: transform .28s }` | `.28s` |
| Tilt strength | `px * 4` (left-right) and `py * 3` (up-down) in the tilt handler | `4°` / `3°` |
| Spotlight fade in or out | `.grid::after { transition: opacity .25s }` | `.25s` |

---

## 4. How it works

1. On `pointermove`, JavaScript writes the cursor position into `--x` and `--y` on the area.
2. CSS uses them in a `radial-gradient` **mask** on the coloured grid layer, so only the part near the cursor is visible.
3. Moving the mouse onto a link moves the `.pill` with `translateY(link.offsetTop)` and resizes it to the link's height.
4. `pointerleave` removes `.on` and the pill, so the area returns to its calm state.

