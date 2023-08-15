from pathlib import Path

base_dir = Path(__file__).parent.parent
template_file = base_dir / "templates" / "base-light-color-theme.json"

with open(template_file) as f:
    light_theme_base = f.readlines()

dark_theme_file = base_dir / "themes" / "gari-dark-color-theme.json"

with open(dark_theme_file) as f:
    dark_theme = f.readlines()

output_file = base_dir / "themes" / "gari-light-color-theme.json"


def replace_line(line):
    return (
        line.replace("#666", "#999")  # gray
        .replace("#ddd", "#333")  # foreground
        .replace("#ae8", "#080")  # green
        .replace("#dbf", "#b0f")  # purple
        .replace("#ee8", "#f60")  # yellow
        .replace("#fb8", "#a00")  # orange
        .replace("#6df", "#00f")  # blue
        .replace("#8ff", "#04f")  # cyan
        .replace("#f44", "#f00")  # red
    )


with open(output_file, "w") as f:
    f.writelines(light_theme_base[:-1])
    f.writelines([replace_line(line) for line in dark_theme[143:]])
