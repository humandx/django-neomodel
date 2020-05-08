from django import setup as setup_django
from django.core.management.base import BaseCommand

from neomodel import remove_all_labels


class Command(BaseCommand):
    help = 'Removes labels and constraints for your neo4j database'

    def handle(self, *args, **options):
        setup_django()
        remove_all_labels(stdout=self.stdout)