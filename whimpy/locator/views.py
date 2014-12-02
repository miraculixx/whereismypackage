from django.shortcuts import render, redirect


# Create your views here.
LOCATOR_URL = 'http://www.post.ch/swisspost-tracking'

def get_locator_url(pkgcodes):
    param = 'formattedParcelCodes=%s' % (';'.join(pkgcodes))
    return "%s?%s" % (LOCATOR_URL, param)

def index(request):
    q = request.GET.get('q')
    if q:
        pkgcodes = q.split(' ')
        context = { 
           'url' : get_locator_url(pkgcodes),
           'pkgcodes' : " ".join(pkgcodes)
        }
        return render(request, 'locator/results.html', context)
    return render(request, 'locator/index.html' )