## `v --help`

```ini
Usage: v [OPTIONS] [COMMAND] [ARGS]...

  Simple git wrapper. Stage and commit.

  If there are no changes staged, stage all changes.

Options:
  -m, --message TEXT    Commit message
  -d, --directory TEXT  Run in this directory
  --version             Show the version and exit
  --help                Show this message and exit.

Commands:
  diff     WIP $EDITOR diff view
  fix      Stage and amend (rewrite) last commit
  log      Show commit log
  ls       List changes
  reset    Delete all changes and untracked files
  rewrite  (interactive rebase)
```

## NotImplemented

- replace aliases from .gitconfig
  - `stat = log --oneline --graph --stat dev..`
- pass on rest params to appropriate git subcommands
- commands
  - `$ v status` show remotes, branches, configured upstream branches, number of commits and changes.
  - `$ v exec` run a shell command, make a commit with the command line
  - `$ v branch`
