# Portfolio

Simple, static portfolio site (no build step). Includes a dark/light theme toggle and a GitHub Pages deployment workflow.

## Run locally

### Option A: localhost (recommended)

```bash
python3 -m http.server 5173
```

Then open `http://localhost:5173/`.

### Option B: open file directly

Open `index.html` in your browser.

## Deploy on GitHub Pages

1. Push to the `main` branch of your repo.
2. In GitHub: **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Wait for the workflow **Deploy to GitHub Pages** to finish.
