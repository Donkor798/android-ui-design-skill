#!/usr/bin/env python3
"""
generate_theme.py — Generate res/values/colors_<theme>.xml for any of the 22 themes.

Usage:
    python3 scripts/generate_theme.py --theme neon_dark --output ./output/
    python3 scripts/generate_theme.py --theme all --output ./output/
    python3 scripts/generate_theme.py --list
"""
from __future__ import annotations
import argparse, sys, textwrap
from pathlib import Path

# ── Complete color data for all 22 themes ────────────────────────────────────
# Each theme: dict of token_suffix → hex_color
# Token naming: {prefix}_{suffix}  e.g. nd_background, sg_primary

THEMES: dict[str, dict] = {
    "neon_dark": {
        "_meta": {"prefix": "nd", "name": "Neon Dark", "dark": True},
        "background": "#0D0D0D", "surface": "#1A1A2E", "surface_variant": "#16213E", "surface_tint": "#1F1035",
        "primary": "#E94560", "primary_dark": "#C73652", "secondary": "#0F3460", "tertiary": "#533483",
        "on_background": "#EAEAEA", "on_surface": "#EAEAEA", "on_surface_dim": "#757575", "on_primary": "#FFFFFF",
        "correct": "#00E676", "wrong": "#FF1744", "score": "#FFD700",
        "timer_normal": "#00FFCC", "timer_warning": "#FF6D00", "highlight": "#00FFCC", "badge": "#E94560",
        "nav_bar": "#1A1A2E", "nav_selected": "#E94560", "nav_unselected": "#555555", "status_bar": "#0D0D0D",
        "tile_empty": "#16213E", "tile_2": "#1A1A3E", "tile_4": "#1E1E4A", "tile_8": "#533483",
        "tile_16": "#6A3D9A", "tile_32": "#E94560", "tile_64": "#C73652", "tile_128": "#00FFCC",
        "tile_256": "#00CCB0", "tile_512": "#FFD700", "tile_1024": "#FF6D00", "tile_2048": "#FFFFFF",
        "overlay": "#CC0D0D0D", "scrim": "#990D0D0D",
    },
    "space_galaxy": {
        "_meta": {"prefix": "sg", "name": "Space Galaxy", "dark": True},
        "background": "#06061A", "surface": "#0D0D2B", "surface_variant": "#151540", "surface_tint": "#1A1050",
        "primary": "#7B2FBE", "primary_dark": "#5C1F9E", "secondary": "#4CC9F0", "tertiary": "#F72585",
        "on_background": "#E8E8FF", "on_surface": "#E8E8FF", "on_surface_dim": "#6060A0", "on_primary": "#FFFFFF",
        "correct": "#4CC9F0", "wrong": "#F72585", "score": "#FFD60A",
        "timer_normal": "#4CC9F0", "timer_warning": "#F72585", "highlight": "#4CC9F0", "badge": "#F72585",
        "nav_bar": "#0D0D2B", "nav_selected": "#7B2FBE", "nav_unselected": "#404070", "status_bar": "#06061A",
        "tile_empty": "#0D0D3A", "tile_2": "#151560", "tile_4": "#1E1E80", "tile_8": "#4A1E8C",
        "tile_16": "#7B2FBE", "tile_32": "#9B4FDE", "tile_64": "#4CC9F0", "tile_128": "#3BB8DF",
        "tile_256": "#F72585", "tile_512": "#FFD60A", "tile_1024": "#FFFFFF", "tile_2048": "#FFD60A",
        "overlay": "#CC06061A", "scrim": "#9906061A",
    },
    "lava_fire": {
        "_meta": {"prefix": "lf", "name": "Lava Fire", "dark": True},
        "background": "#0A0000", "surface": "#1A0800", "surface_variant": "#2D1000", "surface_tint": "#3D1500",
        "primary": "#FF4500", "primary_dark": "#CC3700", "secondary": "#FFB700", "tertiary": "#FF0050",
        "on_background": "#FFE0CC", "on_surface": "#FFE0CC", "on_surface_dim": "#8B5E40", "on_primary": "#FFFFFF",
        "correct": "#FFB700", "wrong": "#FF0050", "score": "#FFE566",
        "timer_normal": "#FFB700", "timer_warning": "#FF0050", "highlight": "#FFB700", "badge": "#FF4500",
        "nav_bar": "#1A0800", "nav_selected": "#FF4500", "nav_unselected": "#5C3020", "status_bar": "#0A0000",
        "tile_empty": "#1A0800", "tile_2": "#2D1000", "tile_4": "#4A1800", "tile_8": "#7A2800",
        "tile_16": "#AA3800", "tile_32": "#CC3700", "tile_64": "#FF4500", "tile_128": "#FF6B00",
        "tile_256": "#FFB700", "tile_512": "#FFD700", "tile_1024": "#FFE566", "tile_2048": "#FFFFFF",
        "overlay": "#CC0A0000", "scrim": "#990A0000",
    },
    "midnight_luxury": {
        "_meta": {"prefix": "ml", "name": "Midnight Luxury", "dark": True},
        "background": "#0A0A0A", "surface": "#141414", "surface_variant": "#1E1E1E", "surface_tint": "#1A1A0A",
        "primary": "#D4AF37", "primary_dark": "#B8941F", "secondary": "#C0C0C0", "tertiary": "#E8D5A3",
        "on_background": "#F5F5F0", "on_surface": "#F5F5F0", "on_surface_dim": "#808080", "on_primary": "#0A0A0A",
        "correct": "#4CAF50", "wrong": "#F44336", "score": "#D4AF37",
        "timer_normal": "#C0C0C0", "timer_warning": "#FF6F00", "highlight": "#D4AF37", "badge": "#D4AF37",
        "nav_bar": "#141414", "nav_selected": "#D4AF37", "nav_unselected": "#505050", "status_bar": "#0A0A0A",
        "tile_empty": "#1E1E1E", "tile_2": "#2A2A2A", "tile_4": "#363636", "tile_8": "#4A3810",
        "tile_16": "#6B5220", "tile_32": "#8C6C2A", "tile_64": "#B8941F", "tile_128": "#D4AF37",
        "tile_256": "#DFC060", "tile_512": "#E8D080", "tile_1024": "#F0E0A0", "tile_2048": "#FFFFFF",
        "overlay": "#E50A0A0A", "scrim": "#990A0A0A",
    },
    "deep_sea": {
        "_meta": {"prefix": "ds", "name": "Deep Sea", "dark": True},
        "background": "#000A1A", "surface": "#001830", "surface_variant": "#00243F", "surface_tint": "#00305A",
        "primary": "#00CFFF", "primary_dark": "#009CC0", "secondary": "#0055AA", "tertiary": "#7FFFFF",
        "on_background": "#B0E8FF", "on_surface": "#B0E8FF", "on_surface_dim": "#405070", "on_primary": "#000A1A",
        "correct": "#7FFFFF", "wrong": "#FF4466", "score": "#00CFFF",
        "timer_normal": "#00CFFF", "timer_warning": "#FF4466", "highlight": "#7FFFFF", "badge": "#00CFFF",
        "nav_bar": "#001830", "nav_selected": "#00CFFF", "nav_unselected": "#204060", "status_bar": "#000A1A",
        "tile_empty": "#00243F", "tile_2": "#003060", "tile_4": "#004080", "tile_8": "#0055AA",
        "tile_16": "#0070CC", "tile_32": "#0090EE", "tile_64": "#00CFFF", "tile_128": "#7FFFFF",
        "tile_256": "#AAFFFF", "tile_512": "#FF4466", "tile_1024": "#FF8800", "tile_2048": "#FFFFFF",
        "overlay": "#CC000A1A", "scrim": "#99000A1A",
    },
    "aurora_night": {
        "_meta": {"prefix": "an", "name": "Aurora Night", "dark": True},
        "background": "#060812", "surface": "#0C1020", "surface_variant": "#131828", "surface_tint": "#1A2030",
        "primary": "#00FF88", "primary_dark": "#00CC66", "secondary": "#AA00FF", "tertiary": "#00CCFF",
        "on_background": "#D0FFE8", "on_surface": "#D0FFE8", "on_surface_dim": "#406050", "on_primary": "#060812",
        "correct": "#00FF88", "wrong": "#FF4488", "score": "#00CCFF",
        "timer_normal": "#00FF88", "timer_warning": "#FF4488", "highlight": "#AA00FF", "badge": "#00FF88",
        "nav_bar": "#0C1020", "nav_selected": "#00FF88", "nav_unselected": "#304040", "status_bar": "#060812",
        "tile_empty": "#131828", "tile_2": "#1A2535", "tile_4": "#003322", "tile_8": "#006644",
        "tile_16": "#00AA66", "tile_32": "#00FF88", "tile_64": "#00CCFF", "tile_128": "#AA00FF",
        "tile_256": "#CC44FF", "tile_512": "#FF4488", "tile_1024": "#FFCC00", "tile_2048": "#FFFFFF",
        "overlay": "#CC060812", "scrim": "#99060812",
    },
    "halloween": {
        "_meta": {"prefix": "hw", "name": "Halloween", "dark": True},
        "background": "#0D0800", "surface": "#1A1000", "surface_variant": "#2A1A00", "surface_tint": "#301800",
        "primary": "#FF6600", "primary_dark": "#CC5200", "secondary": "#8B00FF", "tertiary": "#00CC66",
        "on_background": "#F0E0C0", "on_surface": "#F0E0C0", "on_surface_dim": "#806040", "on_primary": "#FFFFFF",
        "correct": "#00CC66", "wrong": "#FF1744", "score": "#FF6600",
        "timer_normal": "#FF6600", "timer_warning": "#FF1744", "highlight": "#8B00FF", "badge": "#FF6600",
        "nav_bar": "#1A1000", "nav_selected": "#FF6600", "nav_unselected": "#604020", "status_bar": "#0D0800",
        "tile_empty": "#1A1000", "tile_2": "#2A1A00", "tile_4": "#3D2800", "tile_8": "#5C3A00",
        "tile_16": "#7A4E00", "tile_32": "#CC5200", "tile_64": "#FF6600", "tile_128": "#8B00FF",
        "tile_256": "#6A00CC", "tile_512": "#00CC66", "tile_1024": "#FF1744", "tile_2048": "#F0F0F0",
        "overlay": "#CC0D0800", "scrim": "#990D0800",
    },
    "steampunk": {
        "_meta": {"prefix": "sp", "name": "Steampunk", "dark": True},
        "background": "#1A1008", "surface": "#2A1C0C", "surface_variant": "#3A2810", "surface_tint": "#4A3418",
        "primary": "#B87333", "primary_dark": "#8A5520", "secondary": "#D4A838", "tertiary": "#7A6040",
        "on_background": "#F0D898", "on_surface": "#F0D898", "on_surface_dim": "#907050", "on_primary": "#1A1008",
        "correct": "#88CC44", "wrong": "#CC4422", "score": "#D4A838",
        "timer_normal": "#B87333", "timer_warning": "#CC4422", "highlight": "#D4A838", "badge": "#B87333",
        "nav_bar": "#2A1C0C", "nav_selected": "#B87333", "nav_unselected": "#706040", "status_bar": "#1A1008",
        "tile_empty": "#2A1C0C", "tile_2": "#3A2810", "tile_4": "#5A3C18", "tile_8": "#7A5020",
        "tile_16": "#8A5520", "tile_32": "#B87333", "tile_64": "#C88840", "tile_128": "#D4A838",
        "tile_256": "#E0BC50", "tile_512": "#EED068", "tile_1024": "#F5E080", "tile_2048": "#FFFACC",
        "overlay": "#CC1A1008", "scrim": "#991A1008",
    },
    "graffiti_street": {
        "_meta": {"prefix": "gs", "name": "Graffiti Street", "dark": True},
        "background": "#111111", "surface": "#1E1E1E", "surface_variant": "#2E2E2E", "surface_tint": "#333333",
        "primary": "#FFEB00", "primary_dark": "#CCBB00", "secondary": "#0044FF", "tertiary": "#FF2200",
        "on_background": "#FFFFFF", "on_surface": "#FFFFFF", "on_surface_dim": "#888888", "on_primary": "#111111",
        "correct": "#00FF44", "wrong": "#FF2200", "score": "#FFEB00",
        "timer_normal": "#FFEB00", "timer_warning": "#FF2200", "highlight": "#0044FF", "badge": "#FF2200",
        "nav_bar": "#1E1E1E", "nav_selected": "#FFEB00", "nav_unselected": "#666666", "status_bar": "#111111",
        "tile_empty": "#2E2E2E", "tile_2": "#3E3E3E", "tile_4": "#4E4E4E", "tile_8": "#0033CC",
        "tile_16": "#0044FF", "tile_32": "#3366FF", "tile_64": "#FFEB00", "tile_128": "#FFCC00",
        "tile_256": "#FF2200", "tile_512": "#FF5500", "tile_1024": "#00FF44", "tile_2048": "#FFFFFF",
        "overlay": "#CC111111", "scrim": "#99111111",
    },
    "ocean_breeze": {
        "_meta": {"prefix": "ob", "name": "Ocean Breeze", "dark": False},
        "background": "#E8F4FD", "surface": "#FFFFFF", "surface_variant": "#CAF0F8", "surface_tint": "#E0F7FF",
        "primary": "#0077B6", "primary_dark": "#005A8E", "secondary": "#00B4D8", "tertiary": "#0096C7",
        "on_background": "#03045E", "on_surface": "#03045E", "on_surface_dim": "#6B8FAE", "on_primary": "#FFFFFF",
        "correct": "#06D6A0", "wrong": "#EF476F", "score": "#0096C7",
        "timer_normal": "#0077B6", "timer_warning": "#FF9E00", "highlight": "#48CAE4", "badge": "#0077B6",
        "nav_bar": "#FFFFFF", "nav_selected": "#0077B6", "nav_unselected": "#B0C4D8", "status_bar": "#E8F4FD",
        "tile_empty": "#CAF0F8", "tile_2": "#ADE8F4", "tile_4": "#90E0EF", "tile_8": "#48CAE4",
        "tile_16": "#00B4D8", "tile_32": "#0096C7", "tile_64": "#0077B6", "tile_128": "#023E8A",
        "tile_256": "#03045E", "tile_512": "#FFD166", "tile_1024": "#EF476F", "tile_2048": "#06D6A0",
        "overlay": "#80ADE8F4", "scrim": "#500077B6",
    },
    "forest_zen": {
        "_meta": {"prefix": "fz", "name": "Forest Zen", "dark": False},
        "background": "#F1F8E9", "surface": "#FFFFFF", "surface_variant": "#DCEDC8", "surface_tint": "#E8F5E9",
        "primary": "#2E7D32", "primary_dark": "#1B5E20", "secondary": "#66BB6A", "tertiary": "#A67C52",
        "on_background": "#1B3A1C", "on_surface": "#1B3A1C", "on_surface_dim": "#7A9E7B", "on_primary": "#FFFFFF",
        "correct": "#00C853", "wrong": "#D32F2F", "score": "#F9A825",
        "timer_normal": "#2E7D32", "timer_warning": "#FF8F00", "highlight": "#81C784", "badge": "#2E7D32",
        "nav_bar": "#FFFFFF", "nav_selected": "#2E7D32", "nav_unselected": "#9AB89B", "status_bar": "#F1F8E9",
        "tile_empty": "#DCEDC8", "tile_2": "#C5E1A5", "tile_4": "#AED581", "tile_8": "#9CCC65",
        "tile_16": "#8BC34A", "tile_32": "#7CB342", "tile_64": "#558B2F", "tile_128": "#33691E",
        "tile_256": "#2E7D32", "tile_512": "#1B5E20", "tile_1024": "#F9A825", "tile_2048": "#E65100",
        "overlay": "#80DCEDC8", "scrim": "#502E7D32",
    },
    "candy_pop": {
        "_meta": {"prefix": "cp", "name": "Candy Pop", "dark": False},
        "background": "#FFF0F3", "surface": "#FFFFFF", "surface_variant": "#FFCCD5", "surface_tint": "#FFF5F7",
        "primary": "#FF4D6D", "primary_dark": "#C9184A", "secondary": "#A4DEF5", "tertiary": "#FFCB47",
        "on_background": "#590D22", "on_surface": "#590D22", "on_surface_dim": "#B06070", "on_primary": "#FFFFFF",
        "correct": "#06D6A0", "wrong": "#EF476F", "score": "#F4A261",
        "timer_normal": "#FF4D6D", "timer_warning": "#EF476F", "highlight": "#A4DEF5", "badge": "#FF4D6D",
        "nav_bar": "#FFFFFF", "nav_selected": "#FF4D6D", "nav_unselected": "#D4A0B0", "status_bar": "#FFF0F3",
        "tile_empty": "#FFCCD5", "tile_2": "#FFADC0", "tile_4": "#FF8FA8", "tile_8": "#FF6D8E",
        "tile_16": "#FF4D6D", "tile_32": "#E8365A", "tile_64": "#C9184A", "tile_128": "#A4DEF5",
        "tile_256": "#74C2E1", "tile_512": "#FFCB47", "tile_1024": "#F4A261", "tile_2048": "#06D6A0",
        "overlay": "#80FFCCD5", "scrim": "#50FF4D6D",
    },
    "sakura_spring": {
        "_meta": {"prefix": "sk", "name": "Sakura Spring", "dark": False},
        "background": "#FFF5F7", "surface": "#FFFFFF", "surface_variant": "#FFE4EA", "surface_tint": "#FFF0F2",
        "primary": "#E8829A", "primary_dark": "#C96380", "secondary": "#5C8A5F", "tertiary": "#A67C52",
        "on_background": "#3D1C24", "on_surface": "#3D1C24", "on_surface_dim": "#B08898", "on_primary": "#FFFFFF",
        "correct": "#5C8A5F", "wrong": "#C96380", "score": "#A67C52",
        "timer_normal": "#E8829A", "timer_warning": "#C96380", "highlight": "#FFB7C5", "badge": "#E8829A",
        "nav_bar": "#FFFFFF", "nav_selected": "#E8829A", "nav_unselected": "#D4A8B0", "status_bar": "#FFF5F7",
        "tile_empty": "#FFE4EA", "tile_2": "#FFCCD6", "tile_4": "#FFB7C5", "tile_8": "#FF9BB0",
        "tile_16": "#F07A95", "tile_32": "#E8829A", "tile_64": "#C96380", "tile_128": "#5C8A5F",
        "tile_256": "#4A7050", "tile_512": "#A67C52", "tile_1024": "#8B6344", "tile_2048": "#3D1C24",
        "overlay": "#80FFB7C5", "scrim": "#50E8829A",
    },
    "desert_gold": {
        "_meta": {"prefix": "dg", "name": "Desert Gold", "dark": False},
        "background": "#FDF3E7", "surface": "#FFFFFF", "surface_variant": "#F0DFC0", "surface_tint": "#FAF0E0",
        "primary": "#A0522D", "primary_dark": "#7A3B1E", "secondary": "#C8A96E", "tertiary": "#D4AF37",
        "on_background": "#2C1A0E", "on_surface": "#2C1A0E", "on_surface_dim": "#9E7050", "on_primary": "#FDF3E7",
        "correct": "#4CAF50", "wrong": "#D32F2F", "score": "#D4AF37",
        "timer_normal": "#A0522D", "timer_warning": "#D32F2F", "highlight": "#D4AF37", "badge": "#A0522D",
        "nav_bar": "#FFFFFF", "nav_selected": "#A0522D", "nav_unselected": "#C0A080", "status_bar": "#FDF3E7",
        "tile_empty": "#F0DFC0", "tile_2": "#E8D0A0", "tile_4": "#DFC080", "tile_8": "#D4AF37",
        "tile_16": "#C8A96E", "tile_32": "#B8904A", "tile_64": "#A0522D", "tile_128": "#7A3B1E",
        "tile_256": "#5C2810", "tile_512": "#3A1A08", "tile_1024": "#D4AF37", "tile_2048": "#FFFFFF",
        "overlay": "#80F0DFC0", "scrim": "#50A0522D",
    },
    "ice_crystal": {
        "_meta": {"prefix": "ic", "name": "Ice Crystal", "dark": False},
        "background": "#E8F4FD", "surface": "#F0F8FF", "surface_variant": "#D0E8F8", "surface_tint": "#E0F0FF",
        "primary": "#1E88E5", "primary_dark": "#1565C0", "secondary": "#78C8E6", "tertiary": "#B0D8F0",
        "on_background": "#0D2137", "on_surface": "#0D2137", "on_surface_dim": "#7090B0", "on_primary": "#FFFFFF",
        "correct": "#00BCD4", "wrong": "#F06292", "score": "#1E88E5",
        "timer_normal": "#1E88E5", "timer_warning": "#F06292", "highlight": "#78C8E6", "badge": "#1E88E5",
        "nav_bar": "#F0F8FF", "nav_selected": "#1E88E5", "nav_unselected": "#90B8D0", "status_bar": "#E8F4FD",
        "tile_empty": "#D0E8F8", "tile_2": "#B8DCF4", "tile_4": "#9ED0EE", "tile_8": "#78C8E6",
        "tile_16": "#4AB8DE", "tile_32": "#1E88E5", "tile_64": "#1565C0", "tile_128": "#0D47A1",
        "tile_256": "#F06292", "tile_512": "#E91E63", "tile_1024": "#FFFFFF", "tile_2048": "#FFD700",
        "overlay": "#80D0E8F8", "scrim": "#501E88E5",
    },
    "pastel_dream": {
        "_meta": {"prefix": "pd", "name": "Pastel Dream", "dark": False},
        "background": "#FAFAFA", "surface": "#FFFFFF", "surface_variant": "#F0EEF8", "surface_tint": "#F5F3FC",
        "primary": "#9B72CF", "primary_dark": "#7B52AF", "secondary": "#72B7CF", "tertiary": "#CF9B72",
        "on_background": "#2D1B5A", "on_surface": "#2D1B5A", "on_surface_dim": "#9080B0", "on_primary": "#FFFFFF",
        "correct": "#B5EAD7", "wrong": "#FFABAB", "score": "#FFD700",
        "timer_normal": "#9B72CF", "timer_warning": "#FFABAB", "highlight": "#C3B1E1", "badge": "#9B72CF",
        "nav_bar": "#FFFFFF", "nav_selected": "#9B72CF", "nav_unselected": "#C0B0D8", "status_bar": "#FAFAFA",
        "tile_empty": "#F0EEF8", "tile_2": "#FFABAB", "tile_4": "#FFDAAB", "tile_8": "#FFFFAB",
        "tile_16": "#B5EAD7", "tile_32": "#ABE4FF", "tile_64": "#C3B1E1", "tile_128": "#FFB7C5",
        "tile_256": "#9B72CF", "tile_512": "#72B7CF", "tile_1024": "#CF9B72", "tile_2048": "#FFD700",
        "overlay": "#80C3B1E1", "scrim": "#509B72CF",
    },
    "christmas": {
        "_meta": {"prefix": "xm", "name": "Christmas", "dark": False},
        "background": "#F5FFF5", "surface": "#FFFFFF", "surface_variant": "#E8F5E8", "surface_tint": "#F0FFF0",
        "primary": "#CC0000", "primary_dark": "#990000", "secondary": "#165B33", "tertiary": "#D4AF37",
        "on_background": "#1A1A1A", "on_surface": "#1A1A1A", "on_surface_dim": "#708070", "on_primary": "#FFFFFF",
        "correct": "#165B33", "wrong": "#CC0000", "score": "#D4AF37",
        "timer_normal": "#165B33", "timer_warning": "#CC0000", "highlight": "#D4AF37", "badge": "#CC0000",
        "nav_bar": "#FFFFFF", "nav_selected": "#CC0000", "nav_unselected": "#A0B0A0", "status_bar": "#F5FFF5",
        "tile_empty": "#E8F5E8", "tile_2": "#D4EDD4", "tile_4": "#B8DDB8", "tile_8": "#8BC48B",
        "tile_16": "#5A9E5A", "tile_32": "#165B33", "tile_64": "#CC0000", "tile_128": "#990000",
        "tile_256": "#D4AF37", "tile_512": "#B8941F", "tile_1024": "#E8D080", "tile_2048": "#FFFFFF",
        "overlay": "#80E8F5E8", "scrim": "#80165B33",
    },
    "pixel_classic": {
        "_meta": {"prefix": "pc", "name": "Pixel Classic", "dark": True},
        "background": "#1E1E1E", "surface": "#2D2D2D", "surface_variant": "#3D3D3D", "surface_tint": "#353535",
        "primary": "#FF6B35", "primary_dark": "#D4562A", "secondary": "#F7C59F", "tertiary": "#4CC9F0",
        "on_background": "#FFFFFF", "on_surface": "#FFFFFF", "on_surface_dim": "#BDBDBD", "on_primary": "#FFFFFF",
        "correct": "#06D6A0", "wrong": "#FF4757", "score": "#FFBE0B",
        "timer_normal": "#FFBE0B", "timer_warning": "#FF6B35", "highlight": "#4CC9F0", "badge": "#FF6B35",
        "border": "#FF6B35",
        "nav_bar": "#2D2D2D", "nav_selected": "#FF6B35", "nav_unselected": "#707070", "status_bar": "#1E1E1E",
        "tile_empty": "#2D2D2D", "tile_2": "#3D3D3D", "tile_4": "#4D4D4D", "tile_8": "#FF6B35",
        "tile_16": "#D4562A", "tile_32": "#FFBE0B", "tile_64": "#D4A00A", "tile_128": "#4CC9F0",
        "tile_256": "#3BACC8", "tile_512": "#06D6A0", "tile_1024": "#05B386", "tile_2048": "#FFBE0B",
        "overlay": "#CC1E1E1E", "scrim": "#991E1E1E",
    },
    "cartoon_fun": {
        "_meta": {"prefix": "cf", "name": "Cartoon Fun", "dark": False},
        "background": "#FFF9E6", "surface": "#FFFFFF", "surface_variant": "#FFE8CC", "surface_tint": "#FFF0D8",
        "primary": "#FF3333", "primary_dark": "#CC0000", "secondary": "#FFD700", "tertiary": "#33CC33",
        "on_background": "#1A1A1A", "on_surface": "#1A1A1A", "on_surface_dim": "#888888", "on_primary": "#FFFFFF",
        "correct": "#33CC33", "wrong": "#FF3333", "score": "#FFD700",
        "timer_normal": "#FF9900", "timer_warning": "#FF3333", "highlight": "#FFD700", "badge": "#FF3333",
        "nav_bar": "#FFFFFF", "nav_selected": "#FF3333", "nav_unselected": "#BBBBBB", "status_bar": "#FFF9E6",
        "tile_empty": "#FFE8CC", "tile_2": "#FFD0A0", "tile_4": "#FFB870", "tile_8": "#FF9900",
        "tile_16": "#FF6600", "tile_32": "#FF3333", "tile_64": "#CC0000", "tile_128": "#33CC33",
        "tile_256": "#009900", "tile_512": "#FFD700", "tile_1024": "#FF9900", "tile_2048": "#1A1A1A",
        "overlay": "#80FFE8CC", "scrim": "#50FF3333",
    },
    "minimalist_white": {
        "_meta": {"prefix": "mw", "name": "Minimalist White", "dark": False},
        "background": "#F5F5F7", "surface": "#FFFFFF", "surface_variant": "#F0F0F0", "surface_tint": "#FAFAFA",
        "primary": "#0071E3", "primary_dark": "#0055B0", "secondary": "#6E6E73", "tertiary": "#1C1C1E",
        "on_background": "#1C1C1E", "on_surface": "#1C1C1E", "on_surface_dim": "#8E8E93", "on_primary": "#FFFFFF",
        "correct": "#30D158", "wrong": "#FF3B30", "score": "#0071E3",
        "timer_normal": "#0071E3", "timer_warning": "#FF3B30", "highlight": "#0071E3", "badge": "#0071E3",
        "nav_bar": "#FFFFFF", "nav_selected": "#0071E3", "nav_unselected": "#C7C7CC", "status_bar": "#F5F5F7",
        "tile_empty": "#F0F0F0", "tile_2": "#E5E5EA", "tile_4": "#D1D1D6", "tile_8": "#AEAEB2",
        "tile_16": "#8E8E93", "tile_32": "#636366", "tile_64": "#48484A", "tile_128": "#0071E3",
        "tile_256": "#0055B0", "tile_512": "#30D158", "tile_1024": "#FF9F0A", "tile_2048": "#FF3B30",
        "overlay": "#80F0F0F0", "scrim": "#500071E3",
    },
    "paper_craft": {
        "_meta": {"prefix": "ppc", "name": "Paper Craft", "dark": False},
        "background": "#F0E6D0", "surface": "#F8F0E0", "surface_variant": "#E8D8B8", "surface_tint": "#F0E8D8",
        "primary": "#8B5E3C", "primary_dark": "#6B3E1C", "secondary": "#D4936A", "tertiary": "#5B8A4A",
        "on_background": "#2C1A0C", "on_surface": "#2C1A0C", "on_surface_dim": "#9E7850", "on_primary": "#F8F0E0",
        "correct": "#5B8A4A", "wrong": "#C04040", "score": "#8B5E3C",
        "timer_normal": "#8B5E3C", "timer_warning": "#C04040", "highlight": "#D4936A", "badge": "#8B5E3C",
        "nav_bar": "#F8F0E0", "nav_selected": "#8B5E3C", "nav_unselected": "#C0A080", "status_bar": "#F0E6D0",
        "tile_empty": "#E8D8B8", "tile_2": "#F0D8A0", "tile_4": "#E8C880", "tile_8": "#D4B060",
        "tile_16": "#C09040", "tile_32": "#D4936A", "tile_64": "#8B5E3C", "tile_128": "#5B8A4A",
        "tile_256": "#3A6A2A", "tile_512": "#4A6A9A", "tile_1024": "#C04040", "tile_2048": "#2C1A0C",
        "overlay": "#80E8D8B8", "scrim": "#508B5E3C",
    },
    "neon_synthwave": {
        "_meta": {"prefix": "sw", "name": "Neon Synthwave", "dark": True},
        "background": "#0A0010", "surface": "#14002A", "surface_variant": "#1E0040", "surface_tint": "#250050",
        "primary": "#FF00FF", "primary_dark": "#CC00CC", "secondary": "#00FFFF", "tertiary": "#FF6EC7",
        "on_background": "#FFE8FF", "on_surface": "#FFE8FF", "on_surface_dim": "#8040A0", "on_primary": "#FFFFFF",
        "correct": "#00FFFF", "wrong": "#FF0055", "score": "#FFFF00",
        "timer_normal": "#00FFFF", "timer_warning": "#FF0055", "highlight": "#FF00FF", "badge": "#FF00FF",
        "nav_bar": "#14002A", "nav_selected": "#FF00FF", "nav_unselected": "#604080", "status_bar": "#0A0010",
        "tile_empty": "#1E0040", "tile_2": "#2A0060", "tile_4": "#40008A", "tile_8": "#6600BB",
        "tile_16": "#9900DD", "tile_32": "#CC00CC", "tile_64": "#FF00FF", "tile_128": "#00FFFF",
        "tile_256": "#00CCFF", "tile_512": "#FFFF00", "tile_1024": "#FF6EC7", "tile_2048": "#FFFFFF",
        "overlay": "#CC0A0010", "scrim": "#990A0010",
    },
}

