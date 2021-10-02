#!/usr/bin/env python
"""django-cookiecutter post project generation jobs."""
# import os
# import subprocess  # nosec

# PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# REMOTE_REPO = "git@github.com:{{cookiecutter.github_username}}/\
# {{cookiecutter.git_project_name}}.git"


# GIT_USER = "{{cookiecutter.author_name}}"
# GIT_EMAIL = "{{cookiecutter.github_user_email}}"


# def post_gen_setup(*args, supress_exception=False, cwd=None):
#     """Helper to set up the Django project with the chosen options."""
#     cur_dir = os.getcwd()

#     try:
#         if cwd:
#             os.chdir(cwd)

#         with subprocess.Popen(  # nosec
#             args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
#         ) as proc:

#             out, err = proc.communicate()
#             out = out.decode("utf-8")
#             err = err.decode("utf-8")
#             if err and not supress_exception:
#                 raise Exception(err)
#             if err and supress_exception:
#                 return out

#             return out

#     finally:
#         os.chdir(cur_dir)


# def init_git():
#     """Initialise git repository and set the remote."""
#     if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
#         post_gen_setup(
#             "git",
#             "init",
#             "--initial-branch=main",
#             cwd=PROJECT_DIRECTORY,
#         )

#         post_gen_setup(
#             "git",
#             "remote",
#             "add",
#             "origin",
#             REMOTE_REPO,
#             cwd=PROJECT_DIRECTORY,
#         )
#         post_gen_setup(
#             "git",
#             "config",
#             "user.name",
#             GIT_USER,
#             cwd=PROJECT_DIRECTORY,
#         )
#         post_gen_setup(
#             "git",
#             "config",
#             "user.email",
#             GIT_EMAIL,
#             cwd=PROJECT_DIRECTORY,
#         )


# def git_add_and_commit_initial():
#     """Add the local files and commit to the git repository."""
#     post_gen_setup(
#         "git",
#         "add",
#         "-A",
#         cwd=PROJECT_DIRECTORY,
#     )

#     post_gen_setup(
#         "git",
#         "commit",
#         "-m",
#         '"chore(git): Initial Commit"',
#         cwd=PROJECT_DIRECTORY,
#     )


# def git_configure_custom_commit_message():
#     """Configure git to use the custom commit message template."""
#     if os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
#         post_gen_setup(
#             "git",
#             "config",
#             "--local",
#             "commit.template",
#             ".github/.git-commit-template.txt",
#             cwd=PROJECT_DIRECTORY,
#         )


# def remove_file(filepath):
#     """Remove files not required for this generated python package."""
#     if os.path.exists(os.path.join(PROJECT_DIRECTORY, filepath)):
#         os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    print("In main")


# if "Not open source" == "{{ cookiecutter.open_source_license }}":
#     remove_file("LICENSE")

# if "{{ cookiecutter.create_conventional_commits_edit_message }}" != "y":
#     remove_file(".github/.git-commit-template.txt")

# if "{{ cookiecutter.create_repo_auto_test_workflow }}" != "y":
#     remove_file(".github/workflows/test_contribution.yaml")

# if "{{ cookiecutter.use_GH_action_semantic_version }}" != "y":
#     remove_file(".github/workflows/semantic_release.yaml")
#     remove_file(".github/semantic.yaml")

# if "{{ cookiecutter.use_GH_action_semantic_version }}" == "y":
#     remove_file("HISTORY.rst")

# if "{{ cookiecutter.use_GH_custom_issue_templates }}" != "y":
#     remove_file(".github/ISSUE_TEMPLATE/bug-report.md")
#     remove_file(".github/ISSUE_TEMPLATE/chore.md")
#     remove_file(".github/ISSUE_TEMPLATE/documentation-request.md")
#     remove_file(".github/ISSUE_TEMPLATE/feature-request.md")

# if "{{ cookiecutter.use_GH_custom_issue_templates }}" == "y":
#     remove_file(".github/ISSUE_TEMPLATE.md")

# if "{{ cookiecutter.use_pre_commit }}" != "y":
#     remove_file(".pre-commit-config.yaml")

# if "{{ cookiecutter.automatic_set_up_git_and_initial_commit }}" == "y":
#     init_git()
#     git_add_and_commit_initial()

#     if "{{ cookiecutter.create_conventional_commits_edit_message}}" == "y":
#         git_configure_custom_commit_message()
