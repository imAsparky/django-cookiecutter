"""A Django command line tool to delete migration files and dbsqlite in local development."""
import os
import subprocess  # nosec
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Delete app migrations, dbsqlite then makemigrations, migrate and load fixtures.

    .. warning::

        This only deletes the db and migration files.

        Migrations and fixture loading is not implemtented.

    """

    def __init__(self, request=None, *args, **kwargs):
        """Initialise the Basecommand with some local variables.

        Paramaters
        ----------

        :param PROJECT_APPS: A list of only the projects applications.
        :param DB_PATH: A posix path to the local dbsqlite3 db.
        :param PROJECT_ROOT: A posix path to the projects root folder.

        """

        # TODO Fix this...Make sure any changes to migrations are
        # reflected in the testing app.  Makemigrations using this doesnt work.
        # testing_core.migrations is excluded from file deletions in the mean time.
        self.PROJECT_APPS = settings.PROJECT_APPS + [
            "testing_core",
        ]  # noqa: F405

        self.DB_PATH = Path(settings.BASE_DIR / "db.sqlite3")  # noqa: F405
        self.PROJECT_ROOT = Path(settings.BASE_DIR)  # noqa: F405

        self.request = request

        super().__init__(*args, **kwargs)

    def _check_in_debug(self) -> bool:
        """Check that we are in DEBUG and wont be breaking Production DB"""
        if settings.DEBUG:
            return True
        else:
            self.stdout.write(self.style.ERROR("Exiting, not in DEBUG!"))
            return False

    def _delete_dbsqlite3(self) -> bool:
        """If dbsqlite exist, delete and return true, else exit."""

        if Path(self.DB_PATH).is_file():
            # If the database file exists alert user in the console of  the
            # actions taken or ....>
            try:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"DATABASE PATH EXISTS: {str(self.DB_PATH)}"
                    )
                )
                self.stdout.write(
                    self.style.WARNING(
                        f"\tDELETING DATABASE: {str(self.DB_PATH)}"
                    )
                )

                # Delete DB
                self.DB_PATH.unlink()

                if not Path(self.DB_PATH).is_file():
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"\tSUCESSFULLY DELETED {str(self.DB_PATH)}"
                        )
                    )

                return True

            except OSError as e:
                # <... Alert user in console if db failed to delete.

                self.stdout.write(
                    self.style.ERROR(
                        f"\nDELETION ERROR : {str(self.DB_PATH)}::{e.strerror}"
                    )
                )

                return False
        else:
            self.stdout.write(
                self.style.ERROR(
                    f"\n\nERROR: db.sqlite3 {str(self.DB_PATH)} Does not Exist"
                )
            )

            return False

    def _delete_migration_files(
        self, delete_app: str = None
    ) -> None:  # noqa: C901
        """Find, list and delete the required migration files.

        Paramaters
        ----------

        :param delete_app:
            User supplied string of the ``app name`` for migration deletions.


        Private Params
        --------------

        :param _delete_migrations:  :py:class: ``Dict``
                key: App name as string.
                value:  _migration_files_for_deletion as List.

        :param _deletion_errors:  :py:class: ``List``
                A list of ``strings`` of the migration file with ``OS.errors``.

        .. warning::

            This feature is currently incomplete.
            Only full migration deletions has been implemented.


        """
        _delete_migrations: dict = {}
        _deletion_errors: list = []

        if not delete_app:
            """Delete all migration files."""

            for app_name in self.PROJECT_APPS:
                # Check that the path is a valid directory.
                if Path(
                    self.PROJECT_ROOT
                    / app_name.replace(".", "/")
                    / "migrations"
                ).is_dir():
                    self.stdout.write(f"MARKED FOR DELETION::{app_name}")

                    _migration_files_for_deletion: list = []
                    # Get a list of migration files in the app and add to
                    # a deletion dict as a file path.
                    # TODO:
                    for file_path in Path(
                        self.PROJECT_ROOT
                        / app_name.replace(".", "/")
                        / "migrations"
                    ).iterdir():
                        # Dont delete __init__ , testing_core and check the
                        # path is a file first.
                        if (
                            "__init__" not in str(file_path)
                            and "testing_core" not in str(file_path)
                            and file_path.is_file()
                        ):
                            self.stdout.write(
                                self.style.WARNING(f"\t {file_path}")
                            )

                            _migration_files_for_deletion.append(file_path)

                    _delete_migrations[
                        app_name
                    ] = _migration_files_for_deletion

            for app_name, migration_file_path in _delete_migrations.items():
                if migration_file_path:
                    # Alert user in console that the app migrations deletion is
                    # in progress for.
                    self.stdout.write(
                        self.style.NOTICE(
                            f"Deleting Migrations for App:{app_name}"
                        )
                    )

                    for file_path in migration_file_path:
                        try:
                            file_path.unlink()
                            # If file deleted ok,  print success message to console.
                            if not file_path.is_file():
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"\t\t  Delete Successful: \t{str(file_path)}"
                                    )
                                )

                        except OSError as e:
                            _deletion_errors.append(
                                f"{file_path}::ERROR::{e.strerror}"
                            )

                else:
                    # Alert user in the console if no migration files exist.
                    self.stdout.write(
                        self.style.WARNING(
                            f"No migration files to delete\tApp:{app_name}"
                        )
                    )

            if _deletion_errors:
                # Alert user in console of file deletion errors.
                self.stdout.write(
                    self.style.WARNING("Migration Deletion Errors\n")
                )

                for file_error in _deletion_errors:
                    self.stdout.write(self.style.ERROR(f"\t {file_error}"))

        else:
            self.stdout.write(
                self.style.ERROR(
                    f"SINGLE APP:{delete_app} DELETION IS NOT IMPLEMENTED \n Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

            # TODO Complete this functionality.
            # Delete only user specified app migration files.
            # Check if the user supplied app exist and if not ...>
            # if delete_app in self.PROJECT_APPS:
            #     self.stdout.write(
            #         self.style.WARNING(f"Delete migrations for App:{delete_app}")
            #     )
            # else:
            #     # <... Alert user in console that app name does not exist
            #     self.stdout.write(
            #         self.style.ERROR(f"Error: {delete_app} does not exist.")
            #     )

    # +++++++++++++ manage.py methods +++++++++++++

    def _run_manage_py_with_command(
        self, *args, supress_exception=False, cwd=None
    ):
        """Helper to set up Django manage.py in a subprocess."""
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

    def _makemigrations(self) -> bool:
        """Instantiate a subprocess and makemigrations."""

        try:
            self._run_manage_py_with_command(
                "./manage.py",
                "makemigrations",
                supress_exception=False,
                cwd=self.PROJECT_ROOT,
            )

            self.stdout.write(self.style.SUCCESS("SUCCESS: makemigrations"))

            return True

        except OSError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"makemigrations::ERROR::{e.strerror}::Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

    def _migrate(self) -> bool:
        """Instantiate a subprocess and migrate."""

        try:
            self._run_manage_py_with_command(
                "./manage.py",
                "migrate",
                supress_exception=False,
                cwd=self.PROJECT_ROOT,
            )

            self.stdout.write(self.style.SUCCESS("SUCCESS: migrate"))

            return True

        except OSError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"migrate::ERROR::{e.strerror}::Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

    def _createsuperuser_ryan(self) -> bool:
        """Instantiate a subprocess and createsuperuser_ryan."""

        try:
            self._run_manage_py_with_command(
                "./manage.py",
                "createsuperuser_for_testing",
                "--username=user1",
                "--password=user1",
                "--email=user1@user1.com",
                supress_exception=False,
                cwd=self.PROJECT_ROOT,
            )

            self.stdout.write(
                self.style.SUCCESS("SUCCESS: createsuperuser::ryan")
            )

            return True

        except OSError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"createsuperuser-ryan::ERROR::{e.strerror}::Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

    def _createsuperuser_mark(self) -> bool:
        """Instantiate a subprocess and createsuperuser_mark."""

        try:
            self._run_manage_py_with_command(
                "./manage.py",
                "createsuperuser_for_testing",
                "--username=user2",
                "--password=user2",
                "--email=user2@user2.com",
                supress_exception=False,
                cwd=self.PROJECT_ROOT,
            )

            self.stdout.write(
                self.style.SUCCESS("SUCCESS: createsuperuser::mark")
            )

            return True

        except OSError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"createsuperuser-mark::ERROR::{e.strerror}::Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

    def _loadfixtures(self):
        fixtures_path = Path(settings.BASE_DIR / "core/management/fixtures")

        fixtures_list = list(x for x in fixtures_path.iterdir())
        fixtures_list.sort()

        print(f"\nFIXTURES {fixtures_list}")

        fixtures_list_print: str = ""

        for fix in fixtures_list:
            fixtures_list_print += str(fix) + "\n\t"

        self.stdout.write(
            self.style.WARNING(
                f"Loading {len(fixtures_list)} fixtures\n\t{fixtures_list_print}"
            )
        )

        try:
            for fixture in fixtures_list:
                self._run_manage_py_with_command(
                    "./manage.py",
                    "loaddata",
                    fixture,
                    supress_exception=False,
                    cwd=self.PROJECT_ROOT,
                )

                self.stdout.write(
                    self.style.SUCCESS(f"SUCCESS: Loading {fixture}")
                )

                # return True

        except OSError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Loading fixture {fixture}::ERROR::{e.strerror}::Exiting nuke_db_sqlite"
                )
            )

            raise SystemExit(1)

    # +++++++++++++ BASECOMMAND Overrides +++++++++++++

    def add_arguments(self, parser):
        parser.add_argument(
            "-D",
            "--delete_dbsqlite",
            action="store_true",
            default=True,
            help="Delete Django Project dbsqlite3",
        )

        parser.add_argument(
            "-A",
            "--app_name",
            # required=True
            action="store_true",
            help="Provide the Django App name for migrations deletion",
            default=None,
        )

        parser.add_argument(
            "-F",
            "--fixtures",
            # required=True
            action="store_true",
            help="Delete all migrations, migrate and load fixtures",
            default=None,
        )

    def handle(self, *args, **options):
        if self._check_in_debug():
            if options["fixtures"]:
                self._delete_dbsqlite3()
                self._delete_migration_files()
                self._makemigrations()
                self._migrate()
                self._loadfixtures()

            if options["delete_dbsqlite"]:
                if (
                    not input(
                        "You are about to delete all migrations and your local dbsqlite3 DB, proceed [y,n]"
                    )
                    == "y"
                ):
                    self.stdout.write(
                        self.style.ERROR(
                            "User aborted::Exiting nuke_db_sqlite"
                        )
                    )

                    raise SystemExit(2)

                if self._delete_dbsqlite3():
                    # If the database has been deleted successfully delete migrations.
                    self._delete_migration_files()
                    self._makemigrations()
                    self._migrate()

                    valid_choices: list = ["", "1", "2", "3"]

                    choice = input(
                        "Select a value default [1].\nEnter [1] Load fixtures.\nEnter [2] Create two superusers.\nEnter [3] Exit with an empty database."
                    )

                    counter: int = 1
                    while choice not in valid_choices:
                        if counter == 3:
                            self.stdout.write(
                                self.style.ERROR(
                                    "Exiting nuke_db, to many failed selection attempts.\n\tMigrations are complete and you have an empty database."
                                )
                            )

                            raise SystemExit(1)

                        choice = input(
                            "That option is not available.\nPlease select from options below default[1].\nEnter [1] Load fixtures.\nEnter [2] Create two superusers.\nEnter [3] Exit with an empty database."
                        )
                        counter += 1

                    match choice:
                        case "":
                            self._loadfixtures()

                            self.stdout.write(
                                self.style.SUCCESS(
                                    "Exiting nuke_db.\n\tMigrations are complete.\n\tYour fixtures have been loaded."
                                )
                            )

                            raise SystemExit(0)

                        case "1":
                            self._loadfixtures()

                            self.stdout.write(
                                self.style.SUCCESS(
                                    "Exiting nuke_db.\n\tMigrations are complete.\n\tYour fixtures have been loaded."
                                )
                            )

                            raise SystemExit(0)

                        case "2":
                            self._createsuperuser_ryan()
                            self._createsuperuser_mark()

                            self.stdout.write(
                                self.style.SUCCESS(
                                    "Exiting nuke_db.\n\tMigrations are complete.\n\tYou have two superusers in your database."
                                )
                            )

                            raise SystemExit(0)

                        case "3":
                            self.stdout.write(
                                self.style.SUCCESS(
                                    "Exiting nuke_db.\n\tMigrations are complete and you have an empty database."
                                )
                            )

                            raise SystemExit(0)

                else:
                    self.stdout.write(
                        self.style.ERROR("ERROR: Exiting nuke_db_sqlite")
                    )
                    # https://adamj.eu/tech/2021/10/10/the-many-ways-to-exit-in-python/
                    raise SystemExit(1)

            else:
                self.stdout.write(
                    self.style.ERROR(
                        "Deleting only Migration files, DB will not be deleted."
                    )
                )

                self._delete_migration_files()
        else:
            self.stdout.write(
                self.style.ERROR(
                    "ERROR: Not in DEBUG mode::Exiting nuke_db_sqlite"
                )
            )
            # https://adamj.eu/tech/2021/10/10/the-many-ways-to-exit-in-python/
            # https://www.youtube.com/watch?v=ZbeSPc5wL0g explains why to use this approach.
            raise SystemExit(1)
