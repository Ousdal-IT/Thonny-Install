# Screenshot capture plan

M0.16 defines the minimum useful screenshot set for the Ousdal IT guide.

The guide must remain fully usable without images. Screenshots are recognition aids, not instructions by themselves.

## Capture rules

- Capture from a clean test account or VM with no personal files, names, email addresses, bookmarks, notifications or unrelated applications visible.
- Use the current stable Thonny release at capture time.
- Record the exact OS version and Thonny version in `manifest.json`.
- Do not crop away information the reader needs to recognise the window.
- Crop away irrelevant desktop space when it adds no useful context.
- Prefer PNG for UI screenshots.
- Do not fabricate, redraw or AI-generate application or operating-system UI.
- A second person or a separate review pass must check privacy and step accuracy before `status` becomes `verified`.
- Mark an image `stale` when the current UI no longer substantially matches it.

## Minimum set

| ID | Platform | Guide step | What the image must prove |
|---|---|---|---|
| win-download | Windows | Download | The correct Windows download choice on the official Thonny site |
| win-installer | Windows | Install | The real Thonny installer window and the normal forward action |
| win-launch | Windows | Start | How Thonny appears when opened successfully |
| mac-download | macOS | Download | The correct Mac download choice, including architecture context |
| mac-installer | macOS | Install | The real macOS package installer |
| mac-launch | macOS | Start | Thonny visible after installation |
| linux-terminal | Linux | Install | The official installer command entered in a terminal, with no personal shell data visible |
| linux-launch | Linux | Start | Thonny visible after installation |
| thonny-editor | Neutral | First program | Where to type `print("Hei!")` / `print("Hello!")` |
| thonny-run | Neutral | Run | Run/F5 and the expected output visible in Shell |

## Optional images

Only add an optional screenshot when it resolves a recurring point of confusion. Examples are Windows ARM64 identification or a legitimate macOS security dialog. Do not build a gallery of every installer screen.

## Review checklist

Before changing an entry to `verified`, confirm all of these:

1. The screenshot came from the recorded source.
2. It still matches the current guide step.
3. OS and Thonny versions are recorded.
4. No personal or identifying information is visible.
5. Alt text tells the reader what to look for.
6. The guide still makes sense if the image fails to load.
7. The file is registered in the manifest and passes CI.
