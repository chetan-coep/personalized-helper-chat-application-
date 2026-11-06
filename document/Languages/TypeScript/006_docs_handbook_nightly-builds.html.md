---
id: "typescript_006"
technology: "TypeScript"
category: "Languages"
title: "TypeScript: Documentation - Nightly Builds"
doc_order: 6
source_url: "https://www.typescriptlang.org/docs/handbook/nightly-builds.html"
language: "en"
retrieved_at: "2026-11-03 17:56:27"
content_hash: "6f722ef93bda703ab570bd1fd3ae56c24f3cd6bec69e68045de85bb1c6b31679"
---

# TypeScript: Documentation - Nightly Builds

Source: https://www.typescriptlang.org/docs/handbook/nightly-builds.html

---

A nightly build from the [TypeScript’s `main`](https://github.com/Microsoft/TypeScript/tree/main) branch is published by midnight PST to npm.
Here is how you can get it and use it with your tools.

shell

You can also update your editor/IDE to use the nightly drop.
You will typically need to install the package through npm.
The rest of this section mostly assumes `typescript@next` is already installed.

The VS Code website [has documentation on selecting a workspace version of TypeScript](https://code.visualstudio.com/Docs/languages/typescript#_using-newer-typescript-versions).
After installing a nightly version of TypeScript in your workspace, you can follow directions there, or simply update your workspace settings in the JSON view.
A direct way to do this is to open or create your workspace’s `.vscode/settings.json` and add the following property:

json

Alternatively, if you simply want to run the nightly editing experience for JavaScript and TypeScript in Visual Studio Code without changing your workspace version, you can run the [JavaScript and TypeScript Nightly Extension](https://marketplace.visualstudio.com/items?itemName=TypeScriptTeam.vscode-typescript-nightly)

Update the `Settings - User` file with the following:

json

More information is available at the [TypeScript Plugin for Sublime Text installation documentation](https://github.com/Microsoft/TypeScript-Sublime-Plugin#installation).

Note: Most changes do not require you to install a new version of the VS TypeScript plugin.


The nightly build currently does not include the full plugin setup, but we are working on publishing an installer on a nightly basis as well.

1. Download the [VSDevMode.ps1](https://github.com/Microsoft/TypeScript/blob/main/scripts/VSDevMode.ps1) script.
Also see our wiki page on [using a custom language service file](https://github.com/Microsoft/TypeScript/wiki/Dev-Mode-in-Visual-Studio#using-a-custom-language-service-file).
2. From a PowerShell command window, run:

For VS 2015:

`VSDevMode.ps1 14 -tsScript <path to your folder>/node_modules/typescript/lib`

For VS 2013:

`VSDevMode.ps1 12 -tsScript <path to your folder>/node_modules/typescript/lib`

Go to `Preferences` > `Languages & Frameworks` > `TypeScript`:

TypeScript Version: If you installed with npm: `/usr/local/lib/node_modules/typescript/lib`


Go to `File` > `Settings` > `Languages & Frameworks` > `TypeScript`:

TypeScript Version: If you installed with npm: `C:\Users\USERNAME\AppData\Roaming\npm\node_modules\typescript\lib`