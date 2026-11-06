---
id: "prisma_orm_006"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 6
source_url: "https://www.prisma.io/brand"
language: "en"
retrieved_at: "2026-11-01 22:18:10"
content_hash: "8cb7a187cf6dceb965413e51c6e41949b3a1564e38accc683bd6dad513557a8c"
---

# Prisma ORM

Source: https://www.prisma.io/brand

---

# Brand Guidelines

Design tokens, typography, colors, and spacing references for this project. Update `globals.css` to customize these values per client.

## Logo

## Typography

Headings: Sora (--font-heading)

The quick brown fox jumps over the lazy dog

Body: Inter (--font-sans)

The quick brown fox jumps over the lazy dog

Tagline / kicker — the standard section and product label. Sentence case, ink at 70%, colour carried by a dot. Never uppercase, never letter-spaced, never grey. Use `RoleKicker` from `@/components/brand/role-kicker`.

Type-safe data layer

Managed database

App hosting

Heading Scale

# Heading 1 (text-6xl)

## Heading 2 (text-5xl)

### Heading 3 (text-4xl)

#### Heading 4 (text-3xl)

##### Heading 5 (text-2xl)

###### Heading 6 (text-xl)

Body Text

Large body text (text-lg)

Base body text (text-base)

Small body text (text-sm)

Extra small text (text-xs)

Font Weights

Normal (font-normal / 400)

Semibold (font-semibold / 600) — buttons and CTAs

Loaded weights: Inter variable 100–900, Sora variable 100–800.

## Texture & Pattern

`<Texture />`
Shown raw above. In practice it overlays color-washed section panels at 0.06 opacity with multiply blending (the component's default) — a present but fine film grain, never a visible image.

`<Pattern />`
Isometric cube grid, cursor-reactive — cubes bulge away from the pointer. Move your mouse over it.

## Prism Ray

`<PrismRay />`
The triple-band ray — `prism-cyan-400` / `prism-yellow-300` / `prism-red-500` — at the brand angle of −16°, in whisper / structural / hero intensities. `prismBands()` exposes the raw gradient for fills, edges, and rings.

The ray is a state, not a decoration. It appears where something is happening or where you are — never as a static background stripe.

- Scanning — the logo cloud sweep
- Loading — prismatic skeletons
- Active — the selected tab
- Progress — bars, spinners, countdowns

[Open the Ray Lab](https://www.prisma.io/brand/rays)

## Glass Prisms

`<GlassPrism />`
“Any shape can be a Prisma” — a polygon face extruded back into space as translucent glass, drawn from the brand Figma's 3D exploration. The pentagon is the canonical brand shape; hexagon, rectangle, and triangle extend the family. Lean away from the triangle.

Glass lives in the background. Prisms sit behind content, cropped by section edges — never in front of copy, never floating in whitespace as decoration.

- `white` — only over saturated color, where the glass glows
- `ink` — hairline glass for white backgrounds
- `spectral` — hairlines with the face catching the spectrum

[Open the Prism Lab](https://www.prisma.io/brand/prisms)

## Icons

Icon library: Forma Thin by Icons8 — thin-stroke geometric icons matching the light, precise brand voice. One library across the whole site; do not mix.

Source: Icons8, fetched via the `icons8mcp` MCP server (platform `forma-thin`) and committed as React components in `src/components/icons/forma.tsx`. Hero, navbar, and brand pages use Forma Thin; remaining starter sections still render Lucide and get swapped as they're rebuilt.

Icon tiles — when an icon anchors a card or feature row, it sits on an `IconTile` (`src/components/brand/icon-tile.tsx`): a white tile with the panel idiom in miniature — the spectral wash collecting along the tile's bottom edge, the glyph in `text-foreground` on top. Never flat tinted squares. Default `size-12`; pass `className` to resize (stack-bento uses `size-14`).

## Brand Color Scales

The three prism colors, each as an 11-step scale (`prism-cyan`, `prism-red`, `prism-yellow`). The ringed swatch is the exact brand color.

Prism Cyan

50

#EEFFFF

100

#DCFDFF

200

#B3F4F9

300

#7BE7F0

400

#01D7E4

500

#00BBCB

600

#009AAA

700

#007F8D

800

#006772

900

#00545D

950

#00353C

Prism Red

50

#FFEEEE

100

#FFDFDF

200

#FFC2C4

300

#FF9FA4

400

#FF7682

500

#F34A60

600

#D02344

700

#AF0A33

800

#8E0B29

900

#740F22

950

#4B0211

Prism Yellow

50

#FFF7E0

100

#FCEDC2

200

#F8DA85

300

#F3C306

400

#EAA700

500

#D48700

600

#B46700

700

#965100

800

#7A4200

900

#633700

950

#402000

## Colors

All colors are defined as CSS custom properties in `globals.css`. Override them to match the client's brand.

Primary

--primary

Secondary

--secondary

Accent

--accent

Muted

--muted

Destructive

--destructive

Background

--background

Card

--card

Popover

--popover

## Spacing

## Border Radius

sm

--radius-sm

md

--radius-md

lg

--radius-lg

xl

--radius-xl

2xl

--radius-2xl

## Buttons

`<PrismButton />` `<PrismButtonOutline />`
From the approved stylescape: the primary CTA carries a drifting spectrum glow and erupts in a prismatic burst on hover; the secondary is a thin-border pill. Hover them.

Learn more links — the standard in-card text CTA is `<LearnMore />` (`src/components/brand/learn-more.tsx`): a spectrum-ink pill with the bold arrow. Use it wherever a card or feature row links deeper — never ad-hoc link styles. Pass `outline` to escalate to the bordered brand button when the link is a section's single closing CTA.

Variants × States (shadcn/ui)

| Variant | Default | With icon | Disabled | 
|---|---|---|---|
| `default` |  |  |  | 
| `secondary` |  |  |  | 
| `outline` |  |  |  | 
| `ghost` |  |  |  | 
| `link` |  |  |  | 
| `destructive` |  |  |  | 

Sizes

Icon Sizes