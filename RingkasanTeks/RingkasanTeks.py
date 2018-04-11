#ALGORITHM PERSILANGAN AYAT & DICTIONARY

import re

class Ringkasan(object):

    
    def split_content_to_sentences(self,content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    def split_content_to_paragraph(self, content):
        return content.split("\n\n")

    def perhubungan_ayat(self, ayat1, ayat2):

        a1 = set(ayat1.split(" "))
        a2 = set(ayat2.split(" "))

        #jika tiada
        if (len(a1) + len(a2)) == 0:
            return 0

        return len(a1.intersection(a2)) / ((len(a1) + len(a2)) / 2)

    def format_ayat(self, ayat):
        ayat = re.sub(r'\W+', '', ayat)
        return ayat

     
    def kira_skor_ayat(self, content):

        # Split the content into sentences
        ayat = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(ayat)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.perhubungan_ayat(ayat[i], ayat[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        ayat_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            ayat_dic[self.format_ayat(ayat[i])] = score
        return ayat_dic

    def get_best_sentence(self, paragraph, ayat_dic):

        # Split the paragraph into sentences
        ayat = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(ayat) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_ayat = ""
        max_value = 0
        for s in ayat:
            strip_s = self.format_ayat(s)
            if strip_s:
                if ayat_dic[strip_s] > max_value:
                    max_value = ayat_dic[strip_s]
                    best_ayat = s

        return best_ayat

    def hasil_ringkasan(self, tajuk, content, ayat_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraph(content)

        # Add the title
        summary = []
        summary.append(tajuk.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, ayat_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)


def main():
    tajuk = "belajar berkumpulan "
    #content = open('gejala.txt', 'r').read()
    content = """   Kita sering mendengar beberapa istilah seperti kumpulan perbincangan, study group, study circle, halaqah ataupun usrah. Pada umumnya, kumpulan perbincangan ini merupakan suatu kumpulan kecil individu yang ditubuhkan untuk membincangkan dan bertukar-tukar pendapat tentang perkara-perkara tertentu bagi kepentingan anggota kumpulan tersebut. Aktiviti ini dianggap suatu tradisi meningkatkan ilmu jika perbincangan itu dijalankan secara berkekalan.

    Dalam proses memahami bahan-bahan yang kita peroleh daripada buku atau kuliah untuk disusun dalam bentuk lebih kemas, kita memerlukan perbincangan. Kerap kali kita mempunyai pecahan-pecahan ilmu yang terasing atau bahan yang berselerak dan kita tidak dapat mengaitkannya dengan konteks yang sebenarnya. Mungkin pecahan-pecahan yang kita miliki tidak cukup untuk kita kaitkan dan sambungkan sebagai satu kesatuan yang jitu.

    Kita memerlukan orang lain untuk memberikan pecahan-pecahan yang tidak kita miliki itu dan menyusunnya sebagaimana isi kandungan itu seharusnya disusun. Tugas itu memerlukan perkongsian pendapat dengan rakan-rakan atau orang yang sama-sama mahu mendapatkan pengetahuan tersebut. Jikalau perbincangan itu disertai oleh orang yang lebih mahir dan pakar, kesan perbincangan itu lebih bermakna.

    Apabila kita bekerja dengan orang lain, kadar kepantasan kita akan meningkat. Hal ini demikian kerana adanya unsur-unsur persaingan dan tentulah kita mahu mengemukakan pendapat yang terbaik dan sumbangan yang bermanfaat kepada kumpulan. Dengan demkian kita akan membuat persediaan awal yang bersungguh-sungguh untuk menyayakan perbincangan itu.

    Namun begitu, kumpulan perbincangan itu ada juga keburukannya. Bagi sesuatu perkara yang rumit dan memerlukan kebolehan intelektual, perbincangan lebih banyak memberikan gangguan dan akhirnya objektif pembelajaran tidak tercapai.
	"""
     # Create a SummaryTool object
    st = Ringkasan()

    # Build the sentences dictionary
    ayat_dic = st.kira_skor_ayat(content)

    # Build the summary with the sentences dictionary
    summary = st.hasil_ringkasan(tajuk, content, ayat_dic)

    
    print(content)
    print("\n**********************************************************************************************\n\n") 
    print(summary)
    print("\n**********************************************************************************************\n\n")
    

    # Print the ratio between the summary length and the original length
    print("")
    print( "Panjang asal petikan : %s" % len(content))
    print( "Panjang ringkasan : %s" % len(summary))
    print ("Ratio ringkasan: %s" % (100 - (100 * (len(summary) /  len(content)))))
    print("\n**********************************************************************************************\n\n")

if __name__ == '__main__':
    main()
   

