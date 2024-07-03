# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"609572000","system":"snomedct"},{"code":"609572000","system":"snomedct"},{"code":"609572000","system":"snomedct"},{"code":"44054006","system":"snomedct"},{"code":"44054006","system":"snomedct"},{"code":"44054006","system":"snomedct"},{"code":"421750000","system":"snomedct"},{"code":"421750000","system":"snomedct"},{"code":"421750000","system":"snomedct"},{"code":"421847006","system":"snomedct"},{"code":"421847006","system":"snomedct"},{"code":"421847006","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"190372001","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609561005","system":"snomedct"},{"code":"609562003","system":"snomedct"},{"code":"609562003","system":"snomedct"},{"code":"609562003","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"609562003","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"237604008","system":"snomedct"},{"code":"609572000","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-maturityonset---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-maturityonset---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-maturityonset---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
