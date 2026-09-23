#!/bin/sh
# Pull publicly available reference images (Wikipedia/Wikimedia Commons) into
# references/<theme>/ for local comparison. NOT committed to the repo — see
# references/README.md for why these stay as links, not copies, upstream.
# Run from the repo root: sh references/fetch-references.sh
set -e

# Wikimedia rejects anonymous/burst requests with 429 — set a UA and pace requests.
WGET="wget -U ftl-themes-ref-collector/1.0 -q --wait=1 --random-wait -O"

# aperture, aqua, barbie, bloomberg already downloaded — removed from this run.

mkdir -p "references/blue-future"
$WGET "references/blue-future/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/4/4b/MOCR_2_Building_30_JSC_angle_view.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/blue-future/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/3/36/MOCR_2_Building_30_JSC_forward_view.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/blue-future/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/1/13/Chris_Kraft_and_Walt_Williams.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/cue-lab"
$WGET "references/cue-lab/01.png" "https://upload.wikimedia.org/wikipedia/en/1/11/QLab_5_logo_2025.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/cyber-goth"
$WGET "references/cyber-goth/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/4/43/Portrait_of_a_31-year_old_woman_dressed_in_a_cyberpunk_industrial_outfit%2C_photographed_in_2013.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/cyber-goth/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/7/73/BathingSuit1920s.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/cyber-goth/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/a/a0/Cybergoths.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/death-star"
$WGET "references/death-star/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/3/3a/MiniMimas.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/death-star/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/c/c8/Mimas_PIA06258.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/death-star/03.jpeg" "https://upload.wikimedia.org/wikipedia/en/e/ee/Vaderrots.jpeg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/hot-wheels"
$WGET "references/hot-wheels/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/d/d0/2011_Greater_Los_Angeles_Auto_Show_IMG_4306_%286870793840%29.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/hot-wheels/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/e/ec/Hot_wheels.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/hot-wheels/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/0/09/HOT_WHEELS_MAINLINE_2013_-_CHEVY_CAMARO.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/imac-g3"
$WGET "references/imac-g3/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/6/64/Imac_G3_Bondi_Blue_side.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/imac-g3/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_Newton_eMate_300_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/imac-g3/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/5/52/Imac_G3_Graphite_side.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/lcars"
$WGET "references/lcars/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/4/4c/LCARS_panel_from_Star_Trek_Voyager_at_Filmwelt_Center.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/lcars/02.jpg" "https://upload.wikimedia.org/wikipedia/en/8/88/Star_Trek_PADD.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/lego-classic"
$WGET "references/lego-classic/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/c/cd/Lego_Classic_Space_diorama_03.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/lego-classic/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/7/72/Lego_Alien_Raumschiff.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/lego-classic/03.png" "https://upload.wikimedia.org/wikipedia/en/8/84/Classic_Space_logo.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/material"
$WGET "references/material/01.png" "https://upload.wikimedia.org/wikipedia/commons/d/d4/Material_you_light.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/matrix"
$WGET "references/matrix/01.png" "https://upload.wikimedia.org/wikipedia/commons/b/ba/Anonymous_Hacker.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/matrix/02.gif" "https://upload.wikimedia.org/wikipedia/commons/c/c3/Digital_rain_animation_medium_letters_2_clear.gif?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/matrix/03.gif" "https://upload.wikimedia.org/wikipedia/commons/9/9d/Digital_rain_animation_medium_letters_2_shine.gif?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/msdos"
$WGET "references/msdos/01.png" "https://upload.wikimedia.org/wikipedia/en/7/77/Stereo_Shell_S410.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/msdos/02.png" "https://upload.wikimedia.org/wikipedia/en/4/4c/NortonCommanderWin.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/msdos/03.png" "https://upload.wikimedia.org/wikipedia/en/1/1b/Norton_Commander_5.51.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/nerv"
$WGET "references/nerv/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/5/52/STGCC_cosplayers_of_Asuka_Langley_Soryu_and_Rei_Ayanami_20150912.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/nerv/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/d/d3/Studio_GAINAX.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/nerv/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/2/27/EC1835_C_cut.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/pipboy"
$WGET "references/pipboy/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/c/c8/New_York_Comic_Con_2016_-_Wanderer_%2830228494775%29.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/steampunk"
$WGET "references/steampunk/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/2/2a/Sortie_de_l%27op%C3%A9ra_en_l%27an_2000-2.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/steampunk/02.jpg" "https://upload.wikimedia.org/wikipedia/commons/f/f2/Nautilus_Neuville.JPG?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/steampunk/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/c/c5/Aerial_house3.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/vaporwave"
$WGET "references/vaporwave/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/9/9a/Yunglean_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/vaporwave/02.png" "https://upload.wikimedia.org/wikipedia/commons/3/31/Wikiwave_00000.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/vaporwave/03.jpg" "https://upload.wikimedia.org/wikipedia/commons/d/de/Nine_lives_vaporwave.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/win7-aero"
$WGET "references/win7-aero/01.png" "https://upload.wikimedia.org/wikipedia/commons/4/47/Plasma_Workspaces.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/win7-aero/02.png" "https://upload.wikimedia.org/wikipedia/commons/f/f1/Segoe_UI_Revision_Differences.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/win7-aero/03.png" "https://upload.wikimedia.org/wikipedia/en/2/25/ThumbnailWin7.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/winamp-classic"
$WGET "references/winamp-classic/01.jpg" "https://upload.wikimedia.org/wikipedia/commons/d/d3/Milkdrop_Spikeball.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/winamp-classic/02.png" "https://upload.wikimedia.org/wikipedia/en/0/0b/Winampmain.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/winamp-classic/03.png" "https://upload.wikimedia.org/wikipedia/en/6/6d/WinAmp_5.9.2%2C_Windows_10.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/windows95"
$WGET "references/windows95/01.png" "https://upload.wikimedia.org/wikipedia/commons/5/57/323boot.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/windows95/02.png" "https://upload.wikimedia.org/wikipedia/commons/c/c1/About_box_Windows_3.10.07200022_%28EN%29.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/windows95/03.png" "https://upload.wikimedia.org/wikipedia/commons/4/4c/About_box_Windows_4.00.222_%28DE%29_%281994-11-09%29.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/winxp-luna"
$WGET "references/winxp-luna/01.png" "https://upload.wikimedia.org/wikipedia/en/1/10/Windows-XP-Beta-2-Luna.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/winxp-luna/02.png" "https://upload.wikimedia.org/wikipedia/en/6/6f/Windows-XP-build-2419-Blue-Lagoon.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/winxp-luna/03.png" "https://upload.wikimedia.org/wikipedia/en/a/a8/Windows-XP-build-2419-Chartreuse-Mongoose.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

mkdir -p "references/wmp11"
$WGET "references/wmp11/01.png" "https://upload.wikimedia.org/wikipedia/en/c/cf/WMP_12_on_Windows_7.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/wmp11/02.png" "https://upload.wikimedia.org/wikipedia/en/8/85/Windows_Media_Player_12%2C_under_Windows_11.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"
$WGET "references/wmp11/03.jpg" "https://upload.wikimedia.org/wikipedia/en/6/62/Media_Player_v5.0_%28Microsoft%29.jpg?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=original"

# No usable free-licensed images found automatically for: tron
# (Wikipedia/Commons had none indexed under that article at fetch time).
# TRON: Legacy reference is design-blog work (gmunk.com, hudsandguis.com) — not
# freely licensed; source manually if you have rights to use it, or keep as a link.

# alienware, aperture (theportalwiki), bloomberg (bloomberg.com blog), hot-wheels
# (mattel.com), lego-classic (lego.com/brickipedia), nerv (fontsinuse.com), msdos
# (ilyabirman.net) also have no Commons/Wikipedia-hosted free images for their best
# reference material — those best references are the vendor/fan sites already
# linked in references/README.md, which aren't freely licensed for redistribution.
