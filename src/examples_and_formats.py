example_lists = { list_en_PAL = [''' 
                #Roger started with 5 tennis balls. 
                tennis_balls = 5 
                #2 cans of 3 tennis balls each is 
                bought_balls = 2 * 3 tennis balls 
                #The answer is 
                answer = tennis_balls + bought_balls 
                return answer
                #The answer is 11''',
               ''' 
                 #Initially, there were 9 computers in the server room. 
                 initial_computers = 9 
                 #From Monday to Thursday, there are 4 days. 
                 days = 4 
                 #5 computers were added each day 
                 added_computers_per_day = 5 
                 #The total number of computers added is 
                 days * added_computers_per_day = 4 * 5 = 20 
                 #total number of computers in the server room is 
                 answer = initial_computers + total_added_computers = 9 + 20 = 29
                 return answer
                 #The answer is 29.''',
               ''' 
                #Initially, there are 3 cars.
                  initial_cars = 3 
                  #2 more cars arrive. 
                  arriving_cars = 2 
                  #total number of cars in the parking lot is 
                  answer = initial_cars + arriving_cars = 3 + 2 = 5. 
                  return answer
                  #The answer is 5.''',
               ''' 
                #Shawn has 5 toys. 
                  initial_toys = 5 
                  #He got 2 toys from his mom 
                  initial_toys + 2 = 5 + 2 = 7 toys. 
                  #He got 2 more toys from his dad, so now he has 
                  answer = 7 + 2 = 9 toys in total. 
                  return answer
                  #The answer is 9.''',
               ''' 
                #Michael started with 58 golf balls
                initial_balls = 58
                #On Tuesday, he lost 23 golf balls.
                lost_on_tuesday = 23
                #On Wednesday, he lost 2 more golf balls.
                lost_on_wednesday = 2
                #Therefore, at the end of Wednesday, he has 
                answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
                return answer
                #The answer is 33.''',
               ''' 
                #Olivia's initial amount of money as initial_money.
                   initial_money = 23 
                   #She bought five bagels for $3 each 
                   total_cost_bagels = number_bagels * cost_one_beagel = 15 
                   #After buying the bagels, Olivia has 
                   answer = initial_money - total_cost_bagels = 23 - 15 = 8 
                   return answer
                   #The answer is 8.''',
               ''' 
                #Leah had as 32 and the number of chocolates her sister had as 42. 
                leah_chocolates = 32 
                sister_chocolates = 42 
               total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
               #If they ate 35 chocolates 
               eaten_chocolates = 35 
              #The remaining number of chocolates is 
              answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
              return answer
              #The answer is 39.'''              
              ]


list_es_PAL = [
    ''' 
                #Roger empezó con 5 pelotas de tenis. 
                tennis_balls = 5 
                #2 latas de 3 pelotas de tenis cada una son 
                bought_balls = 2 * 3 tennis balls 
                #La respuesta es 
                answer = tennis_balls + bought_balls 
                return answer
                #La respuesta es 11''',
    ''' 
                #Inicialmente, había 9 computadoras en la sala de servidores. 
                 initial_computers = 9 
                 #De lunes a jueves hay 4 días. 
                 days = 4 
                 #Se añadieron 5 computadoras cada día 
                 added_computers_per_day = 5 
                 #El número total de computadoras añadidas es 
                 days * added_computers_per_day = 4 * 5 = 20 
                 #El número total de computadoras en la sala de servidores es 
                 answer = initial_computers + total_added_computers = 9 + 20 = 29
                 return answer
                 #La respuesta es 29.''',
    ''' 
                #Inicialmente, hay 3 coches. 
                  initial_cars = 3 
                  #Llegan 2 coches más. 
                  arriving_cars = 2 
                  #El número total de coches en el estacionamiento es 
                  answer = initial_cars + arriving_cars = 3 + 2 = 5. 
                  return answer
                  #La respuesta es 5.''',
    ''' 
                #Shawn tiene 5 juguetes. 
                  initial_toys = 5 
                  #Recibió 2 juguetes de su mamá 
                  initial_toys + 2 = 5 + 2 = 7 juguetes. 
                  #Recibió 2 juguetes más de su papá, ahora tiene 
                  answer = 7 + 2 = 9 juguetes en total. 
                  return answer
                  #La respuesta es 9.''',
    ''' 
                #Michael empezó con 58 pelotas de golf
                initial_balls = 58
                #El martes perdió 23 pelotas de golf.
                lost_on_tuesday = 23
                #El miércoles perdió 2 pelotas de golf más.
                lost_on_wednesday = 2
                #Por lo tanto, al final del miércoles, tiene 
                answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
                return answer
                #La respuesta es 33.''',
    ''' 
                #El monto inicial de dinero de Olivia era initial_money.
                   initial_money = 23 
                   #Compró cinco bagels por $3 cada uno 
                   total_cost_bagels = number_bagels * cost_one_beagel = 15 
                   #Después de comprar los bagels, Olivia tiene 
                   answer = initial_money - total_cost_bagels = 23 - 15 = 8 
                   return answer
                   #La respuesta es 8.''',
    ''' 
                #Leah tenía 32 y el número de chocolates de su hermana era 42. 
                leah_chocolates = 32 
                sister_chocolates = 42 
               total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
               #Si comieron 35 chocolates 
               eaten_chocolates = 35 
              #El número restante de chocolates es 
              answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
              return answer
              #La respuesta es 39.'''
]


list_zh_PAL = [
    ''' 
        # 罗杰开始时有5个网球
        tennis_balls = 5 
        # 2罐每罐3个网球
        bought_balls = 2 * 3 tennis balls 
        # 答案是
        answer = tennis_balls + bought_balls 
        return answer
        # 答案是11''',
    ''' 
        # 起初，服务器室里有9台电脑
        initial_computers = 9 
        # 从星期一到星期四共有4天
        days = 4 
        # 每天增加5台电脑
        added_computers_per_day = 5 
        # 增加的电脑总数是
        days * added_computers_per_day = 4 * 5 = 20 
        # 服务器室的电脑总数是
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # 答案是29''',
    ''' 
        # 起初有3辆车
        initial_cars = 3 
        # 又来了2辆车
        arriving_cars = 2 
        # 停车场的车辆总数是
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
    # 答案是5''',
    ''' 
    # 肖恩有5个玩具
    initial_toys = 5 
    # 他从妈妈那里得到2个玩具
    initial_toys + 2 = 5 + 2 = 7 toys. 
    # 他从爸爸那里又得到了2个玩具，现在他总共有
    answer = 7 + 2 = 9 toys in total. 
    return answer
    # 答案是9''',
    ''' 
    # 迈克尔起初有58个高尔夫球
    initial_balls = 58
    # 星期二他丢了23个高尔夫球
    lost_on_tuesday = 23
    # 星期三他又丢了2个高尔夫球
    lost_on_wednesday = 2
    # 因此，在星期三结束时，他有
    answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
    return answer
    # 答案是33''',
    ''' 
    # 奥利维亚的初始金额为初始金额
    initial_money = 23 
    # 她花了$3买了5个百吉饼
    total_cost_bagels = number_bagels * cost_one_beagel = 15 
    # 买完百吉饼后，奥利维亚还剩
    answer = initial_money - total_cost_bagels = 23 - 15 = 8 
    return answer
    # 答案是8''',
    ''' 
    # 莱娅有32个巧克力，她的妹妹有42个
    leah_chocolates = 32 
    sister_chocolates = 42 
    total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
    # 如果他们吃了35个巧克力
    eaten_chocolates = 35 
    # 剩下的巧克力数量是
    answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
    return answer
    # 答案是39'''
]


list_de_PAL = [
    ''' 
        # Roger begann mit 5 Tennisbällen. 
        tennis_balls = 5 
        # 2 Dosen mit jeweils 3 Tennisbällen sind 
        bought_balls = 2 * 3 Tennisbälle 
        # Die Antwort ist 
        answer = tennis_balls + bought_balls 
        return answer
        # Die Antwort ist 11''',
    ''' 
        # Anfangs gab es 9 Computer im Serverraum. 
        initial_computers = 9 
        # Von Montag bis Donnerstag gibt es 4 Tage. 
        days = 4 
        # Es wurden täglich 5 Computer hinzugefügt 
        added_computers_per_day = 5 
        # Die Gesamtzahl der hinzugefügten Computer beträgt 
        days * added_computers_per_day = 4 * 5 = 20 
        # Die Gesamtzahl der Computer im Serverraum beträgt 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # Die Antwort ist 29.''',
    ''' 
        # Anfangs gab es 3 Autos. 
        initial_cars = 3 
        # Es kamen 2 weitere Autos an. 
        arriving_cars = 2 
        # Die Gesamtzahl der Autos auf dem Parkplatz beträgt 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # Die Antwort ist 5.''',
    ''' 
        # Shawn hat 5 Spielzeuge. 
        initial_toys = 5 
        # Er bekam 2 Spielzeuge von seiner Mutter 
        initial_toys + 2 = 5 + 2 = 7 Spielzeuge. 
        # Er bekam 2 weitere Spielzeuge von seinem Vater, jetzt hat er insgesamt 
        answer = 7 + 2 = 9 Spielzeuge. 
        return answer
        # Die Antwort ist 9.''',
    ''' 
        # Michael begann mit 58 Golfbällen
        initial_balls = 58
        # Am Dienstag verlor er 23 Golfbälle.
        lost_on_tuesday = 23
        # Am Mittwoch verlor er 2 weitere Golfbälle.
        lost_on_wednesday = 2
        # Also hat er am Ende des Mittwochs 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # Die Antwort ist 33.''',
    ''' 
        # Olivia's Anfangsbetrag an Geld als initial_money.
        initial_money = 23 
        # Sie kaufte fünf Bagels für je $3 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # Nach dem Kauf der Bagels hat Olivia 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # Die Antwort ist 8.''',
    ''' 
        # Leah hatte 32 und die Anzahl der Schokoladen, die ihre Schwester hatte, war 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # Wenn sie 35 Schokoladen gegessen haben 
        eaten_chocolates = 35 
        # Die verbleibende Anzahl von Schokoladen ist 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # Die Antwort ist 39.'''
]

list_ja_PAL = [
    ''' 
        # ロジャーは5個のテニスボールから始めました。 
        tennis_balls = 5 
        # 3個ずつの2缶は 
        bought_balls = 2 * 3 テニスボール 
        # 答えは 
        answer = tennis_balls + bought_balls 
        return answer
        # 答えは11''',
    ''' 
        # 最初は、サーバールームに9台のコンピュータがありました。 
        initial_computers = 9 
        # 月曜日から木曜日まで、4日間です。 
        days = 4 
        # 1日に5台のコンピュータが追加されました 
        added_computers_per_day = 5 
        # 追加されたコンピュータの合計数は 
        days * added_computers_per_day = 4 * 5 = 20 
        # サーバールームのコンピュータの合計は 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # 答えは29.''',
    ''' 
        # 最初は車が3台ありました。 
        initial_cars = 3 
        # 2台の車が追加されました。 
        arriving_cars = 2 
        # 駐車場の車の合計は 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # 答えは5.''',
    ''' 
        # ショーンは5つのおもちゃを持っています。 
        initial_toys = 5 
        # 彼は母親からおもちゃを2つもらいました 
        initial_toys + 2 = 5 + 2 = 7 おもちゃ。 
        # 彼はさらに2つのおもちゃを父親からもらい、合計で 
        answer = 7 + 2 = 9 個のおもちゃを持っています。 
        return answer
        # 答えは9.''',
    ''' 
        # マイケルは58個のゴルフボールで始めました
        initial_balls = 58
        # 火曜日に23個のゴルフボールを失いました。
        lost_on_tuesday = 23
        # 水曜日にさらに2個のゴルフボールを失いました。
        lost_on_wednesday = 2
        # したがって、水曜日の終わりには、彼は 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # 答えは33.''',
    ''' 
        # オリビアの初期金額はinitial_moneyです。
        initial_money = 23 
        # 彼女は1つあたり$3のベーグルを5つ買いました 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # ベーグルを購入した後、オリビアは 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # 答えは8.''',
    ''' 
        # リアは32個、彼女の妹は42個のチョコレートを持っていました。 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # 彼らが35個のチョコレートを食べた場合 
        eaten_chocolates = 35 
        # 残りのチョコレートの数は 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # 答えは39'''
]

list_es_PAL = [
    ''' 
        #Roger empezó con 5 pelotas de tenis. 
        tennis_balls = 5 
        #2 latas de 3 pelotas de tenis cada una son 
        bought_balls = 2 * 3 tennis balls 
        #La respuesta es 
        answer = tennis_balls + bought_balls 
        return answer
        #La respuesta es 11''',
    ''' 
        #Inicialmente, había 9 computadoras en la sala de servidores. 
        initial_computers = 9 
        #De lunes a jueves hay 4 días. 
        days = 4 
        #Se añadieron 5 computadoras cada día 
        added_computers_per_day = 5 
        #El número total de computadoras añadidas es 
        days * added_computers_per_day = 4 * 5 = 20 
        #El número total de computadoras en la sala de servidores es 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #La respuesta es 29.''',
    ''' 
        #Inicialmente, hay 3 coches. 
        initial_cars = 3 
        #Llegan 2 coches más. 
        arriving_cars = 2 
        #El número total de coches en el estacionamiento es 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #La respuesta es 5.''',
    ''' 
        #Shawn tiene 5 juguetes. 
        initial_toys = 5 
        #Recibió 2 juguetes de su mamá 
        initial_toys + 2 = 5 + 2 = 7 juguetes. 
        #Recibió 2 juguetes más de su papá, ahora tiene 
        answer = 7 + 2 = 9 juguetes en total. 
        return answer
        #La respuesta es 9.''',
    ''' 
        #Michael empezó con 58 pelotas de golf
        initial_balls = 58
        #El martes perdió 23 pelotas de golf.
        lost_on_tuesday = 23
        #El miércoles perdió 2 pelotas de golf más.
        lost_on_wednesday = 2
        #Por lo tanto, al final del miércoles, tiene 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #La respuesta es 33.''',
    ''' 
        #El monto inicial de dinero de Olivia era initial_money.
        initial_money = 23 
        #Compró cinco bagels por $3 cada uno 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Después de comprar los bagels, Olivia tiene 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #La respuesta es 8.''',
    ''' 
        #Leah tenía 32 y el número de chocolates de su hermana era 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Si comieron 35 chocolates 
        eaten_chocolates = 35 
        #El número restante de chocolates es 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #La respuesta es 39.'''
]


list_bn_PAL = [
    ''' 
        #রজার সাথে ৫টি টেনিস বল ছিল। 
        tennis_balls = 5 
        # ২টি ক্যান প্রতি ক্যানে ৩টি টেনিস বল আছে 
        bought_balls = 2 * 3 tennis balls 
        # উত্তর হল 
        answer = tennis_balls + bought_balls 
        return answer
        # উত্তর হল ১১''',
    ''' 
        #প্রাথমিকভাবে, সার্ভার রুমে ৯টি কম্পিউটার ছিল। 
        initial_computers = 9 
        # সোমবার থেকে বৃহস্পতিবার পর্যন্ত, ৪টি দিন আছে। 
        days = 4 
        # প্রতি দিন ৫টি কম্পিউটার যোগ করা হয়েছে 
        added_computers_per_day = 5 
        # যোগ করা কম্পিউটারের মোট সংখ্যা 
        days * added_computers_per_day = 4 * 5 = 20 
        # সার্ভার রুমে মোট কম্পিউটারের সংখ্যা 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # উত্তর হল ২৯.''',
    ''' 
        #প্রাথমিকভাবে, ৩টি গাড়ি ছিল। 
        initial_cars = 3 
        # ২টি আরও গাড়ি আসছে। 
        arriving_cars = 2 
        # পার্কিংয়ে গাড়ির মোট সংখ্যা 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # উত্তর হল ৫.''',
    ''' 
        #শওনের কাছে ৫টি খেলনা আছে। 
        initial_toys = 5 
        # তিনি তার মা থেকে ২টি খেলনা পেয়েছিলেন 
        initial_toys + 2 = 5 + 2 = 7 টি খেলনা। 
        # তিনি তার বাবা থেকে আরও ২টি খেলনা পেয়েছিলেন, এখন তার মোটে 
        answer = 7 + 2 = 9 টি খেলনা আছে। 
        return answer
        # উত্তর হল ৯.''',
    ''' 
        #মাইকেল ৫৮টি গল্ফ বল দিয়ে শুরু করেছিলেন
        initial_balls = 58
        # মঙ্গলবার তিনি ২৩টি গল্ফ বল হারিয়েছিলেন।
        lost_on_tuesday = 23
        # বুধবার তিনি আরো ২টি গল্ফ বল হারিয়েছিলেন।
        lost_on_wednesday = 2
        # তাই, মঙ্গলবারের শেষে, তার কাছে আছে 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # উত্তর হল ৩৩.''',
    ''' 
        #অলিভিয়ার প্রাথমিক টাকা পরিমাণ হচ্ছে initial_money।
        initial_money = 23 
        # তিনি প্রতি টাকায় ৩ টি বেগেল কিনলেন 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # বেগেল কিনার পরে, অলিভিয়ার কাছে হচ্ছে 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # উত্তর হল ৮.''',
    ''' 
        # লিয়ার কাছে ৩২টি চকোলেট ছিল এবং তার বোনের কাছে ছিল ৪২টি। 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # যদিও তারা ৩৫টি চকোলেট খায়। 
        eaten_chocolates = 35 
        # বাকি থাকা চকোলেটের সংখ্যা হচ্ছে 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # উত্তর হল ৩৯'''
]


list_sw_PAL = [
    ''' 
        #Roger alianza na mipira ya tenisi 5. 
        tennis_balls = 5 
        #Viboko vya 2 kila kimoja na mipira ya tenisi 3 ni 
        bought_balls = 2 * 3 tennis balls 
        #Jibu ni 
        answer = tennis_balls + bought_balls 
        return answer
        #Jibu ni 11''',
    ''' 
        #Kwa mwanzo, kulikuwa na kompyuta 9 kwenye chumba cha seva. 
        initial_computers = 9 
        #Kuanzia Jumatatu hadi Alhamisi, kuna siku 4. 
        days = 4 
        #Kompyuta 5 ziliwekwa kila siku 
        added_computers_per_day = 5 
        #Jumla ya kompyuta zilizoongezwa ni 
        days * added_computers_per_day = 4 * 5 = 20 
        #Jumla ya kompyuta kwenye chumba cha seva ni 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Jibu ni 29.''',
    ''' 
        #Kwa mwanzo, kulikuwa na magari 3. 
        initial_cars = 3 
        #Magari 2 zaidi yalifika. 
        arriving_cars = 2 
        #Jumla ya magari kwenye maegesho ni 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Jibu ni 5.''',
    ''' 
        #Shawn ana vitu vya kuchezea 5. 
        initial_toys = 5 
        #Alipata vitu vya kuchezea 2 kutoka kwa mama yake 
        initial_toys + 2 = 5 + 2 = 7 vitu vya kuchezea. 
        #Alipata vitu vingine 2 kutoka kwa baba yake, sasa ana 
        answer = 7 + 2 = 9 vitu vya kuchezea jumla. 
        return answer
        #Jibu ni 9.''',
    ''' 
        #Michael alianza na mipira ya gofu 58
        initial_balls = 58
        #Jumanne, alipoteza mipira ya gofu 23.
        lost_on_tuesday = 23
        #Jumatano, alipoteza mipira mingine 2 ya gofu.
        lost_on_wednesday = 2
        #Kwa hivyo, mwisho wa Jumatano, ana 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Jibu ni 33.''',
    ''' 
        #Kiasi cha awali cha pesa cha Olivia kama initial_money.
        initial_money = 23 
        #Alijua mikate mitano kwa $3 kila moja 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Baada ya kununua mikate ya bageli, Olivia 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Jibu ni 8.''',
    ''' 
        #Leah alikuwa na 32 na idadi ya chokoleti dada yake alikuwa na 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ikiwa walila chokoleti 35 
        eaten_chocolates = 35 
        #Idadi ya chokoleti zilizobaki ni 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Jibu ni 39'''
]

list_ru_PAL = [
    ''' 
        # Роджер начал с 5 теннисных мячей. 
        tennis_balls = 5 
        # 2 банки по 3 теннисных мяча каждая 
        bought_balls = 2 * 3 теннисных мяча 
        # Ответ 
        answer = tennis_balls + bought_balls 
        return answer
        # Ответ 11''',
    ''' 
        # Изначально в серверной комнате было 9 компьютеров. 
        initial_computers = 9 
        # С понедельника по четверг 4 дня. 
        days = 4 
        # Каждый день добавляется 5 компьютеров 
        added_computers_per_day = 5 
        # Общее количество добавленных компьютеров 
        days * added_computers_per_day = 4 * 5 = 20 
        # Общее количество компьютеров в серверной комнате 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # Ответ 29.''',
    ''' 
        # Изначально было 3 машины. 
        initial_cars = 3 
        # Прибыли еще 2 машины. 
        arriving_cars = 2 
        # Общее количество машин на парковке 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # Ответ 5.''',
    ''' 
        # У Шона было 5 игрушек. 
        initial_toys = 5 
        # Он получил 2 игрушки от мамы. 
        initial_toys + 2 = 5 + 2 = 7 игрушек. 
        # Затем он получил еще 2 игрушки от папы, теперь у него всего 
        answer = 7 + 2 = 9 игрушек. 
        return answer
        # Ответ 9.''',
    ''' 
        # Майкл начал с 58 гольф-мячами
        initial_balls = 58
        # Во вторник он потерял 23 гольф-мяча.
        lost_on_tuesday = 23
        # В среду он потерял еще 2 гольф-мяча.
        lost_on_wednesday = 2
        # Таким образом, к концу среды у него есть 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # Ответ 33.''',
    ''' 
        # Исходная сумма денег у Оливии как начальные деньги.
        initial_money = 23 
        # Она купила пять бубликов по $3 каждый 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # После покупки бубликов у Оливии есть 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # Ответ 8.''',
    ''' 
        # У Лии было 32 и количество шоколадок у ее сестры было 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # Если они съели 35 шоколадок 
        eaten_chocolates = 35 
        # Осталось 
        answer = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # Ответ 39.''',
    ''' 
        # Начальное количество яблок у Сергея 
        initial_apples = 37 
        # Он съел 4 яблока вечером 
        eaten_evening = 4 
        # И 2 яблока утром следующего дня. 
        eaten_morning_next_day = 2 
        # Сколько яблок осталось у Сергея? 
        answer = initial_apples - eaten_evening - eaten_morning_next_day = 37 - 4 - 2 = 31 
        return answer
        # Ответ 31.''',
    ''' 
        # Сумма денег, которая была у Михаила изначально.
        initial_money = 98
        # Он потратил 19 долларов на новую рубашку.
        spent_on_shirt = 19
        # И 25 долларов на новые джинсы.
        spent_on_jeans = 25
        # Оставшаяся у него сумма денег:
        answer = initial_money - spent_on_shirt - spent_on_jeans = 98 - 19 - 25 = 54
        return answer
        # Ответ 54.''',
    ''' 
        # У Миши было 14 батонов хлеба.
        initial_bread_loaves = 14
        # Он купил еще 8 батонов.
        bought_bread_loaves = 8
        # После покупки у него было всего:
        answer = initial_bread_loaves + bought_bread_loaves = 14 + 8 = 22.
        return answer
        # Ответ 22.'''
]

list_th_PAL = [
    ''' 
        # โรเจอร์เริ่มต้นด้วยลูกเทนนิส 5 ลูก 
        tennis_balls = 5 
        # ซื้อเพิ่ม 2 กระป๋อง แต่ละกระป๋องมีลูกเทนนิส 3 ลูก 
        bought_balls = 2 * 3 
        # คำตอบคือ 
        answer = tennis_balls + bought_balls 
        return answer
        # คำตอบคือ 11''',
    ''' 
        # เริ่มต้นด้วยคอมพิวเตอร์ 9 เครื่องในห้องเซิร์ฟเวอร์ 
        initial_computers = 9 
        # มี 4 วัน ตั้งแต่วันจันทร์ถึงวันพฤหัสบดี 
        days = 4 
        # เพิ่มคอมพิวเตอร์ 5 เครื่องต่อวัน 
        added_computers_per_day = 5 
        # จำนวนคอมพิวเตอร์ที่เพิ่มขึ้นทั้งหมด 
        total_added_computers = days * added_computers_per_day 
        # จำนวนคอมพิวเตอร์ทั้งหมดในห้องเซิร์ฟเวอร์ 
        answer = initial_computers + total_added_computers 
        return answer
        # คำตอบคือ 29''',
    ''' 
        # เริ่มต้นด้วยรถยนต์ 3 คัน 
        initial_cars = 3 
        # มีรถยนต์เพิ่มเข้ามาอีก 2 คัน 
        arriving_cars = 2 
        # จำนวนรถยนต์ทั้งหมดในที่จอด 
        answer = initial_cars + arriving_cars 
        return answer
        # คำตอบคือ 5''',
    ''' 
        # ชอว์นมีของเล่นอยู่ 5 ชิ้น 
        initial_toys = 5 
        # เขาได้รับของเล่นเพิ่ม 2 ชิ้นจากแม่ 
        # ต่อมาเขาได้รับของเล่นเพิ่มอีก 2 ชิ้นจากพ่อ 
        answer = initial_toys + 2 + 2 
        return answer
        # คำตอบคือ 9''',
    ''' 
        # ไมเคิลเริ่มต้นด้วยกอล์ฟบอล 58 ลูก 
        initial_balls = 58
        # เขาสูญเสียกอล์ฟบอล 23 ลูกในวันอังคาร 
        # และเสียอีก 2 ลูกในวันพุธ 
        answer = initial_balls - 23 - 2
        return answer
        # คำตอบคือ 33''',
    ''' 
        # โอลิเวียเริ่มต้นด้วยเงิน 23 บาท 
        initial_money = 23 
        # เธอซื้อเบเกิล 15 ชิ้นด้วยเงินทั้งหมด 
        total_cost_bagels = 15 
        # จำนวนเงินที่เหลือหลังจากซื้อเบเกิล 
        answer = initial_money - total_cost_bagels 
        return answer
        # คำตอบคือ 8''',
    ''' 
        # ลีอามีช็อกโกแลต 32 ชิ้นและน้องสาวเธอมี 42 ชิ้น 
        leah_chocolates = 32 
        sister_chocolates = 42 
        # พวกเขาทานช็อกโกแลตไป 35 ชิ้น 
        eaten_chocolates = 35 
        # จำนวนช็อกโกแลตที่เหลือ 
        remaining_chocolates = (leah_chocolates + sister_chocolates) - eaten_chocolates 
        return remaining_chocolates
        # คำตอบคือ 39'''
]


list_te_PAL = [
    ''' 
        # రోజర్ వద్ద 5 టెన్నిస్ బాల్స్ ఉన్నాయి. 
        tennis_balls = 5 
        # 2 టిన్నులు కొన్నారు, ప్రతి టిన్నులో 3 టెన్నిస్ బాల్స్ ఉన్నాయి 
        bought_balls = 2 * 3 
        # సమాధానం 
        answer = tennis_balls + bought_balls 
        return answer
        # సమాధానం 11''',
    ''' 
        # సర్వర్ గదిలో మొదట 9 కంప్యూటర్లు ఉన్నాయి. 
        initial_computers = 9 
        # సోమవారం నుండి గురువారం వరకు 4 రోజులు ఉన్నాయి. 
        days = 4 
        # ప్రతి రోజు 5 కంప్యూటర్లు చేర్చబడ్డాయి 
        added_computers_per_day = 5 
        # మొత్తం చేర్చబడిన కంప్యూటర్ల సంఖ్య 
        total_added_computers = days * added_computers_per_day 
        # సర్వర్ గదిలో మొత్తం కంప్యూటర్ల సంఖ్య 
        answer = initial_computers + total_added_computers 
        return answer
        # సమాధానం 29''',
    ''' 
        # ప్రారంభంలో 3 కార్లు ఉన్నాయి. 
        initial_cars = 3 
        # మరియు 2 కొత్త కార్లు రాబట్టబడ్డాయి. 
        arriving_cars = 2 
        # పార్కింగ్ లోట్ లో మొత్తం కార్ల సంఖ్య 
        answer = initial_cars + arriving_cars 
        return answer
        # సమాధానం 5''',
    ''' 
        # షాన్ వద్ద 5 బొమ్మలు ఉన్నాయి. 
        initial_toys = 5 
        # అతను తన తల్లి నుండి 2 బొమ్మలు పొందాడు 
        # అనంతరం తన తండ్రి నుండి మరొక 2 బొమ్మలు పొందాడు 
        answer = initial_toys + 2 + 2 
        return answer
        # సమాధానం 9''',
    ''' 
        # మైకేల్ గోల్ఫ్ బంతులతో 58 మొదలుపెట్టాడు 
        initial_balls = 58
        # అతను మంగళవారం 23 గోల్ఫ్ బంతులు కోల్పోయాడు 
        # బుధవారం మరో 2 బంతులు కోల్పోయాడు 
        answer = initial_balls - 23 - 2
        return answer
        # సమాధానం 33''',
    ''' 
        # ఒలివియా వద్ద ప్రారంభ నగదు 23 రూపాయలు 
        initial_money = 23 
        # ఆమె 15 బేగల్స్ కొనుగోలు కోసం ఖర్చుచేసిన మొత్తం ధర 
        total_cost_bagels = 15 
        # బేగల్స్ కొనుగోలు అనంతరం మిగిలిన నగదు 
        answer = initial_money - total_cost_bagels 
        return answer
        # సమాధానం 8''',
    ''' 
        # లియా వద్ద 32 చాక్లెట్లు మరియు ఆమె సోదరి వద్ద 42 చాక్లెట్లు ఉన్నాయి 
        leah_chocolates = 32 
        sister_chocolates = 42 
        # వారు 35 చాక్లెట్లు తిన్నారు 
        eaten_chocolates = 35 
        # మిగిలిన చాక్లెట్ల సంఖ్య 
        remaining_chocolates = (leah_chocolates + sister_chocolates) - eaten_chocolates 
        return remaining_chocolates
        # సమాధానం 39'''
]
                }

final_format_dict = {
    "zh": "答案是：[数字]。",
    "bn": "উত্তর হল: [num]",
    "de": "Die Antwort ist: [num]",
    "es": "La respuesta es: [num]",
    "fr": "La réponse est : [num]",
    "ja": "答えは：[数字]。",
    "ru": "Ответ: [num]",
    "sw": "Jibu ni: [num]",
    "te": "సమాధానం: [num]",
    "th": "คำตอบคือ: [num]",
    "en": "The answer is: [num]"
}

