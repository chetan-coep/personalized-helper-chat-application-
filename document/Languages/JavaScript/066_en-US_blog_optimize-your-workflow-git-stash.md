---
id: "javascript_066"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 66
source_url: "https://developer.mozilla.org/en-US/blog/optimize-your-workflow-git-stash"
language: "en"
retrieved_at: "2026-11-01 21:53:30"
content_hash: "7f85a9b221ab29c5466c8aeeb8efffddae8a056aecd0d3ff2ef95ee1469f9ac9"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/optimize-your-workflow-git-stash

---

# Optimize your workflow with Git stash

If you haven't used Git stash before, are already using it, or are curious about alternative workflows, this post is for you. We'll delve into use cases for stashing, discuss some of its pitfalls, and introduce an alternative method that makes managing uncommitted code safer and more convenient. By the end of this post, you'll better understand how to stash effectively and discover different strategies to improve your workflow.

## [What is Git stash?](https://developer.mozilla.org#what_is_git_stash)

You might have heard about [`git stash`](https://git-scm.com/docs/git-stash).
It's a Git built-in command that can be used to store away uncommitted local changes.
For example, when you have modified files in your working tree (often referred to as "dirty"), `git status` might show something like:

```
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.go
no changes added to commit (use "git add" and/or "git commit -a")
```
When you want to save these changes, but don't want to commit them to the current branch, you can instead stash them:

```
$ git stash
Saved working directory and index state WIP on main: 821817d some commit message
```
This will clean up your working tree:

```
$ git status
On branch main
nothing to commit, working tree clean
```
The `git stash list` command shows your existing stashes, numbering them from `0` starting with the newest first. In this case, we see one stash:

```
$ git stash list
stash@{0}: WIP on main: 821817d some commit message
```
## [Stashing when switching branches](https://developer.mozilla.org#stashing_when_switching_branches)

The most common use case for Git stash is when you want to store any work-in-progress code before switching branches to work on something else. For example:

```
$ git status
On branch feature-a
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   lib/feature-a/file.go
no changes added to commit (use "git add" and/or "git commit -a")
$ git stash
Saved working directory and index state WIP on feature-a: fd25af5 start feature A
$ git switch feature-b
# ... start working of feature B
```
Stashing changes when you switch branches has a few downsides:

- After creating a stash, it's possible to completely forget about its existence and duplicate work.
- It's easy to forget which branch a stash belongs to. Whenever changes in a stash are built on top of an unmerged feature branch, you might have a hard time unstashing these changes unless you're on the correct branch.
- It might be difficult to reapply a stash to a branch if more changes have been made to the branch in the meantime, or if the branch might has been rebased.
- A stash isn't backed up on the server. Your changes are gone when your local copy disappears (e.g., if the repository is deleted or a hard disk fails).

## [Alternative workflow for switching branches](https://developer.mozilla.org#alternative_workflow_for_switching_branches)

Instead of using Git stash to store away your local changes, consider committing them to the branch. These commits will be temporary, and you should state this clearly in the commit message, for example by giving them the title "WIP". You can do this by running:

```
git add .
git commit -m "WIP"
# or 'git commit -mWIP'
```
Later, when you return to that branch and see the title of the last commit as "WIP", you can roll it back with:

```
git reset --soft HEAD~
```
This removes the last commit from the current branch, but leaves the changes in your working tree in place.
To make this process more convenient, you can set up two [aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) for this:

```
git config --global alias.wip '!git add -A && git commit -mWIP'
git config --global alias.unwip '!git reset --soft $(git log -1 --format=format:"%H" --invert-grep --grep "^WIP$")'
```
These aliases add two Git subcommands:

- `git wip`: This command stages all your local changes (even untracked files) and writes a commit with the title "WIP" to the current branch.
- `git unwip`: This command uses `git log` to look from the tip of the current branch to find a commit that doesn't have "WIP" as title.
Then it resets to this commit using `--soft` to leave the changes in the working tree.

Now, when you have local changes and need to switch branches, just type `git wip` and the changes are stored in the current branch.
If you're on a feature branch and your team's workflow is fine with rewriting history in such branches, you can even push this branch to back up these changes.
Later, when you come back to this branch, you can type `git unwip` to continue working on these changes.
If your workflow allows, you can rebase the branch before using `git unwip`. This will rebase the whole branch, including the WIP changes, to make sure you're working on the latest version of the target branch.

The `git unwip` command is designed to work on any branch.
If there is no WIP commit on the tip of the current branch, nothing happens.
If there are multiple commits on the tip, they are all undone.
And if there is a non-WIP commit on top of a WIP commit, it's not rolled back. You'll need to resolve that manually.

**Warning:**
Because `git wip` commits all untracked files, ensure any files containing secrets are in your `.gitignore`. Otherwise, they'll become part of the Git history, and you might accidentally push them to a remote where everyone can access them.

## [When to use Git stash](https://developer.mozilla.org#when_to_use_git_stash)

As mentioned earlier, Git stash isn't ideal for when you're switching branches. A better use case for Git stash is breaking down commits.

There is a lot written already about so-called "commit hygiene", and there are many opinions about it. It can be really beneficial if each commit tells its own story. Each commit makes one functional change at a time, preferably accompanied with a well-written commit message. In a workflow where you have smaller commits, it is easier for code reviews to go through the commits one by one and understand the story step by step. Whenever it's needed, it also enables you to revert a smaller set of changes.

Imagine you have a Go project, and this is an example of what you've started with:

```
package main
import "fmt"
func Greet() {
	fmt.Print("Hello world!")
}
func main() {
	Greet()
}
```
This piece of code prints "Hello world!" when you run it. For various reasons, you need to refactor this. After making a bunch of changes, you end up with:

```
package main
import (
	"fmt"
	"io"
	"os"
	"time"
)
var now = time.Now
func Format(whom string) string {
	greeting := "Hello"
	if h := now().Hour(); 6 < h && h < 12 {
		greeting = "Good morning"
	}
	return fmt.Sprintf("%v %v!", greeting, whom)
}
func Greet(w io.Writer) {
	fmt.Fprint(w, Format("world"))
}
func main() {
	Greet(os.Stdout)
}
```
The main functionality remains the same, but there are a few feature changes:

- You can specify `whom` to greet.
- You can specify where to write the greeting.
- The greeting will differ depending on the time of day.

In this scenario, we like to commit each of these functional changes separately.
In many situations, you would be able to use `git add -p` to stage small hunks of code at once, but in this case, the changes are too intertwined.
And this is where `git stash` comes in real handy.
In the next steps below, we'll use it as a backup, where we save the end result in a stash, apply it, and then undo the changes we don't need for the current functional change.
Because the end result is stored in a stash, we can repeat this process for each commit we want to make.

Let's have a look:

```
git stash push --include-untracked
```
This saves all your local changes in a stash, and you can start breaking down changes into separate commits.
The option `--include-untracked` will also include files that were never committed, which is useful if you've added new files.

Now we can start working on the first commit.
Type `git stash apply` to bring the changes from the stash back into your local working tree:

```
$ git stash apply
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.go
no changes added to commit (use "git add" and/or "git commit -a")
```
Open `main.go` in your favorite editor, and modify it so it includes the changes to add `whom`.
This might look something like:

```
package main
import (
	"fmt"
)
func Greet(whom string) string {
	return fmt.Sprintf("Hello %v!", whom)
}
func main() {
	fmt.Print(Greet("world"))
}
```
In this process, you can throw away all unwanted changes because the end result is safely stored away in a stash. This means you can adapt the code so it properly compiles and ensures the tests pass with these changes. When you're happy, these changes can be committed as usual:

```
git add .
git commit -m "allow caller to specify whom to greet"
```
We can repeat these steps for the next commit.
Type `git stash apply` to get started.
Unfortunately, this might give you conflicts:

```
$ git stash apply
Auto-merging main.go
CONFLICT (content): Merge conflict in main.go
Recorded preimage for 'main.go'
On branch main
Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   main.go
no changes added to commit (use "git add" and/or "git commit -a")
```
Resolving conflicts is outside the scope of this article, but there is a quick way to restore the changes from the stash that may work well in such cases:

```
git restore --theirs .
git restore --staged .
```
Let's look at what that's doing. The [`git restore --theirs`](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---theirs) command will tell Git to resolve the conflict by taking all changes from *theirs*.
In this case, *theirs* is the stash, which will apply the changes from there.
The [`git restore --staged .`](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---staged) command will unstage these changes, meaning they are no longer added to the index and are omitted the next time you type `git commit`.

Now you can start hacking on the code again, and eventually you might end up with something like:

```
package main
import (
	"fmt"
	"io"
	"os"
)
func Greet(w io.Writer, whom string) {
	fmt.Fprintf(w, "Hello %v!", whom)
}
func main() {
	Greet(os.Stdout, "world")
}
```
Here you can repeat the usual commands to write another commit:

```
git add .
git commit -m "allow caller to specify where to write the greeting to"
```
For the final commit, simply run:

```
git stash apply
git checkout --theirs .
git reset HEAD
git add .
git commit -m "use different greeting in the morning"
```
And you're done! You end up with a history of three commits added, and each commit adds one feature change at a time.

## [Summary](https://developer.mozilla.org#summary)

Stashing has various use cases. I wouldn't recommend it for saving changes when switching branches. Instead I recommend making temporary commits that you can push and manage easily. I use aliases to simplify this workflow and make it less prone to mistakes. On the other hand, stashing is an excellent fit for breaking down large, related commits into smaller, individual ones. With this in mind, you can maintain a cleaner project history and ensure your work is always backed up and organized.

I hope you enjoyed reading.
If you're interested in the tests used in every commit for this post, this example project can be accessed at [https://gitlab.com/toon/greetings](https://gitlab.com/toon/greetings).

## [About the author](https://developer.mozilla.org#about_the_author)

[Toon Claes](https://iotcl.com/) is a Senior Backend Engineer at GitLab with a background in C & C++ and web and mobile development.
He's passionate about mechanical keyboards, always on the lookout for the perfect one.
A dedicated GNU Emacs user, Toon actively engages with the community and loves using Org mode for his projects.

*This is a sponsored article by GitLab. [GitLab](https://about.gitlab.com/) is a comprehensive web-based DevSecOps platform providing Git-repository management, issue-tracking, continuous integration, and deployment pipeline features. Available in both open-source and proprietary versions, it's designed to cover the entire DevOps lifecycle, making it a popular choice for teams looking for a single platform to manage both code and operational data.*