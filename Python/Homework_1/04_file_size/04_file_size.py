def file_size(size_in_bytes):
    """ this function convert bytes to KB, MB and GB """
    for x in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return "%3.1f %s" % (size_in_bytes, x)
        size_in_bytes /= 1024.0
    return "%3.1f %s" % (size_in_bytes, 'GB')


print(file_size(1101947))
