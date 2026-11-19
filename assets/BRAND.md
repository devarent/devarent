# Brand assets

A small, reusable identity for the profile and project READMEs.

## Files

| File | Use |
| --- | --- |
| `brand-banner.svg` | Wide profile banner (1280×360). Preferred for README headers. |
| `brand-banner.png` | Raster fallback / social preview (2560×720). |
| `brand-logo.svg` | Square monogram (512×512). Use for avatars, repo headers, and favicons. |
| `brand-logo.png` | Raster avatar (1024×1024). |

## Palette

| Token | Hex | Use |
| --- | --- | --- |
| Ink | `#0B0F17` | Background |
| Surface | `#0F172A` | Cards and frames |
| Cyan | `#22D3EE` | Primary accent |
| Indigo | `#6366F1` | Mid-gradient |
| Violet | `#A855F7` | Secondary accent |
| Text | `#F8FAFC` | Headings |
| Muted | `#94A3B8` | Body and captions |

## Type

Inter (or Segoe UI / Arial as fallbacks), weights 400–800. The monogram uses tight tracking and a cyan-to-violet gradient.

## Usage

- Keep clear space around the monogram equal to at least 12% of its width.
- Use the SVG on light and dark backgrounds; the mark has its own dark surface.
- Do not stretch, recolor outside the palette, or add extra text inside the mark.
- For a repository header, place `brand-logo.svg` at 64–96 px and link it to the profile.

## Regenerating PNGs

The PNGs were rendered from the SVGs with Sharp:

```bash
npm install sharp
node -e "const sharp=require('sharp'); sharp('brand-banner.svg',{density:192}).png().toFile('brand-banner.png')"
```
