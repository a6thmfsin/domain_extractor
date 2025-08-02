#/usr/bin/python3

import re

def extract_domains(input_file, output_file):
    domains = []

    domain_pattern = re.compile(
        r'\b(?:[a-zA-Z0-9-]+\.)+(?:[a-zA-Z]{2,})\b'
    )

    with open(input_file, 'r', encoding='utf-8') as f:
        contents = f.read()

    matches = domain_pattern.findall(contents)

    unique_domains = sorted(set(matches))

    with open(output_file, 'w', encoding='utf-8') as f:
        for domain in unique_domains:
            f.write(domain + '\n')

    print(f"extracted {len(unique_domains)} domains to {output_file}")

extract_domains('extract_domains.txt', 'domains_extracted.txt')
