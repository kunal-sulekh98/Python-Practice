
class FormatError(Exception):
    pass

class TableFormatter:

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
    

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):

    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):

    def headings(self, headers):
        head = "<tr>"
        for h in headers:
            head = head + "<th>" + str(h) + "</th>"
        head += "</tr>"
        print(head)
    
    def row(self, rowdata):
        ro = "<tr>"
        for r in rowdata:
            ro = ro + "<td>" + str(r) + "</td>"
        ro += "</tr>"
        print(ro)

def createFormatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')
    
    return formatter

def print_table(portfolio, colnames, formatter):
    import stock
    pfolio = []
    headers = colnames
    for stoc in portfolio:
        row = []
        for col in colnames:
            row.append(str(getattr(stoc, col)))
        pfolio.append(row)
    
    formatter.headings(headers)
    for r in pfolio:
        formatter.row(r)

        
        
