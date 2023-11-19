1. `$ python3 --version` 3
2. Download `./bin.py`
3. [`sudo`] Save as `/usr/local/bin/v`
4. [`sudo`] `$ chmod +x /usr/local/bin/v`
5. [close, open, the terminal]
6. `$ v --version`

## Implemented

```sh
Usage: v [OPTIONS] COMMAND [ARGS]...

  Simple git wrapper

  Stage and commit in one command. If there are no changes staged, stage all
  changes.

Options:
  -d, --directory TEXT  Run in this directory
  -m, --message TEXT    Commit message
  --version             Show the version and exit
  --help                Show this message and exit.

Commands:
  diff
  fix      Stage and amend (rewrite) latest commit
  log      Show commit log
  ls       List changes
  reset    Reset the working tree and index to HEAD
  rewrite  Rebase HEAD onto REF.
```

## NotImplemented

- replace aliases from .gitconfig
  - `stat = log --oneline --graph --stat dev..`
- pass on rest params to appropriate git subcommands
- commands
  - `$ v status` show remotes, branches, configured upstream branches, number of commits and changes.
  - `$ v exec` run a shell command, make a commit with the command line
  - `$ v branch`
