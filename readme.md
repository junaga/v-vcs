```sh
git --version && python --version && pip --version

cd $HOME
git clone https://github.com/junaga/v-vcs
cd v-vcs
pip install --upgrade --requirement dependencies

# format
python -m black ./
# test and dev
alias v="python -m $PWD/bin.py"
cd ../
cp -r v-vcs/ v-vcs-minefield/
cd v-vcs-minefield/
v WHATEVER && git WHATEVER
```

## Implemented

```sh
Usage: v [OPTIONS] COMMAND [ARGS]...

  Simple git wrapper

  Stage and commit and push in one command. If there are no changes staged,
  stage all changes. Push commits if an upstream branch is set.

Options:
  -d, --directory TEXT  Run in this directory
  -m, --message TEXT    Commit message
  --version             Show the version and exit
  --help                Show this message and exit.

Commands:
  diff
  log      Show commit log
  ls       List changes
  rewrite  Rebase HEAD onto REF.
```

## NotImplemented

- replace aliases from .gitconfig
  - `stat = log --oneline --graph --stat dev..`
- pass on rest params to appropriate git subcommands
- commands
  - `$ v status` show remotes, branches, configured upstream branches, number of commits and changes.
  - `$ v reset`
  - `$ v branch`
