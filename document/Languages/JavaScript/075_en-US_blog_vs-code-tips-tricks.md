---
id: "javascript_075"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 75
source_url: "https://developer.mozilla.org/en-US/blog/vs-code-tips-tricks"
language: "en"
retrieved_at: "2026-11-01 21:53:54"
content_hash: "da1dc7d4d1512577785548a19cb4bd5629e6841054d294ddbbbc87ac69859f8e"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/vs-code-tips-tricks

---

# VS Code: Tips and tricks for beginners

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) is more than a standard code editorâit's an [integrated development environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment), packed with a lot of features right out of the box. As a technical writer for MDN, I use VS Code primarily for writing documentation in Markdown. When I started using VS Code, I discovered a lot of features I could use right away. Although it is simple to use, knowing a few extra features and extensions can help you get things done faster, whether you're coding, writing, or doing both.

This article provides a beginner's overview, taking you through some practical tips, interesting features, including the built-in Git capabilities, and a few and extensions, that can enhance your VS Code experience. I'm excited to share the tricks and tools I've learned that will be beneficial for those just starting out.

## [Keyboard shortcuts](https://developer.mozilla.org#keyboard_shortcuts)

Let's explore some keyboard shortcuts that can make navigation and editing in VS Code quicker. Many of these shortcuts are also supported in other editors. For example, if you're familiar with Sublime Text, you'll find that most of the shortcuts are quite similar. Learning these shortcuts can help you work faster in VS Code, and they'll also be useful if you switch to or use another editor.

### [Shortcuts for navigation](https://developer.mozilla.org#shortcuts_for_navigation)

