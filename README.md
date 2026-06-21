Maya Transform & Visibility Manager

An artist-facing production utility for Autodesk Maya that provides a centralized interface to manage scene meshes. This tool optimizes layout workflows by replacing repetitive Channel Box operations with unified visibility toggles and channel locking controls.

## 🚀 Features
* **Live Scene Scanning:** Instantly enumerates all mesh nodes in the active Maya scene.
* **Batch Visibility Control:** Quick checkbox toggles to hide/show scene geometry.
* **Unified Channel Locking:** One-click toggling to instantly lock or unlock Translate, Rotate, and Scale attributes simultaneously.
* [coming soon: **Clean & Modern UI:** Built natively with PySide6 to dock smoothly within the Maya ecosystem.]

## 🛠️ Technical Details
* **Language:** Python 3
* **Libraries:** PySide6, Maya `cmds`, `shiboken6`, `OpenMayaUI`
* **Pattern:** Event-driven UI  [coming soon: signal blocking (`blockSignals`) to handle seamless data synchronization between Maya attributes and Qt components.]

## 📦 Installation & Usage
1. Download or copy the code from `transform_manager.py`.
2. Open Autodesk Maya.
3. Open the **Script Editor** (`Windows > General Editors > Script Editor`).
4. Paste the script into a **Python** tab.
5. Highlight the text and run it, or save it to your Maya Shelf for quick access.
