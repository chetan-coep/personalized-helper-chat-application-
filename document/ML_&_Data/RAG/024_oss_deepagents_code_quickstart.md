---
id: "rag_024"
technology: "RAG"
category: "ML & Data"
title: "Quickstart - Docs by LangChain"
doc_order: 24
source_url: "https://docs.langchain.com/oss/deepagents/code/quickstart"
language: "en"
retrieved_at: "2026-11-03 17:58:13"
content_hash: "e1db6819bc5b77e4a28993056a94b0d26aa05582f3ff5f1a7b1d1a929bc2845f"
---

# Quickstart - Docs by LangChain

Source: https://docs.langchain.com/oss/deepagents/code/quickstart

---

Deep Agents Code (

`dcode`) is a terminal coding agent built on the [Deep Agents SDK](https://docs.langchain.com/oss/python/deepagents/quickstart). This guide covers installation, your first task, daily interactive use, automation with piping, and LangSmith tracing. For a feature overview, see

[Deep Agents Code overview](https://docs.langchain.com/oss/deepagents/code/overview). For

`config.toml` and provider settings, see [Configuration](https://docs.langchain.com/oss/deepagents/code/configuration).

## Install and run your first task

Install and launch

Add provider credentials

`/auth` command to connect with a provider. See [Providers](https://docs.langchain.com/oss/deepagents/code/providers)for the full list and credential details.

Give the agent a task

Enable tracing (optional)

`/auth` and add your LangSmith API key. Tracing is enabled on the next launch.For choosing an agent environment, advanced options, and CI or headless setup, see [Trace with LangSmith](https://docs.langchain.com#trace-with-langsmith).

## Interactive mode

Type naturally as you would in a chat interface. The agent uses its built-in tools, skills, and memory to help you with tasks.
## Slash commands


- `/model`: Switch models or open the interactive model selector.
- `/effort`: Set reasoning effort for the current model.
- `/agents`: Hot-swap between pre-configured agents without relaunching. See [Command reference](https://docs.langchain.com/oss/deepagents/code/cli-reference#command-line-options) for related flags.
- `/auth`: Manage stored API keys for model providers and services (such as Tavily web search). See [Provider credentials](https://docs.langchain.com/oss/deepagents/code/credentials) for details.
- `/goal <objective>`: Draft acceptance criteria from a measurable objective. See [Goals and rubrics](https://docs.langchain.com/oss/deepagents/code/goals-and-rubrics).
- `/rubric`: Set explicit acceptance criteria for grading. See [Goals and rubrics](https://docs.langchain.com/oss/deepagents/code/goals-and-rubrics).
- `/remember [context]`: Review conversation and update memory and skills. Optionally pass additional context.
- `/skill:<name> [args]`: Directly invoke a skill by name. The agent server resolves the skill and loads its `SKILL.md` instructions before the first model call. See [Invoke a skill mid-session](https://docs.langchain.com/oss/deepagents/code/memory-and-skills#invoke-a-skill-mid-session).
- `/skill-creator [task]`: Guide for creating effective agent skills.
- `/offload` (alias `/compact`) - Free up context window space by offloading messages to storage with a summary placeholder. The agent can retrieve the full history from the offloaded file if needed.
- `/context`: Open a color-coded context-window usage report with model capacity, usage categories, and remaining space.
- `/context-doctor`: Audit the context injected into the session and its estimated token cost. See [Audit injected context](https://docs.langchain.com/oss/deepagents/code/cli-reference#audit-injected-context).
- `/tools`: List the built-in and MCP tools available to the current agent. See [List available tools](https://docs.langchain.com/oss/deepagents/code/cli-reference#list-available-tools).
- `/extensions`: List loaded [Python extensions](https://docs.langchain.com/oss/deepagents/code/extensions), their registrations, and their source paths. Requires `DEEPAGENTS_CODE_EXPERIMENTAL=1`.
- `/cost`: Show the thread’s estimated cost. See [Track thread cost](https://docs.langchain.com/oss/deepagents/code/cli-reference#track-thread-cost).
- `/btw`: Ask a side question about the conversation without interrupting the main task. See [Ask a side question](https://docs.langchain.com/oss/deepagents/code/cli-reference#ask-a-side-question).
- `/tokens`: Display current context window token usage breakdown.
- `/clear`: Start a fresh thread.
- `/force-clear`: Recover a stuck session with a fresh thread.
- `/copy`: Copy the latest assistant message to the clipboard.
- `/prompts`: Search, preview, copy, and reuse previously submitted prompts.
- `/rename [name]`: Name the current thread, or generate an editable suggestion when you omit the name. See [Name a thread](https://docs.langchain.com/oss/deepagents/code/cli-reference#name-a-thread).
- `/threads`: Browse and resume previous conversation threads.
- `/mcp [login <server> | reconnect]`: Show active MCP servers and tools. `login <server>` runs the OAuth flow for a server; `reconnect` loads deferred logins.
- `/plugins`: Manage [plugins and marketplaces](https://docs.langchain.com/oss/deepagents/code/plugins).
- `/notifications`: Configure startup warning preferences.
- `/reload`: Re-read `.env` files, refresh configuration, and re-discover skills without restarting. This also reloads plugin skills and MCP configuration. Conversation state is preserved. See [`DEEPAGENTS_CODE_` prefix](https://docs.langchain.com/oss/deepagents/code/configuration#deepagents_code_-prefix) for override behavior.
- `/theme`: Open the interactive theme selector to switch color themes. Built-in themes are available plus any [user-defined themes](https://docs.langchain.com/oss/deepagents/code/configuration#themes).
- `/scrollbar`: Show or hide the chat scrollbar.
- `/line-numbers`: Show or hide file-relative line numbers in new diffs. See [Diff line numbers](https://docs.langchain.com/oss/deepagents/code/config-file#diff-line-numbers).
- `/update`: Check for and install Deep Agents Code updates inline. Detects your install method (uv, Homebrew, pip) and runs the appropriate upgrade command.
- `/auto-update`: Toggle automatic updates on or off.
- `/install`: Install an optional integration.
- `/trace`: Open the current thread in LangSmith.
- `/editor`: Open the current prompt in your external editor (`$VISUAL` / `$EDITOR`). See [External editor](https://docs.langchain.com#external-editor).
- `/restart`: Restart the agent server.
- `/timestamps`: Toggle message timestamp footers.
- `/changelog`: Open Deep Agents Code changelog in your browser.
- `/docs`: Open the documentation in your browser.
- `/feedback`: Send feedback or report an issue.
- `/version` (alias `/about`) - Show installed `deepagents-code` and SDK versions.
- `/help`: Show help and available commands.
- `/quit`: Exit Deep Agents Code.

## Shell commands


`!` to enter shell mode, then type your command.
## Keyboard shortcuts


**General**

**Text editing in the prompt**The chat input uses standard readline-style bindings:

**Search prompt history**Prompt history search lets you find and reuse previously submitted prompts without leaving the chat input. Press

`Ctrl+R` to open an inline search of prompts stored on your machine.
**Reference a previous thread**Type

`@@` in the chat input to search recent threads by their initial prompt, thread ID, agent, branch, or working directory. Select a result to insert an `@@(thread:<thread-id>)` reference. Deep Agents Code can inspect the referenced conversation when its context is relevant to your request.Add text after `@@` to filter the results. While the suggestions are open, press `Ctrl+R` to browse all threads with the same search. In the full thread picker, press `Ctrl+C` to copy the selected thread ID.
**macOS`Cmd+Left` / `Cmd+Right` / `Cmd+Delete`**Terminal emulators intercept

`Cmd`-modified keys before they reach the terminal process, so Deep Agents Code never receives them directly. Instead, the terminal translates them into the readline shortcuts above.
- **Ghostty:** Works out of the box. `Cmd+Left`, `Cmd+Right`, and `Cmd+Delete` are translated to `Ctrl+A`, `Ctrl+E`, and `Ctrl+U` by default.
- **iTerm2:** Not bound by default. Add the following under **Settings > Profiles > Keys > Key Mappings** as `Send Text with vim special chars`:
  - `Cmd+Left` → `\x01` (Ctrl+A)
  - `Cmd+Right` → `\x05` (Ctrl+E)
  - `Cmd+Delete` → `\x15` (Ctrl+U)
- **Terminal.app:** No native UI for this remap. Use the `Ctrl`-based shortcuts directly.

Word-wise motion (

`Option+Left` / `Option+Right`) is handled the same way: terminals send `Esc+b` / `Esc+f`, which Deep Agents Code interprets as word-left/right.
### Inspect context-window usage

Run`/context` to open a color-coded report of the current model’s context-window usage. The report shows the model’s context limit, used tokens, remaining capacity, and a breakdown between the conversation and system prompt plus tools when those values are available.
Provider-reported totals remain distinct from local conversation estimates. When a provider total is unavailable, the report labels the conversation count as an estimate and marks the total usage as unavailable. Use `/tokens` when you want a text summary in the conversation transcript instead.
When usage grows faster than expected, run `/context-doctor` to attribute tokens to each injected component: the base system prompt, memory files, the skills index, built-in tool schemas, and MCP tool schemas. To confirm which tools the agent can currently call, run `/tools`. For the thread’s running cost estimate, run `/cost`; the same figure appears in the status bar. See [Diagnose and audit a session](https://docs.langchain.com/oss/deepagents/code/cli-reference#diagnose-and-audit-a-session).

### External editor

Press`Ctrl+G` or type `/editor` to compose prompts in an external editor. Deep Agents Code checks `$VISUAL`, then `$EDITOR`, then falls back to `vi` (macOS/Linux) or `notepad` (Windows). GUI editors (VS Code, Cursor, Zed, etc.) automatically receive a `--wait` flag so Deep Agents Code blocks until you close the file.
## Non-interactive mode and piping

Use`-n` to run a single task without launching the interactive UI:
`-n` or `-m`, the piped content appears first, followed by the text you pass to the flag.
`-S`/`--shell-allow-list` to enable specific commands (e.g., `-S "pytest,git,make"`), `recommended` for safe defaults, or `all` to permit any command.
## Cap turn count


`--max-turns N` gives operators a hard upper bound without having to touch SDK internals:`N` must be a positive integer, and overrides the internal safety default that otherwise caps runaway loops. Exits with code 124 (matching GNU `timeout`) when the budget is exceeded, so CI can distinguish a budget hit from a generic failure. Requires `-n` or piped stdin; otherwise exits with code 2.For a time-based limit instead of (or in addition to) a turn-count limit, see [Cap wall-clock time with`--timeout`](https://docs.langchain.com#non-interactive-mode-and-piping).

## Cap wall-clock time


`--timeout SECONDS` enforces a hard wall-clock limit on a non-interactive run. It complements `--max-turns` (turn count) with a time-based budget—whichever limit is hit first cancels the agent.`--max-turns`, so CI can treat both budget hits uniformly. Requires `-n` or piped stdin; otherwise exits with code 2.
## Clean output and buffering


`-q` for clean output suitable for piping into other commands, and `--no-stream` to buffer the full response (instead of streaming) before writing to stdout:`npm init -y`, `apt-get install -y`).
## Shell execution examples


## Trace with LangSmith

`project_name` or `LANGSMITH_PROJECT`. [Create an agent](https://docs.langchain.com/langsmith/create-an-agent), choose its environment, and

[retrieve that environment’s`tracer_session_name`](https://docs.langchain.com/langsmith/create-an-agent#use-an-environment-project). Use that returned value in the destination setting and any overrides. For integrations that support agent addressing, use the

[agent identifier and environment](https://docs.langchain.com/langsmith/log-traces-to-agent)directly.

[LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-deepagents-code-quickstart)tracing to see agent operations, tool calls, and decisions in a LangSmith agent environment. Run

`/auth` and add your LangSmith API key. Tracing is enabled on the next launch and persists across sessions. See [Provider credentials](https://docs.langchain.com/oss/deepagents/code/credentials#use-%2Fauth-recommended)for details on the credential manager. To select the agent environment or configure tracing without the TUI, add keys to

`~/.deepagents/.env` so tracing is enabled in every session without per-shell exports:
`DEEPAGENTS_CODE_LANGSMITH_PROJECT` to the coding agent environment’s `tracer_session_name`. This setting controls Deep Agents Code’s own traces. A separate `LANGSMITH_PROJECT` in your repository’s `.env` controls traces from code run in shell commands. See **Separate coding-agent traces from shell-command traces**below. To override the destination for a specific working directory, add

`DEEPAGENTS_CODE_LANGSMITH_PROJECT` to a `.env` in that directory. See [environment variables](https://docs.langchain.com/oss/deepagents/code/configuration#environment-variables)for the full loading order.

## Disable agent tracing


`dcode --no-tracing` to disable LangSmith agent tracing for one session. For future launches, set `DEEPAGENTS_CODE_LANGSMITH_TRACING=false` in your shell or `~/.deepagents/.env`.The flag overrides the environment setting. An explicit `false` in `DEEPAGENTS_CODE_LANGSMITH_TRACING` overrides other tracing-enable flags, including `LANGSMITH_TRACING=true`. Shell exports take precedence over `.env` values for the same variable.Disabling agent tracing does not disable local conversation history or model-provider requests. It is separate from trace redaction and tracing emitted by agents run in shell commands.
## Separate coding-agent traces from shell-command traces


- `Agent traces` are Deep Agents Code’s own model calls, tool calls, orchestration, and middleware.
- `Shell-command traces` are traces emitted by code that Deep Agents Code runs for you in a shell, such as tests, scripts, or a local LangGraph agent.

To select the environment for Deep Agents Code’s own traces, set

`DEEPAGENTS_CODE_LANGSMITH_PROJECT`:`LANGSMITH_PROJECT` with a different agent environment’s `tracer_session_name`:
[`DEEPAGENTS_CODE_` prefix](https://docs.langchain.com/oss/deepagents/code/configuration#deepagents_code_-prefix)(e.g.,

`DEEPAGENTS_CODE_LANGSMITH_API_KEY`).
## Copy traces to a second agent environment


`DEEPAGENTS_CODE_LANGSMITH_REPLICA_PROJECTS`. This is useful for sending the same traces to agent environments in both a personal workspace and a shared team workspace.`tracer_session_name` values. Leave the replica variable unset to write to one environment.`/trace` to print the URL and open it in your browser.