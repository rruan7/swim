from django.shortcuts import render
from sets.models import Set
import random

# Create your views here.

# index view (set gallery)
def set_index(request):
    # queryset: returns a collection of all Set objects
    sets = Set.objects.all()
    warmups = sets.filter(category='warmup')
    mainsets = sets.filter(category='mainset')
    cooldowns = sets.filter(category='cooldown')
    # context dictionary: used to send information to template
    context = {
        'sets': sets,
        'warmups': warmups,
        'mainsets': mainsets,
        'cooldowns': cooldowns,
    }
    return render(request, 'set_index.html', context)

# detail view (specific set info)
def set_detail(request, pk):
    set = Set.objects.get(pk=pk)
    context = {
        'set': set
    }
    return render(request, 'set_detail.html', context)

# random set generator
def set_generator(request):
    sets = Set.objects.all()
    # getting a random warmup
    warmups = sets.filter(category='warmup')
    warmup = random.sample(list(warmups), 1)[0]
    # getting random sets
    mainsets = sets.filter(category='mainset')
    mainset = random.sample(list(mainsets), 2)
    mainset1 = mainset[0]
    mainset2 = mainset[1]
    # getting a random cooldown
    cooldowns = sets.filter(category='cooldown')
    cooldown = random.sample(list(cooldowns), 1)[0]
    # updating context dictionary
    context = {
        'sets': sets,
        'warmup': warmup,
        'mainset1': mainset1,
        'mainset2': mainset2,
        'cooldown': cooldown,
    }
    return render(request, 'set_generator.html', context)
