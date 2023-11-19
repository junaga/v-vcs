#!/usr/bin/env python3
from subprocess import run
from os import system, chdir
import click

CLI_VERSION = "0.3.0"


# relevant xkcd: https://xkcd.com/1296/
def git(args: list[str], ansi: bool = True) -> str:
    color_arg = ["-c", "color.status=always"] if ansi else []
    command = ["git"] + color_arg + args

    completed_process = run(command, capture_output=True)
    stdout = completed_process.stdout.decode("utf-8")
    stderr = completed_process.stderr.decode("utf-8")

    if completed_process.returncode != 0:
        raise Exception(stdout + stderr)
    else:
        return stdout + stderr


@click.command()
def ls():
    """List changes"""
    system("git status --short")


@click.command()
def fix():
    """
    Stage and amend (rewrite) last commit

    If there are no changes staged, stage all changes.
    """

    # are changes staged - `$ git add $FILE1 $FILE2`?
    staged = git(["diff", "--cached", "--name-only"], ansi=False)

    # print the staged info section in "git status"
    if staged:
        status = git(["status"])
        start = "Changes to be committed:"
        end = "\n\n"
        print(status[status.find(start) : status.find(end)], "\n")

    # stage all changes
    if not staged:
        print(git(["add", "./"]), end="")

    print(git(["commit", "--amend", "--no-edit"]), end="")


@click.group(invoke_without_command=True)
def log():
    """Show commit log"""
    system("git log --graph --oneline")


@log.command()
def all():
    """Show commit log for all branches"""
    system("git log --graph --oneline --branches")


@click.command()
def diff():
    """WIP $EDITOR diff view"""
    system("git difftool --no-prompt --extcmd 'code --diff'")


@click.command()
def reset():
    """Delete all changes and untracked files"""
    system("git reset --hard HEAD && git clean --force -d")


@click.command()
@click.argument("branch", default="--root")
def rewrite(branch: str):
    """(interactive rebase)"""
    system("git rebase --interactive " + branch)


def stage_commit(message: str):
    # are there already changes staged with `$ git add $FILE1 $FILE2`?
    staged = git(["diff", "--cached", "--name-only"], ansi=False)

    # print the staged info section in "git status"
    if staged:
        status = git(["status"])
        start = "Changes to be committed:"
        end = "\n\n"
        print(status[status.find(start) : status.find(end)], "\n")

    stdin = click.get_text_stream("stdin").read()

    if stdin and message:
        raise Exception("Error: Commmit message set twice, by `/dev/stdin` and `-m`.")

    if stdin is None and message is None:
        message = click.prompt("-m TEXT is required\nIf applied, this commit will")

    if stdin:
        message = stdin

    # stage all changes
    if not staged:
        print(git(["add", "."]), end="")

    print(git(["commit", "--message", message]), end="")


@click.group(invoke_without_command=True)  # always run function
@click.pass_context
@click.option("-m", "--message", help="Commit message")
@click.option("-d", "--directory", help="Run in this directory")
@click.option("--version", is_flag=True, help="Show the version and exit")
def main(ctx: click.Context, message: str, directory: str, version: bool = False):
    """
    Simple git wrapper. Stage and commit.

    If there are no changes staged, stage all changes.
    """

    if ctx.params["directory"]:
        chdir(ctx.params["directory"])

    if ctx.invoked_subcommand is None:
        if version:
            print(CLI_VERSION)
        else:
            stage_commit(message)


if __name__ == "__main__":
    main.add_command(log)
    main.add_command(diff)
    main.add_command(reset)
    main.add_command(rewrite)
    main.add_command(fix)
    main.add_command(ls)
    main()
