from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import random
from time import time

path = "./results.csv"
def save(text):
    global path
    f = open(path,"a")
    f.write(text)
    f.close()

#Function to display next phase of the experiment
phaseCounter = 0
phaseLocked = False
time_start = None
time_end = None
def nextPhase(mainframe : Frame):
    global phaseCounter
    global phaseLocked
    global time_start
    global time_end
    if(phaseLocked) : return
    phaseCounter+=1
    clear_children(mainframe)
    match phaseCounter:
        case 1: #Training sSession start
            place_text(mainframe,pre_session_text())
            save("Trening\n")
        case 2|5|8|11: #Training session sentence
            place_text(mainframe,fixation_point_text())
            select_name()
            select_active_trn_question()
            save(trn_question_text()[0][0][0]+",")
            save(trn_sentence_completer_text()[0][0][0]+",")
            save(str(trn_correct_answer())+",")
            mainframe.after(800,lambda : clear_children(mainframe))
            mainframe.after(800,lambda : place_text(mainframe,trn_question_text()))
            
        case 3|6|9|12 : #Training session query
            place_text(mainframe,mask_text())
            
            mainframe.after(34,lambda : clear_children(mainframe))
            mainframe.after(34,lambda : place_text(mainframe,trn_sentence_completer_text()))
            
            mainframe.after(68,lambda : clear_children(mainframe))
            mainframe.after(68,lambda : place_text(mainframe,mask_text()))
            
            mainframe.after(102,lambda : clear_children(mainframe))
            mainframe.after(102,lambda : place_text(mainframe,trn_query_text()))
            
            phaseLocked = True
            time_start = time()
        case 4|7|10|13: # display if correct, then loop to next phase
            place_text(mainframe,trn_answer_correctness_text())
            time_end = time()
            save(str(user_answer)+","+str(1000*(time_end-time_start))+"\n")
            mainframe.after(2000,lambda : clear_children(mainframe))
            mainframe.after(2800,lambda : nextPhase(mainframe))
        case 14 | 45 | 76 |107 : #Exp session start
            place_text(mainframe,pre_session_text())
            save("Sesja Eksperymentalna "+str(1+(phaseCounter//31))+"\n")
        #Experimental session sentence
        case 15|18|21|24|27|30|33|36|39|42|46|49|52|55|58|61|64|67|70|73|77|80|83|86|89|92|95|98|101|104|108|111|114|117|120|123|126|129|132|135: 
            place_text(mainframe,fixation_point_text())
            select_name()
            select_active_exp_question()
            save(exp_question_text()[0][0][0]+",")
            save(exp_sentence_completer_text()[0][0][0]+",")
            save(str(exp_correct_answer())+",")
            mainframe.after(800,lambda : clear_children(mainframe))
            mainframe.after(800,lambda : place_text(mainframe,exp_question_text()))
        #Experimental session query
        case 16|19|22|25|28|31|34|37|40|43|47|50|53|56|59|62|65|68|71|74|78|81|84|87|90|93|96|99|102|105|109|112|115|118|121|124|127|130|133|136: 
            place_text(mainframe,mask_text())
            
            mainframe.after(34,lambda : clear_children(mainframe))
            mainframe.after(34,lambda : place_text(mainframe,exp_sentence_completer_text()))
            
            mainframe.after(68,lambda : clear_children(mainframe))
            mainframe.after(68,lambda : place_text(mainframe,mask_text()))
            
            mainframe.after(102,lambda : clear_children(mainframe))
            mainframe.after(102,lambda : place_text(mainframe,exp_query_text()))
            time_start = time()
            phaseLocked = True
        # Experimental session - do not display correctness
        case 17|20|23|26|29|32|35|38|41|44|48|51|54|57|60|63|66|69|72|75|79|82|85|88|91|94|97|100|103|106|110|113|116|119|122|125|128|131|134|137: 
            time_end = time()
            save(str(user_answer)+","+str(1000*(time_end-time_start))+"\n")
            mainframe.after(800, lambda : nextPhase(mainframe))
        case 138:
            place_text(mainframe,goodbye_text())
            
#Mock impl. It will save the answer further.
user_answer = None
def recieveAnswer(ans:bool,mainframe:Frame):
    global phaseLocked
    global user_answer
    if(phaseLocked):
        user_answer = ans
        phaseLocked = False
        nextPhase(mainframe)
        
#root config
def root_cfg() -> Tk:
    root = Tk()
    root.attributes('-fullscreen',True)
    root.config(cursor="none")
    root.configure(background="black")
    root.bind("<F5>",quit) # Ubije od razu bez patrzenia na wszystko. (?) 
    
    # bind wants a positional arg in lambda for reasons unknown.
    # IDK what it pulls, but we ignore and plug mainframe which is what we truly want.
    root.bind("<space>",lambda _ : nextPhase(mainframe)) 
    root.bind("<t>",lambda _ : recieveAnswer(True,mainframe))
    root.bind("<n>",lambda _ : recieveAnswer(False,mainframe))
    return root

#mainframe config
def mf_config(root:Tk) -> Frame:
    frame = Frame(root,background="black")
    frame.place(relx=0.5,rely=0.5,anchor="center")
    return frame
#initializator for fonts.
def fonts_init() -> None:
    global DEFAULT_FONT_SIZE
    global norm
    global bold
    global ital
    global bdit #bold-italic
    
    DEFAULT_FONT_SIZE = 21
    norm = Font(size=DEFAULT_FONT_SIZE)
    bold = Font(size=DEFAULT_FONT_SIZE,weight="bold")
    ital = Font(size=DEFAULT_FONT_SIZE,slant="italic")
    bdit = Font(size=DEFAULT_FONT_SIZE,weight="bold",slant="italic")

#Multiple fonts inside one line support
def place_text_line(text_font_pairs:list[tuple[str,Font]],master:Widget) -> None:
    frame = Frame(master,background="black")
    frame.pack(side=TOP)
    for text, font in text_font_pairs:
        ttk.Label(frame,background="black",foreground="white",text=text,font=font).pack(side=LEFT)

#Place multi-line text.
def place_text(mainframe:Frame,lines:list[list[tuple[str,Font]]]) -> None:
    for i in lines:
        place_text_line(i,mainframe)

# De facto used as "clear screen"    
def clear_children(parent: Widget):
    for child in parent.winfo_children(): child.destroy()

#Randomizer that puts puller values into the buffer, then swaps back
def get_random_value_without_repeats(src:list,buf:list):
    if(len(src) == 0):
        for i in buf: src.append(i)
        del buf[:]
    index = random.randint(0,len(src)-1)
    retval = src.pop(index)
    buf.append(retval)
    return retval

# Text aldente
#Instruction formated text
def instruction_text() : 
    return [
    [("INSTRUKCJA WYKONANIA ZADANIA",norm)],
    [("",norm)],
    [("W zadaniu, które za chwilę wykonasz, na ekranie będą pojawiać się zdania z",norm)],
    [("brakującym ostatnim słowem. Kiedy naciśniesz spację, na bardzo krótko",norm)],
    [("wyświetli się brakujący wyraz. Nie przejmuj się jeśli nie zdążysz go przeczytać",norm)],
    [("- nie wpłynie to negatywnie na wynik eksperymentu. Twoim zadaniem będzie",norm)],
    [("udzielenie odpowiedzi na pytanie dotyczące treści poprzedniego zdania,",norm)],
    [("zgodnie z intuicją. Aby odpowiedzieć TAK, naciśnij klawisz [T], aby",norm)],
    [("odpowiedzieć NIE, naciśnij klawisz [N].",norm)],
    [("",norm)],
    [("PRZYKŁAD: Jeśli zobaczysz zdanie ",norm), ("Jurek lubi ... ",bold), ("a po nim słowo ",norm), ("truskawki,",bold)],
    [("na pytanie ",norm), ("Czy Jurek lubi owoce? ",bold),("powinieneś odpowiedzieć naciśnięciem",norm)],
    [("klawisza ",norm), ("[T] ",bold), ("dla odpowiedzi ",norm), ("TAK.",bold)],
    [("",norm)],
    [("Zanim rozpocznie się sesja eksperymentalna, zostaniesz poddany sesji",norm)],
    [("treningowej, która ułatwi Ci zrozumienie zadania. W trakcie sesji treningowej,",norm)],
    [("po każdej udzielonej odpowiedzi zostaniesz poinformowany o tym, czy Twoja",norm)],
    [("odpowiedź była poprawna czy błędna. Informacja o poprawności nie będzie",norm)],
    [("się pojawiać w sesji eksperymentalnej.",norm)],
    [("",norm)],
    [("Aby przejść dalej naciścnij spację.",norm)]]
def pre_session_text() : 
    return [
        [("Zadanie zaraz się rozpocznie.",norm)],
        [("",norm)],
        [("Umieść palce na klawiszach [T] i [N], oznaczających odpowiedzi TAK i NIE.",norm)],
        [("Skup swój wzrok na znaku „+” i uważnie czytaj zdania oraz pytania",norm)],
        [("wyświetlane na ekranie. Nie przejmuj się jeśli nie zauważysz któregoś słowa -",norm)],
        [("odpowiadaj zgodnie ze swoją intuicją.",norm)],
        [("",norm)],
        [("Gdy będziesz gotowy/a naciśnij spację.",norm)]]
def fixation_point_text() : return [[("+",norm)]]

def goodbye_text():
    return [
        [("Koniec eksperymentu",norm)],
        [("",norm)],
        [("Dziękujemy za udział w badaniu!",norm)]]

english_conosants = ["Q","W","R","T","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
english_conosants_buf = []
def mask_text() :
    global english_conosants
    global english_conosants_buf
    retval = ""
    for _ in range(13):
        retval += get_random_value_without_repeats(english_conosants,english_conosants_buf)
    return [[(retval,norm)]]

names = ["Janek", "Andrzej", "Krzysztof","Henryk","Marek","Piotrek",
         "Janusz","Adam","Edward","Grzegorz","Darek","Wojtek","Jacek",
         "Tomasz","Stefan","Bogdan","Antek","Paweł","Maria","Ania","Basia",
         "Ela","Julia","Zosia","Ewa","Małgorzata","Grażyna","Jolanta","Alicja",
         "Agnieszka","Beata","Kasia","Wiktoria","Asia","Iwona","Mikołaj","Kamila"]
names_buf = []
active_name = None
def select_name():
    global names
    global names_buf
    global active_name
    active_name = get_random_value_without_repeats(names,names_buf)

trn_questions = [("Miejscem, w którym przebywa obecnie "," jest [x]."),
                      ("Miejscem, w którym przebywa obecnie "," jest [x]."),
                      (""," ma alergię na [x]."),
                      (""," ma alergię na [x].")]
trn_completers = ["więzienie","przedszkole","pyłki","sierść"]
trn_queries = [("Czy uważasz że "," jest dobrą osobą?"),
                    ("Czy uważasz że "," jest dobrą osobą?"),
                    ("Czy "," może mieć kota?"),
                    ("Czy "," może mieć kota?")]
trn_answers = [False,True,True,False]
trn_active_index = None
trn_indexes = [x for x in range(len(trn_questions))]
trn_indexes_buf = []
def select_active_trn_question():
    global trn_indexes
    global trn_indexes_buf
    global trn_active_index
    trn_active_index = get_random_value_without_repeats(trn_indexes,trn_indexes_buf)

def trn_question_text():
    global trn_active_index
    global trn_questions
    global active_name
    return [[(trn_questions[trn_active_index][0] + active_name + trn_questions[trn_active_index][1],norm)]]

def trn_sentence_completer_text():
    global trn_active_index
    global trn_completers
    return [[(trn_completers[trn_active_index],norm)]]

def trn_query_text():
    global trn_active_index
    global trn_queries
    global active_name
    return [[(trn_queries[trn_active_index][0]+active_name+trn_queries[trn_active_index][1],norm)]]

def trn_correct_answer():
    global trn_active_index
    global trn_answers
    return trn_answers[trn_active_index]

def trn_answer_correctness_text():
    global trn_active_index
    global trn_answers
    global user_answer
    return [[("dobrze",norm)]] if user_answer == trn_answers[trn_active_index] else [[("źle",norm)]]

exp_questions = [" lubi kuchnię [x]."," lubi kuchnię [x].",
                 " lubi czytać książki [x]."," lubi czytać książki [x].",
                 " z zawodu jest [x]."," z zawodu jest [x].",
                 " nie lubi nosić [x]."," nie lubi nosić [x].",
                 " uwielbia [x]."," uwielbia [x]."]
exp_completers = ["japońską.","hiszpańską.","kryminalne.","fantastyczne.",
                  "pilotem.","aktorem.","spodni.","czapek.","słonie.","bajki."]

exp_queries = [("Czy "," lubi sushi?"),
               ("Czy "," lubi sushi?"),
               ("Czy "," ucieszy się z książki o smokach?"),
               ("Czy "," ucieszy się z książki o smokach?"),
               ("Czy "," pracuje w sektorze transportu?"),
               
               ("Czy "," pracuje w sektorze transportu?"),
               ("Czy myślisz, że "," ucieszył_by się z jeansów?"),
               ("Czy myślisz, że "," ucieszył_by się z jeansów?"),
               ("Czy sądzisz, "," chciał_by pójść do zoo?"),
               ("Czy sądzisz, "," chciał_by pójść do zoo?")]
exp_answers = [False,True,True,False,True,False,False,True,True,False,False,True,True,False]
exp_active_index = None
exp_indexes = [x for x in range(len(exp_questions))]
exp_indexes_buf = []

def select_active_exp_question():
    global exp_indexes
    global exp_indexes_buf
    global exp_active_index
    exp_active_index = get_random_value_without_repeats(exp_indexes,exp_indexes_buf)

def exp_question_text():
    global exp_active_index
    global exp_questions
    global active_name
    return [[active_name + exp_questions[exp_active_index],norm]]

def exp_sentence_completer_text():
    global exp_active_index
    global exp_completers
    return [[(exp_completers[exp_active_index],norm)]]

def exp_query_text():
    global exp_active_index
    global exp_queries
    global active_name
    return [[(exp_queries[exp_active_index][0]+active_name+exp_queries[exp_active_index][1],norm)]]


def exp_correct_answer():
    global exp_active_index
    global exp_answers
    return exp_answers[exp_active_index]

def exp_answer_correctness_text():
    global exp_active_index
    global exp_answers
    global user_answer
    return [[("dobrze",norm)]] if user_answer == exp_answers[exp_active_index] else [[("źle",norm)]]

#Tyle jest samego programu.
random.seed()
root = root_cfg()
mainframe = mf_config(root)
fonts_init()
place_text(mainframe,instruction_text())
root.mainloop()


