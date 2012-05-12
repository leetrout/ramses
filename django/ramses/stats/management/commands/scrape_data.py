from xml.etree import ElementTree

from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
import requests

from stats.models import Player, Team


class Command(BaseCommand):
    
    args = '<team_id>'
    help = 'Loads data for the given team'
    
    url = 'http://alexgmcclelland.com/McClelland_Project3/player_stats.xml'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Expected 1 argument, got %d' % len(args))
        try:
            team = Team.objects.get(pk=args[0])
            self.stdout.write('Adding players to team "%s"\n' % team)
        except Team.DoesNotExist:
            raise CommandError('Team %s does not exist' % args[0])
        self.stdout.write('Requesting data from "%s"\n' % self.url)
        resp = requests.get(self.url)
        rcode = resp.status_code
        if rcode == 200:
            self.stdout.write('Response received "%s"\n' % rcode)
            xml_tree = ElementTree.fromstring(resp.text)
            players = xml_tree.findall('player')
            self.stdout.write('Found %d players...\n' % len(players))
            for player in players:
                fn = player.find('first_name').text
                ln = player.find('last_name').text
                
                player_args = {
                    "first_name": fn,
                    "last_name": ln,
                    "slug": slugify("%s %s" % (fn, ln)),
                    "team": team
                }
                
                plyr, created = Player.objects.get_or_create(**player_args)
                
                if created:
                    self.stdout.write('Created player %s %s\n' % (fn, ln))
                else:
                    self.stdout.write('Skipping player %s %s\n' % (fn, ln))
        else:
            raise CommandError('Received response code "%s", expected 200'
                               % rcode)
