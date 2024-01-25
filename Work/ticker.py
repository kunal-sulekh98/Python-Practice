from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfile, logfile, fmt):
    import report
    import tableformat
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.createFormatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        name = row['name']
        price = row['price']
        change = row['change']
        rowdata = [ str(name), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


if __name__ == '__main__':
    """lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    
    for row in rows:
        print(row)"""
    