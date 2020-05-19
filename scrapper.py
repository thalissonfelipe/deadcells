import re
import json
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.url = 'https://deadcells.gamepedia.com/'
        self.data = {}

    def insert(self, data):
        if data['name'] not in self.data:
            self.data[data['name']] = {}
        self.data[data['name']] = data

    def get(self, name):
        if name not in self.data:
            return None
        return self.data[name]

    def get_gears(self):
        html = requests.get(self.url + 'Gear')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            tables = soup.select('.wikitable.sortable')

            data = []
            keys = [
                'image', 'name', 'description',
                'location', 'base_dps', 'special_dps', 'scaling'
            ]
            gear_types = [
                'malee_weapons', 'ranged_weapons', 'shields',
                'traps_and_turrets', 'grenades', 'powers', 'amulets'
            ]
            # remove intermiate table and set amulet type to six position
            del tables[6]

            for i, (table, gear_type) in enumerate(zip(tables, gear_types)):
                gear = {
                    'type': gear_type,
                    'gears': []
                }
                for tr in table.find_all('tr')[1:]:
                    item = {}
                    # amulet case
                    if i == 6:
                        keys = ['name', 'image']
                    for td, key in zip(tr.find_all('td'), keys):
                        if key == 'image':
                            item[key] = td.find('img')['src']
                        elif key == 'scaling':
                            value = td.find('img')
                            if value:
                                item[key] = td.find('img')['src']
                            else:
                                item[key] = td.text.strip()
                        else:
                            item[key] = re.sub('\n', ' ', td.text.strip())
                    gear['gears'].append(item)
                    data.append(gear)

            return {'name': 'gears', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_enemies(self):
        html = requests.get(self.url + 'Enemies')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            table = soup.select('.wikitable.sortable')[0]

            data = []
            keys = [
                'image', 'name', 'zones',
                'offensive_abilities', 'deffensive_abilities',
                'elite', 'cell_drops', 'blueprint_drops'
            ]

            for tr in table.find_all('tr')[1:]:
                enemy_dict = {}
                for td, key in zip(tr.find_all('td'), keys):
                    if key == 'image':
                        enemy_dict[key] = td.find('img')['src']
                    else:
                        value = re.sub('• ', '', td.text.strip()).split('\n')
                        enemy_dict[key] = \
                            value[0] if len(value) == 1 else value
                data.append(enemy_dict)

            return {'name': 'enemies', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_runes(self):
        html = requests.get(self.url + 'Runes')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            table = soup.select('.wikitable')[0]

            data = []
            keys = [
                'name', 'image', 'biome',
                'location', 'enemy', 'ability', 'access'
            ]

            for tr in table.find_all('tr')[1:]:
                rune = {}
                for td, key in zip(tr.find_all('td'), keys):
                    if key == 'image':
                        rune[key] = td.find('img')['src']
                    else:
                        value = td.text.strip().split('\n')
                        if key == 'access':
                            value = [v.strip() for v in value[0].split(',')]
                        rune[key] = value[0] if len(value) == 1 else value
                data.append(rune)

            return {'name': 'runes', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_achievements(self):
        html = requests.get(self.url + 'Achievements_and_Trophies')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            table = soup.select('.wikitable.sortable')[0]

            data = []
            keys = ['image', 'name', 'description', 'score', 'trophy']

            for tr in table.find_all('tr')[1:]:
                achievement = {}
                for td, key in zip(tr.find_all('td'), keys):
                    if key == 'image':
                        achievement[key] = td.find('img')['src']
                    else:
                        achievement[key] = td.text.strip()
                data.append(achievement)

            return {'name': 'achievements', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_outfits(self):
        html = requests.get(self.url + 'Outfits')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            table = soup.select('.wikitable.sortable')[0]

            data = []
            keys = [
                'image', 'name', 'description', 'location',
                'difficulty_required', 'cell_cost', 'reference'
            ]

            for tr in table.find_all('tr')[1:]:
                outfit = {}
                for td, key in zip(tr.find_all('td'), keys):
                    if key == 'image':
                        outfit[key] = td.find('img')['src']
                    else:
                        outfit[key] = td.text.strip()
                data.append(outfit)

            return {'name': 'outfits', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_mutations(self):
        html = requests.get(self.url + 'Mutations')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            tables = soup.select('.wikitable')

            data = []
            keys = [
                'name', 'image', 'description',
                'acquisition_method', 'unlock_cost', 'notes'
            ]
            mutation_types = ['brutality', 'tactics', 'survival', 'colorless']

            for table, mutation_type in zip(tables, mutation_types):
                mutation = {
                    'type': mutation_type,
                    'mutations': []
                }
                for tr in table.find_all('tr')[1:]:
                    item = {}
                    for td, key in zip(tr.find_all('td'), keys):
                        if key == 'image':
                            item[key] = td.find('img')['src']
                        else:
                            value = td.text.strip().split('\n')
                            item[key] = value[0] if len(value) == 1 else value
                    mutation['mutations'].append(item)
                data.append(mutation)

            return {'name': 'mutations', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_biome(self, biome):
        html = requests.get(self.url + biome)
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')

            if (
                biome == 'Black_Bridge' or
                biome == 'Guardian%27s_Haven' or
                biome == 'Throne_Room' or
                biome == 'Astrolab'
            ):
                table = soup.find_all('table')[2].find('tbody')
            else:
                table = soup.find('table').find('table').find('tbody')

            if biome == 'Prisoners%27_Quarters':
                biome = 'Prisoners_Quarters'
            elif biome == 'Guardian%27s_Haven':
                biome = 'Guardians_Haven'
            biome = {'name': re.sub('_', ' ', biome)}

            for tr in table.find_all('tr')[1:]:
                tds = tr.find_all('td')
                for i in range(0, len(tds)-1, 2):
                    key = re.sub('[#:]', '', tds[i].text.strip().lower())
                    value = tds[i+1].text.strip().split('\n')
                    biome[re.sub(' ', '_', key)] = \
                        value[0] if len(value) == 1 else value

            if 'stage_' in biome:
                biome['stage'] = biome.pop('stage_')
            else:
                biome['stage'] = 'boss_stage'

            return biome
        else:
            raise Exception('Requests Exception')

    def get_biomes(self):
        biomes = [
            'Prisoners%27_Quarters', 'Promenade_of_the_Condemned',
            'Toxic_Sewers', 'Dilapidated_Arboretum', 'Prison_Depths',
            'Corrupted_Prison', 'Ramparts', 'Ancient_Sewers', 'Ossuary',
            'Morass_of_the_Banished', 'Black_Bridge', 'Insufferable_Crypt',
            'Nest', 'Stilt_Village', 'Graveyard', 'Slumbering_Sanctuary',
            'Forgotten_Sepulcher', 'Clock_Tower', 'Cavern', 'Clock_Room',
            'Guardian%27s_Haven', 'High_Peak_Castle', 'Throne_Room',
            'Astrolab', 'Observatory'
        ]

        data = [self.get_biome(biome) for biome in biomes]

        return {'name': 'biomes', 'data': data}

    def get_boss(self, boss):
        html = requests.get(self.url + boss)
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')

            if (
                boss == 'Mama_Tick' or
                boss == 'The_Collector_(Boss)' or
                boss == 'Conjonctivius'
            ):
                table = soup.find_all('table')[1]
            else:
                table = soup.find('table').find('tbody')

            if boss == 'The_Collector_(Boss)':
                boss = 'The Collector'
            boss = {'name': re.sub('_', ' ', boss)}

            for tr in table.find_all('tr')[1:]:
                tds = tr.find_all('td')
                for i in range(0, len(tds)-1, 2):
                    value = tds[i+1].text.strip().split('\n')
                    boss[tds[i].text.strip().lower()] = \
                        value[0] if len(value) == 1 else value

            return boss
        else:
            raise Exception('Requests Exception')

    def get_bosses(self):
        bosses = [
            'The_Concierge', 'Conjonctivius', 'Mama_Tick', 'The_Time_Keeper',
            'The_Giant', 'The_Hand_of_the_King', 'The_Collector_(Boss)'
        ]

        data = [self.get_boss(boss) for boss in bosses]

        return {'name': 'bosses', 'data': data}

    def get_npcs(self):
        html = requests.get(self.url + 'NPCs')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            table = soup.find('table')

            data, keys = [], ['name', 'info', 'location', 'image']

            for tr in table.find_all('tr')[1:]:
                npc = {}
                for td, key in zip(tr.find_all('td'), keys):
                    if key == 'image':
                        npc[key] = td.find('img')['src']
                    else:
                        npc[key] = re.sub('\n', ' ', td.text.strip())
                data.append(npc)

            return {'name': 'npcs', 'data': data}
        else:
            raise Exception('Requests Exception')

    def get_pickups(self):
        html = requests.get(self.url + 'Pickups')
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            tables = soup.find_all('table')

            data = []
            keys = {
                'gems': [
                    'name', 'image', 'description', 'value_range', 'sources'
                ],
                'minor_foods': ['name', 'image', 'diet'],
                'major_foods': ['name', 'image', 'diet'],
                'scrolls': ['name', 'image', 'effect', 'sources'],
                'keys': ['name', 'image', 'location', 'description']
            }
            pickup_types = [
                'gems', 'minor_foods', 'major_foods', 'scrolls', 'keys'
            ]

            for table, pickup_type in zip(tables, pickup_types):
                pickup = {
                    'type': pickup_type,
                    'pickups': []
                }
                for tr in table.find_all('tr')[1:]:
                    item = {}
                    for td, key in zip(tr.find_all('td'), keys[pickup_type]):
                        if key == 'image':
                            item[key] = td.find('img')['src']
                        else:
                            item[key] = td.text.strip()
                    pickup['pickups'].append(item)
                data.append(pickup)

            return {'name': 'pickups', 'data': data}
        else:
            raise Exception('Requests Exception')

    def save(self, data, filename):
        with open('data/' + filename, 'w') as file:
            json.dump(data, file, indent=4)
