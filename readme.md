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

## todo

### replace aliases from .gitconfig

- `ls = status -sb`
- `stat = log --oneline --graph --stat dev..`

### implement these commands

- `$ v` => (stage_commit_push)
- maybe: `$ v status`
- `$ v ls`
- `$ v branch`
- `$ v log`
