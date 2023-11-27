I use a set of commit verbs, or types, similar to [conventional commits](https://www.conventionalcommits.org/).

- **new** <- feature
- **fix** <- fix, bug, test, localize
- **docs** <- typo, comment, docs
- **clean** <- style, wording, chore, refactor
- merge <- `git merge`
- revert <- `git revert`

## Why

> not every commit needs a type

The lack of a commit type should incentive to look, at the changes, or the multiline commit message.

- Refactors are so big, they dont happen in commits, they happen in branches. no point in type'ing them.
- Formatting is so essential it should happen in a script. just commit the script name executed (`npm run fmt`).
- Tests are either required, or overengineered.
- Locals are either required, or overengineered.
