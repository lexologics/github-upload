import csv
from collections import defaultdict, Counter

with open('data\\survey_results_public.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    # total = 0

    # counts = defaultdict(int)
    # counts = Counter()
    # language_counter = Counter()

    dev_type_info = {}

    for line in csv_reader:
        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })

            languages = line['LanguageWorkedWith'].split(';')
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1

for dev_type, info in dev_type_info.items():
    print(dev_type)

    for language, value in info['language_counter'].most_common(5):
        language_pct = (value / info['total']) * 100
        language_pct = round(language_pct, 2)

        print(f'{language} {language_pct}%')

'''
    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

        total += 1

        # for language in languages:
        #    language_counter[language] += 1

        # print(language_counter)
        # break

for language, value in language_counter.most_common(5):
    language_pct = (value / total) * 100
    language_pct = round(language_pct, 2)

    print(f'{language} {language_pct}%')

# no_pct = (counts['No'] / total) * 100
# no_pct = round(no_pct, 2)

# print(f'No: {no_pct}%')
'''
