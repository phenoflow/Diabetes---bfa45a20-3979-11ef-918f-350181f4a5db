# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"237599002","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"385041000000108","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"75682002","system":"snomedct"},{"code":"314893005","system":"snomedct"},{"code":"314771006","system":"snomedct"},{"code":"314771006","system":"snomedct"},{"code":"237613005","system":"snomedct"},{"code":"237613005","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"11530004","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"4855003","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"268519009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"230577008","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"237599002","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"49455004","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"127013003","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"201724008","system":"snomedct"},{"code":"237613005","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-hyperproinsulinaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-hyperproinsulinaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-hyperproinsulinaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
