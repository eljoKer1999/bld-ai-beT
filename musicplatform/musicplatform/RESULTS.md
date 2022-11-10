
# RESULTS.md

## queries used and their results

### create some artists

- Q) Artist.objects.create(stageName="Ava",socialLink="FB")

Output : <Artist: Artist stageName is:Ava>

- Q) Artist.objects.create(stageName="Drake",socialLink="YT")

Output : <Artist: Artist stageName is:Drake>

- Q) Artist.objects.create(stageName="Calum Scott",socialLink="FB")

Output : <Artist: Artist stageName is:Calum Scott>

- Q) Artist.objects.create(stageName="SIA",socialLink="")

Output : <Artist: Artist stageName is:SIA>

### list down all artists

- Q) Artist.objects.all()

Output : <QuerySet [<Artist: Artist stageName is:Ava>, <Artist: Artist stageName is:Calum Scott>, <Artist: Artist stageName is:Drake>, <Artist: Artist stageName is:SIA>]>

### list down all artists sorted by name

- Q) Artist.objects.all().order_by('stageName')

Output : <QuerySet [<Artist: Artist stageName is:Ava>, <Artist: Artist stageName is:Calum Scott>, <Artist: Artist stageName is:Drake>, <Artist: Artist stageName is:SIA>]>

### list down all artists whose name starts with a

- Q) Artist.objects.filter(stageName__startswith='a')

Output : <QuerySet [<Artist: Artist stageName is:Ava>]>

### in 2 different ways, create some albums and assign them to any artists

Q1) 
- dua = Artist.objects.create(stageName="dua", socialLink="")
- dua.save()
- Artist.objects.all()
- Album.objects.create(Artist=dua,release_date="2017-07-20",cost=90.5,name="New Rules")

Output 1: <Album: Album Name is:New Rules>

- Q2) dua.album_set.create(Artist=dua,release_date="2019-12-09",cost=78.6,name="Deezer")

Output 2: <Album: Album Name is:Deezer>

### get the latest released album

- Q) Album.objects.all().order_by("-release_date")[0]

Output : <Album: Album Name is:Deezer>

### get all albums released before today

Q)
- import datetime
- Album.objects.filter(release_date__lt= datetime.date.today())

Output : <QuerySet [<Album: Album Name is:New Rules>, <Album: Album Name is:Deezer>]>

### get all albums released today or before but not after today

- Q) Album.objects.filter(release_date__lte= datetime.date.today())

Output : <QuerySet [<Album: Album Name is:New Rules>, <Album: Album Name is:Deezer>]>

### count the total number of albums

- Q) Album.objects.count()

Output : 2

### in 2 different ways, for each artist, list down all of his/her albums

Q1) 
- dic = dict()
- for albums in Album.objects.select_related('Artist'):
-     dic.setdefault(albums.Artist.stageName,[]).append(albums.name) 
- print(dic)


Output 1: {'dua': ['New Rules', 'Deezer']}


Q2) 
- dic = dict()
- for artist in Artist.objects.all():
-       dic[artist.stageName] = artist.album_set.all()
- print(dic)

Output 2: {'Ava': <QuerySet []>, 'Calum Scott': <QuerySet []>, 'Drake': <QuerySet []>, 'SIA': <QuerySet 
[]>, 'dua': <QuerySet [<Album: Album Name is:New Rules>, <Album: Album Name is:Deezer>]>}


### list down all albums ordered by cost then by name

- Q) Album.objects.all().order_by("cost","name")

Output : <QuerySet [<Album: Album Name is:Deezer>, <Album: Album Name is:New Rules>]>
