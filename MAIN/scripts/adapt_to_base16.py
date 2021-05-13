import os
import sys
import yaml
import json

if len(sys.argv) > 1:
    base16_path = os.path.expanduser(sys.argv[1])
    base16 = yaml.load(open(base16_path, "r").read(), Loader=yaml.FullLoader)
    base16_name = os.path.splitext(os.path.basename(base16_path))[0]

    base16_theme_path = os.path.expanduser("~/MAIN/themes/base16.json")
    base16_theme = {
        "polybar.1_bg": "#" + base16["base00"],
        "polybar.1_fg": "#" + base16["base05"],
        "polybar.1_widget_bg": base16["base01"],
        "polybar.1_accent": "#" + base16["base0C"],
        "polybar.1_empty": "#" + base16["base01"],
        "polybar.1_error": "#" + base16["base08"],
        "polybar.1_warn": "#" + base16["base09"],
        "polybar.1_success": "#" + base16["base0B"],
        "polybar.1_icon": "#" + base16["base0A"],
        
        "polybar.2_bg": "#" + base16["base00"],
        "polybar.2_fg": "#" + base16["base05"],
        "polybar.2_focused": "#" + base16["base0B"],
        "polybar.2_occupied": "#" + base16["base04"],
        "polybar.2_empty": "#" + base16["base02"],

        "bspwm.focused_border_color": "#" + base16["base05"],
        "bspwm.normal_border_color": "#" + base16["base01"],
        "bspwm.active_border_color": "#" + base16["base02"],
        "bspwm.urgent_border_color": "#" + base16["base08"],
        "bspwm.presel_feedback_color": "#" + base16["base05"],

        "rofi.bottom-bg": "#" + base16["base00"],
        "rofi.bottom-fg": "#" + base16["base05"],
        "rofi.bottom-bg-focused": "#" + base16["base0C"],
        "rofi.bottom-fg-focused": "#" + base16["base00"],
        "rofi.bottom-prompt-fg": "#" + base16["base0E"],

        "alacritty.colorscheme": "~/.config/alacritty/colors/base16-" + base16_name + ".yml",

        "dunst.background": "#" + base16["base00"],
        "dunst.foreground": "#" + base16["base05"],
        "dunst.frame_color": "#" + base16["base0E"],
    }

    os.system("base16-builder build -t ~/repos/base16-builder/templates/alacritty/ -s {} -o ~/.config/alacritty/colors/ -d".format(base16_path))

    if len(sys.argv) == 3:
        base16_theme["neovim.colorscheme"] = sys.argv[2]
    else:
        os.system("base16-builder build -t ~/repos/base16-builder/templates/vim/ -s {} -o ~/MAIN/tmp/vim_colors/colors/ -d".format(base16_path))
        base16_theme["neovim.colorscheme"] = "base16-" + base16_name

    open(base16_theme_path, "w").write(json.dumps(base16_theme, indent=4))

    os.system("exconman load {}".format(base16_theme_path))
    os.system("sh ~/MAIN/scripts/restart_all.sh")
