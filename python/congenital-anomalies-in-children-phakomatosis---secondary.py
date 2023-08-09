# Zylbersztejn A, Verfürden M, Hardelid P, Gilbert R, Wijlaars L., 2023.

import sys, csv, re

codes = [{"code":"Q702","system":"icd10"},{"code":"Q703","system":"icd10"},{"code":"Q858","system":"icd10"},{"code":"Q859","system":"icd10"},{"code":"Q858","system":"icd10"},{"code":"Q859","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('congenital-anomalies-in-children-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["congenital-anomalies-in-children-phakomatosis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["congenital-anomalies-in-children-phakomatosis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["congenital-anomalies-in-children-phakomatosis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