TOKEN_ORDER = [
    "background", "surface", "surface_variant", "surface_tint",
    "primary", "primary_dark", "secondary", "tertiary",
    "on_background", "on_surface", "on_surface_dim", "on_primary",
    "correct", "wrong", "score", "timer_normal", "timer_warning", "highlight", "badge",
    "border",  # pixel_classic only
    "nav_bar", "nav_selected", "nav_unselected", "status_bar",
    "tile_empty", "tile_2", "tile_4", "tile_8", "tile_16", "tile_32", "tile_64",
    "tile_128", "tile_256", "tile_512", "tile_1024", "tile_2048",
    "overlay", "scrim",
]

SECTION_COMMENTS = {
    "background":  "    <!-- Background layers -->",
    "primary":     "    <!-- Primary colors -->",
    "on_background": "    <!-- Text colors -->",
    "correct":     "    <!-- Functional colors -->",
    "nav_bar":     "    <!-- Navigation -->",
    "tile_empty":  "    <!-- 2048 tile colors -->",
    "overlay":     "    <!-- Overlays -->",
}


def build_xml(theme_id: str) -> str:
    data = THEMES[theme_id]
    meta = data["_meta"]
    prefix = meta["prefix"]
    name = meta["name"]

    lines = [
        f'<?xml version="1.0" encoding="utf-8"?>',
        f'<!-- res/values/colors_{theme_id}.xml — {name} theme -->',
        f'<resources>',
    ]

    for token in TOKEN_ORDER:
        if token in SECTION_COMMENTS:
            lines.append("")
            lines.append(SECTION_COMMENTS[token])
        if token in data:
            lines.append(f'    <color name="{prefix}_{token}">{data[token]}</color>')

    lines.append("")
    lines.append("</resources>")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate res/values/colors_<theme>.xml")
    parser.add_argument("--theme", help="Theme ID, or 'all' to generate all 22 themes")
    parser.add_argument("--list", action="store_true", help="List all theme IDs")
    parser.add_argument("--output", default="./output", help="Output directory (default: ./output)")
    args = parser.parse_args(argv)

    if args.list:
        print(f"\n{'ID':<22} Name                    Mode")
        print("─" * 55)
        for tid, data in THEMES.items():
            m = data["_meta"]
            mode = "DARK " if m["dark"] else "LIGHT"
            print(f"  {tid:<22} {m['name']:<24} {mode}")
        print(f"\nTotal: {len(THEMES)} themes")
        return 0

    if not args.theme:
        parser.print_help()
        return 1

    out_dir = Path(args.output) / "res" / "values"
    out_dir.mkdir(parents=True, exist_ok=True)

    targets = list(THEMES.keys()) if args.theme == "all" else [args.theme]

    for tid in targets:
        if tid not in THEMES:
            print(f"ERROR: unknown theme '{tid}'. Run --list to see all.", file=sys.stderr)
            return 1
        xml = build_xml(tid)
        out_file = out_dir / f"colors_{tid}.xml"
        out_file.write_text(xml, encoding="utf-8")
        print(f"Generated: {out_file}")

    if len(targets) > 1:
        print(f"\n✓ {len(targets)} theme files written to {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
