# Brand assets

A small, reusable identity for the profile and project READMEs.

## Files

| File | Use |
| --- | --- |
| `brand-banner.svg` | Wide profile banner (1280×640). Preferred for README headers. |
| `brand-banner.png` | Raster banner (1280×640). |
| `social-preview.png` | Repository social preview (1280×640). Unggah lewat Settings → Social preview. |
| `brand-logo.svg` | Square **D** monogram (512×512), astral gradient + orbit + grain. Use for avatars, repo headers, and favicons. |
| `brand-logo.png` | Raster monogram (512×512). |
| `avatar.png` | GitHub profile avatar (1024×1024). Unggah lewat Settings → Profile → Avatar. |
| `logo-pulse.gif` | Animated hero mark (360×360), orbit particles in cyan / pink / amber. |

## Mark v5 — Astral Grain

Logo saat ini memakai monogram **D** geometris dengan **astral gradient** (pink `#FF9BD2` → violet `#8B5CF6` → blue `#5B8CFF` → cyan `#4DE1FF`), orbit ring, aksen sirkuit, dan **film grain** di atas deep space `#06070E`. Ini menggantikan mark v4 yang memakai cyan → indigo → violet tanpa grain.

Arah visual ini mengikuti koleksi **Grainient** (mesh gradient + grain halus) dan motion **Arc / uiarc** (press scale, label morph, loading state) yang dipakai di dashboard `repo-atlas-next`.

## Palette

| Token | Hex | Use |
| --- | --- | --- |
| Void | `#06070E` | Background |
| Surface | `#0A0C17` | Cards and frames |
| Violet | `#8B5CF6` | Primary |
| Blue | `#5B8CFF` | Mid-gradient |
| Cyan | `#4DE1FF` | Accent |
| Pink | `#FF9BD2` | Warm accent |
| Amber | `#FFB86B` | Signal / highlight |
| Text | `#F2F4FF` | Headings |
| Muted | `#9AA3C4` | Body and captions |

## Type

Inter (or Segoe UI / Arial as fallbacks), weights 400–800. The wordmark uses tight tracking; the monogram uses a 4-stop astral gradient.

## Usage

- Keep clear space around the monogram equal to at least 12% of its width.
- Use the SVG on light and dark backgrounds; the mark has its own dark surface.
- Do not stretch, recolor outside the palette, or add extra text inside the mark.
- For a repository header, place `brand-logo.svg` at 64–96 px and link it to the profile.

## Regenerating PNGs

The PNGs were rendered from the SVGs with Sharp:

```bash
npm install sharp
node scripts/render-brand.mjs
python scripts/make-animated-logo.py
```
