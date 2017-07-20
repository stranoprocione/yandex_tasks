import re
pattern = r'^https?:\/\/(?:.*@)*([^\/\n:]+)'
regexr = re.compile(pattern)
with open ('/home/mapache/python/urls_set.csv') as in_file:
    with open('/home/mapache/python/result.txt', 'w') as out_file:
        for line in in_file:
            try:
                domen = regexr.match(line).group(1)
                out_file.write('{}\n'.format(domen))
            except AttributeError:
                print('Error: ' + line)
        out_file.close()
    in_file.close()
