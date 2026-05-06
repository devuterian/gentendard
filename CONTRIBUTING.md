# Contributing

Normal commits must follow [LPFchan/repo-template](https://github.com/LPFchan/repo-template) conventions enforced by `.githooks/` and `.github/workflows/commit-standards.yml`.

1. Install hooks: `sh scripts/install-hooks.sh`
2. Generate a message: `sh scripts/new-commit-message.sh --subject "feat: ..." --agent <id>`
3. Edit the body (`changes`, `rationale`, `checks`), then `git commit -F <file>`

The first repository seed may use a **bootstrap** subject line; see `scripts/check-commit-standards.sh` for the exception rule.

Do not redistribute merged fonts under a license other than **SIL OFL 1.1**. Keep [`OFL.txt`](OFL.txt) with any binary release.
