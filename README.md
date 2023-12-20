# Bezi-r-algoritma-izmanto-ana-2D-objekta-p-rvieto-anai
Beziér līknes funkcija: Šī funkcija aprēķina Beziér līknes punktus, izmantojot kontrolpunktus un parametru t, kas norāda līknes pozīciju. Tā atgriež x un y koordinātas.

Binomiālās funkcijas definīcija: Šī funkcija aprēķina binomiālo koeficientu, kas ir nepieciešams Beziér līknes aprēķināšanai.

Galvenā loga izveide: Izveido galveno logu un audeklu, kurā tiks zīmēta līkne un pārvietots objekts.

Vadības punktu inicializācija: Izveido sarakstu, kurā tiks glabāti vadības punkti.

Vadības punktu pievienošana: Šī funkcija tiek izsaukta, kad lietotājs noklikšķina uz audekla. Tā pievieno vadības punktu un zīmē to audeklā. Kad ir pievienoti trīs punkti, tiek zīmēta līkne.

Līknes zīmēšana: Šī funkcija zīmē Beziér līkni, izmantojot vadības punktus.

Vadības punktu atiestatīšana: Šī funkcija tiek izsaukta, kad lietotājs nospiež taustiņu “r”. Tā dzēš visus vadības punktus un audekla saturu.

Objekta animācija: Šī funkcija animē objektu, pārvietojot to pa Beziér līknes trajektoriju. Tā arī regulē animācijas ātrumu, izmantojot slīdni.

bezier(t, points): Šī funkcija aprēķina Bezier līkni dotajam punktu kopumam un parametram t.

binomial(n, k): Šī funkcija aprēķina binomiālo koeficientu dotajiem n un k.

add_point(event): Šī funkcija pievieno vadības punktu audeklam, kad tiek noklikšķināta kreisā peles poga.

draw_curve(): Šī funkcija uz audekla zīmē Bezier līkni, izmantojot vadības punktus.

reset_points(event): Šī funkcija atiestata vadības punktus un notīra audeklu, kad tiek nospiež taustiņš ‘r’.

animate_object(t=0, obj=None): Šī funkcija animē objektu pa Bezier līkni.

start_animation(): Šī funkcija sāk animāciju, kad tiek noklikšķināta poga ‘Start’.

increase_speed(): Šī funkcija palielina animācijas ātrumu, kad tiek noklikšķināta poga ‘+’.

decrease_speed(): Šī funkcija samazina animācijas ātrumu, kad tiek noklikšķināta poga ‘-’.

Šīs funkcijas kopā veido interaktīvu Bezier līkņu zīmēšanas un animācijas programmu. bezier un binomial funkcijas ir matemātiskas funkcijas, kamēr pārējās ir saistītas ar grafisko lietotāja interfeisu un animāciju. add_point, draw_curve, reset_points, animate_object, start_animation, increase_speed un decrease_speed funkcijas visi ir notikumu vadītas, tas nozīmē, ka tās tiek izsauktas atbildē uz lietotāja darbībām, piemēram, peles klikšķiem vai pogu nospiešanu.

Kodā funkcija binomiāls (n, k) ir rekursīva funkcija. Tā atsaucas uz savu definīciju, lai aprēķinātu binoma koeficientu dotajam n un k. Šī funkcija izmanto binomiālo koeficientu rekursīvo īpašību, binomiālais koeficients (n, k) ir vienāds ar binomiālo koeficientu (n-1, k-1) un (n-1, k) summu. Citas koda funkcijas nav rekursīvas. Tās ir vai nu notikuma vadītas funkcijas (piemēram, add_point (event), reset_punkts (event), start_animation (), increase_speed (), decrease_speed ()), vai arī tās veic noteiktus aprēķinus (piemēram, Bezier (t, punkti)) vai darbības (piemēram, draw_curve (), animate_object (t = 0, obj = nav)), nenosaucot sevi. Sakne. maincilpa () skripta beigās nav definēta funkcija, bet tā ir iebūvēta funkcija tkinter, kas startē programmas galveno notikumu cilpu. Šī funkcija arī nav rekursīva. Tā ir bezgalīga cilpa, kas gaida notikumus un atjaunina GUI, bet pati sevi nesauc.

Par to, kāpēc Bēzera līkni ierobežoju līdz otrās pakāpes Bezjē līkni. Kad sāku rakstīt kodu, sākumā varēja daudzkārt klikšķināt uz canvasa, veidojot visādas beziér līknes, bet man sāka rasties problēmas ar tkinter. Tās lagoja pēc 6 vai 7 kontrolpunktu izveidošanas un animācija bija dīvaina, tā nejauši kļūs ātra vai lēnāka kaut vai man nebija sliders vel gatavs lai to kontroletu. Tāpēc es to ierobežoju līdz 3 kontrolpunktiem lai man būtu vieglāk strādāt. Mana pašreizējā Bezjē līknes funkcijas implementācija ir vispārināta, kas darbojas ar jebkuru kontroles punktu skaitu. Tā balstās uz Bernšteina polinomu, kas ir Bezjē līknes definīcijas pamatā. Tomēr, ierobežojot kontroles punktu skaitu līdz 3, es būtībā izveidoju kvadrātisko Bezjē līkni (otrās pakāpes Bezjē līkne). Tehneski es varetu izmantot
