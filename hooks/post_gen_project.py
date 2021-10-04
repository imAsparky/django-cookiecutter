#!/usr/bin/env python
"""django-cookiecutter post project generation jobs."""
import os
import subprocess  # nosec

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

REMOTE_REPO = "git@github.com:{{cookiecutter.github_username}}/\
{{cookiecutter.git_project_name}}.git"


GIT_USER = "{{cookiecutter.author_name}}"
GIT_EMAIL = "{{cookiecutter.github_user_email}}"

# Helper functions


def post_gen_setup(*args, supress_exception=False, cwd=None):
    """Helper to set up the Django project with the chosen options."""
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        with subprocess.Popen(  # nosec
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as proc:

            out, err = proc.communicate()
            out = out.decode("utf-8")
            err = err.decode("utf-8")
            if err and not supress_exception:
                raise Exception(err)
            if err and supress_exception:
                return out

            return out

    finally:
        os.chdir(cur_dir)


def recursive_force_delete_a_folder(folder_path):
    """Recursively force delete a folder. USE WITH CAUTION."""
    post_gen_setup(
        "rm",
        "-rf",
        folder_path,
        cwd=PROJECT_DIRECTORY,
    )


def remove_file(filepath):
    """Remove files not required for this generated Django project."""
    if os.path.exists(os.path.join(PROJECT_DIRECTORY, filepath)):
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


# Git functions


def init_git():
    """Initialise git repository and set the remote."""
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        post_gen_setup(
            "git",
            "init",
            "--initial-branch=main",
            cwd=PROJECT_DIRECTORY,
        )

        post_gen_setup(
            "git",
            "remote",
            "add",
            "origin",
            REMOTE_REPO,
            cwd=PROJECT_DIRECTORY,
        )
        post_gen_setup(
            "git",
            "config",
            "user.name",
            GIT_USER,
            cwd=PROJECT_DIRECTORY,
        )
        post_gen_setup(
            "git",
            "config",
            "user.email",
            GIT_EMAIL,
            cwd=PROJECT_DIRECTORY,
        )


def git_add_and_commit_initial():
    """Add the local files and commit to the git repository."""
    post_gen_setup(
        "git",
        "add",
        "-A",
        cwd=PROJECT_DIRECTORY,
    )

    post_gen_setup(
        "git",
        "commit",
        "-m",
        '"chore(git): Initial Commit"',
        cwd=PROJECT_DIRECTORY,
    )


def git_configure_custom_commit_message():
    """Configure git to use the custom commit message template."""
    if os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        post_gen_setup(
            "git",
            "config",
            "--local",
            "commit.template",
            ".github/.git-commit-template.txt",
            cwd=PROJECT_DIRECTORY,
        )


if __name__ == "__main__":

    # Documentation options

    if "{{ cookiecutter.include_sphinx_docs }}" == "n":
        recursive_force_delete_a_folder("docs")

    if "{{ cookiecutter.use_readthedocs }}" == "n":
        remove_file(".readthedocs.yaml")

    if (
        "{{ cookiecutter.include_contributor_covenant_code_of_conduct }}"
        == "n"
    ):
        remove_file("docs/source/code-of-conduct.rst")

    if "{{ cookiecutter.include_documentation_templates }}" == "n":
        recursive_force_delete_a_folder("docs/source/doc-templates")

    if "{{ cookiecutter.include_how_to_contribute_template }}" == "n":
        remove_file("docs/source/how-tos/how-to-contribute.rst")

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE.rst")

    # Git options

    if "{{ cookiecutter.create_conventional_commits_edit_message }}" == "n":
        remove_file(".github/.git-commit-template.txt")

    if "{{ cookiecutter.automatic_set_up_git_and_initial_commit }}" == "y":
        init_git()
        git_add_and_commit_initial()

        if "{{ cookiecutter.create_conventional_commits_edit_message}}" == "y":
            git_configure_custom_commit_message()

    if "{{ cookiecutter.use_GH_custom_issue_templates }}" == "y":
        remove_file(".github/ISSUE_TEMPLATE.md")
    else:
        recursive_force_delete_a_folder(".github/ISSUE_TEMPLATE")

    # Workflow options

    if "{{ cookiecutter.use_pre_commit }}" == "n":
        remove_file(".pre-commit-config.yaml")

    if "{{ cookiecutter.use_GH_action_semantic_version }}" != "y":
        remove_file("CHANGELOG.md")
        remove_file(".github/semantic.yaml")
        remove_file(".github/workflows/semantic_release.yaml")

    if "{{ cookiecutter.create_repo_auto_test_workflow }}" == "n":
        remove_file(".github/workflows/test_contribution.yaml")
