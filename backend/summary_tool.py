book_summaries_dict = {
    "The Hobbit": (
        "Bilbo Baggins, un hobbit liniștit și iubitor de confort, este luat prin surprindere atunci când un grup de pitici "
        "îl recrutează într-o aventură pentru a recupera comoara furată de dragonul Smaug. Pe parcursul călătoriei, Bilbo "
        "înfruntă troli, goblini și alte creaturi fantastice, descoperindu-și treptat curajul și ingeniozitatea. Povestea "
        "explorează teme precum prietenia, curajul și ieșirea din zona de confort."
    ),
    "1984": (
        "Într-o societate distopică condusă de un regim totalitar, fiecare mișcare a cetățenilor este monitorizată de „Big Brother”. "
        "Gândirea independentă este interzisă, iar realitatea este manipulată constant. Winston Smith, un funcționar obedient, "
        "începe să se revolte în taină, căutând adevărul și libertatea interioară. Romanul este un avertisment despre pericolele "
        "supravegherii totale și pierderea individualității."
    ),
    "Harry Potter and the Sorcerer’s Stone": (
        "Harry Potter, un băiat orfan crescut de rudele sale abuzive, află că este vrăjitor și este invitat la Hogwarts – o școală de magie. "
        "Acolo își face prieteni, descoperă secretele lumii magice și înfruntă primele provocări legate de trecutul său și inamicul său de moarte, Voldemort. "
        "Este o poveste despre prietenie, curaj și descoperirea propriei identități."
    ),
    "To Kill a Mockingbird": (
        "Scout Finch, o fetiță curajoasă din sudul Statelor Unite, își povestește copilăria în timp ce tatăl ei, Atticus, apără un bărbat de culoare "
        "acuzat pe nedrept de viol. Într-un context de rasism profund, romanul explorează justiția, inocența pierdută și formarea conștiinței morale. "
        "Este o poveste emoționantă despre empatie și curaj civil."
    ),
    "The Great Gatsby": (
        "Jay Gatsby, un milionar enigmatic, organizează petreceri fastuoase în speranța că va recâștiga iubirea lui Daisy, femeia pe care a pierdut-o. "
        "Povestea este relatată de Nick Carraway, un observator prins între iluzii și realități amare. Romanul critică visul american și superficialitatea "
        "unei societăți obsedate de statut și aparențe."
    ),
    "Lord of the Flies": (
        "Un grup de băieți supraviețuiește prăbușirii unui avion pe o insulă nelocuită. Inițial încearcă să creeze o societate proprie, dar curând lucrurile "
        "scapă de sub control și haosul pune stăpânire pe ei. Cartea explorează instinctele umane primare, destrămarea ordinii și întunericul care zace în fiecare individ."
    ),
    "Animal Farm": (
        "Animalele de la o fermă se revoltă împotriva stăpânului lor uman și creează o nouă ordine condusă de porci. Cu timpul, conducătorii devin la fel de opresivi ca fostul stăpân, "
        "iar idealurile revoluției se pierd. Este o satiră politică despre trădarea valorilor, corupția puterii și ciclicitatea tiraniei."
    ),
    "Pride and Prejudice": (
        "Elizabeth Bennet, o femeie inteligentă și independentă, se ciocnește de prejudecățile sociale și de mândria domnului Darcy într-o poveste de dragoste complexă. "
        "Pe măsură ce se cunosc mai bine, cei doi depășesc obstacolele impuse de statutul social și orgoliile personale. Romanul analizează cu subtilitate diferențele de clasă "
        "și relațiile dintre sexe."
    ),
    "The Catcher in the Rye": (
        "Holden Caulfield, un adolescent confuz și alienat, fuge de la internatul său și petrece câteva zile haotice în New York. Prin ochii lui vedem o lume pe care o respinge, "
        "în timp ce caută sens, sinceritate și o conexiune autentică. Cartea este un simbol al crizei de identitate și al rezistenței față de falsitatea lumii adulte."
    ),
    "Fahrenheit 451": (
        "Într-un viitor în care cititul este interzis, iar pompierii ard cărți în loc să stingă incendii, Montag – un pompier – începe să pună sub semnul întrebării sistemul. "
        "Prin întâlniri cu persoane curajoase și idei interzise, el se trezește spiritual și intelectual."
    ),
}

def get_summary_by_title(title: str) -> str:
    return book_summaries_dict.get(title, "Rezumatul pentru această carte nu este disponibil.")