| Action | On Windows | On macOS | 
|---|---|---|
| Open a file | `Ctrl` + `O` | `Command` + `O` | 
| Go to a line in a file | `Ctrl` + `G` | `Control` + `G` | 
| Go to a symbol in a file | `Ctrl` + `Shift` + `O` | `Command` + `Shift` + `O` | 
| Open the Command Palette | `Ctrl` + `Shift` + `P` | `Command` + `Shift` + `P` | 
| [Open Keyboard Shortcuts](https://developer.mozilla.org#customization_of_shortcuts) | `Ctrl` + `K`, `Ctrl` + `S` | `Command` + `K`, `Command` + `S` | 
| [Open Zen Mode](https://developer.mozilla.org#zen_mode) | `Ctrl` + `K`, `Z` | `Command` + `K`, `Z` | 
| [Open the Terminal](https://developer.mozilla.org#integrated_terminal) | `Ctrl` + `` ` `` | `Ctrl` + `` ` `` | 
| [Open Markdown Preview](https://developer.mozilla.org#markdown_preview) | `Ctrl` + `K`, `V` | `Command` + `K`, `V` | 

### [Shortcuts for editing](https://developer.mozilla.org#shortcuts_for_editing)

| Action | On Windows | On macOS | 
|---|---|---|
| Move a line up or down | `Alt` + `â` or `â` | `Option` + `â` or `â` | 
| Duplicate a line or selection | `Ctrl` + `Alt` + `â` or `â` | `Shift` + `Option` + `â` or `â` | 
| Select the next occurrence | `Ctrl` + `D` | `Command` + `D` | 
| Navigate between occurrences | `Ctrl` + `K` + `D` | `Shift` + `Command` + `G` and `Command` + `G` | 

### [Customizing shortcuts](https://developer.mozilla.org#customizing_shortcuts)

If some of the shortcuts listed above don't work for you, check your Keyboard Shortcuts settings. You can access the settings by pressing `Command` + `K`, then `Command` + `S` on macOS or by using the menu **Code** > **Settings** > **Keyboard Shortcuts** (as of Version 1.83.1). You might notice that a different key combination is set up for a particular action, or you might need to set up a new shortcut. You can customize the keyboard shortcuts to suit your style and needs.

### [Using Zen Mode](https://developer.mozilla.org#using_zen_mode)

I learned about [Zen Mode](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_zen-mode) while writing this article. I find this feature similar to the Pageless feature in Google Docs. You can activate Zen Mode via `Command` + `K`, `Z` on macOS (**View** > **Appearance** > **Zen Mode**). To exit, use the same key combination or press `Esc` twice. You might like this mode if you prefer your working area to be clutter- or distraction-free.

### [Personal favorite](https://developer.mozilla.org#personal_favorite)

The shortcut I like the most is `Command` + `D` because it allows me to select multiple occurrences of a word or a phrase and edit them all in-place simultaneously. For example, to make multiple occurrences of a keyword bold, I use this key combination to select them, then type two asterisks. VS Code will automatically place an asterisk on either side of each selected word (see the [Surrounding characters](https://developer.mozilla.org#optimized_editing) feature), making them bold. This is often faster than using the traditional "Find and Replace" utility, especially when working with a smaller number of occurrences in the visible frame. "Find and Replace" can help when you're handling bulk replacements or when you need to perform a regex search.

How many of the above shortcuts are you already using? Do you use all of them, or are there others you find more helpful? I've found that by using even a few shortcuts while working in VS Code improves my efficiency, not to mention that it's fun to use these shortcuts! And isn't it just a tad annoying when these shortcuts don't work when you're using Google Docs!? ð

## [Built-in features](https://developer.mozilla.org#built-in_features)

VS Code provides some nifty features that can immediately speed up your writing and editing.

### [Integrated terminal](https://developer.mozilla.org#integrated_terminal)

The built-in "Terminal" in VS Code allows you to run shell commands right from the editor, so you don't have to toggle between VS Code and a separate terminal window. It supports multiple terminals, and you can easily switch between them. To open the terminal, press `Ctrl` + `` ` `` on Windows and macOS (**View** > **Terminal**). The terminal also supports text selection, so you can easily copy and paste text to and from the terminal.

### [Outline view](https://developer.mozilla.org#outline_view)

The Outline view feature in VS Code displays a tree structure of your document, showing headings, classes, methods, and other significant elements in your file. You can click on the desired element to navigate directly to the corresponding section in the file. The tree structure adjusts dynamically as you add, remove, or rearrange the headings, allowing you to navigate to different sections with ease without the need for scrolling the document. Apart from quick navigation, it helps provide a quick overview of your document's structure.

The Outline view can be accessed from the side bar; it is typically located below the **Explorer** tab. If it not already visible, you can enable it via **View** > **Open View...** menu, type "Outline" and press `Return`.

The Outline view is available for various file types, from [programming](https://code.visualstudio.com/docs/getstarted/userinterface#_outline-view) to [markup](https://code.visualstudio.com/Docs/languages/markdown#_document-outline) languages. In Markdown files, the headers turn into a clickable table of contents in the Outline view.

### [Markdown Preview](https://developer.mozilla.org#markdown_preview)

For working with Markdown files, VS Code provides the [Markdown Preview](https://code.visualstudio.com/Docs/languages/markdown#_markdown-preview) feature. It displays a live preview of your `.md` file's formatted output, similar to how the content would appear on a webpage. To open the preview, press `Command` + `K` and then `V` on macOS. This opens a side-by-side view where your Markdown text is rendered and updates as you edit the file.

I find this preview feature quite convenient while writing and editing documentation because it allows me to spot and fix any formatting issues immediately. Plus, since the preview updates as you type, what you see is always up to date. It helps you focus more on content creation and less on formatting issues.

This feature can be handy whether you're creating a short README or writing extensive documentation.

### [Editing support](https://developer.mozilla.org#editing_support)

- **Automatic surrounding characters**: An awesome feature in VS Code is that when a word or phrase is selected, typing a character [surrounds the selected text](https://code.visualstudio.com/updates/v1_27#_auto-closing-surrounding-characters) with that character. This feature is a big time saver when you need to wrap multiple occurrences of a word with characters like quotes or parentheses. Combined with the `Command` + `D` key combination we saw earlier on macOS, you can quickly make these edits on multiple selections in one go.
- **Multi-cursor editing**: This is my next favorite feature. By pressing the `Option` key and clicking the mouse at all the required places, you can create [multiple cursors](https://code.visualstudio.com/docs/editor/codebasics#_multiple-selections-multicursor) for simultaneously editing multiple lines or phrases.

Additionally, you can click at a starting point, press `Option` and `Shift` keys (on macOS) and drag to create multiple cursors in a column, which is handy for editing lines that are one below the other. I find this feature effective when I need to indent multiple lines; instead of pressing the `Tab` key for each line, I create multi-cursors by clicking at the selected place, pressing `Option` and `Shift`, and dragging the cursor and then indenting them all with a single `Tab` key press.

### [Git integration](https://developer.mozilla.org#git_integration)

VS Code's built-in Git capabilities help in managing version control and also make it easier to handle some complex scenarios.

- **Resolving merge conflicts**: When working on a collaborative project such as MDN, [merge conflicts](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts) are almost inevitable. VS Code's intuitive GUI helps to resolve these conflicts. You can easily compare the conflicting files, identify the differences, and choose how to resolve them.
- **Viewing commit history**: You can use the Source Control view (`Control` + `Shift` + `G` on macOS) to see a list of changes and the [commit](https://code.visualstudio.com/docs/sourcecontrol/overview#_commit) history in the current repository, as illustrated by the image below. You can even type a commit message directly in the provided input field to capture your changes before committing.
- **Managing branches**: You can quickly access the branch management features from the Status Bar at the bottom of the window. When you click on the current branch name, you can [search and switch to other branches](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags) via the quick pick menu or even create new ones. The Source Control view provides another way to manage and access different branches.

## [Extensions](https://developer.mozilla.org#extensions)

You can add a ton of extra functionality on top of the built-in features of VS Code by installing Extensions (`Command` + `Shift` + `X` on macOS). You can install them directly from the Marketplace within VS Code. Use them with caution though; they have their own settings, which might override your project's settings.

### [Ensure consistency in markdown files](https://developer.mozilla.org#ensure_consistency_in_markdown_files)

I find the [Markdown Linter](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) extension quite helpful for maintaining consistent markdown syntax. With this extension enabled, if there are any deviations from the rules as you type, they get flagged. You can also see all warnings in the **PROBLEMS** tab in the IDE by pressing `Command` + `Shift` + `M` or by hovering over a line in the file to see specific warnings.

### [Avoid typos](https://developer.mozilla.org#avoid_typos)

Typos can be frustrating and embarassing if they land in production. Spellchecker extensions like [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) are a must to catch these errors before you commit your changes. Words not in the dictionary get underlined and also appear in the **PROBLEMS** tab in the IDE. You can also use the lightbulb icon for quick fixes.

### [Get Git insights](https://developer.mozilla.org#get_git_insights)

[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) enhances the built-in Git features of VS Code. This extension is quite resourceful to quickly see who changed the file contents, when, and why, all directly within the editor, eliminating the need to visit GitHub or run Git commands to view the commit history. It provides real-time, inline blame annotation, as shown in the image below.

When you install GitLens, a dedicated tab called **GITLENS** is added next to the **TERMINAL** tab. You can use it to see the commit history visually.

## [Summary](https://developer.mozilla.org#summary)

In this article, you learned about how VS Code can help make your work easier and faster, whether you're writing code or documentation. We looked at shortcuts, extensions like GitLens, and other built-in Git features that can speed up your work.

I'd love to hear your hacks for using VS Code. Feel free to share them on our MDN Web Docs [Discord server](https://developer.mozilla.org/discord).