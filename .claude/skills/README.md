# Skills for Claude Code cloud sessions

Skills in this folder load automatically in every Claude Code session started on
this repository, including cloud sessions started from the Claude mobile app.

| Skill | Source | Version | License |
|---|---|---|---|
| `banana` | https://github.com/AgriciDaniel/banana-claude (commit 08e329b, `skills/banana`) | 3.1.0 | MIT (see `banana/LICENSE`) |

## banana: setup

Image generation calls Google's Gemini API and needs a billing-enabled key.
The scripts read it only from the `GEMINI_API_KEY` environment variable.
Never commit the key to this repository. In a cloud session, add it as a
network secret for `generativelanguage.googleapis.com` in the environment's
settings instead.

To update, copy `skills/banana` from a newer release of the upstream repo over
`banana/`.
