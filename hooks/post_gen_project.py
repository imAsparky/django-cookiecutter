#!/usr/bin/env python
"""django-cookiecutter post project generation jobs."""
import os
import subprocess  # nosec
from shutil import rmtree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

REMOTE_REPO = "git@github.com:{{cookiecutter.github_username}}/\
{{cookiecutter.git_project_name}}.git"


GIT_USER = "{{cookiecutter.author_name}}"
GIT_EMAIL = "{{cookiecutter.github_user_email}}"


REMOVE_FILES = [
    '{% if cookiecutter.use_pyup_io == "n" %} \
        .pyup.yml  {% endif %}',
    '{% if cookiecutter.include_sphinx_docs == "n" %} \
        docs {% endif %}',
    '{% if cookiecutter.use_readthedocs == "n" %} \
        .readthedocs.yaml {% endif %}',
    '{% if cookiecutter.include_contributor_covenant_code_of_conduct == "n" %} \
        docs/source/code-of-conduct.rst {% endif %}',
    '{% if cookiecutter.include_documentation_templates == "n" %} \
        docs/source/doc-templates {% endif %}',
    '{% if cookiecutter.include_how_to_contribute_template == "n" %} \
        docs/source/how-tos/how-to-contribute.rst {% endif %}',
    '{% if cookiecutter.open_source_license == "Not open source" %} \
        LICENSE.rst {% endif %}',
    '{% if cookiecutter.create_conventional_commits_edit_message == "n" %} \
        .github/.git-commit-template.txt {% endif %}',
    '{% if cookiecutter.use_pre_commit == "n" %} \
        .pre-commit-config.yaml {% endif %}',
    '{% if cookiecutter.use_GH_action_semantic_version == "n" %} \
        CHANGELOG.md {% endif %}',
    '{% if cookiecutter.use_GH_action_semantic_version == "n" %} \
        .github/semantic.yaml {% endif %}',
    '{% if cookiecutter.use_GH_action_semantic_version == "n" %} \
        .github/workflows/semantic_release.yaml {% endif %}',
    '{% if cookiecutter.create_repo_auto_test_workflow == "n" %} \
        .github/workflows/test_contribution.yaml {% endif %}',
    '{% if cookiecutter.use_GH_custom_issue_templates == "n" %} \
        .github/ISSUE_TEMPLATE {% endif %}',
    '{% if cookiecutter.use_GH_custom_issue_templates == "y" %} \
        .github/ISSUE_TEMPLATE.md {% endif %}',
    '{% if cookiecutter.deploy_with_docker == "n" %} \
        Dockerfile {% endif %}',
    '{% if cookiecutter.deploy_with_docker == "n" %} \
        .dockerignore {% endif %}',
    '{% if cookiecutter.deploy_with_docker == "n" %} \
        compose {% endif %}',
    '{% if cookiecutter.deploy_with_docker == "n" %} \
        docker-entrypoint.sh {% endif %}',
    '{% if cookiecutter.use_django_allauth == "n" %} \
        templates/account {% endif %}',
]

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


def remove_files(filepath):
    """Remove files not required for this generated Django project."""

    for path in filepath:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                rmtree(path)
            else:
                os.unlink(path)


# Git functions


def init_git():
    """Initialise git repository and set the remote."""
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        post_gen_setup(
            "git",
            "init",
            supress_exception=True,
            cwd=PROJECT_DIRECTORY,
        )

        post_gen_setup(
            "git",
            "branch",
            "-M",
            "main",
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

    remove_files(REMOVE_FILES)

    # Git options

    if "{{ cookiecutter.automatic_set_up_git_and_initial_commit }}" == "y":
        init_git()
        git_add_and_commit_initial()

        if "{{ cookiecutter.create_conventional_commits_edit_message}}" == "y":
            git_configure_custom_commit_message()
