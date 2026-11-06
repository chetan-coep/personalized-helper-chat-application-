# DocSyntax AI — Frontend Interface

This is the pure frontend interface for the documentation code & syntax assistant, designed directly from the user's 3-panel blueprint layout.

---

## Blueprint Layout Implementation

1. **Top-Left Panel**: **Explanation & Why to Use**
   - Displays conceptual explanation, rationale, use cases, and official documentation reference.
2. **Bottom-Left Panel**: **User's Prompt for the LLM**
   - Input field with keyboard shortcuts (`Ctrl + Enter`), clear button, and quick-example chips.
3. **Right-Column Panel (Full Height)**: **Syntax with Code**
   - Clean, copy-pasteable code snippet with one-click copy button, line styling, and parameter/signature breakdown.

---

## Features
- **Dark & Light Mode**: Soft, natural earth-toned palette (warm basalt/sage in dark mode, linen/olive parchment in light mode) preventing eye fatigue over long coding sessions.
- **No Harsh Blues or Distracting Colors**: Calm, muted, developer-friendly contrast.
- **Zero Sensitive Backend Exposure**: Client-side only. Does not leak API keys or vector DB URLs.
- **Responsive**: Adapts gracefully across monitor sizes and mobile devices.

---

## How to Open and View

### Option 1: Direct Browser File
Simply open [`index.html`](file:///C:/final_year/temp%20project/ai%20course/project/ui/index.html) in any web browser (Chrome, Edge, Firefox, Brave).

### Option 2: Local Web Server
```bash
cd "C:\final_year\temp project\ai course\project\ui"
python -m http.server 3000
```
Then visit: `http://localhost:3000`

