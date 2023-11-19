```sh
git --version # 2
python3 --version # 3
pip --version
```

```sh
cd $HOME
git clone https://github.com/junaga/v-vcs
cd v-vcs
pip install --upgrade --requirement dependencies

# format
python3 -m black ./

# test
alias v="python3 $PWD/bin.py"
cd ../
cp -r v-vcs/ v-vcs-minefield/
cd v-vcs-minefield/
v WHATEVER && git WHATEVER
```
