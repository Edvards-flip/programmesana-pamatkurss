# Programmēšana - pamatkurss
Autors: **Edvards Gedrovics**
## Kā palaist
- Atver github desktop
- Tālāk izvēlies visual studio code
## Licence
-MIT is a short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.--
### **Es gribu tieši toooooo**
### **.md fails nav parasts teksta fails, jo tas satur strukturētu marķējuma valodu (Markdown), kas ļauj vienkāršu tekstu automātiski pārvērst vizuāli noformētā dokumentā (ar virsrakstiem, treknrakstu, sarakstiem un saitēm).**



### <class 'str'> ir a
### <class 'int'> ir b
### <class 'float'> ir c

## Dalīšana un inventāra kalkulators

Aprēķini ar 17 un 5:

- `17 / 5` = `3.4` — parastā dalīšana.
- `17 // 5` = `3` — pilno dalījumu skaits.
- `17 % 5` = `2` — atlikums.
- `2 ** 3` = `8` — kāpināšana pakāpē.

Tātad 17 dalīts ar 5 ir 3 pilnas reizes, un pāri paliek 2.
Inventāra kalkulators ar 17 mantām un 5 vietām somā izvada `3` pilnas somas un `2` mantas pāri.

Kalkulatora izvade ar f-string ir: `Vajag 3 somas un 2 mantas paliks pāri.` Vidējais aritmētiskais ir 3.4 somas. Formāts `:.1f` attēlo skaitli ar vienu ciparu aiz komata. Šajā piemērā arī neformatētais rezultāts ir 3.4; citām vērtībām formatēšana var noapaļot redzamo rezultātu.

## Koda lasāmības pārbaude

Iztēlotais klasesbiedrs saprata, ka kods aprēķina veselības punktus pēc uzbrukuma, bet nosaukums `atlikums` viņam nebija pietiekami skaidrs. Tāpēc to pārsaucu par `atlikusie_hp_punkti`. Labs mainīgā vārds ir svarīgāks par komentāru, jo tas uzreiz pasaka, kāda vērtība tajā glabājas.

## Spēles pseidokods

### Ievade
1. Pajautā spēlētāja vārdu.
2. Pajautā spēlētāja sākotnējo veselības punktu skaitu.
3. Pajautā uzbrukuma spēku.

### Apstrāde
4. Aprēķini spēlētāja atlikušos veselības punktus, no sākotnējiem punktiem atņemot uzbrukuma spēku.

### Izvade
5. Parādi spēlētāja vārdu.
6. Parādi spēlētāja atlikušos veselības punktus.

Parādi šo plānu klasesbiedram un pajautā, vai viņš saprot, ko spēle dara.

## Spēles mainīgie un formula

### | Mainīgā vārds         | Datu tips | Ko glabā                                  |
### | `speletaja_vards`     | `str`     | Spēlētāja vārdu                           |
### | `hp_punkti`           | `int`     | Spēlētāja sākotnējos veselības punktus    |
### | `uzbrukuma_jauda`     | `float`   | Uzbrukuma spēku                           |
### | `atlikusie_hp_punkti` | `float`   | Spēlētāja veselības punktus pēc uzbrukuma |

Formula: `atlikusie_hp_punkti = hp_punkti - uzbrukuma_jauda`

`speletaja_vards`, `hp_punkti` un `uzbrukuma_jauda` vērtības tiek iegūtas no `input()`. `atlikusie_hp_punkti` tiek izrēķināts ar formulu.
Formulā izmantotie mainīgie ir norādīti tabulā.

## Formulas pārbaude

| Pārbaude            | hp_punkti   | uzbrukuma_jauda   | Aprēķins  | atlikusie_hp_punkti   |
| Maza vērtību kopa   | 20          | 5                 | 20 - 5    | 15                    |
| Vidēja vērtību kopa | 100         | 25                | 100 - 25  | 75                    |
| Liela vērtību kopa  | 500         | 125               | 500 - 125 | 375                   |

Secinājums: formulu ir vērts pārbaudīt pirms visas programmas rakstīšanas, lai laikus pamanītu kļūdas aprēķinā un pārliecinātos, ka rezultāti ir loģiski.