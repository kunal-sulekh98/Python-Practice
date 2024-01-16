# fileparse.py
#
# Exercise 3.3

import csv 


def parse_csv(filename, select = None, types=[str, int, float], has_headers = True, delimiter = None, silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''

    if not has_headers:
        if select:
            raise RuntimeError("select argument requires column headers")
        with open(filename,'rt') as f:
            records = []
            rows = csv.reader(f)
            for row in rows:
                record = tuple([func(val) for func, val in zip(types, row)])
                records.append(record)
        return records


    records = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        header = next(rows)
        if select:
            indices = [header.index(x) for x in select]
            header = select
        else:
            indices = []
        records = []
        for i, row in enumerate(rows):
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors == True:
                    continue
                else:
                    print("Row ",i+1,": Couldn't convert ",row)
                    print("Row ",i+1,": Reason ",e)

            record = dict(zip(header,row))

            records.append(record)
    return records



