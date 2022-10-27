    Osoba.objects.all()
    returns <QuerySet [<Osoba: Rafał Brzeziński>, <Osoba: Rafał Olszewski>, <Osoba: Janusz Zadarmo>]>

    Osoba.objects.filter(id=3)
    <QuerySet []> (Empty Object, doesnt exist with this ID)
    
    Osoba.objects.filter(id=5)
    <QuerySet [<Osoba: Janusz Zadarmo>]> (Due to DB changes)

    Osoba.objects.filter(imie__startswith='R')
    <QuerySet [<Osoba: Rafał Brzeziński>, <Osoba: Rafał Olszewski>]>

    Osoba.objects.order_by().values('druzyna').distinct()
    <QuerySet [{'druzyna': 1}, {'druzyna': None}]>

    Druzyna.objects.order_by('-nazwa')
    <QuerySet [<Druzyna: Tree Orchard (IE)>, <Druzyna: Epic Gamers (US)>]>