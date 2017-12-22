from . import models
def add_variable_to_context(request):
    return {
        'testme': 'Hello world!',
        'footer':models.HomeDetail.objects.all().first(),
    }


