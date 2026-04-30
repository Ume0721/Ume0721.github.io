# Ume0721.github.io

## VS Code / Codespaces minimal Emacs-style setup

This repository keeps terminal behavior unchanged and focuses on a simpler VS Code UI plus Emacs-like editing experience.

### What is configured

- [`.vscode/settings.json`](.vscode/settings.json): UI simplification and editor defaults.
- [`.vscode/extensions.json`](.vscode/extensions.json): Emacs-related extension recommendations.
- [`.vscode/keybindings.json`](.vscode/keybindings.json): minimal Emacs-style shortcuts for common operations.
- [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json): plain Ubuntu base image for Codespaces.

### UI simplification scope

- Hidden activity bar and command center.
- Disabled breadcrumbs and sticky scroll.
- Kept tabbed editor and stable sidebar position.
- No changes to your terminal workflow.

### Shortcut experience

- Emacs window navigation: `C-x 2` (split down), `C-x 3` (split right), `C-x o` (next group), `C-x 1` (close others).
- File operations: `C-x C-s` (save), `C-x C-w` (close).
- Command palette: `M-x` (show commands), `C-s` (quick open).
- Find & replace: `C-h`.
- Common edits: `C-a` (select all), `C-w` (kill line), `C-y` (paste), `M-w` (copy), `C-/` (comment).
- Selection: `Alt+Shift+W` to shrink region (via expand-region extension).
- Main keybinding behavior comes from `nisheetjain.emacs` extension.
- All shortcuts are workspace-committed for instant availability in Codespaces.
- 图版总览: [shortcut-cheatsheet.svg](shortcut-cheatsheet.svg)

### Compatibility notes

- No OS-specific absolute paths are used.
- No project runtime dependencies are added.
- If recommended extensions are not installed, the repository still works as a normal GitHub Pages project.