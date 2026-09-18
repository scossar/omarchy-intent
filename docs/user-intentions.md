# Omarchy keybindings by user intention

Snapshot: 2026-09-17. Source: `omarchy menu keybindings --print` on this machine, checked against the installed binding definitions, command implementations, and personal overrides.

This document classifies all **227 printed entries (225 distinct shortcuts)**. Original shortcut spelling, labels, and order are preserved. `ALT + TAB` and `SHIFT ALT + TAB` each have both a focus action and a reveal action, so each appears twice. Intentions are interpretive, based on the action's purpose; multiple intentions are not ranked.

## Intention vocabulary

| Intention | Meaning |
| --- | --- |
| Access | Open, launch, show, reveal |
| Movement | Move attention or move an object |
| Removal | Close, dismiss, clear, disable |
| Transformation | Resize, rearrange, scale, change layout |
| State change | Toggle or set modes and properties |
| Transfer | Copy, paste, cut, share, download, capture |
| Adjustment | Raise or lower a continuous value |
| Playback/control | Play, pause, advance, lock, power off |
| Discovery | Show menus, history, bindings, information |

## Classification conventions

- Classify the immediate action or the specific workflow the shortcut starts. Generic menus and control panels are **Access + Discovery**; their later choices can have other intentions. For example, the Power menu does not itself power off, and Share does not immediately send a file.
- Opening/toggling a menu or information panel is treated as **Access + Discovery**, without adding State change and Removal just for its open/closed state. Explicit visibility controls for the scratchpad and top bar include showing, hiding, and state changes.
- Ordinary app launchers are **Access**. Launch-or-focus shortcuts also include **Movement** when the installed implementation explicitly focuses an existing window. Launching an editor, music app, email composer, or post composer does not itself edit, play, send, or publish.
- Moving attention or relocating a window is **Movement**. Swapping windows or moving them into/out of groups also rearranges their layout, so includes **Transformation**.
- Resizing, zooming, and scaling are **Transformation + Adjustment**. Volume and brightness are **Adjustment**, including fixed minimum/maximum values and stepped keyboard brightness. Mode toggles are **State change** rather than automatically treating every numerical or visual change as a state change.
- An intention may apply to one branch of a toggle or conditional action. Notes explain those branches. A disabled device, absent app, missing bar panel, or unsuitable active window can make a binding do nothing.
- Labels are preserved even when implementation is more specific: “Play” and “Pause” both call play/pause; “Brightness minimum” sets 1%; “Toggle menu” opens the menu of toggles. Resize labels describe the supplied binding names, while the actual effect of signed resize steps depends on the layout.

## Complete classification

