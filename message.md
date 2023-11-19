I use a set of commit verbs, or types, similar to [conventional commits](https://www.conventionalcommits.org/).

- **new** <- feature, localize
- **fix** <- typo, fix, test
- **clean** <- style, wording, chore, refactor
- **docs** <- comment, docs
- merge <- `git merge`
- revert <- `git revert`

## Why

My strongest thought is,

> not every commit needs a type

- Refactors are so big, they dont happen in commits, they happen in branches. no point in type'ing them.
- Formatting is so essential it should happen in a script. just commit the script name `npm run fmt` executed.
- Tests are either required, or overengineered.
