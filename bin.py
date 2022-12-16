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
def ls():
    print(git(["status", "--short"]), end="")


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
        message = click.prompt("If applied, this commit will")

    # stage all changes
    if not staged:
        git(["add", "."])

    print(git(["commit", "--message", message]), end="")


@click.group(invoke_without_command=True)  # always run function
@click.pass_context
@click.option("-m", "--message", help="Commit message")
@click.option("--version", is_flag=True, help="Show the version and exit")
def main(ctx: click.Context, message: str, version: bool):
    """
    Simple git wrapper.

    Stage and commit and push in one command.
    If there are no changes staged, stage all changes.
    Push commits if an upstream branch is set.
    """

    if ctx.invoked_subcommand is None:
        if version:
            print("0.1.0")
            return

        stage_commit_push(message)


if __name__ == "__main__":
    main.add_command(ls)
    main()
