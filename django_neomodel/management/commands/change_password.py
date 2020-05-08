from django.core.management.base import BaseCommand

from neomodel import db, change_neo4j_password


class Command(BaseCommand):
    help = 'Changes the password for your neo4j database'

    def add_arguments(self, parser):
        parser.add_argument(
            "--password",
            dest = "password",
            type = str,
            help = (
                """New password for your Neo4j database."""
            )
        )
    
    def handle(self, *args, **options):
        password = options.get("password")
        if not password:
            self.stdout.write('No password provided, quitting..\n')
            return

        self.stdout.write('Changing password..\n')
        change_neo4j_password(db, password)
        self.stdout.write('Done.\n')