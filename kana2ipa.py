def kana2ipa(word):
     IPA_dict={
     'ぴゃ':'pʲa',
     'ぴゅ':'pʲɯ',
     'ぴょ':'pʲo',
    　'びゃ':'bʲa',
     'びゅ':'bʲɯ',
     'びょ':'bʲo',
     'みゃ':'mʲa',
     'みゅ':'mʲɯ',
     'みょ':'mʲo',
     'りゃ':'ɾʲa',
     'りゅ':'ɾʲɯ',
     'りょ':'ɾʲo',
     'きゃ':'kʲa',
     'きゅ':'kʲɯ',
     'きょ':'kʲo',
     'ぎゃ':'ɡʲa',
     'ぎゅ':'ɡʲɯ',
     'ぎょ':'ɡʲo',
     'しゃ':'ɕa',
     'しゅ':'ɕɯ',
     'しょ':'ɕo',
     'じゃ':'ʥa',
     'じゅ':'ʥɯ',
     'じょ':'ʥo',
     'ちゃ':'ʨa',
     'ちゅ':'ʨɯ',
     'ちょ':'ʨo',
     'ぢゃ':'ʥa',
     'ぢゅ':'ʥɯ',
     'ぢょ':'ʥo',
     'にゃ':'ɲa',
     'にゅ':'ɲɯ',
     'にょ':'ɲo',
     'ひゃ':'ça',
     'ひゅ':'çɯ',
     'ひょ':'ço',
     'あ':'a',
     'い':'i',
     'う':'ɯ',
     'え':'e',
     'お':'o',
     'か':'ka',
     'き':'ki',
     'く':'kɯ',
     'け':'ke',
     'こ':'ko',
     'さ':'sa',
     'し':'ɕi',
     'す':'sɯ',
     'せ':'se',
     'そ':'so',
     'た':'ta',
     'ち':'ʨi',
     'つ':'ʦɯ',
     'て':'te',
     'と':'to',
     'な':'na',
     'に':'ni',
     'ぬ':'nɯ',
     'ね':'ne',
     'の':'no',
     'は':'ha',
     'ひ':'çi',
     'ふ':'ɸɯ',
     'へ':'he',
     'ほ':'ho',
     'ま':'ma',
     'み':'mi',
     'む':'mɯ',
     'め':'me',
     'も':'mo',
     'や':'ja',
     'ゆ':'jɯ',
     'よ':'ja',
     'ら':'ɾa',
     'り':'ɾi',
     'る':'ɾɯ',
     'れ':'ɾe',
     'ろ':'ɾo',
     'わ':'ɰa',
     'を':'o',
     'ん':'ɴ',
     'が':'ɡa',
     'ぎ':'ɡi',
     'ぐ':'ɡɯ',
     'げ':'ɡe',
     'ご':'ɡo',
     'ざ':'za',
     'じ':'ʥi',
     'ず':'zɯ',
     'ぜ':'ze',
     'ぞ':'zo',
     'だ':'da',
     'ぢ':'ʥi',
     'づ':'zɯ',
     'で':'de',
     'ど':'do',
     'ば':'ba',
     'び':'bi',
     'ぶ':'bɯ',
     'べ':'be',
     'ぼ':'bo',
     'ぱ':'pa',
     'ぴ':'pi',
     'ぷ':'pɯ',
     'ぺ':'pe',
     'ぽ':'po'
    }
     for char in IPA_dict:
        if char in word:
            word=word.replace(char,IPA_dict[char])
     word_list=list(word)


     # do geminates and glottal stops
     done=False
     while not done:
         try:
             i=word_list.index('っ')
             if i==len(word_list)-1:
                 word_list[i]='ʔ'
             else:
                 word_list[i]=word_list[i+1]
                 word_list[i+1]='ː'
         except ValueError:
             done=True

     # add length sign for long vowels
     i=0
     while i<len(word_list)-1:
         if word_list[i]==word_list[i+1]:
             word_list[i+1]='ː'
         i+=1

     # oɯ in Japanese is just oː

     word=''.join(word_list)
     word=word.replace('oɯ','oː')
     word=word.replace('ー','ː')

     return word
     
             

     



