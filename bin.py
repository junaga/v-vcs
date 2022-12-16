#!/usr/bin/env python
from subprocess import run
import click


# relevant xkcd: https://xkcd.com/1296/
def git(args: list[str], ansi: bool = True) -> str:
    color_arg = ["-c", "color.status=always"] if ansi else []
    command = ["git"] + color_arg + args

    completed_process = run(command, capture_output=True)

    if completed_process.returncode != 0:
        raise Exception(completed_process.stderr.decode("utf-8"))
    else:
        return completed_process.stdout.decode("utf-8")


@click.command()
@click.version_option("0.0.1")
@click.option("-m", "--message", help="commit message")
def stage_commit_push(message: str):
    """
    Stage, commit, and push.
    If there are no changes staged, stage all changes.
    If an upstream branch is set, push commits to that branch.
    """

    # todo: pass if subcommand is given

    # are there already changes staged with `$ git add FILE1 FILE2`?
    staged = git(["diff", "--cached", "--name-only"], ansi=False)

    # print the staged info section in "git status"
    if staged:
        status = git(["status"])
        start = "Changes to be committed:"
        end = "\n\n"
        print(status[status.find(start) : status.find(end)], "\n")

    if message is None:
        message = click.prompt("If applied, this commit will")

    # stage all changes
    if not staged:
        git(["add", "."])

    print(git(["commit", "--message", message]))


main = stage_commit_push

if __name__ == "__main__":
    main()
