from random import choice,randint
matematica=['O girafa poate cantari intre 700 si 1200 kilograme iar o pisica de casa are aproximativ 5 kilograme. Cum bagi girafa in frigider?',
'Un elefant african poate ajunge pana la 6 000 de kilograme in timp ce un pui de elefant asiatic poate cantari cat o girafa. Cum bagi elefantul in frigider?',
'Cum se scrie 1980 in cifre romane?',
'Cate ore sunt in 2 zile si jumatate?',
'Care este cel mai mare numar pe care il poti forma din 7,3,1 si 5?',
'Ce numar se afla la mijloc in intervalul 36-42?',
'Cubul lui 3 este...',
'Cate zile de nastere are un om nascut in Franta in 1948?',
'Un tren electric se indreapta din Bucuresti catre Iasi cu 70 km/ora iar vantul bate din nord cu 14 km/h. Un autobuz pleaca din acelasi punct al orasului catre Iasi cu 50 de km/ora insa cu 30 de minute mai devreme si se confrunta cu un vant de 10 km/h.',
'De cate ori poti sa il scazi pe 2 din 100?']
biologia=['Botanica este studiul a ce formă de viață?',
'Adevărat sau fals: melcii au dinți',
'Ce parte a corpului uman este mandibula?',
'Câte oase are un om adult?',
'Adevărat sau fals: meduzele au inimi',
'Heterocromia duce la ce schimbare a aspectului fizic?',
'Termenul „renal” se referă la ce organe?',
'Care este numele celei mai mari părți a creierului uman?',
'Boala Crohn face parte din ce grup de boli?',
'Cine a descoperit penicilina?']
istoria=['În ce an s-a născut Regele Mihai I?',
'Ce grad de rudenie este între Carol al II-lea și Ferdinand I?',
'În ce țară s-a născut Adolf Hitler?',
'În ce oraș au fost executați soții Ceaușescu?',
'În ce an a reușit Mihai Viteazul unirea celor trei mari țări medievale?',
' Când a avut loc Primul Război Mondial?',
'În ce an a intrat România în Uniunea Europeana?',
' În ce an a murit Prințesa Diana?',
' Ce naționalitate are Papa Francisc I?',
'În ce an s-a proclamat independența de stat a României?',
]
chimia=['Molecula metil (CH3) este nepolara sau polara?',
'Ce face aurul atât de valoros?',
'De ce se topesc metalele la temperaturi diferite?',
'Grupa este șirul orizontal sau vertical?',
'HSO4 are si caracter bazic si caracter acid?',
'Cum se explica proprietatea fierului de a fi atras de magneti?',
'Ce sunt atomii?',
'Cine a inventat carbidul si varul?',
'Ce anume determina culoarea unui element chimic?',
'Sub ce forma se afla metalele in minereuri?']
fizica=['Ce tip de lentilă este lupa?',
'In ce tip de unităţi de măsură este calculată rezistenţa electrică?',
'Când sunt încălzite, metalele se dilată. Ce se întâmplă cu ele când sunt răcite?',
'Care este unitatea de măsură pentru puterea electrică?',
'Cum se numeşte modelul cosmologic care explică cum s-a format universul?',
'Cum se numeşte firul din interiorul unui bec?',
'Lumina infraroșie are o undă care este prea lungă sau prea scurtă pentru a fi vizibilă cu ochiul liber?',
'Cum se numeşte eclipsa care se produce atunci când luna se află între soare şi Pământ?']
n=randint(1,5)
if n==1:
    print('domeniul:matematica')
    print(choice(matematica))
if n==2:
    print('domeniul:biologia')
    print(choice(biologia))
if n==3:
    print('domeniul:istoria')
    print(choice(istoria))
if n==4:
    print('domeniul:chimia')
    print(choice(chimia))
if n==5:
    print('domeniul:fizica')
    print(choice(fizica))