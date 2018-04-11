#ALGORITHM FREKUENSI PERKATAAN
import re
from nltk.tokenize import sent_tokenize, word_tokenize
class Ringkasan(object):

    def split_content_to_sentences(self,content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    def remove_katakerja(self,katafrasa):
        
        i = 0
        while i < len(katafrasa):
            if katafrasa[i].startswith('ber'):
                del katafrasa[i]
            elif katafrasa[i].startswith('mem'):
                del katafrasa[i]
            elif katafrasa[i].startswith('meng'):
                del katafrasa[i]
            elif katafrasa[i].startswith('di'):
                del katafrasa[i]
            elif katafrasa[i].startswith('men'):
                del katafrasa[i]
            elif katafrasa[i].startswith('me'):
                del katafrasa[i]
            elif katafrasa[i].startswith('ter'):
                del katafrasa[i]
            else:
                i+=1
            s = ' '.join(katafrasa)
        return s.split()

    def stopword(self, content):

        stopword  = ['ada','adakah','adakan','adalah','adanya','adapun','agak','agar','akan','aku']
        stopword += ['akulah','alangkah','allah','amat','antara','antaramu','antaranya','apa','apa-apapun','apabila']
        stopword += ['atas','atasmu','atasnya','atau','ataukah','ataupun']
        stopword += ['bagaimana','bagi','bahawa','bahkan','bahwa','banyak','banyaknya','barangsiapa','bawah']
        stopword += ['beberapa','begitu','begitupun','belaka','belum','berada','berkenaan','berupa','berserta','belakang','besar']
        stopword += ['biarpun','bila','bilamana','boleh','bukankah','bukanlah','cantik']
        stopword += ['dahulu','dalam','dalamnya','dan','dapat','dapati','dapatkah','dapatlah','dari','daripada','dunia']
        stopword += ['demi','demikian','demikianlah','dengan','dengannya','di','dia','dialah','didapati','dimana']
        stopword += ['engkau','engkaulah','engkaupun']
        stopword += ['hai','hampir','hanya','hanyalah','hendak','hendaklah','hingga','gus','hadapan']
        stopword += ['ia','iaitu','ialah','ianya','inginkah','ini','inikah','inilah','itu', 'itukah','itulah']
        stopword += ['jadi','jangan','janganlah','jika','jikalau','jika','jikalau','jua','juapun','juga']
        stopword += ['kalau','kami','kamikah','kamipun','kamu','katakan','ke','kecuali','kelak','kembali']
        stopword += ['kemudian','kepada','kepadaku','kepadanya','kepadamu','kerana','kerananya','kesan','ketika','kini']
        stopword += ['kita','ku','kurang','lagi','lain','lalu','lamanya','langsung','lebih']
        stopword += ['mahu','maka','malah','mana','manapun','masih','masing','masing-masing','melainkan']
        stopword += ['memang','mempunyai','mendapat','mendapatkan','mengadakan','mengapa','mengapakah','mengenai','menjadi','menyebabkan','menyebabkannya']
        stopword += ['mereka','merekalah','merekapun','meskipun','mu']
        stopword += ['nescaya','niscaya','nya', 'olah','oleh','orang','nanti']
        stopword += ['pada','padahal','padamu','padanya','paling','para','perlulah','pepatah','pantas']
        stopword += ['pasti','patut','per','pergi','perkara','perlu','pernah','pertama','pula','pun','pelbagai']
        stopword += ['sahaja','saja','saling','sama','sama-sama','samakah','sambil','sampai','sana','sangat','sangatlah','saya','se']
        stopword += ['semakin','seandainya','sebab','sebagai','sebagaimana','sebanyak','sebelum','sebenar','sebenarnya']
        stopword += ['secara','sedang','sedangkan','sedikit','sedikitpun','segala','sehingga','sejak','sekali','sekalipun','sebelah']
        stopword += ['sekalian','sekarang','sekitar','selain','sekarang','sekitar','selain','selalu','selama','selama-lamanya']
        stopword += ['seluruh','seluruhnya','sementara','semua','sentiasa','sendiri','seolah','seolah-olah','seorang','suka','sukar']
        stopword += ['separuh','sepatutnya','seperti','seraya','sering','serta','seseorang','sesiapa','sesuatu','sesudah','sesungguhnya']
        stopword += ['setelah','setiap','siapa','siapakah','sini','situ','situlah','suatu','sudah','sudahkah','sungguh','sungguhpun']
        stopword += ['supaya','tadinya','tahukah','tak','tanpa','tanya','tanyakanlah','tapi','telah','tentang','tentu','terdapat','terhadap']
        stopword += ['terhadapmu','termasuk','terpaksa','tertentu','tetapi','tiada','tiadakah','tiap','tiap-tiap','tidak','tidakkah']
        stopword += ['tidaklah','turut','untuk','untukmu']
        stopword += ['wahai','walau','walaupun','wajar','ya','yaini','yaitu','yakni','yang']

        #contentnew = content.lower().replace(".","")
        nstr = re.sub(r'[?|$|.|!|,|''|"|-]',r'',content)
        contentnew = nstr.lower()
        wordlist = word_tokenize(contentnew)
        

        return [w for w in wordlist if w not in stopword]

    def freq_summary(self,tajuk,katafreq,content):
       
        
        katafrasa = [i[0] for i in katafreq]
        katafrasa = self.remove_katakerja(katafrasa)
        sentences = sent_tokenize(content)
        c = tajuk.split()
        katafrasa = katafrasa + c
        
        stt=[]
        for sentence in sentences:
            if (any(map(lambda word: word in sentence, katafrasa))):
                stt.append(sentence)
        sr= " ".join(stt)
        return sr




def main():
    tajuk = "belajar berkumpulan"
    content = open('belajar.txt', 'r').read()
   
    st = Ringkasan()
    y =[]
   
    wordlist = st.stopword(content)
    wordfreq = []
    for w in wordlist:
        if (wordlist.count(w) > 6):
            wordfreq.append(wordlist.count(w))
     
    print("Petikan Asal\n" + content +"\n")
    print("\n**********************************************************************************************\n\n")
    
    
    y = sorted(zip(wordlist,wordfreq), key=lambda x:x[1], reverse=True)
    katafreq=[]
    for s in y:
        if s not in katafreq:
            katafreq.append(s)

    print(katafreq)
    print("\n**********************************************************************************************\n\n")

    summary = st.freq_summary(tajuk,katafreq,content)
    
    print(summary)

    print("\n**********************************************************************************************\n\n")
    
    print( "Panjang asal petikan : %s" %  len(content) )
    print( "Panjang ringkasan : %s" % len(summary))
    print ("Ratio ringkasan: %s" % (100 - (100 * (len(summary) / len(content)))))
    
    print("\n**********************************************************************************************\n\n")

    katafrasa = [i[0] for i in katafreq]
    katafrasa = st.remove_katakerja(katafrasa)

    print(katafrasa)




if __name__ == '__main__':
    main()
   