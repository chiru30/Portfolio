function getPreferredTheme() {
  try {
    const saved = localStorage.getItem("theme");
    if (saved === "light" || saved === "dark") return saved;
  } catch (_) {}
  return null;
}

function getSystemTheme() {
  return window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

function setTheme(theme) {
  applyTheme(theme);
  try {
    localStorage.setItem("theme", theme);
  } catch (_) {}
}

function currentTheme() {
  return (
    document.documentElement.getAttribute("data-theme") ||
    getPreferredTheme() ||
    getSystemTheme()
  );
}

function updateToggleLabel(btn) {
  const theme = currentTheme();
  // Show the *target* theme as an icon:
  // - currently dark → show sun (switch to light)
  // - currently light → show moon (switch to dark)
  btn.textContent = theme === "dark" ? "☀" : "☾";
  btn.setAttribute(
    "aria-label",
    theme === "dark" ? "Switch to light theme" : "Switch to dark theme"
  );
  btn.setAttribute("title", btn.getAttribute("aria-label"));
}

function initThemeToggle() {
  const btn = document.getElementById("themeToggle");
  if (!btn) return;

  // If nothing is set yet, fall back to system.
  if (!document.documentElement.getAttribute("data-theme")) {
    const saved = getPreferredTheme();
    applyTheme(saved || getSystemTheme());
  }

  updateToggleLabel(btn);
  btn.addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    setTheme(next);
    updateToggleLabel(btn);
  });

  // Keep in sync with system theme if user hasn't chosen explicitly.
  try {
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    mq.addEventListener("change", () => {
      const saved = getPreferredTheme();
      if (!saved) {
        applyTheme(getSystemTheme());
        updateToggleLabel(btn);
      }
    });
  } catch (_) {}
}

function initFooterYear() {
  const el = document.getElementById("year");
  if (!el) return;
  el.textContent = String(new Date().getFullYear());
}

initThemeToggle();
initFooterYear();
