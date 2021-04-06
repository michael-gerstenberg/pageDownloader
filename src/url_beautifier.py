def prepare_url_for_storage_path(url):
    try:

        # https://www.thaiai.de/                                -> thaiai.de/
        if 'http' in url:
            url = url.split('://')[1].replace('www.', '')

        # thaiai.de/something/word.html#translations            -> thaiai.de/something/word.html
        url = url.split('#')[0]

        # thaiai.de/page/profile.php?id=333                     -> thaiai.de/page/profile.php/?id=333
        url = url.replace('?', '/?')
        url = url.replace('//?', '/?')

        # thaiai.de                                             -> thaiai.de/index.html
        # thaiai.de?l=x                                         -> thaiai.de/?l=x
        if '/' not in url:
            if '?' in url:
                url += '.html'
            else:
                url += '/index.html'

        # thaiai.de/                                            -> thaiai.de/index.html
        # thaiai.de/translation/                                -> thaiai.de/translation/index.html
        if url[-1] == '/':
            url += 'index.html'

        # thaiai.de/route                                       -> thaiai.de/route/index.html
        # thaiai.de/route/?w=bo                                 -> thaiai.de/route/?w=bo.html
        if '.' not in url.split('/')[-1]:
            if '?' in url.split('/')[-1]:
                url += '.html'
            else:
                url += '/index.html'
        else:
            url = url.replace('.' + url.split('/')[-1].split('.')[-1], '.html')

        return url

    except:
        return False