| Shortcut | Original label | Intentions | Action / rationale |
| --- | --- | --- | --- |
| `SUPER + K` | Keybindings | Access; Discovery | Open searchable shortcut help. |
| `SUPER + SPACE` | Omarchy menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER + RETURN` | Terminal | Access | Open the named application or entry point. |
| `SUPER SHIFT + F` | File manager | Access | Open the named application or entry point. |
| `SUPER + ESCAPE` | System menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER SHIFT CTRL + SPACE` | Theme menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER + F` | Full screen | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER ALT + F` | Full width | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER + W` | Close window | Removal | Close the current window or all windows. |
| `CTRL ALT + DELETE` | Close all windows | Removal | Close the current window or all windows. |
| `SUPER CTRL + L` | Lock system | Playback/control; State change | Lock the session. |
| `SUPER + T` | Toggle window floating/tiling | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER + J` | Toggle window split | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER + O` | Pop window out (float & pin) | State change; Transformation; Movement | Toggle floating/pinned presentation; popping out also resizes and centers the window. |
| `SUPER + C` | Universal copy | Transfer | Transfer content through the clipboard. |
| `SUPER + V` | Universal paste | Transfer | Transfer content through the clipboard. |
| `SUPER + X` | Universal cut | Transfer; Removal | Cut selected content into the clipboard, removing it from its current location. |
| `SUPER CTRL + V` | Clipboard manager | Access; Discovery | Open clipboard history to find and select an item; selection performs the transfer. |
| `SUPER CTRL + E` | Emojis | Access; Discovery | Open the emoji picker; inserting/copying a choice is a later action. |
| `SUPER + PRINT` | Color picker | Transfer; Discovery | Inspect a screen color and copy its value; pressing again can cancel the picker. |
| `PRINT` | Screenshot | Transfer | Begin interactive screen capture. |
| `ALT + PRINT` | Screenrecording | Transfer; Playback/control; Access; Discovery | Stop an active recording, otherwise open recording options to begin a capture. |
| `SUPER ALT + RETURN` | Tmux | Access | Open the named application or entry point. |
| `SUPER CTRL + RETURN` | Herdr | Access | Open the named application or entry point. |
| `SUPER SHIFT ALT + B` | Browser (private) | Access | Open a browser in private mode; the shortcut's main intent is launching it. |
| `SUPER SHIFT + B` | Browser | Access | Open the named application or entry point. |
| `SUPER SHIFT ALT + F` | File manager (cwd) | Access | Open the named application or entry point. |
| `SUPER + 0` | Switch to workspace 10 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 1` | Switch to workspace 1 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 2` | Switch to workspace 2 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 3` | Switch to workspace 3 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 4` | Switch to workspace 4 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 5` | Switch to workspace 5 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 6` | Switch to workspace 6 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 7` | Switch to workspace 7 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 8` | Switch to workspace 8 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + 9` | Switch to workspace 9 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER CTRL + TAB` | Former workspace | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER SHIFT + TAB` | Previous workspace | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + TAB` | Next workspace | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER SHIFT + 0` | Move window to workspace 10 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 1` | Move window to workspace 1 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 2` | Move window to workspace 2 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 3` | Move window to workspace 3 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 4` | Move window to workspace 4 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 5` | Move window to workspace 5 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 6` | Move window to workspace 6 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 7` | Move window to workspace 7 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 8` | Move window to workspace 8 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + 9` | Move window to workspace 9 | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT ALT + 0` | Move window silently to workspace 10 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 1` | Move window silently to workspace 1 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 2` | Move window silently to workspace 2 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 3` | Move window silently to workspace 3 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 4` | Move window silently to workspace 4 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 5` | Move window silently to workspace 5 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 6` | Move window silently to workspace 6 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 7` | Move window silently to workspace 7 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 8` | Move window silently to workspace 8 | Movement | Move the window without following it. |
| `SUPER SHIFT ALT + 9` | Move window silently to workspace 9 | Movement | Move the window without following it. |
| `SUPER SHIFT + DOWN` | Swap window down | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER SHIFT + LEFT` | Swap window to the left | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER SHIFT + RIGHT` | Swap window to the right | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER SHIFT + UP` | Swap window up | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `ALT + TAB` | Focus on next window | Movement | Move attention to another window, workspace, group member or monitor. |
| `CTRL ALT + TAB` | Focus on next monitor | Movement | Move attention to another window, workspace, group member or monitor. |
| `SHIFT ALT + TAB` | Focus on previous window | Movement | Move attention to another window, workspace, group member or monitor. |
| `SHIFT CTRL ALT + TAB` | Focus on previous monitor | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + DOWN` | Focus on below window | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + LEFT` | Focus on left window | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + RIGHT` | Focus on right window | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + UP` | Focus on above window | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + LEFT MOUSE BUTTON` | Move window | Movement | Move the window or workspace to another position or destination. |
| `SUPER + RIGHT MOUSE BUTTON` | Resize window | Transformation; Adjustment | Drag to change window dimensions. |
| `SUPER ALT + MINUS` | Expand window left a little | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER CTRL + MINUS` | Expand window left a lot | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER + MINUS` | Expand window left | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT ALT + EQUAL` | Expand window down a little | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT CTRL + EQUAL` | Expand window down a lot | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT + EQUAL` | Expand window down | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER ALT + EQUAL` | Shrink window left a little | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER CTRL + EQUAL` | Shrink window left a lot | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER + EQUAL` | Shrink window left | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT ALT + MINUS` | Shrink window up a little | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT CTRL + MINUS` | Shrink window up a lot | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER SHIFT + MINUS` | Shrink window up | Transformation; Adjustment | Resize by a numeric step: little = 25, normal = 100, lot = 300; direction depends on layout. |
| `SUPER ALT + S` | Move window to scratchpad | Movement | Move the window without following it. |
| `SUPER + S` | Toggle scratchpad | Access; Removal; State change | Show or hide the scratchpad workspace. |
| `SUPER ALT + COMMA` | Invoke last notification | Access; Removal | Invoke the newest popup's default action, then dismiss it; the action is supplied by the notifying app. |
| `SUPER + COMMA` | Dismiss last notification | Removal | Dismiss the notification(s) or clear reminders. |
| `SUPER CTRL + COMMA` | Toggle silencing notifications | State change; Removal | Enable or disable notification silencing; suppresses popups when enabled. |
| `SUPER SHIFT ALT + COMMA` | Open notification history | Access; Discovery | Replay recent notifications from history. |
| `SUPER SHIFT + COMMA` | Dismiss all notifications | Removal | Dismiss the notification(s) or clear reminders. |
| `SUPER + BACKSPACE` | Toggle window transparency | State change | Toggle a visual property or display mode. |
| `SUPER CTRL + N` | Toggle nightlight | State change | Toggle a visual property or display mode. |
| `SUPER CTRL + I` | Toggle locking on idle | State change; Removal | Enable or disable automatic idle locking. |
| `SHIFT ALT + D` | Download Video from Web App | Transfer | Download web-app media or copy its URL; provided as a web-app shortcut by the listing. |
| `SHIFT ALT + L` | Copy URL from Web App | Transfer | Download web-app media or copy its URL; provided as a web-app shortcut by the listing. |
| `SUPER ALT + BRACKETLEFT` | Make webcam overlay smaller | Transformation; Adjustment | Change the capture webcam overlay size. |
| `SUPER ALT + BRACKETRIGHT` | Make webcam overlay larger | Transformation; Adjustment | Change the capture webcam overlay size. |
| `SUPER ALT + Home` | Save window width | State change | Store the current width as the saved preference for this app and workspace. |
| `SUPER ALT + SLASH` | Monitor scaling down | Transformation; Adjustment | Change display scale or zoom; reset returns zoom to 1. |
| `SUPER ALT + SPACE` | Apps menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + 1` | Bar panel 1 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 2` | Bar panel 2 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 3` | Bar panel 3 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 4` | Bar panel 4 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 5` | Bar panel 5 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 6` | Bar panel 6 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 7` | Bar panel 7 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 8` | Bar panel 8 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + 9` | Bar panel 9 | Access; Discovery | Toggle the numbered panel in the bar's right section; does nothing if that panel is absent. |
| `SUPER CTRL + A` | Audio | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL ALT + B` | Show battery remaining | Access; Discovery | Display the requested status or information. |
| `SUPER CTRL ALT + D` | Calendar | Access; Discovery | Open/toggle the shell clock/calendar panel. |
| `SUPER CTRL ALT + Delete` | Toggle laptop display mirroring | State change; Transformation | Toggle the monitor mirroring configuration. |
| `SUPER CTRL ALT + R` | Show reminders | Access; Discovery | Display the requested status or information. |
| `SUPER CTRL ALT + T` | Show time | Access; Discovery | Display the requested status or information. |
| `SUPER CTRL ALT + W` | Toggle weather | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL ALT + Z` | Reset zoom | Transformation; Adjustment | Change display scale or zoom; reset returns zoom to 1. |
| `SUPER CTRL + BACKSPACE` | Toggle single-window square aspect | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER CTRL + B` | Bluetooth | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL + C` | Capture menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + D` | Display | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL + Delete` | Toggle laptop display | State change; Removal | Enable or disable the laptop's built-in display. |
| `SUPER CTRL + F` | Tiled full screen | State change; Transformation | Toggle client fullscreen while keeping the compositor's tiled layout; changes application presentation. |
| `SUPER CTRL + H` | Hardware menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + O` | Toggle menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + PERIOD` | Transcode | Access; Discovery; Transformation; Transfer | Choose a file, format and resolution; convert the media and copy the output file URI to the clipboard. |
| `SUPER CTRL + P` | Power | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL + PRINT` | Extract text (OCR) from screenshot | Transfer; Transformation | Capture a region, convert its image text into text, and copy it to the clipboard. |
| `SUPER CTRL + Q` | Calculator | Access | Open the calculator. |
| `SUPER CTRL + R` | Set reminder | Access; Discovery | Open the reminder-setting menu; saving a reminder requires a subsequent choice. |
| `SUPER CTRL + SPACE` | Background switcher | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + S` | Share | Access; Discovery | Open the named menu to discover and choose an action. |
| `SUPER CTRL + T` | Activity | Access; Discovery | Open btop to inspect system activity. |
| `SUPER CTRL + W` | Network | Access; Discovery | Open/toggle the corresponding information and controls panel. |
| `SUPER CTRL + Z` | Zoom in | Transformation; Adjustment | Change display scale or zoom; reset returns zoom to 1. |
| `SUPER + Home` | Restore window width | Transformation; Adjustment | Resize toward the saved width. |
| `SUPER + L` | Toggle workspace layout | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER + P` | Pseudo window | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER SHIFT + A` | ChatGPT here | Access; Movement | Move and focus the most recently used matching window on this workspace, or launch the app. |
| `SUPER SHIFT ALT + A` | Grok | Access | Open the named application or entry point. |
| `SUPER SHIFT ALT + DOWN` | Move workspace to down monitor | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT ALT + E` | New email | Access | Open the named application or entry point. |
| `SUPER SHIFT ALT + G` | WhatsApp | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT ALT + LEFT` | Move workspace to left monitor | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT ALT + M` | Music TUI | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT ALT + RIGHT` | Move workspace to right monitor | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT ALT + UP` | Move workspace to up monitor | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT ALT + X` | X Post | Access | Open the named application or entry point. |
| `SUPER SHIFT + BACKSPACE` | Toggle window gaps | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER SHIFT + C` | Calendar | Access | Open the HEY Calendar web app. |
| `SUPER SHIFT CTRL + A` | Agent | Access; Discovery | Open the agent picker. |
| `SUPER SHIFT CTRL + D` | Word lookup | Access; Discovery | Open the local spelling/word lookup panel. |
| `SUPER SHIFT CTRL + G` | Google Messages | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT CTRL + LEFT` | Floating window to top left | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT CTRL + R` | Clear reminders | Removal | Dismiss the notification(s) or clear reminders. |
| `SUPER SHIFT CTRL + RIGHT` | Floating window to top right | Movement | Move the window or workspace to another position or destination. |
| `SUPER SHIFT + D` | Docker | Access | Open the named application or entry point. |
| `SUPER SHIFT + E` | Email | Access | Open the named application or entry point. |
| `SUPER SHIFT + G` | Signal | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT + M` | Music | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT + N` | Editor | Access | Open the named application or entry point. |
| `SUPER SHIFT + O` | Obsidian here | Access; Movement | Move and focus the most recently used matching window on this workspace, or launch the app. |
| `SUPER SHIFT + P` | Google Photos | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT + RETURN` | Floating terminal | Access | Open the named application or entry point. |
| `SUPER SHIFT + S` | Google Maps | Access; Movement | Launch the app, or move attention to an existing matching window. |
| `SUPER SHIFT + SLASH` | Passwords | Access | Open the named application or entry point. |
| `SUPER SHIFT + SPACE` | Toggle top bar | Access; Removal; State change | Show or hide the top bar. |
| `SUPER SHIFT + W` | Omawrite | Access | Open the named application or entry point. |
| `SUPER SHIFT + X` | X | Access | Open the named application or entry point. |
| `SUPER SHIFT + Y` | YouTube | Access | Open the named application or entry point. |
| `SUPER + SLASH` | Monitor scaling up | Transformation; Adjustment | Change display scale or zoom; reset returns zoom to 1. |
| `SUPER ALT + 1` | Switch to group window 1 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + 2` | Switch to group window 2 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + 3` | Switch to group window 3 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + 4` | Switch to group window 4 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + 5` | Switch to group window 5 | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + DOWN` | Move window to group on bottom | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER ALT + G` | Move active window out of group | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER ALT + LEFT` | Move window to group on left | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER ALT + mouse_down` | Next window in group | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + mouse_up` | Previous window in group | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + RIGHT` | Move window to group on right | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER ALT + TAB` | Next window in group | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER ALT + UP` | Move window to group on top | Movement; Transformation | Reposition the window and rearrange its layout or group membership. |
| `SUPER CTRL + LEFT` | Move grouped window focus left | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER CTRL + RIGHT` | Move grouped window focus right | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + G` | Toggle window grouping | State change; Transformation | Change the window or workspace layout/geometry mode. |
| `SUPER SHIFT ALT + TAB` | Previous window in group | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + mouse_down` | Scroll active workspace forward | Movement | Move attention to another window, workspace, group member or monitor. |
| `SUPER + mouse_up` | Scroll active workspace backward | Movement | Move attention to another window, workspace, group member or monitor. |
| `ALT + TAB` | Reveal active window on top | Access | Raise the active window to reveal it above overlapping windows. |
| `SHIFT ALT + TAB` | Reveal active window on top | Access | Raise the active window to reveal it above overlapping windows. |
| `ALT + XF86AudioLowerVolume` | Volume down precise | Adjustment | Raise or lower volume or brightness. |
| `ALT + XF86AudioPlay` | Next track | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `ALT + XF86AudioRaiseVolume` | Volume up precise | Adjustment | Raise or lower volume or brightness. |
| `ALT + XF86MonBrightnessDown` | Brightness down precise | Adjustment | Raise or lower volume or brightness. |
| `ALT + XF86MonBrightnessUp` | Brightness up precise | Adjustment | Raise or lower volume or brightness. |
| `SHIFT ALT + XF86AudioPlay` | Previous track | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `SHIFT + XF86AudioMute` | Switch audio output | State change; Playback/control | Change the audio output device or the media source controlled by playback shortcuts. |
| `SHIFT + XF86AudioPause` | Switch media source | State change; Playback/control | Change the audio output device or the media source controlled by playback shortcuts. |
| `SHIFT + XF86AudioPlay` | Switch media source | State change; Playback/control | Change the audio output device or the media source controlled by playback shortcuts. |
| `SHIFT + XF86MonBrightnessDown` | Brightness minimum | Adjustment | Set display brightness to 1%. |
| `SHIFT + XF86MonBrightnessUp` | Brightness maximum | Adjustment | Set display brightness to 100%. |
| `XF86AudioLowerVolume` | Volume down | Adjustment | Raise or lower volume or brightness. |
| `XF86AudioMicMute` | Mute microphone | State change; Playback/control | Toggle microphone or output mute. |
| `XF86AudioMute` | Mute | State change; Playback/control | Toggle microphone or output mute. |
| `XF86AudioNext` | Next track | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `XF86AudioPause` | Pause | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `XF86AudioPlay` | Play | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `XF86AudioPrev` | Previous track | Playback/control | Control media playback; both Play and Pause bindings actually toggle play/pause. |
| `XF86AudioRaiseVolume` | Volume up | Adjustment | Raise or lower volume or brightness. |
| `XF86Calculator` | Calculator | Access | Open the calculator. |
| `XF86Eject` | Eject media | Removal; Playback/control | Eject removable media. |
| `XF86KbdBrightnessDown` | Keyboard brightness down | Adjustment | Raise or lower volume or brightness. |
| `XF86KbdBrightnessUp` | Keyboard brightness up | Adjustment | Raise or lower volume or brightness. |
| `XF86KbdLightOnOff` | Keyboard backlight cycle | Adjustment | Advance keyboard brightness by a step, wrapping to zero above the maximum. |
| `XF86MonBrightnessDown` | Brightness down | Adjustment | Raise or lower volume or brightness. |
| `XF86MonBrightnessUp` | Brightness up | Adjustment | Raise or lower volume or brightness. |
| `XF86PowerOff` | Power menu | Access; Discovery | Open the named menu to discover and choose an action. |
| `XF86TouchpadOff` | Disable touchpad | Removal; State change | Disable touchpad input. |
| `XF86TouchpadOn` | Enable touchpad | State change | Enable touchpad input or toggle whether it is enabled. |
| `XF86TouchpadToggle` | Toggle touchpad | State change | Enable touchpad input or toggle whether it is enabled. |
| `SUPER ALT + K` | Tmux keybindings | Access; Discovery | Open searchable shortcut help. |
| `SUPER CTRL + K` | Herdr keybindings | Access; Discovery | Open searchable shortcut help. |

## Coverage and implementation sources

The table covers exactly the printed listing, including its two web-app shortcuts appended by the listing command. It is a snapshot of this machine, including custom bindings, rather than a universal inventory for every Omarchy installation.

The local config also contains an **Obsidian vault search** binding on `SUPER + SHIFT + code:201` (the Copilot key), but the command did not print it in this snapshot. Its classification is **Access + Discovery**. It is noted here separately rather than inserted into the 227-row inventory. Temporary capture-selection bindings and conditionally installed dictation bindings are likewise outside this printed snapshot.

Installed sources inspected:

- [Keybinding listing implementation](/usr/share/omarchy/bin/omarchy-menu-keybindings) — collection, rendering, and appended web-app shortcuts.
- [Personal bindings](/home/scossar/.config/hypr/bindings.lua) — app-here behavior, floating terminal, word lookup, and floating-window placement.
- [Application bindings](/usr/share/omarchy/default/hypr/bindings/applications.lua), [tiling bindings](/usr/share/omarchy/default/hypr/bindings/tiling.lua), [utility bindings](/usr/share/omarchy/default/hypr/bindings/utilities.lua), [clipboard bindings](/usr/share/omarchy/default/hypr/bindings/clipboard.lua), and [media bindings](/usr/share/omarchy/default/hypr/bindings/media.lua) — concrete commands and dispatchers.
- [Window pop-out](/usr/share/omarchy/bin/omarchy-hyprland-window-pop), [saved window width](/usr/share/omarchy/bin/omarchy-hyprland-window-width), and [tiled fullscreen](/usr/share/omarchy/bin/omarchy-hyprland-window-tiled-fullscreen-toggle) — compound window operations.
- [Transcode](/usr/share/omarchy/bin/omarchy-transcode), [keyboard brightness](/usr/share/omarchy/bin/omarchy-brightness-keyboard), and [weather panel](/usr/share/omarchy/bin/omarchy-notification-weather) — behavior beyond the displayed label.
- [Notification service](/usr/share/omarchy/shell/plugins/notifications/Service.qml) — history, dismissal, and invoking the last notification's default action.
- [Launch or focus](/usr/share/omarchy/bin/omarchy-launch-or-focus), [web-app launch or focus](/usr/share/omarchy/bin/omarchy-launch-or-focus-webapp), [Spotify launcher](/usr/share/omarchy/bin/omarchy-launch-spotify), and [Signal launcher](/usr/share/omarchy/bin/omarchy-launch-signal) — conditional focus behavior.

## Intention counts

Counts refer to table entries, not distinct shortcuts. An entry can contribute to multiple intentions.

| Intention | Entries |
| --- | ---: |
| Access | 76 |
| Movement | 81 |
| Removal | 14 |
| Transformation | 43 |
| State change | 29 |
| Transfer | 10 |
| Adjustment | 33 |
| Playback/control | 14 |
| Discovery | 42 |

