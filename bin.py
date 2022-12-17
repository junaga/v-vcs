#!/usr/bin/env python
from subprocess import run
from os import system, chdir
import click

CLI_VERSION = "0.2.0"


# relevant xkcd: https://xkcd.com/1296/
def git(args: list[str], ansi: bool = True) -> str:
    color_arg = ["-c", "color.status=always"] if ansi else []
    command = ["git"] + color_arg + args

    completed_process = run(command, capture_output=True)

    if completed_process.returncode != 0:
        print(completed_process.stdout.decode("utf-8"))
        raise Exception(completed_process.stderr.decode("utf-8"))
    else:
        return completed_process.stdout.decode("utf-8")


@click.command()
def log():
    """Show commit log"""
    system("git log --graph --oneline")


@click.command()
def ls():
    """List changes"""
    system("git status --short")


@click.command()
def diff():
    system("git difftool --no-prompt --extcmd 'code --wait --diff'")


@click.command()
@click.argument("branch", default="--root")
def rewrite(branch: str):
    """Rebase HEAD onto REF. If REF is not specified, rebase onto the root commit."""
    system("git rebase --interactive " + branch)


def stage_commit_push(message: str):
    # are there already changes staged with `$ git add FILE1 FILE2`?
    staged = git(["diff", "--cached", "--name-only"], ansi=False)

    # print the staged info section in "git status"
    if staged:
        status = git(["status"])
        start = "Changes to be committed:"
        end = "\n\n"
        print(status[status.find(start) : status.find(end)], "\n")

    if message is None:
        message = click.prompt("-m TEXT is required\nIf applied, this commit will")

    # stage all changes
    if not staged:
        git(["add", "."])

    print(git(["commit", "--message", message]), end="")


@click.group(invoke_without_command=True)  # always run function
@click.pass_context
@click.option("-d", "--directory", help="Run in this directory")
@click.option("-m", "--message", help="Commit message")
@click.option("--version", is_flag=True, help="Show the version and exit")
def main(ctx: click.Context, message: str, directory: str, version: bool = False):
    """
    Simple git wrapper

    Stage and commit and push in one command.
    If there are no changes staged, stage all changes.
    Push commits if an upstream branch is set.
    """

    if ctx.params["directory"]:
        chdir(ctx.params["directory"])

    if ctx.invoked_subcommand is None:
        if version:
            print(CLI_VERSION)
        else:
            stage_commit_push(message)


if __name__ == "__main__":
    main.add_command(ls)
    main.add_command(log)
    main.add_command(diff)
    main.add_command(rewrite)
    main()
