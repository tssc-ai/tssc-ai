### Epigrafe {.unnumbered .unlisted}

> Il significato non è localizzato in un termine né depositato staticamente in una rete di relazioni: esso emerge come evento distribuito quando un contesto perturba una memoria strutturale. In tale evento, pattern ricorrenti possono stabilizzarsi in nuove unità mentali, generando un lessico interno non necessariamente coincidente con il lessico esterno.

## Introduzione {#sec:1}

La modellazione del significato è stata spesso costruita attorno a oggetti relativamente stabili: termini, concetti, nodi, vettori, matrici, reti di relazioni, embedding e strutture associative. Tali oggetti hanno reso possibile una grande quantità di analisi teoriche e computazionali, ma tendono a lasciare in ombra un punto decisivo: il significato non si manifesta mai come pura struttura a riposo. Esso appare sempre in una situazione, in risposta a una sollecitazione, come configurazione attuale di un sistema che interpreta.

La presente teoria nasce da questa distinzione. Una rete di relazioni può descrivere ciò che un sistema ha sedimentato; un vettore può rappresentare una posizione in uno spazio semantico; un grafo può conservare una memoria associativa. Tuttavia, nessuno di questi oggetti coincide ancora con il significato in atto. Il significato emerge quando una memoria strutturale viene perturbata da un contesto e produce una risposta distribuita. Tale risposta è ciò che qui viene chiamato Campo Semantico.

Il Campo Semantico non è dunque un luogo del sistema, né una proprietà statica di un termine. È un evento distribuito: una configurazione temporaneamente attualizzata, osservabile e interpretabile, generata dalla collisione tra un ingresso contestuale e un mezzo semantico persistente. In questa prospettiva, il mezzo non contiene direttamente i significati; contiene le condizioni strutturali affinché i significati possano accadere.

Questa inversione ha conseguenze teoriche rilevanti. Se il significato è un evento di campo, allora la semantica non può limitarsi a descrivere la topologia del mezzo. Deve anche descrivere il modo in cui una sorgente contestuale sollecita il sistema, il modo in cui lo stato risultante viene osservato, e il modo in cui stati ricorrenti, conflittuali o lacunari possono trasformare la struttura stessa che li ha generati.

Il lavoro propone quindi una teoria architetturale della semantica dinamica. Essa non prescrive una specifica implementazione computazionale. Dinamiche di diffusione, spreading activation, reti neurali, modelli probabilistici, sistemi su grafo o architetture ibride possono costituirne possibili realizzazioni. Tuttavia, nessuna di queste dinamiche coincide con il nucleo della teoria. Il nucleo consiste nella distinzione tra mezzo, sorgente, campo, osservazione e trasformazione.

La formulazione base della teoria descrive il Campo Semantico come stato distribuito non negativo, indotto da un contesto su un mezzo strutturale. La formulazione estesa introduce invece un livello dinamico più profondo: il Potenziale interno, capace di assumere valori positivi e negativi, nel quale si esprimono sinergia, antagonismo, conflitto e soppressione. Il Campo osservabile è la rettificazione fenomenologica di tale Potenziale. Questo scisma tra Potenziale e Campo consente di preservare la leggibilità semantica dello stato, senza cancellare la dinamica interna del conflitto.

Il contributo più radicale della teoria riguarda però la trasformazione del mezzo. Un sistema semantico non dovrebbe essere pensato soltanto come struttura che interpreta, ma anche come struttura che può essere modificata dalla propria storia interpretativa. Quando pattern di campo ricorrenti, tensioni negative persistenti o lacune d’interfaccia si stabilizzano nel tempo, il mezzo può generare nuove unità mentali latenti, differenziare unità ambigue, fondere configurazioni convergenti o dissolvere unità non più sostenute. La semantica diventa così non soltanto attivazione di significati dati, ma ontogenesi di un lessico interno.

Il paper è organizzato come segue. La \cref{sec:2} definisce il problema teorico e chiarisce perché una topologia semantica statica non sia sufficiente. La \cref{sec:3} posiziona la teoria rispetto ai principali precedenti parziali. Le \crefrange{sec:4}{sec:5} introducono gli oggetti fondamentali della teoria base e gli osservatori del Campo Semantico. La \cref{sec:6} sviluppa la formulazione estesa, fondata sullo scisma tra Potenziale interno e Campo osservabile. La \cref{sec:7} introduce la Trasformazione Strutturale Parametrica, cioè il regime ordinario di adattamento del mezzo a dimensionalità costante. La \cref{sec:8} descrive invece l’Ontogenesi Semantica del mezzo, cioè i casi in cui l’adattamento parametrico non è più sufficiente e diventa necessaria una riorganizzazione della granularità interna. La \cref{sec:9} discute le dinamiche ammissibili come possibili realizzazioni, senza identificarle con la teoria. La \cref{sec:10} esamina la complementarità con i Large Language Models. La \cref{sec:11} indica limiti e sviluppi. La \cref{sec:12} conclude il percorso teorico.


## Il problema: oltre il significato come luogo {#sec:2}

Gran parte delle teorie semantiche, esplicite o implicite, tendono a collocare il significato in un oggetto. Tale oggetto può essere una definizione, un referente, una voce lessicale, una posizione in uno spazio vettoriale, un nodo di una rete o un insieme di relazioni. Anche quando la rappresentazione è distribuita, resta spesso la tendenza a trattare il significato come una configurazione relativamente stabile, calcolabile o recuperabile.

Questa impostazione coglie una parte essenziale del problema, ma non lo esaurisce. Un sistema semantico non si limita a possedere una struttura; risponde a sollecitazioni. La stessa parola può assumere ruoli diversi in contesti diversi; la stessa regione del mezzo può essere mobilitata in modi incompatibili; un termine può diventare centrale in un episodio e marginale in un altro. La semantica effettiva non è quindi riducibile alla posizione del termine nel mezzo, ma dipende dallo stato che il mezzo assume quando viene perturbato.

La distinzione tra struttura e stato è il primo punto teorico fondamentale. La struttura descrive le condizioni di possibilità della risposta; lo stato descrive la risposta in atto. Confondere i due livelli significa attribuire alla topologia ciò che appartiene all’evento. Una rete semantica può dire quali percorsi sono disponibili, quali regioni sono dense, quali nodi risultano centrali. Non dice ancora quale significato emerga quando un contesto specifico attraversa quella rete.

Il problema diventa allora formulabile in questi termini: che cosa accade quando un contesto perturba una memoria strutturale? Quale oggetto teorico descrive la risposta del sistema? Come si distingue la mera attivazione locale da uno stato semantico distribuito? Come si osserva tale stato? E in quali condizioni uno stato ricorrente o conflittuale può trasformare la struttura che lo ha generato?

La teoria dello Spazio Semantico Continuo risponde proponendo il Campo Semantico come oggetto primario della semantica in atto. Il campo non sostituisce il grafo, il vettore o la rete, ma li ricolloca: essi appartengono al mezzo, non al significato attuale. Il significato attuale è lo stato distribuito che emerge dall’interazione tra mezzo e sorgente contestuale.

Questa posizione consente anche di reinterpretare il problema della memoria. Una memoria semantica non è soltanto un archivio di associazioni, ma un mezzo capace di generare eventi. La sua qualità non dipende solo da ciò che conserva, ma da come risponde, da come discrimina, da come sopprime, da come stabilizza e da come si trasforma. La semantica dinamica del campo è quindi anche una teoria della memoria come supporto generativo.


## Related Works: radici e differenza specifica {#sec:3}

La teoria dello Spazio Semantico Continuo non nasce in un vuoto concettuale. Essa si colloca all’incrocio di più tradizioni: reti semantiche, spreading activation, semantica distribuzionale, modelli vettoriali, graph neural networks, teorie del linguaggio del pensiero, conceptual blending e architetture cognitive. Ciascuna di queste tradizioni fornisce precedenti parziali. Nessuna, tuttavia, coincide con la combinazione specifica qui proposta: significato come evento di campo, osservazione formale dello stato, conflitto come informazione strutturale e trasformazione ontogenetica del mezzo.

### Reti semantiche e spreading activation {#sec:3-1}

Le teorie di spreading activation hanno introdotto l’idea che l’elaborazione semantica possa essere descritta come propagazione di attivazione attraverso una rete di concetti *(Collins & Loftus, 1975; Anderson, 1983)*. Esse rappresentano un precedente importante perché rifiutano una concezione puramente locale del significato: un concetto non agisce isolatamente, ma mobilita una regione della rete.

Il limite, dal punto di vista della presente teoria, è che la rete tende a rimanere un supporto relativamente rigido. La propagazione attraversa una struttura data, ma la tensione prodotta dall’attivazione non diventa normalmente il principio di una trasformazione ontologica del mezzo. La rete può attivare concetti, ma non viene tematizzata come sistema che, sotto pressione, può generare nuove unità mentali, differenziare unità ambigue o dissolvere unità non più sostenute.

La teoria del Campo Semantico conserva l’intuizione dinamica della propagazione, ma la riformula. Non è l’attivazione in sé a costituire il significato, bensì il campo osservabile prodotto dalla perturbazione del mezzo. Inoltre, lo stato osservato può retroagire sulla struttura, rendendo possibile una teoria della trasformazione semantica.

### Semantica distribuzionale, embeddings e modelli contestuali {#sec:3-2}

La semantica distribuzionale ha mostrato che il significato dipende dai contesti d’uso e può essere rappresentato in spazi ad alta dimensionalità *(Firth, 1957)*. Gli embeddings *(Mikolov et al., 2013; Pennington et al., 2014)* hanno reso questa intuizione computazionalmente potente, permettendo di trattare termini, frasi e documenti come configurazioni vettoriali.

I modelli neurali contestuali, e in particolare i Large Language Models *(Vaswani et al., 2017; Brown et al., 2020)*, estremizzano questa fluidità. Essi producono stati vettoriali altamente sensibili al contesto, capaci di adattarsi a una grande varietà di input. Da questo punto di vista, costituiscono una delle più potenti realizzazioni contemporanee dell’idea che il significato sia dipendente dal contesto.

La presente teoria non intende negare questo risultato né proporsi come alternativa sostitutiva. Il punto è diverso. Gli LLM eccellono nel produrre stati contestuali; la teoria del Campo Semantico indaga le condizioni sotto cui uno stato contestuale può diventare struttura. Il problema non è la mancanza di contestualità, ma la difficoltà di trasformare la ricorrenza di eventi semantici in una riorganizzazione stabile del mezzo interno, senza ricorrere necessariamente a riaddestramenti costosi, memorie esterne non integrate o aggiornamenti parametrici fragili. Va inoltre precisata la distanza dalle nozioni di embedding e di fattore latente. A differenza di un embedding statico o contestuale, un'unità latente $\zeta$ non è definita soltanto da una posizione nello spazio, ma da una funzione dinamica: si attiva a soglia, completa il proprio nucleo da evidenza parziale e sopprime selettivamente i propri antagonisti, conservando al tempo stesso la distinzione fra fattore comune e residuo episodico. Vi è parentela con l'analisi fattoriale, ma non identità: gli episodi non vengono cancellati, il residuo permane, il fattore ha soglia non-lineare e migra energia fuori dalla sedimentazione pairwise.

### Dinamiche su Grafo e Teorie Matematiche del Campo {#sec:3-3}

L'idea di descrivere il significato non come un'entità puntuale, ma come uno stato continuo distribuito, ha spinto la ricerca verso modelli in cui l'elaborazione avviene su un'infrastruttura relazionale o spaziale. Questo paradigma si è sviluppato storicamente lungo due direttrici principali, l'una computazionale e l'altra matematico-analitica.

Sul versante computazionale, le *Graph Neural Networks* (GNN) *(Scarselli et al., 2008; Kipf & Welling, 2017)* hanno dimostrato che è possibile calcolare stati continui distribuiti sui nodi di un grafo attraverso passaggi iterativi di messaggi (*message passing*). Esse offrono un precedente tecnico formidabile per coniugare dinamiche locali e globali su strutture relazionali. Tuttavia, le GNN assumono normalmente il grafo come un'impalcatura preesistente e ottimizzano gli stati in funzione di un obiettivo predittivo o rappresentazionale esterno. Anche quando la struttura viene appresa o aggiornata, la trasformazione ontologica del mezzo non costituisce di solito il fenomeno semantico centrale.

Sul versante analitico, un precedente teorico diretto è costituito dalle formalizzazioni matematiche della *Semantic Field Theory* (SFT), come proposte ad esempio da Vartziotis (2012), e dai modelli affini di semantica topologica o quantistica *(Aerts et al., 2013)*. Questi approcci traducono l'intuizione linguistica dei campi semantici in rigorosi enti matematici (spazi metrici o spazi di Hilbert), cercando le leggi algebriche di composizione continua che governano la sovrapposizione e l'interferenza dei concetti al fine di calcolare il significato combinato di entità linguistiche complesse.

A una prima analisi, la Teoria dello Spazio Semantico Continuo (TSSC) sembra porsi come perfetta sintesi di questi due mondi: condivide con le GNN l'uso di una struttura relazionale e con la SFT il superamento del nodo isolato a favore di una fenomenologia continua. Tuttavia, la TSSC se ne distacca radicalmente su tre snodi epistemologici e architetturali.

**In primo luogo, differisce lo statuto ontologico del campo e dello spazio.** Nei modelli matematici puri (SFT), il campo continuo *coincide* con lo spazio di rappresentazione: l'infrastruttura stessa è concepita a priori come un *continuum*. Nelle GNN, il grafo agisce tipicamente come un'infrastruttura di calcolo inerte. Nella TSSC, la memoria persistente è un reticolo topologico intrinsecamente discreto (il mezzo $\mathcal{G}$); la continuità non appartiene allo spazio di base, ma unicamente all'**energia dinamica** (il Potenziale e il Campo) che lo attraversa. Il campo non è l'impalcatura geometrica a riposo, ma l'evento fenomenologico termodinamico transitorio.

**In secondo luogo, si ribalta il trattamento del conflitto.** Le teorie matematiche del campo si affidano generalmente a operatori di composizione lineare in cui l'incompatibilità semantica si riduce a *interferenza distruttiva*: i segnali contrapposti si annullano e svaniscono nell'algebra. Nelle GNN, il conflitto è spesso un rumore da minimizzare o viene diluito dai meccanismi di aggregazione. La TSSC, tramite lo scisma duale tra Potenziale Interno e Campo Osservabile, rifiuta il semplice annullamento fenomenologico: il conflitto viene represso sotto la soglia dell'osservabilità, ma genera e si accumula come *Tensione Negativa* e *Tensione di Taglio*. Il mezzo conserva un'esatta metrica dell'attrito strutturale, impedendo che l'antagonismo si dissolva in un vuoto algebrico.

**Infine, emerge una netta divergenza nell'orizzonte teleologico.** I modelli analitici (SFT) e le reti su grafo (GNN) eccellono nella *composizione sincronica* o predittiva degli stati semantici, ma operano in spazi a dimensionalità e granularità tendenzialmente fisse. La differenza specifica della TSSC risiede nell'integrare la dinamica continua con l'**Ontogenesi Semantica diacronica**. Mentre i modelli classici descrivono come i concetti si fondono o si propagano nel momento dell'uso su un palcoscenico inerte, la TSSC assume il mezzo come vera e propria *memoria strutturale semantica* e spiega come l'attrito ripetuto di tali configurazioni continue costringa l'ontologia discreta del sistema a riorganizzarsi irreversibilmente. Il punto decisivo non è calcolare uno stato temporaneo sui nodi, ma dimostrare come la pressione di tali stati giustifichi la nascita (Genesi), la differenziazione (Mitosi) o la soppressione (Apoptosi) delle unità mentali interne. La fenomenologia di campo non è il fine ultimo della computazione, ma il motore causale per l'evoluzione strutturale del vocabolario sistemico.

### Language of Thought e lessico mentale {#sec:3-4}

Le teorie del linguaggio del pensiero hanno sostenuto che la cognizione possa essere organizzata attraverso un sistema rappresentazionale interno *(Fodor, 1975)*. Esse costituiscono un precedente importante perché riconoscono che il pensiero non coincide necessariamente con il linguaggio naturale esterno.

La differenza specifica è che, nella teoria qui proposta, il linguaggio mentale non viene assunto come struttura data. Esso può emergere dalla dinamica del mezzo. Nuove unità mentali latenti possono formarsi quando pattern di campo ricorrenti, tensioni persistenti o lacune d’interfaccia vengono stabilizzati come entità interne. Il lessico mentale è quindi un risultato ontogenetico, non un presupposto.

### Conceptual Blending e creazione concettuale {#sec:3-5}

Le teorie del conceptual blending *(Fauconnier & Turner, 1998)* hanno mostrato che nuove strutture concettuali possono emergere dall’integrazione di domini distinti. La teoria dello Spazio Semantico Continuo condivide l’idea che la semantica non sia solo recupero, ma produzione.

La differenza sta nel livello esplicativo. La novità concettuale non viene descritta soltanto come combinazione di spazi mentali, ma come stabilizzazione strutturale di pattern di campo. La creazione concettuale diventa così un fenomeno del mezzo: una risposta alla ricorrenza, al conflitto, alla lacuna o alla convergenza di stati semantici osservati.

### Differenza specifica {#sec:3-6}

La differenza specifica della teoria non consiste nell’aver introdotto isolatamente attivazione su rete, rappresentazioni distribuite, grafi, stati contestuali o lessico mentale. Ognuno di questi elementi possiede precedenti riconoscibili.

Il contributo originale consiste nella loro unificazione in una teoria del significato come evento di campo. In questa teoria, la frizione dinamica tra Potenziale interno e Campo osservabile produce tensioni misurabili; tali tensioni possono motivare una riorganizzazione dell’ontologia interna del mezzo. Il sistema non si limita ad attivare concetti già dati: può generare, differenziare, fondere o dissolvere unità mentali latenti.


## Oggetti fondamentali e Struttura Estesa del Mezzo {#sec:4}

Questa sezione introduce l'impalcatura topologica e ontologica della teoria. Per mediare tra la contingenza dell'evento (il singolo episodio semantico) e la permanenza della memoria (il lessico strutturato), la teoria rigetta il collasso istantaneo dell'informazione e postula un'**Architettura Duale**. Il modello opera su una struttura estesa in cui i concetti stabili e la memoria delle loro co-occorrenze episodiche coesistono in spazi topologicamente distinti ma interconnessi.

### Universo linguistico e partizione del vocabolario {#sec:4-1}

Sia $\mathcal U$ l’universo linguistico, cioè l’insieme teorico degli elementi simbolici, lessicali o testuali che possono comparire nei contesti osservabili esterni.

Il modello astrae da questo universo un proprio vocabolario interno stabile, denotato con $\mathcal V$. A differenza delle reti associative piatte, $\mathcal V$ è rigorosamente partizionato in due sottoinsiemi mutuamente esclusivi:

$$
\mathcal V = \mathcal V_{\mathrm{lex}} \cup \mathcal V_{\mathrm{lat}}
$$

- $\mathcal V_{\mathrm{lex}}$ è il **vocabolario osservabile (lessicale)**. Costituisce l'interfaccia esplicita del modello ed è un sottoinsieme dell'universo esterno ($\mathcal V_{\mathrm{lex}} \subseteq \mathcal U$). Questo insieme cresce tipicamente attraverso la Genesi per Lacuna d'Interfaccia: quando il modello incontra un elemento esterno ignoto ($u \in \mathcal U \setminus \mathcal V_{\mathrm{lex}}$) e lo assimila tramite un Nodo Ombra, quest'ultimo, una volta stabilizzato, entra a far parte stabilmente di $\mathcal V_{\mathrm{lex}}$.
- $\mathcal V_{\mathrm{lat}}$ è l'**ontologia latente**. Raccoglie le unità mentali ($\zeta$) generate ontogeneticamente dal modello come cause comuni latenti di pattern ricorrenti (Aggregazione), come esito della differenziazione di bacini di significato sovrapposti (Mitosi) o come risultato dell'unificazione di unità ridondanti (Coalescenza). A differenza dei fattori episodici in $\mathcal X$, che registrano eventi situati, le unità in $\mathcal V_{\mathrm{lat}}$ sono variabili dinamiche stabili: la loro ragione d'essere non è archiviare un episodio, ma permettere al sistema di completare pattern da evidenza parziale e di sopprimere selettivamente i propri antagonisti. Poiché queste unità sono cause strutturali puramente endogene, non derivano da alcun termine del vocabolario esterno ($\mathcal V_{\mathrm{lat}} \cap \mathcal U = \emptyset$).

La distinzione tra $\mathcal U$ e $\mathcal V_{\mathrm{lex}}$ definisce i limiti dell'interfaccia corrente del modello; la distinzione tra $\mathcal V_{\mathrm{lex}}$ e $\mathcal V_{\mathrm{lat}}$ garantisce che la mappa concettuale interna possa evolvere strutturalmente in modo autonomo, sviluppando un lessico mentale non necessariamente isomorfo al vocabolario esterno.

### L'Architettura Duale e i Fattori Episodici ($\mathcal X$) {#sec:4-2}

Il mezzo semantico non può ridursi a un archivio di concetti stabili; deve anche processare e conservare le tracce storiche degli eventi senza polverizzarle. Nelle reti classiche, un evento contestuale che coinvolge molteplici unità viene tipicamente memorizzato proiettando immediatamente una cricca densa di archi pairwise tra di esse. Questo approccio causa una rapida esplosione combinatoria e, soprattutto, distrugge l'informazione topologica di ordine superiore (l'iper-relazione unitaria dell'evento).

Per evitare questo errore categoriale, il modello reifica l'evento attraverso un **Fattore Episodico** $\chi_C$. Un fattore episodico non è una nuova unità mentale, non è un concetto provvisorio e non appartiene a $\mathcal V$. È un *iperarco contestuale reificato*, un dispositivo transazionale che **registra topologicamente la co-mobilitazione** di un gruppo di unità stabili in un preciso evento. L'insieme di tutti i fattori episodici generati e conservati dal modello è denotato con $\mathcal X$.

La struttura estesa del mezzo assume quindi la forma di un grafo eterogeneo (formalmente, un *Factor Graph* topologico):

$$
\mathcal G^+ = (\mathcal N^+, E^+)
$$

L'insieme esteso dei nodi $\mathcal N^+$ affianca all'ontologia stabile il layer episodico:

$$
\mathcal N^+ = \mathcal V_{\mathrm{lex}} \cup \mathcal V_{\mathrm{lat}} \cup \mathcal X
$$

Questa distinzione topologica risolve un problema epistemologico profondo: le unità in $\mathcal V$ sono *variabili di stato* su cui la dinamica semantica può stabilizzarsi e sostare; i fattori in $\mathcal X$ sono *eventi di routing* (o transazioni) che la dinamica attraversa per rievocare configurazioni contingenti passate, senza che essi costituiscano un significato autonomo. I fattori episodici non vengono mai compressi né sostituiti da unità latenti: restano tracce storiche separate, leggibili come istanze parziali delle cause comuni che il sistema apprende nel tempo.

### Tipizzazione delle Relazioni {#sec:4-3}

Di conseguenza, anche l'insieme delle relazioni $E^+$ è rigorosamente tipizzato, impedendo al modello di confondere la vicinanza semantica astratta con la contingenza storico-temporale:

$$
E^+ = E_{\mathrm{sem}} \cup E_{\mathrm{inc}}
$$

- $E_{\mathrm{sem}}$ definisce gli **archi semantici stabili**. Connettono esclusivamente nodi appartenenti a $\mathcal V$ (siano essi lessicali o latenti) e descrivono legami cristallizzati nel tempo. Costituiscono il *Grafo Semantico* $\mathcal G_{\mathrm{sem}} = (\mathcal V, E_{\mathrm{sem}})$ e possiedono magnitudo strutturale ($\mathbf M$) e polarità dinamica ($\mathbf W$).
- $E_{\mathrm{inc}}$ definisce gli **archi di incidenza**. Connettono i fattori episodici $\chi \in \mathcal X$ ai nodi del vocabolario $\mathcal V$ co-mobilitati in quell'evento. Essi costituiscono l'*Iper-grafo Episodico* $\mathcal G_{\mathrm{epis}} = (\mathcal V \cup \mathcal X, E_{\mathrm{inc}})$. Non trasportano significato stabile astratto, ma quantificano l'intensità della partecipazione di un nodo a uno specifico contesto episodico.

La ridondanza tra fattori episodici simili non viene risolta con archi interni a $\mathcal X$. Una tale struttura genererebbe *semantic bleeding*: un contesto attuale rievocherebbe impropriamente i dettagli specifici di episodi storici analoghi, contaminando il campo corrente con varianti non pertinenti. Inoltre, comprimere o collegare gli iperarchi ne tradirebbe la funzione costitutiva: essi sono stati introdotti precisamente per non collassare un evento multi-pivot in una cricca pairwise o in un prototipo archivistico. La ridondanza episodica viene invece assorbita dall'unico canale che la teoria prevede a tale scopo: la sedimentazione strutturale progressiva in $\mathbf M$ e $\mathbf W$ tramite gli accumulatori duali (\cref{sec:7}), e — quando la sedimentazione raggiunge una soglia di stabilità sufficiente — la nascita di una causa comune latente in $\mathcal V_{\mathrm{lat}}$ (\cref{sec:8-2}).

### Contesto e Sorgente {#sec:4-4}

Un contesto $C$ è una configurazione temporanea e osservabile di elementi linguistici in ingresso. Poiché l'interfaccia primaria del modello è definita su $\mathcal V_{\mathrm{lex}}$, il contesto deve essere proiettato sul vocabolario osservabile:

$$
C_{\mathcal V} = C \cap \mathcal V_{\mathrm{lex}}.
$$

La **sorgente semantica** $S_C$ è la forma vettoriale con cui il contesto sollecita il mezzo strutturale:

$$
S_C : \mathcal V \to \mathbb R_{\ge 0}.
$$

Essa indica quali nodi di interfaccia vengono perturbati per primi e con quale intensità iniziale.

### Campo Semantico {#sec:4-5}

Dato il mezzo esteso $\mathcal G^+$ e una sorgente $S_C$, il Campo Semantico è la risposta distribuita della rete alla perturbazione:

$$
\Psi_C = \mathcal D(\mathcal G^+, S_C),
$$

oppure, nella sua forma fenomenologica osservata solo sui nodi stabili:

$$
\Psi_C : \mathcal V \to \mathbb R_{\ge 0}.
$$

Il campo è l’oggetto semantico primario della fenomenologia in atto. Non coincide con la sorgente (input), né si riduce alla topologia inerte del grafo a riposo. È lo *stato-evento* transitorio che si attualizza quando l'energia dell'ingresso attraversa i vincoli del mezzo. Come si vedrà nelle sezioni successive, è la morfologia interna di questo campo a determinare la creazione di un nuovo fattore episodico in $\mathcal X$ e, nel lungo termine, a guidare le trasformazioni ontogenetiche in $\mathcal V_{\mathrm{lat}}$.


## Osservazione del Campo Semantico {#sec:5}

Una teoria del campo non può limitarsi a generare stati. Deve anche definire come tali stati vengano osservati, confrontati e resi semanticamente leggibili. Il Campo Semantico, infatti, non è immediatamente identico alla sua interpretazione: esso è una configurazione distribuita di intensità sul mezzo, mentre l’osservazione è l’insieme degli operatori attraverso cui tale configurazione viene descritta, selezionata e valutata.

Questa distinzione è cruciale. La dinamica produce il campo, ma non decide da sola che cosa nel campo sia semanticamente rilevante. Perché il campo diventi utilizzabile, occorre introdurre osservatori capaci di leggerne l’intensità globale, la forma distributiva, il grado di concentrazione, la porzione attiva e la coda dissipativa. L’osservazione non è quindi un’aggiunta esterna alla teoria: è il livello in cui lo stato distribuito diventa oggetto semantico interpretabile.

Gli osservatori del campo hanno quattro funzioni principali. In primo luogo, separano la scala dell’attivazione dalla sua forma. In secondo luogo, permettono di confrontare campi prodotti da contesti diversi. In terzo luogo, distinguono il nucleo informativo dalla dispersione residua. In quarto luogo, forniscono la base per le successive trasformazioni del mezzo. Senza una teoria dell’osservazione, non sarebbe possibile stabilire quali parti di un evento semantico debbano restare episodiche e quali possano invece diventare evidenza strutturale.

### Massa globale del campo {#sec:5-1}

La prima osservabile del Campo Semantico è la sua massa globale. Data una configurazione osservabile $\Psi_C : \mathcal{V} \to \mathbb{R}_{\ge 0}$, la massa è definita come:

$$
M(\Psi_C) = \sum_{t \in \mathcal{V}} \Psi_C(t)
$$

La massa misura l’intensità complessiva della risposta prodotta dal mezzo in seguito alla perturbazione contestuale. Essa non descrive ancora la forma del significato, ma la quantità totale di attivazione fenomenologicamente leggibile generata dall’evento.

Due campi possono avere la stessa massa e forme radicalmente diverse. Un campo può distribuire la propria massa su molti nodi debolmente attivati, oppure concentrarla su un nucleo ristretto di nodi dominanti. Per questa ragione, la massa è un’osservabile necessaria ma non sufficiente. Essa dice quanto il mezzo è stato mobilitato, ma non dice come tale mobilitazione si è organizzata.

La massa svolge tuttavia un ruolo teorico importante. Un campo a massa nulla indica assenza di risposta osservabile o completa soppressione nel caso della teoria estesa. Un campo a massa elevata indica invece che il contesto ha prodotto una perturbazione significativa del mezzo. La massa costituisce quindi il primo livello di leggibilità dello stato: misura la forza globale dell’evento semantico.

### Firma semantica {#sec:5-2}

Per confrontare campi diversi non è sufficiente confrontarne la massa. Occorre separare l’intensità assoluta dalla forma distributiva. A tale scopo, quando $M(\Psi_C) > 0$, si definisce la firma semantica globale:

$$
\Sigma_C(t) = \frac{\Psi_C(t)}{M(\Psi_C)}
$$

La firma $\Sigma_C$ è una distribuzione normalizzata sul vocabolario interno. Essa soddisfa:

$$
\sum_{t \in \mathcal{V}} \Sigma_C(t) = 1
$$

La firma rappresenta la forma del campo indipendentemente dalla sua scala. Essa consente di dire se due contesti hanno prodotto stati semanticamente simili anche quando l’intensità complessiva della risposta è diversa. In questo senso, la massa descrive la quantità dell’evento, mentre la firma descrive la sua morfologia.

La distinzione tra massa e firma permette di evitare una confusione frequente nelle teorie distribuzionali: confondere la forza della risposta con il suo contenuto strutturale. Un campo molto intenso ma disperso può essere meno semanticamente selettivo di un campo meno massivo ma altamente focalizzato. La firma rende osservabile questa differenza.

### Entropia e concentrazione della firma {#sec:5-3}

Poiché la firma semantica si comporta come una distribuzione discreta, su di essa possono essere definiti osservatori informativi. Il più immediato è l’entropia:

$$
H(\Sigma_C) = - \sum_{t \in \mathcal{V}} \Sigma_C(t) \log \Sigma_C(t)
$$

con la convenzione usuale secondo cui i termini nulli non contribuiscono alla somma.

L’entropia misura il grado di dispersione della firma. Un campo a bassa entropia concentra la propria massa su pochi nodi dominanti; un campo ad alta entropia distribuisce la propria attivazione su una regione più ampia del mezzo.

Questa osservabile non va interpretata come misura diretta di qualità semantica. Un campo a bassa entropia non è necessariamente migliore di uno ad alta entropia. La sua interpretazione dipende dal tipo di evento. Una query precisa dovrebbe produrre un campo relativamente focalizzato; un contesto esplorativo o ambiguo può invece generare un campo più diffuso. L’entropia non giudica il campo: ne descrive la morfologia.

Accanto all’entropia, la teoria utilizza la concentrazione quadratica della firma:

$$
Q(\Sigma_C) = \sum_{t \in \mathcal{V}} \Sigma_C(t)^2
$$

Questa quantità cresce quando la massa della firma è concentrata su pochi nodi e diminuisce quando la distribuzione è più uniforme. In statistica e nella fisica dei sistemi complessi, grandezze di questo tipo sono note rispettivamente come indice di Simpson e come Inverse Participation Ratio. Essa è il nucleo matematico da cui deriva il Supporto Effettivo.

### Supporto Effettivo {#sec:5-4}

Il Supporto Effettivo misura il numero ideale di nodi sui quali la massa del campo risulterebbe distribuita se la firma osservata venisse sostituita da una distribuzione uniforme equivalente in termini di concentrazione. Esso è definito come:

$$
N_{\mathrm{eff}}(\Sigma_C) = \frac{1}{\sum_{t \in \mathcal{V}} \Sigma_C(t)^2}
$$

Questa quantità corrisponde all’inverso della concentrazione quadratica della firma. Se la firma è perfettamente uniforme su $K$ nodi e nulla altrove, allora:

$$
N_{\mathrm{eff}}(\Sigma_C) = K
$$

Se invece tutta la massa è concentrata su un solo nodo, allora:

$$
N_{\mathrm{eff}}(\Sigma_C) = 1
$$

Il Supporto Effettivo non coincide necessariamente con il numero di nodi non nulli. Una coda lunga di nodi debolmente attivati può aumentare il supporto formale del campo senza aumentare in modo proporzionale il suo supporto effettivo. Per questa ragione, $N_{\mathrm{eff}}$ è più adatto del semplice conteggio dei nodi attivi a descrivere la dimensionalità semantica reale dell’evento.

Il ruolo teorico del Supporto Effettivo è duplice. Da un lato, esso osserva la forma del campo. Dall’altro, consente di definire una soglia semantica endogena, evitando che il Supporto Attivo dipenda da un parametro arbitrario.

### Supporto Attivo e soglia semantica endogena {#sec:5-5}

Il Supporto Attivo identifica la regione del mezzo effettivamente coinvolta in modo significativo dallo stato semantico. In una formulazione puramente preliminare, si potrebbe definire mediante una soglia semantica di attivazione $\varepsilon_{\mathrm{act}}$:

$$
\mathcal{A}_C^{(\varepsilon_{\mathrm{act}})} = \{\, t \in \mathcal{V} \mid \Psi_C(t) \ge \varepsilon_{\mathrm{act}} \,\}
$$

Tuttavia, assumere $\varepsilon_{\mathrm{act}}$ come parametro libero costante introdurrebbe una difficoltà metodologica. Una soglia fissata dall’esterno applicherebbe lo stesso criterio di taglio a campi altamente focalizzati e a campi esplorativi diffusi. In questo modo, il campo verrebbe osservato attraverso una misura indipendente dalla sua morfologia, violando il principio di endogeneità della teoria.

La teoria postula quindi che la soglia semantica non debba essere imposta dall’esterno, ma dedotta come proprietà emergente dello stato. Se $N_{\mathrm{eff}}(\Sigma_C)$ esprime il numero ideale di gradi di libertà attivati dal campo, allora la soglia naturale è l’attivazione media che ciascuno di quei gradi di libertà riceverebbe se l’intera massa del campo fosse distribuita uniformemente su di essi:

$$
\varepsilon_{\mathrm{act}}^*(C) = \frac{M(\Psi_C)}{N_{\mathrm{eff}}(\Sigma_C)}
$$

Sostituendo la definizione di $N_{\mathrm{eff}}$ si ottiene:

$$
\varepsilon_{\mathrm{act}}^*(C) = M(\Psi_C) \cdot \sum_{t \in \mathcal{V}} \Sigma_C(t)^2
$$

Poiché $\Sigma_C(t) = \Psi_C(t) / M(\Psi_C)$ segue:

$$
\varepsilon_{\mathrm{act}}^*(C) = M(\Psi_C) \cdot \sum_{t \in \mathcal{V}} \left( \frac{\Psi_C(t)}{M(\Psi_C)} \right)^2
$$

quindi:

$$
\varepsilon_{\mathrm{act}}^*(C) = \frac{\sum_{t \in \mathcal{V}} \Psi_C(t)^2}{M(\Psi_C)}
$$

Poiché $M(\Psi_C) = \sum_{t \in \mathcal{V}} \Psi_C(t)$, la soglia può essere scritta anche come:

$$
\varepsilon_{\mathrm{act}}^*(C) = \sum_{t \in \mathcal{V}} \Psi_C(t) \cdot \Sigma_C(t)
$$

La Soglia di Autoconsistenza Entropica coincide dunque con il valore atteso dell’intensità del campo sotto la sua stessa firma distribuzionale. Il campo definisce il proprio livello di guardia. I nodi che superano tale valore costituiscono il Segnale; i nodi che restano al di sotto appartengono alla coda dissipativa.

La definizione canonica del Supporto Attivo diventa:

$$
\mathcal{A}_C^* = \{\, t \in \mathcal{V} \mid \Psi_C(t) \ge \varepsilon_{\mathrm{act}}^*(C) \,\}
$$

In questa forma, il Supporto Attivo non dipende più da un numero magico scelto dall’osservatore. Dipende dalla forma stessa del campo.

Qualora policy specifiche richiedano una lettura più permissiva o più severa, la teoria non introduce una soglia assoluta arbitraria, ma un moltiplicatore adimensionale $\alpha$ centrato su $1$:

$$
\varepsilon_{\mathrm{act}}(C) = \alpha \cdot \varepsilon_{\mathrm{act}}^*(C)
$$

Il caso $\alpha = 1$ resta la scelta canonica. Valori $\alpha < 1$ producono una lettura più inclusiva; valori $\alpha > 1$ producono una lettura più selettiva.

### Massa ristretta e Firma Ristretta {#sec:5-6}

Una volta isolato il Supporto Attivo $\mathcal{A}_C^*$, il sistema può concentrare la propria osservazione esclusivamente sul nucleo semantico dell’evento, escludendo la coda dissipativa. Tuttavia, il taglio del campo produce una conseguenza matematica immediata: la somma della firma trattenuta dal solo Supporto Attivo non è più necessariamente uguale a $1$.

Per questa ragione, occorre distinguere tra massa globale del campo e massa ristretta del nucleo. Si definisce la Massa Ristretta come l’attivazione totale trattenuta dal Supporto Attivo canonico:

$$
M^*(\Psi_C) = \sum_{t \in \mathcal{A}_C^*} \Psi_C(t)
$$

Poiché il taglio della coda dissipativa comporta in generale $M^*(\Psi_C) \le M(\Psi_C)$, la distribuzione dell’energia all’interno del solo nucleo richiede una nuova normalizzazione. Si definisce quindi la Firma Ristretta:

$$
\widetilde{\Sigma}_C(t) =
\begin{cases}
\dfrac{\Psi_C(t)}{M^*(\Psi_C)} & \text{se } t \in \mathcal{A}_C^*, \\
0 & \text{altrimenti.}
\end{cases}
$$

Per costruzione, la Firma Ristretta ripristina la normalizzazione sul solo nucleo attivo, tale per cui $\sum_{t \in \mathcal{A}_C^*} \widetilde{\Sigma}_C(t) = 1$.

La Firma Ristretta costituisce l’oggetto osservativo primario per i processi di ordine superiore. Essa restituisce una distribuzione di probabilità depurata dall’inerzia del mezzo, essenziale per calcolare operatori relazionali puliti, confrontare nuclei semantici distinti e guidare la selezione del Nucleo Trasformativo.

La distinzione tra firma globale e firma ristretta è importante. La firma globale descrive la morfologia complessiva dell’evento, inclusa la sua coda dissipativa. La firma ristretta descrive invece la forma interna del Segnale dopo il taglio endogeno. La prima serve a osservare l’intero campo; la seconda serve a lavorare sul nucleo semanticamente operativo.

### Proprietà della soglia di autoconsistenza {#sec:5-7}

La Soglia di Autoconsistenza Entropica possiede tre proprietà metodologicamente rilevanti.

In primo luogo, è parameter-free nel caso canonico. Non richiede una soglia fissata dall’esterno, ma deriva direttamente dalla massa e dalla firma del campo.

In secondo luogo, respira con l’evento. Se il contesto genera un campo acuminato e a bassa entropia, il termine quadratico domina e la soglia si innalza, recidendo la coda dissipativa. Se invece il campo è diffuso e sfumato, la soglia si abbassa, preservando una regione semantica più ampia.

In terzo luogo, è invariante rispetto alla scala dell’energia immessa. Se il campo viene moltiplicato per una costante positiva $k$, anche $\varepsilon_{\mathrm{act}}^*(C)$ viene moltiplicata per $k$. Il criterio di taglio resta quindi coerente rispetto alla forma del campo.

La soglia può essere letta come rapporto tra la norma quadratica del campo e la sua massa:

$$
\varepsilon_{\mathrm{act}}^*(C) = \frac{\lVert \Psi_C \rVert_2^2}{\lVert \Psi_C \rVert_1}.
$$

L'invarianza di scala e l'adattamento endogeno diventano del tutto trasparenti esprimendo la soglia in forma chiusa rispetto alla statistica descrittiva del campo. Ricordando che il momento secondo di una distribuzione è legato alla varianza dalla relazione $E[X^2] = \sigma^2 + \mu^2$, e dividendo per la media $\mu = \bar{x}$, si ottiene un'identità esatta. Indicando con $\bar{x}$ l'attivazione media e con $\mathrm{CV} = \sigma/\bar{x}$ il coefficiente di variazione del campo:

$$
\varepsilon_{\mathrm{act}}^*(C) = \bar{x}\,\big(1 + \mathrm{CV}^2\big).
$$

La soglia è dunque la media del campo, *sollevata in proporzione esatta alla sua dispersione relativa*. Se la sorgente è priva di fuoco --- rumore diffuso o ambiguità --- si ha $\mathrm{CV} \to 0$, la soglia collassa sulla media e il sistema si rifiuta di forzare un'individuazione spuria; se la sorgente è semanticamente focalizzata, l'alta dispersione ($\mathrm{CV} \gg 0$) spinge dinamicamente l'asticella verso l'alto, recidendo la coda dissipativa. È questa, in forma compatta, la ragione per cui l'operatore è parameter-free: il criterio di taglio è la morfologia stessa del campo.

La presenza del termine quadratico rende la soglia sensibile alla localizzazione dello stato. Essa cresce quando pochi nodi concentrano una quota dominante della massa e diminuisce quando l’attivazione è distribuita in modo più uniforme.

### Casi limite {#sec:5-8}

Nel caso di un campo uniforme, se $\Psi_C(t) = c$ per ogni nodo coinvolto, allora:

$$
\varepsilon_{\mathrm{act}}^*(C) = \frac{N c^2}{N c} = c
$$

Tutti i nodi raggiungono la soglia con eguaglianza. Il Supporto Attivo coincide quindi con l’intera regione uniformemente coinvolta.

Nel caso di un campo concentrato su un singolo nodo $t_0$, con massa totale $M$, si ha:

$$
\varepsilon_{\mathrm{act}}^*(C) = \frac{M^2}{M} = M.
$$

Solo il nodo $t_0$ sopravvive al taglio. Il comportamento è quello atteso da un campo perfettamente focalizzato.

Nel caso di un campo bimodale netto, in cui una popolazione di nodi presenta intensità alta $a$ e una popolazione presenta intensità bassa $b$, con $a > b$, la soglia separa il bacino ad alta energia da quello a bassa energia. Il comportamento è coerente con l’interpretazione del Supporto Attivo come nucleo del Segnale e della regione sottosoglia come coda dissipativa.

Questi casi limite mostrano che la soglia endogena non si limita a funzionare in condizioni ordinarie, ma conserva un comportamento interpretabile anche nelle configurazioni estreme.

### Distribuzioni a coda pesante {#sec:5-9}

È essenziale esplicitare il comportamento della soglia nel caso di distribuzioni fortemente asimmetriche a destra, tipiche delle topologie semantiche in cui pochi nodi centrali concentrano alte attivazioni e una vasta periferia assorbe la coda dissipativa.

Poiché la soglia seleziona i nodi che superano il valore atteso di $\Psi_C$ sotto la propria stessa firma, in presenza di distribuzioni heavy-tailed essa tende a comportarsi come un filtro elitario. Il Supporto Attivo $\mathcal{A}_C^*$ può restringersi a un nucleo molto circoscritto di nodi dominanti. La percentuale di massa trattenuta non è una costante garantita a priori, ma una funzione della morfologia dell’evento.

Questo comportamento non costituisce un limite, ma una proprietà di salvaguardia epistemologica e computazionale. La teoria non richiede che il Supporto Attivo trattenga una frazione costante della massa totale. Al contrario, la severità del taglio in presenza di code lunghe impedisce che il mezzo scambi l’ampia dispersione topologica per informazione strutturale rilevante.

Il taglio netto protegge il sistema dal consolidamento del rumore. Solo la porzione di campo autenticamente focale viene candidata a costituire il Nucleo Trasformativo e ad accedere alle successive dinamiche di riorganizzazione parametrica o ontogenetica del mezzo.

### Nucleo Trasformativo e Pivot {#sec:5-10}

Il Supporto Attivo non coincide ancora necessariamente con ciò che deve trasformare il mezzo. Esso individua i nodi semanticamente significativi dell’evento, ma la trasformazione strutturale richiede un’ulteriore selezione. La teoria introduce quindi il Nucleo Trasformativo come sottoinsieme del Supporto Attivo candidato a lasciare traccia nella memoria strutturale.

Il passaggio da Supporto Attivo a Nucleo Trasformativo dipende da osservatori aggiuntivi: coerenza locale, ricorrenza storica, tensione negativa, novità, stabilità e ruolo topologico dei nodi coinvolti. Un nodo può essere attivo in un singolo evento senza meritare aggiornamento strutturale. Viceversa, una configurazione moderatamente attiva ma ricorrente può diventare altamente rilevante per l’apprendimento del mezzo.

Il Nucleo Trasformativo svolge quindi una funzione di filtro tra osservazione e apprendimento. Esso impedisce che ogni attivazione episodica venga convertita in memoria persistente. Le unità che superano questa ulteriore selezione endogena emergono come Pivot. I Pivot costituiscono l’impalcatura semantica dell’evento: non sono semplicemente i nodi più accesi, ma quelli che il sistema giudica sufficientemente informativi da innescare la Trasformazione Strutturale Parametrica tramite accumulo di evidenza o, nei casi di frustrazione profonda, l’ontogenesi del mezzo.

### Osservatori Topologici e Relazionali {#sec:5-11}

Per supportare le trasformazioni del mezzo, l’osservazione di intensità e forma deve essere integrata da altre due famiglie di operatori: gli osservatori topologici e gli osservatori relazionali.

Gli osservatori topologici leggono la struttura relazionale del Supporto Attivo. Proiettando $\mathcal{A}_C^*$ sul mezzo $\mathcal{G}$, si ottiene un sottografo indotto dal nucleo semantico dell’evento. La misura delle sue componenti connesse, della densità interna, della modularità o della distanza tra regioni attive permette di stabilire se l’evento sia semanticamente coeso, frammentato o polarizzato.

Questa informazione è decisiva per la trasformazione del mezzo. Un Supporto Attivo compatto e densamente connesso suggerisce un evento coerente, potenzialmente assimilabile attraverso trasformazione parametrica o coalescenza. Un Supporto Attivo frammentato, composto da componenti distanti o scarsamente comunicanti, può invece segnalare una sovrapposizione impropria di bacini semantici distinti. In tali condizioni, la frammentazione topologica diventa una diagnosi rilevante per la Mitosi Semantica.

Gli osservatori relazionali misurano invece la distanza, la somiglianza o la divergenza tra campi distinti. In particolare, il confronto tra Firme Ristrette consente di valutare la novità di un contesto, la sovrapposizione cronica tra eventi o la divergenza progressiva tra regioni che in origine apparivano unitarie. Metriche simmetriche come la divergenza di Jensen-Shannon possono essere utilizzate per confrontare distribuzioni semantiche depurate dalla coda dissipativa.

Questi osservatori preparano direttamente i processi trasformativi. Una forte sovrapposizione ricorrente tra Firme Ristrette può sostenere la Coalescenza; una divergenza stabile tra campi generati dalla stessa unità può indicare necessità di Mitosi; una distanza persistente tra il lessico osservabile e una posizione latente può contribuire alla formazione di un Nodo Ombra o alla Genesi per lacuna d’interfaccia.

### Sintesi {#sec:5-12}

La teoria dell’osservazione del campo stabilisce il passaggio dallo stato distribuito alla sua leggibilità semantica. Massa, firma, entropia, Supporto Effettivo, Soglia di Autoconsistenza Entropica, Firma Ristretta e osservatori topologico-relazionali costituiscono una catena coerente di osservatori: la massa misura l’intensità dell’evento; la firma ne descrive la forma globale; l’entropia e il Supporto Effettivo ne misurano la dispersione; la soglia endogena ne estrae il Supporto Attivo; la Firma Ristretta normalizza il Segnale depurato dalla coda; gli osservatori topologici e relazionali ne valutano coesione, novità, sovrapposizione e frammentazione; il Nucleo Trasformativo seleziona ciò che può diventare evidenza strutturale.

In questo modo, il campo non viene osservato attraverso parametri arbitrari, ma attraverso grandezze generate dalla sua stessa morfologia. L’evento semantico produce la propria leggibilità.


## Formulazione estesa: Potenziale interno e Campo osservabile {#sec:6}

La teoria base descrive il Campo Semantico come configurazione non negativa, distribuita e osservabile. Questa formulazione è sufficiente per trattare l’emersione del significato come risposta del mezzo a una perturbazione contestuale, e consente di costruire una teoria coerente dell’osservazione: massa, firma, entropia, supporto effettivo, soglia endogena, firma ristretta e Nucleo Trasformativo.

Tuttavia, alcuni fenomeni semantici non sono pienamente descrivibili se il sistema dispone soltanto di stati non negativi. Antagonismo, inibizione, incompatibilità, soppressione attiva, conflitto tra bacini semantici e disambiguazione per esclusione richiedono un livello dinamico più profondo. Non basta sapere quali unità emergono nel campo osservabile: occorre anche sapere quali unità siano state represse, quali regioni siano entrate in collisione e quale costo dinamico sia stato necessario per rendere leggibile un certo stato.

La formulazione estesa introduce quindi uno scisma tra due livelli: il **Potenziale interno** $V_C$, che può assumere valori positivi o negativi, e il **Campo osservabile** $\Psi_C$, che resta non negativo. Il campo osservabile mostra ciò che emerge; il Potenziale interno conserva anche la traccia di ciò che è stato impedito a emergere.

### Perché la teoria base non basta {#sec:6-1}

Nella formulazione base, la risposta del mezzo a un contesto è descritta direttamente come Campo Semantico:

$$
\Psi_C : \mathcal{V} \to \mathbb{R}_{\ge 0}.
$$

Questa scelta ha un vantaggio decisivo: rende il campo immediatamente leggibile come distribuzione di intensità semantica. Non esistono significati negativi, ma solo gradi diversi di partecipazione osservabile all’evento. Tutta la teoria dell’osservazione può quindi essere costruita su grandezze non negative.

Il limite di questa formulazione emerge quando la semantica dell’evento dipende non solo da ciò che viene attivato, ma anche da ciò che viene escluso. In molti casi, un contesto non genera significato soltanto propagando attivazione: genera significato anche reprimendo interpretazioni concorrenti. Una disambiguazione efficace non consiste solo nel portare in primo piano il bacino corretto, ma anche nel sopprimere bacini incompatibili.

Se il modello dispone solo di $\Psi_C$, due situazioni molto diverse possono apparire identiche. Un nodo può essere nullo nel campo osservabile perché non è stato coinvolto dal contesto; oppure può essere nullo perché è stato attivamente soppresso da una dinamica antagonista. Nel primo caso abbiamo semplice irrilevanza; nel secondo caso abbiamo conflitto risolto per esclusione. Dal punto di vista osservabile entrambi appaiono come $\Psi_C(t)=0$, ma dal punto di vista dinamico sono fenomeni radicalmente diversi.

La teoria estesa nasce per rendere trattabile questa differenza senza rinunciare alla chiarezza della formulazione base. Il campo osservabile resta non negativo, ma viene fatto derivare da un livello interno firmato.

### Mezzo strutturale duale {#sec:6-2}

Nella formulazione estesa, il mezzo persistente non è descritto da una sola matrice di pesi, ma da due strutture complementari:

$$
\mathcal{G} = (\mathcal{V}, E, \mathbf{M}, \mathbf{W}).
$$

Qui $\mathcal{V}$ è il vocabolario interno del mezzo, $E$ è l’insieme delle relazioni ammissibili, $\mathbf{M}$ è la matrice di magnitudo strutturale e $\mathbf{W}$ è la matrice di interazione firmata.

La matrice di magnitudo strutturale è non negativa:

$$
\mathbf{M} \in \mathbb{R}_{\ge 0}^{N \times N}.
$$

Essa descrive la geometria del mezzo: quali unità sono strutturalmente vicine, quali regioni sono densamente connesse, quali percorsi risultano disponibili. La matrice $\mathbf{M}$ è il supporto su cui vengono calcolate le osservabili topologiche e geometriche.

La matrice di interazione firmata è invece reale:

$$
\mathbf{W} \in \mathbb{R}^{N \times N}.
$$

Essa governa la dinamica interna dell’episodio. Valori positivi indicano relazioni sinergiche, eccitatorie o convergenti; valori negativi indicano relazioni antagoniste, inibitorie o di mutua esclusione:

$$
w_{ij} > 0 \quad \text{sinergia},
$$

$$
w_{ij} < 0 \quad \text{antagonismo},
$$

$$
w_{ij} = 0 \quad \text{assenza di interazione dinamica netta}.
$$

La distinzione tra $\mathbf{M}$ e $\mathbf{W}$ è essenziale. Due unità possono essere topologicamente vicine proprio perché fortemente opposte. In tal caso, la loro relazione deve essere intensa nella geometria del mezzo, ma antagonista nella dinamica. La magnitudo conserva la forza strutturale della relazione; il segno ne governa la polarità dinamica.

In una formulazione ingenua, si potrebbe essere tentati di assumere che la geometria coincida con la semplice magnitudo della dinamica:

$$
m_{ij} = |w_{ij}|.
$$

La presente teoria rigetta questa identificazione diretta. Se due unità fossero legate da un conflitto cronico, ad esempio da forte eccitazione alternata a forte inibizione, la loro polarità netta $w_{ij}$ potrebbe tendere a zero. Assumendo $m_{ij}=|w_{ij}|$, le due unità apparirebbero topologicamente scollegate, occultando proprio la lacerazione che le unisce.

La matrice $\mathbf{M}$ deve invece registrare l’integrale del coinvolgimento strutturale: la larghezza di banda storica del canale. La matrice $\mathbf{W}$ ne registra il differenziale: il bilancio polarizzato dell’interazione. Solo mantenendo l’indipendenza di $\mathbf{M}$, il mezzo può riconoscere regioni topologicamente densissime ma dinamicamente frustrate. Questa separazione è una condizione necessaria per diagnosticare correttamente tensione di taglio, frattura semantica e Mitosi Semantica.

### Potenziale interno {#sec:6-3}

Quando una sorgente semantica $S_C$ sollecita il mezzo, la risposta primaria del sistema non è più il Campo osservabile, ma il Potenziale interno:

$$
V_C : \mathcal{V} \to \mathbb{R}.
$$

Il Potenziale interno è l’arena algebrica in cui contributi eccitatori e antagonisti si sommano, interferiscono e si sopprimono. Esso rappresenta lo stato dinamico nascosto del mezzo durante l’episodio semantico.

In forma generale, una dinamica ammissibile della teoria estesa può essere scritta come:

$$
V_C = \mathcal{D}_V(\mathcal{G}, S_C, \Theta),
$$

dove $\mathcal{D}_V$ è un operatore dinamico compatibile con la teoria, $S_C$ è la sorgente contestuale e $\Theta$ è l’insieme dei parametri o delle condizioni operative della dinamica scelta.

Il valore di $V_C(t)$ ha significato diagnostico:

- $V_C(t) > 0$ indica una spinta attivante, convergente con la configurazione semantica emergente;
- $V_C(t) \approx 0$ indica inerzia, equilibrio locale o estraneità relativa al contesto;
- $V_C(t) < 0$ indica soppressione attiva, incompatibilità o pressione antagonista.

Questa interpretazione è fondamentale. Un valore negativo non indica un significato negativo. Indica che l’unità corrispondente è stata dinamicamente repressa dall’episodio in corso.

### Campo osservabile come rettificazione {#sec:6-4}

Il Campo Semantico osservabile viene definito come rettificazione non lineare del Potenziale interno:

$$
\Psi_C(t) = \max(0, V_C(t)).
$$

In forma equivalente:

$$
\Psi_C = [V_C]_+.
$$

Dal punto di vista computazionale, questa operazione coincide con la funzione ReLU, Rectified Linear Unit, ubiqua nelle moderne reti neurali. Tuttavia, il suo ruolo qui non è ingegneristico, bensì epistemologico: la rettificazione è l’operatore asimmetrico che traduce la termodinamica nascosta del conflitto, cioè il Potenziale, nella fenomenologia positiva del significato, cioè il Campo.

Questa operazione conserva solo la parte positiva del Potenziale, rendendo il campo semanticamente leggibile come configurazione non negativa. La teoria dell’osservazione sviluppata nella \cref{sec:5} resta quindi applicabile senza essere rifondata.

La rettificazione non cancella il conflitto. Lo separa epistemologicamente. Il Campo osservabile descrive la configurazione fenomenologica del significato; il Potenziale interno descrive il lavoro dinamico necessario per produrla.

Questa distinzione consente di trattare l’inibizione senza introdurre l’idea problematica di un significato negativo. Il conflitto esiste nel Potenziale, ma si manifesta osservativamente come silenzio per soppressione.

### Scisma dinamico tra Potenziale e Campo {#sec:6-5}

Lo scisma tra $V_C$ e $\Psi_C$ introduce una differenza decisiva tra assenza e soppressione.

Se $\Psi_C(t)=0$, il solo campo osservabile non permette di distinguere tra due casi:

$$
V_C(t) = 0,
$$

oppure:

$$
V_C(t) < 0.
$$

Nel primo caso, il nodo non partecipa in modo rilevante all’episodio. Nel secondo, il nodo partecipa negativamente: è stato coinvolto come possibilità incompatibile, respinta o repressa. Il silenzio osservabile può dunque avere due origini diverse: irrilevanza o soppressione.

Questa differenza è essenziale per la teoria della trasformazione. Un nodo semplicemente irrilevante non deve lasciare traccia strutturale. Un nodo ripetutamente soppresso, invece, può indicare la presenza di un antagonismo stabile, di una tensione non risolta o di una frattura semantica ricorrente. In altre parole, ciò che non appare nel campo può comunque essere decisivo per capire il mezzo.

Il Potenziale interno è quindi il luogo in cui il sistema registra la parte invisibile dell’evento semantico: esclusioni, conflitti, opposizioni, attriti e frustrazioni.

### Doppio regime osservativo {#sec:6-6}

La formulazione estesa implica due famiglie di osservatori.

La prima famiglia è costituita dagli osservatori distribuzionali, applicati al Campo osservabile $\Psi_C$. Essi descrivono ciò che emerge: massa, firma, entropia, Supporto Effettivo, soglia endogena, Supporto Attivo, Firma Ristretta, Nucleo Trasformativo e proprietà topologico-relazionali del segnale.

La seconda famiglia è costituita dagli osservatori di conflitto, applicati al Potenziale interno $V_C$. Essi descrivono ciò che viene impedito, soppresso o reso invisibile dalla dinamica antagonista.

Questa biforcazione impedisce di confondere la leggibilità fenomenologica del campo con la totalità della dinamica. Il campo osservabile è ciò che il sistema rende positivo e semanticamente presente. Il Potenziale interno è ciò che il sistema ha dovuto attraversare per produrre quella presenza.

### Tensione Negativa Globale e soglia antagonista {#sec:6-7}

La principale osservabile di conflitto è la Tensione Negativa Globale, definita come la massa complessiva della parte negativa del Potenziale:

$$
\mathcal{T}_{C}^{-} = \sum_{t \in \mathcal{V}} \max(0, -V_C(t)).
$$

Questa quantità misura l’intensità totale della soppressione esercitata nell’episodio. Valori prossimi allo zero indicano che il campo osservabile è stato prodotto senza incontrare forti resistenze interne. Valori elevati indicano invece che la configurazione positiva è emersa al prezzo di una forte repressione di alternative antagoniste.

Si definisce inoltre la componente negativa locale:

$$
\tau_C^-(t) = \max(0, -V_C(t)).
$$

Essa misura la quantità di soppressione subita da ciascuna unità. Quando $\mathcal{T}_{C}^{-} > 0$, è possibile normalizzare la soppressione in una firma negativa globale:

$$
\Omega_C^-(t) = \frac{\tau_C^-(t)}{\mathcal{T}_{C}^{-}}.
$$

La firma negativa non descrive il significato osservabile, ma la distribuzione della soppressione. Essa permette di capire quali regioni del mezzo siano state maggiormente respinte dall’episodio.

Tuttavia, così come il campo positivo possiede una coda dissipativa, anche il Potenziale interno produce un rumore di soppressione: micro-fluttuazioni negative prive di reale peso antagonistico. Non ogni valore $V_C(t)<0$ deve quindi essere promosso a evidenza strutturale. Per isolare la soppressione autenticamente rilevante, la teoria applica al campo negativo lo stesso principio endogeno sviluppato per il Supporto Attivo.

Si definisce la Soglia di Autoconsistenza Antagonista come il valore atteso dell’intensità soppressiva sotto la propria firma negativa:

$$
\varepsilon_{\mathrm{supp}}^*(C) = \sum_{t \in \mathcal{V}} \tau_C^-(t) \cdot \Omega_C^-(t).
$$

In forma equivalente:

$$
\varepsilon_{\mathrm{supp}}^*(C) = \frac{\sum_{t \in \mathcal{V}} \tau_C^-(t)^2}{\mathcal{T}_{C}^{-}}.
$$

Si definisce così il Supporto Negativo Canonico, o Nucleo Soppresso:

$$
\mathcal{S}_C^* = \{\, t \in \mathcal{V} \mid \tau_C^-(t) \ge \varepsilon_{\mathrm{supp}}^*(C) \,\}.
$$

Solo le unità che superano questa soglia partecipano alla soppressione strutturalmente rilevante. Il rumore negativo resta nella coda dissipativa antagonista e non deve contribuire direttamente agli osservatori di conflitto.

Come per il campo positivo, è utile definire una massa negativa ristretta:

$$
\mathcal{T}_{C}^{-*} = \sum_{t \in \mathcal{S}_C^*} \tau_C^-(t),
$$

e una firma negativa ristretta:

$$
\widetilde{\Omega}_C^-(t) =
\begin{cases}
\dfrac{\tau_C^-(t)}{\mathcal{T}_{C}^{-*}} & \text{se } t \in \mathcal{S}_C^* \, \\
0 & \text{altrimenti.}
\end{cases}
$$

La firma negativa ristretta è l’oggetto corretto per confrontare la soppressione con il nucleo positivo del campo. Essa impedisce che micro-soppressioni diffuse annacquino la diagnosi di conflitto.

Infine, si può introdurre un rapporto di pressione antagonista:

$$
\sigma_C^- = \frac{\mathcal{T}_{C}^{-}}{M(\Psi_C) + \mathcal{T}_{C}^{-}},
$$

definito quando il denominatore è positivo. Questo rapporto misura la quota relativa di energia dinamica spesa in soppressione rispetto alla totalità positiva-negativa dell’episodio. Valori bassi indicano un episodio pacifico; valori alti indicano un episodio dominato da forte frizione interna.

### Soppressione e silenzio semantico {#sec:6-8}

Il concetto di silenzio per soppressione è uno dei punti chiave della formulazione estesa.

Un’unità può non comparire nel Campo osservabile per almeno tre ragioni:

1. non è stata raggiunta dalla perturbazione contestuale;
2. è stata raggiunta, ma la sua attivazione è rimasta sotto soglia;
3. è stata attivamente spinta sotto zero da una dinamica antagonista.

Solo il terzo caso costituisce soppressione in senso forte. Il campo osservabile, da solo, non consente di distinguerlo dagli altri due. Il Potenziale interno, invece, conserva questa informazione.

Questa distinzione protegge la teoria da una lettura ingenuamente positivista del campo. Ciò che appare non è tutto ciò che è accaduto. Un evento semantico può essere definito tanto dai nodi che emergono quanto dai nodi che vengono esclusi. In molti casi, il significato di una risposta dipende proprio dall’alternativa che essa ha dovuto sopprimere.

Il silenzio semantico non è quindi sempre assenza. Talvolta è traccia negativa di un conflitto.

### Conflitto, frustrazione e tensione di taglio {#sec:6-9}

La Tensione Negativa Globale misura la quantità complessiva di soppressione, ma non basta da sola a stabilire se il mezzo debba trasformarsi. Una tensione negativa elevata può essere episodica e non richiedere alcun aggiornamento persistente. Diventa teoricamente rilevante quando si ripete, si concentra o si associa a configurazioni topologiche specifiche.

Una forma particolarmente importante è la tensione di taglio. Essa si verifica quando un nucleo positivo attivo e una regione negativa soppressa risultano topologicamente vicini nel mezzo, ma dinamicamente incompatibili. In questo caso, il sistema non sta semplicemente ignorando una regione distante: sta separando con forza regioni semanticamente contigue.

In termini qualitativi, la tensione di taglio segnala una frattura tra prossimità strutturale e incompatibilità dinamica. Il mezzo dice che due regioni sono vicine; il Potenziale dice che non possono emergere insieme.

Una possibile forma osservativa della tensione di taglio può essere costruita pesando la contiguità tra Supporto Attivo e Nucleo Soppresso:

$$
\mathcal{K}_C^- = \sum_{i \in \mathcal{A}_C^*} \sum_{j \in \mathcal{S}_C^*} m_{ij} \; \widetilde{\Sigma}_C(i) \; \widetilde{\Omega}_C^-(j).
$$

Questa quantità può essere interpretata come un **taglio di grafo pesato probabilistico**. Misura quanto il nucleo positivo dell’evento sia topologicamente adiacente alla regione soppressa. Valori elevati indicano che il conflitto non è periferico, ma attraversa una zona strutturalmente densa del mezzo.

Dalla misura regionale è possibile, e necessario ai fini ontogenetici, derivare la Tensione di Taglio Locale per una singola unità $t$. Essa quantifica lo strappo dinamico a cui il nodo è sottoposto, calcolando il prodotto delle sollecitazioni opposte che riceve dal proprio vicinato:

$$
\kappa_C^-(t) =
\left(
\sum_{i \in \mathcal{A}_C^*} m_{ti} \, \widetilde{\Sigma}_C(i)
\right)
\times
\left(
\sum_{j \in \mathcal{S}_C^*} m_{tj} \, \widetilde{\Omega}_C^-(j)
\right).
$$

Un nodo presenta un valore elevato di $\kappa_C^-(t)$ solo se risulta strutturalmente contiguo sia all’epicentro dell’attivazione sia all’epicentro della soppressione. Questa grandezza individua matematicamente i nodi cerniera incastrati nella frattura semantica.

Una Tensione di Taglio Locale persistente su una specifica unità fornisce il segnale diagnostico più diretto per innescare la Mitosi Semantica. Se una stessa unità produce ripetutamente campi positivi incompatibili e soppressioni adiacenti, il problema potrebbe non essere più risolvibile modificando i pesi. Potrebbe essere necessario distinguere ciò che il mezzo continua impropriamente a trattare come unitario.

### Continuità con la teoria dell’osservazione {#sec:6-10}

La formulazione estesa non sostituisce la teoria dell’osservazione del campo. La conserva e la amplia.

Tutti gli operatori distribuzionali introdotti nella \cref{sec:5} restano validi, ma il loro dominio corretto è il Campo osservabile $\Psi_C$, non il Potenziale interno $V_C$. Massa, firma, entropia, Supporto Effettivo, soglia endogena e Firma Ristretta richiedono infatti una distribuzione non negativa.

Il Potenziale interno fornisce invece una seconda classe di osservabili: soppressione locale, firma negativa globale, Supporto Negativo Canonico, firma negativa ristretta, Tensione Negativa Globale, pressione antagonista e tensione di taglio. Queste grandezze non descrivono il significato emergente, ma il costo dinamico della sua emersione.

La distinzione può essere riassunta così:

$$
\Psi_C \quad \Rightarrow \quad \text{osservatori del significato emerso},
$$

$$
V_C \quad \Rightarrow \quad \text{osservatori del conflitto interno}.
$$

In questo senso, la teoria estesa non nega il primato del campo. Lo rafforza, mostrando che il campo osservabile è il livello fenomenologico di una dinamica più ricca.

### Ponte verso la trasformazione parametrica {#sec:6-11}

Il ruolo principale degli osservatori di conflitto è preparare la trasformazione del mezzo. Essi non decidono automaticamente l’aggiornamento, ma forniscono evidenza diagnostica.

Una Tensione Negativa Globale moderata può essere ignorata o riassorbita. Una soppressione locale episodica può non avere alcun valore strutturale. Ma una tensione negativa ricorrente, concentrata sugli stessi bacini o associata alla stessa frontiera topologica, indica che il mezzo incontra ripetutamente lo stesso attrito.

Nel regime parametrico, questa informazione alimenta gli accumulatori duali. Le co-attivazioni coerenti contribuiscono all’evidenza sinergica $c_{ij}^+$; le esclusioni ricorrenti, le soppressioni e le incompatibilità contribuiscono all’evidenza antagonista $c_{ij}^-$. Il sistema impara quindi non solo quali unità tendano a cooperare, ma anche quali tendano a escludersi.

Quando l’adattamento parametrico riesce, il mezzo assorbe la tensione modificando intensità e polarità dei legami. Quando fallisce, la tensione cronica diventa indizio di insufficienza ontologica: la granularità del mezzo non è più adeguata a spiegare la storia dei campi. È in questo punto che la trasformazione parametrica prepara l’ontogenesi semantica.

### Sintesi {#sec:6-12}

La formulazione estesa introduce un secondo livello sotto il Campo Semantico osservabile. Il Potenziale interno $V_C$ rende trattabili sinergia, antagonismo, soppressione e conflitto. Il Campo osservabile $\Psi_C$ resta invece la configurazione non negativa del significato emerso.

Questa scissione evita sia la riduzione del significato a pura attivazione positiva, sia l’idea problematica di un significato negativo. La negatività appartiene al motore dinamico, non al campo fenomenologico. Essa misura ciò che è stato impedito, non ciò che è semanticamente presente.

La teoria estesa conserva quindi la teoria base come caso osservabile e la integra con una teoria del conflitto interno. Il risultato è un modello capace di distinguere presenza, assenza, soppressione e frustrazione; e capace di trasformare tali diagnosi in evidenza per l’adattamento parametrico e, nei casi limite, per l’ontogenesi del mezzo.


## Trasformazione Strutturale Parametrica {#sec:7}

La teoria dello Spazio Semantico Continuo distingue due livelli di trasformazione del mezzo. Il primo è parametrico: il modello modifica intensità, polarità e affidabilità delle relazioni tra unità già esistenti. Il secondo è ontogenetico: il modello altera la propria granularità interna, generando, fondendo, differenziando o dissolvendo unità semantiche.

Questa distinzione è essenziale. Un modello semantico non deve creare nuovi nodi ogni volta che incontra una tensione, una novità o una configurazione ricorrente. Prima di modificare la propria ontologia $\mathcal{V}$, il modello deve tentare una forma più economica di adattamento: aggiornare la struttura relazionale a vocabolario costante. La Trasformazione Strutturale Parametrica è precisamente questo regime ordinario di apprendimento.

In termini generali, data la struttura estesa del mezzo $\mathcal{G}^+$, la trasformazione parametrica conserva $\mathcal{V}$ e agisce su $E_{\mathrm{sem}}$, aggiornando la magnitudo strutturale $\mathbf{M}$ e la polarità dinamica $\mathbf{W}$ dei legami stabili. Il modello non cambia ancora il proprio alfabeto interno; cambia il modo in cui le unità esistenti si sostengono, si escludono, si avvicinano o si respingono nel grafo semantico $\mathcal{G}_{\mathrm{sem}}$.

### Funzione teorica del regime parametrico {#sec:7-1}

La trasformazione parametrica svolge una funzione di mediazione tra evento e ontologia. Da un lato riceve evidenza dall'ipergrafo episodico $\mathcal{G}_{\mathrm{epis}}$; dall’altro protegge il modello da una crescita incontrollata del vocabolario interno $\mathcal{V}_{\mathrm{lat}}$.

Senza un regime parametrico intermedio, ogni configurazione ricorrente rischierebbe di essere promossa immediatamente a nuova unità latente. Il risultato sarebbe un’esplosione ontologica: il modello produrrebbe nodi per ogni variazione contestuale, saturando la propria memoria e perdendo capacità discriminativa.

Allo stesso modo, senza trasformazione parametrica il modello resterebbe troppo rigido. Le unità esistenti non potrebbero adattare progressivamente i propri legami alla storia dei campi osservati. Il regime parametrico evita entrambi i rischi. Esso costituisce il primo tentativo del modello di assorbire l’esperienza: rafforzare relazioni ricorrenti, indebolire relazioni non confermate, registrare antagonismi persistenti, preservare conflitti cronici come informazione diagnostica e cancellare rumore episodico.

### Dal Campo osservato all’evidenza trasformativa {#sec:7-2}

La trasformazione parametrica non utilizza il Campo Semantico grezzo. Essa riceve in ingresso gli oggetti filtrati dagli osservatori distribuzionali e di conflitto:

- il Supporto Attivo $\mathcal{A}_C^*$;
- la Firma Ristretta $\widetilde{\Sigma}_C$;
- il Supporto Negativo Canonico $\mathcal{S}_C^*$;
- la firma negativa ristretta $\widetilde{\Omega}_C^-$;
- la Tensione Negativa Globale $\mathcal{T}_{C}^{-}$;
- la tensione di taglio regionale $\mathcal{K}_C^-$;
- la tensione di taglio locale $\kappa_C^-(t)$.

Questi oggetti impediscono che l’intero campo venga convertito in memoria. Il modello non apprende dalla coda dissipativa, ma dal nucleo informativo dell’evento e dalle soppressioni strutturalmente rilevanti. In questa prospettiva, l’apprendimento parametrico non è un aggiornamento cieco dei pesi. È una forma di digestione semantica: il campo viene osservato, tagliato, normalizzato, confrontato e solo infine convertito in evidenza relazionale.

### Nucleo Trasformativo e selezione dei Pivot {#sec:7-3}

Il Supporto Attivo identifica il Segnale, ma non tutto il Segnale deve diventare evidenza strutturale. La teoria introduce quindi un sottoinsieme del Supporto Attivo, il Nucleo Trasformativo, indicato con:

$$
\mathcal{P}_C \subseteq \mathcal{A}_C^*.
$$

Gli elementi di $\mathcal{P}_C$ sono i **Pivot** dell’evento. Essi non sono semplicemente i nodi più attivati, ma le unità che il modello considera sufficientemente informative per contribuire alla trasformazione.

La selezione dei Pivot può dipendere da diversi criteri: intensità nella Firma Ristretta, centralità topologica nel sottografo indotto da $\mathcal{A}_C^*$, ricorrenza storica in eventi simili, partecipazione a tensioni di taglio o novità. In forma astratta, la selezione è un operatore endogeno:

$$
\mathcal{P}_C = \Pi(\mathcal{A}_C^*, \widetilde{\Sigma}_C, \mathcal{G}_{\mathrm{sem}}, \mathcal{G}_{\mathrm{epis}}).
$$

### Il Fattore Episodico $\chi_C$ e la Delimitazione dell'Evento {#sec:7-4}

Per trasformare un evento in evidenza senza convertirlo immediatamente in ontologia (evitando la proliferazione incontrollata di nodi latenti $\zeta$), la teoria reifica l'evento introducendo il **Fattore Episodico**, indicato con $\chi_C \in \mathcal{X}$.

La funzione di $\chi_C$ è duplice. In primo luogo, svolge una **funzione computazionale anti-esplosione**: evita che ogni evento multi-pivot generi immediatamente una cricca completa e densa di archi nel grafo semantico $\mathcal{G}_{\mathrm{sem}}$. Invece di materializzare $\mathcal{O}(k^2)$ relazioni a coppie tra i Pivot, il modello fattorizza topologicamente l'evento con una struttura a stella, collegando $\chi_C$ ai Pivot tramite archi di incidenza in $E_{\mathrm{inc}}$:

$$
P_1, P_2, \dots, P_k \xrightarrow{E_{\mathrm{inc}}} \chi_C
$$

L'intensità dell'arco di incidenza tra un Pivot $i$ e il fattore episodico $\chi_C$ è data dalla sua partecipazione al nucleo dell'evento:

$$
a_C(i) = \widetilde{\Sigma}_C(i).
$$

In secondo luogo, $\chi_C$ svolge una **funzione epistemica e probatoria**: impedisce che un singolo episodio venga ontologizzato. Trattiene l'evento nell'ipergrafo episodico $\mathcal{G}_{\mathrm{epis}}$, rappresentandone la co-appartenenza contestuale come fatto storico, senza ancora cristallizzarlo in un concetto astratto in $\mathcal{V}_{\mathrm{lat}}$.

L’azione di $\chi_C$ definisce l'**Episodio Semantico**, ovvero il ciclo locale in cui una sorgente contestuale genera un campo, seleziona i Pivot e forma il fattore episodico:

$$
\mathcal{E}_C = (C, S_C, \Psi_C, \mathcal{A}_C^*, \mathcal{P}_C, \chi_C, E_{\mathrm{inc}}).
$$

I criteri di delimitazione dell'episodio dipendono dal regime operativo:

- Nel **regime batch**, l’episodio coincide con il ciclo chiuso di elaborazione di un contesto isolato $C$. Al termine della perturbazione, l'episodio si chiude.
- Nel **regime streaming**, il contesto evolve in modo continuo ($C_1, C_2, \dots$). La delimitazione richiede una *policy di segmentazione dinamica endogena*: l'episodio corrente si chiude quando la derivata temporale della topologia del Campo Osservabile o la divergenza del Supporto Attivo segnalano un brusco spostamento attenzionale verso una nuova configurazione semantica.

Al termine dell'episodio, il fattore $\chi_C$ decade come entità attiva di calcolo per il campo corrente. Tuttavia, non viene distrutto. Affronta una biforcazione architetturale con quattro possibili destini:

1. **Decadimento completo (Garbage Collection):** se l'evento è debole, frammentato o puramente rumoroso, $\chi_C$ viene rimosso.
2. **Conservazione Episodica (buffer a capacità finita):** archiviazione in $\mathcal{G}_{\mathrm{epis}}$ come traccia di memoria a medio termine. Per scongiurare l'esplosione combinatoria e l'accumulo storico incontrollato, questo layer **opera a capacità finita**: i fattori episodici non più mobilitati, o la cui informazione relazionale è già stata interamente marginalizzata negli accumulatori $c^{+}$ e $c^{-}$ senza innescare alcuna Genesi, subiscono l'*oblio episodico* e vengono rimossi, preservando l'omeostasi computazionale. La statistica di co-occorrenza che essi avevano contribuito a depositare sopravvive in $\mathbf{M}$, $\mathbf{W}$ e negli accumulatori, sicché l'oblio del singolo episodio grezzo non cancella l'evidenza strutturale che ne è derivata.
3. **Proiezione Pairwise:** marginalizzazione dell'evidenza relazionale verso gli accumulatori per l'aggiornamento asincrono di $E_{\mathrm{sem}}$.
4. **Sedimentazione aggregativa:** il fattore contribuisce agli accumulatori duali $c^+$ e $c^-$, aumentando il peso della propria risonanza nella storia episodica. Quando episodi diversi co-mobilitano ripetutamente gli stessi Pivot, tale sedimentazione approfondisce un bacino in $\mathbf{M}$ e $\mathbf{W}$; se il bacino raggiunge la saturazione, esso può fungere da seme per la Genesi di una causa comune latente (la famiglia rilevante non è però pre-raggruppata per similarità, ma emerge a posteriori dalla fattorizzazione locale; vedi \cref{sec:7-14,sec:8-2}). Il fattore stesso non viene raggruppato né compresso: resta in $\mathcal X$ come traccia individuale.

### L'evidenza sinergica come proiezione derivata {#sec:7-5}

Nell'architettura duale, le relazioni pairwise non costituiscono la memoria primaria dell'evento, ma emergono come una **vista derivata** (proiezione marginalizzata) degli archi di incidenza $E_{\mathrm{inc}}$.

La traccia di co-occorrenza sinergica tra due Pivot $i$ e $j$ si calcola come il collasso topologico del percorso indiretto che li unisce attraverso il fattore episodico $\chi_C$:

$$
e_{ij}^{+}(C) = a_C(i) \cdot a_C(j) = \widetilde{\Sigma}_C(i) \cdot \widetilde{\Sigma}_C(j).
$$

L’evidenza sinergica non decreta ancora il rafforzamento permanente del legame semantico. Stabilisce solo l'impronta pairwise minima dell'episodio. Mantenere l'evidenza come proiezione derivata offre un vantaggio computazionale notevole: il modello può calcolare il consolidamento solo in finestre asincrone o selettive, evitando di aggiornare densamente la rete a ogni istante.

### Evidenza antagonista {#sec:7-6}

La seconda forma di evidenza parametrica è antagonista. Essa riguarda coppie di unità in cui una parte emerge nel campo osservabile mentre l’altra viene soppressa dal Potenziale interno.

Per un nodo attivo $i \in \mathcal{P}_C$ e un nodo soppresso $j \in \mathcal{S}_C^*$, la misura elementare di evidenza antagonista episodica è definita dalla collisione pura delle rispettive firme ristrette:

$$
e_{ij}^{-}(C) = \widetilde{\Sigma}_C(i) \cdot \widetilde{\Omega}_C^-(j).
$$

Questa equazione è dimensionalmente simmetrica rispetto all’evidenza sinergica e garantisce che il modello possa registrare un conflitto anche tra unità strutturalmente inedite (cioè quando $m_{ij}=0$). Il conflitto viene depositato senza necessitare di archi stabili pregressi, superando il paradosso di bootstrap inibitorio.

### Accumulatori duali e decadimento {#sec:7-7}

L’evidenza episodica derivata deve essere integrata nel tempo per guidare la plasticità del grafo semantico. La teoria impiega accumulatori relazionali duali, $c_{ij}^{+}$ e $c_{ij}^{-}$, che possono essere calcolati interrogando la storia episodica conservata in $\mathcal{X}$. In forma ricorsiva locale, il loro aggiornamento è:

$$
c_{ij}^{+} \leftarrow \lambda^{+} c_{ij}^{+} + \eta^{+} e_{ij}^{+}(C),
$$

$$
c_{ij}^{-} \leftarrow \lambda^{-} c_{ij}^{-} + \eta^{-} e_{ij}^{-}(C),
$$

dove $\lambda^{+},\lambda^{-} \in [0,1]$ sono fattori di decadimento (oblio temporale) e $\eta^{+},\eta^{-}$ sono coefficienti di apprendimento.

Questi accumulatori conservano due storie distinte: quanto spesso due unità cooperano positivamente nello stesso fattore episodico, e quanto spesso entrano in collisione. Questa separazione è essenziale per diagnosticare relazioni ambigue e tensioni strutturali, impedendo che cooperazione e conflitto si annullino algebricamente in un unico valore scalare.

### Coinvolgimento strutturale e aggiornamento di $\mathbf{M}$ {#sec:7-8}

La matrice $\mathbf{M} \in E_{\mathrm{sem}}$ non registra la polarità dell’interazione, ma il coinvolgimento strutturale puro tra unità. Essa deve quindi essere aggiornata non solo dalla cooperazione, ma anche dal conflitto.

L'evidenza di coinvolgimento totale dell'episodio corrente è:

$$
e_{ij}^{M}(C) = e_{ij}^{+}(C) + \tfrac{1}{2}\big( e_{ij}^{-}(C) + e_{ji}^{-}(C) \big).
$$

L’aggiornamento di magnitudo è governato da:

$$
m_{ij} \leftarrow \lambda^{M} m_{ij} + \eta^{M} e_{ij}^{M}(C).
$$

In questo modo, $\mathbf{M}$ cresce quando due unità risultano ripetutamente coinvolte nello stesso canale attenzionale, sia esso cooperativo o conflittuale. Due nodi in attrito cronico tenderanno ad avere alta magnitudo e polarità instabile o negativa, fornendo la metrica necessaria per diagnosticare la tensione di taglio.

### PMI dinamica e cristallizzazione asimmetrica {#sec:7-9}

Il consolidamento permanente nei pesi stabili $\mathbf{W}$ avviene trasformando gli accumulatori in probabilità storiche dinamiche. Normalizzando l'evidenza accumulata rispetto all'energia totale transitata ($Z^+$ e $Z^-$), si estraggono le distribuzioni $p^{+}(i,j)$ e $p^{-}(i,j)$:

$$
Z^{+} = \sum_{a,b} c_{ab}^{+}, \quad Z^{-} = \sum_{a,b} c_{ab}^{-},
$$

$$
p^{+}(i,j) = \frac{c_{ij}^{+}}{Z^{+}}, \quad p^{-}(i,j) = \frac{c_{ij}^{-}}{Z^{-}}.
$$

Si valuta la sorpresa relazionale tramite la Pointwise Mutual Information (PMI) dinamica:

$$
\operatorname{PMI}_{ij}^{+} = \log \frac{p^{+}(i,j)}{p^{+}(i)p^{+}(j)}.
$$

Per l’evidenza antagonista, l’asimmetria direzionale è concettualmente rilevante (la sorpresa che $i$ sia attivo mentre $j$ sia soppresso):

$$
\operatorname{PMI}_{i \to j}^{-} = \log \frac{p^{-}(i,j)}{p^{+}(i)p^{-}(j)}.
$$

Quando $\mathbf{W}$ è mantenuta simmetrica, la sorpresa si compone globalmente come $\operatorname{PMI}_{ij}^{-} = \operatorname{PMI}_{i \to j}^{-} + \operatorname{PMI}_{j \to i}^{-}$.

La simmetrizzazione dell'evidenza antagonista è necessaria perché $\mathbf{M}$ registra la *larghezza di banda* topologica del conflitto, indipendente dalla direzione: l'evidenza $e_{ij}^{-}$ è direzionale, ma $\mathbf{M}$ deve restare geometria simmetrica. Si fissa così la convenzione complessiva: $\mathbf{M}$ è spazio strutturale sempre simmetrico, mentre $\mathbf{W}$ è interazione firmata, simmetrica nel caso canonico (con la direzionalità del flusso che emerge via $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$) o direzionale in implementazioni che adottano la prova di stabilità in norma 1. La cristallizzazione in $E_{\mathrm{sem}}$ è asimmetrica. Stabilire una mutua esclusione permanente riduce la fluidità del mezzo in modo drastico; pertanto, il modello richiede un carico probatorio inibitorio più esigente: $\theta^{-}_{\mathrm{cryst}} > \theta^{+}_{\mathrm{cryst}}$.

### Aggiornamento della matrice firmata $\mathbf{W}$ {#sec:7-10}

La matrice $\mathbf{W}$ registra il bilancio polarizzato dell’interazione. Applicando una funzione di gating asimmetrica ricavata dalle PMI:

$$
\Delta w_{ij} = \eta^{+} \max(0, \operatorname{PMI}_{ij}^{+} - \theta^{+}_{\mathrm{cryst}}) - \eta^{-} \max(0, \operatorname{PMI}_{ij}^{-} - \theta^{-}_{\mathrm{cryst}}).
$$

L'aggiornamento strutturale include un decadimento fisiologico simmetrico a quello di $\mathbf{M}$ (\cref{sec:7-8}):

$$
w_{ij} \leftarrow \lambda^W w_{ij} + \Delta w_{ij}, \qquad \lambda^W \in (0,1],
$$

con $\lambda^W$ eventualmente coincidente con $\lambda^M$. Senza questo decadimento, $\mathbf{M}$ svanirebbe nel tempo mentre $\mathbf{W}$ resterebbe puramente incrementale: i conflitti deboli --- quelli il cui modulo non tocca mai il tetto $m_{ij}$, e che l'oblio di 7.11 pota solo a livello degli accumulatori $c^{\pm}$, non di $\mathbf{W}$ --- diverrebbero immortali. Con $\lambda^W$, le tensioni negative non riconfermate dalla storia sfumano dolcemente, e la topologia permanente di $\mathcal{G}_{\mathrm{sem}}$ evolve assorbendo solo le tendenze storicamente confermate e depurate dal rumore transitorio.

Poiché $\mathbf{M}$ e $\mathbf{W}$ sono aggiornate da accumulatori distinti (7.8 per la prima, il gating PMI per la seconda), nulla nelle regole precedenti garantisce che dopo un passo valga ancora l'invariante di compatibilità strutturale $|w_{ij}| \leq m_{ij}$. Tale invariante non è opzionale: la prova di contrazione dell'operatore canonico $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$ nella \cref{sec:9} vi poggia direttamente (è ciò che assicura $\lVert \mathbf{J} \rVert \leq 1$). Al termine di ogni consolidamento parametrico si applica dunque una proiezione esplicita sulla regione ammissibile:

$$
w_{ij} \leftarrow \operatorname{clip}\!\left(w_{ij},\, -m_{ij},\, +m_{ij}\right).
$$

Questa proiezione non è una scelta di policy ma il meccanismo con cui la teoria preserva la propria invariante strutturale: la polarità di un canale non può mai eccedere in modulo il coinvolgimento strutturale che la sostiene. Essa è coerente con la rettificazione $\max(0, \cdot)$ imposta su $\mathbf{M}$ al commit di una causa latente (8.2.6), di cui costituisce il complemento sul lato firmato.

Un'eccezione vale per le cause latenti aggregative già committate. Il loro accoppiamento al proprio nucleo generativo non appartiene alla sedimentazione pairwise, ma ai caricamenti non-lineari $(R_{\zeta}^+, R_{\zeta}^-)$; il blocco $\zeta \times \mathcal{K}_{\zeta}$ e perciò **mascherato** negli aggiornamenti ordinari,

$$
\Delta m_{\zeta t} = 0, \qquad \Delta w_{\zeta t} = 0, \qquad t \in \mathcal{K}_{\zeta},
$$

salvo processi ontogenetici esplicitamente dichiarati. Senza questa maschera, la plasticità ordinaria riaccumulerebbe nel tempo archi lineari verso il nucleo, ricostruendo proprio la macro lineare esclusa in 8.2.2 (poiché $\zeta$ co-occorre sistematicamente col proprio nucleo).

### Oblio fisiologico {#sec:7-11}

Per preservare la plasticità ed evitare l'irrigidimento topologico, l’oblio fisiologico agisce come potatura (pruning). Gli accumulatori o i legami stabili di magnitudo debole che non vengono confermati dall'attraversamento di nuovi fattori episodici decadono progressivamente verso lo zero:

$$
c_{ij}^{+} < \theta^{+}_{\mathrm{prune}} \quad \Rightarrow \quad c_{ij}^{+} \to 0,
$$

$$
c_{ij}^{-} < \theta^{-}_{\mathrm{prune}} \quad \Rightarrow \quad c_{ij}^{-} \to 0.
$$

L’oblio non è un'amnesia sistemica, ma l'omeostasi necessaria per distinguere la traccia strutturale rilevante dall'obsolescenza informativa, garantendo la sparsità essenziale di $E_{\mathrm{sem}}$.

### Saturazione, oscillazione e frustrazione parametrica {#sec:7-12}

Il regime parametrico ha limiti intrinseci. Quando non riesce ad assorbire la storia dei campi a dimensionalità $\mathcal{V}$ costante, produce specifiche patologie diagnostiche:

- **Saturazione:** un legame o una regione raggiunge asintoti di aggiornamento ma le tensioni di campo osservate non decrescono.
- **Oscillazione:** una relazione fluttua cronicamente tra cooperazione e inibizione.
- **Frustrazione parametrica:** l'accumulo simultaneo genera un coinvolgimento strutturale intenso ($m_{ij} \gg 0$), ma l'algebra del commit sottrae le forze opponenti costringendo il peso firmato all'equilibrio statico ($\Delta w_{ij} \approx 0$). La geometria avvince i nodi, ma la dinamica non riesce ad assegnare un bilancio netto.

### Criteri di fallimento del regime parametrico {#sec:7-13}

Tensioni di taglio persistenti ($\kappa_C^- \gg 0$), divergenze crescenti tra Firme Ristrette associate alla stessa unità, e frustrazioni parametriche croniche indicano che la risoluzione del conflitto non è raggiungibile aggiornando $\mathbf{M}$ e $\mathbf{W}$. Il modello ottiene così una giustificazione endogena per certificare il collasso della dimensionalità corrente, autorizzando la transizione all'Ontogenesi.

### Innesco dell'ontogenesi: saturazione strutturale, non similarità episodica {#sec:7-14}

Prima di innescare la Genesi di una nuova Unità Latente ($\zeta$), occorre stabilire quale condizione del mezzo licenzia l'ingresso nel regime ontogenetico. Una formulazione ingenua la cercherebbe in una similarità morfologica fra episodi; mostriamo qui perché la condizione corretta è invece strutturale e spaziale, e perché ciò evita sia gli iperparametri di clustering sia il costoso confronto episodio-episodio.

La condizione che apre il regime probatorio dell'ontogenesi non è una similarità morfologica calcolata fra episodi storici, ma la **saturazione strutturale dello spazio** sedimentato in $\mathbf{M}$ e $\mathbf{W}$. Il regime parametrico ordinario (\cref{sec:7}) assorbe la ricorrenza finché la dimensionalità corrente è sufficiente; quando una regione del mezzo accumula magnitudo oltre la propria capacità di assorbimento --- saturazione in $\mathbf{M}$, frustrazione e tensione di taglio croniche in $\mathbf{W}$ (cfr. 7.12) --- quella regione diventa il **seme** del possibile commit di una causa comune latente (non di una condensazione fisica degli episodi: questi non collassano in alcun oggetto comune).

È essenziale sottolineare la direzione causale, perché distingue questa teoria dal paradigma distribuzionale classico. La famiglia di episodi che concorre alla nascita di $\zeta$ **non viene pre-raggruppata** confrontando ogni nuovo evento con tutta la storia $\mathcal{X}$ (operazione che reintrodurrebbe il costoso confronto episodio-episodio e contraddirebbe il principio di nascita per sedimentazione). La regione satura individua soltanto *dove guardare*; *quali* episodi appartengano effettivamente alla famiglia è un esito a posteriori, determinato dalla fattorizzazione locale e dal doppio taglio autoconsistente descritti in 8.2. In altri termini, il "pool di richiamo" degli episodi incidenti sulla regione satura --- quelli che condividono archi d'incidenza in $E_{\mathrm{inc}}$ con i Pivot saturi --- fornisce unicamente lo *scope di località* entro cui la causa latente verrà cercata, non una premessa di appartenenza.

Questa impostazione mantiene coerenza piena con 8.2.5, dove la famiglia storica rilevante $\mathcal{H}_{\zeta}$ emerge come risultato della risonanza e non come premessa, e con 8.1, che elenca proprio la saturazione di $\mathbf{M}$ e la frustrazione di $\mathbf{W}$ fra i criteri diagnostici di ingresso nel regime ontogenetico. La densità e la stabilità della regione satura costituiscono dunque la condizione necessaria, ma non sufficiente, per il commit probatorio di una nuova causa comune latente $\zeta$. La scelta lessicale è deliberata: nessuna struttura topologica comune in cui gli episodi si fondono, ma una causa latente che viene ammessa nel lessico al superamento del doppio test dinamico di 8.2.7.

### Ponte verso l'ontogenesi {#sec:7-15}

La Trasformazione Strutturale Parametrica costituisce il confine dell'adattamento a dimensionalità costante. Quando le tensioni relazionali non sono più assorbibili in $E_{\mathrm{sem}}$, o quando la sedimentazione progressiva in $\mathbf M$ e $\mathbf W$ rivela pattern di partecipazione ricorrenti sufficientemente stabili da giustificare una causa comune latente, il modello supera il regime ordinario. La sezione successiva descriverà l'Ontogenesi Semantica, il meccanismo attraverso cui la ricorrenza storica dei fattori episodici in $\mathcal X$ — senza comprimerli né raggrupparli — motiva la nascita di nuove unità latenti stabili all'interno di $\mathcal V_{\mathrm{lat}}$.


## Ontogenesi Semantica del Mezzo {#sec:8}

La Trasformazione Strutturale Parametrica modifica il modello a dimensionalità costante. Essa aggiorna le relazioni stabili in $E_{\mathrm{sem}}$, ma conserva inalterata l’estensione del vocabolario interno $\mathcal{V}$. L’Ontogenesi Semantica inizia quando questo principio di conservazione topologica non è più sufficiente a garantire stabilità, economia rappresentazionale e capacità interpretativa del modello. In tale regime, il mezzo non si limita ad aggiornare i pesi tra unità già date: modifica le unità stesse.

L’Ontogenesi Semantica è il regime in cui il modello altera la propria granularità interna. In termini formali, l’operatore ontogenetico mappa il vocabolario corrente in un nuovo spazio di dimensionalità differente:

$$
\mathcal{V} \longrightarrow \mathcal{V}'.
$$

Questo salto dimensionale è un’operazione computazionalmente ed epistemologicamente costosa. Non deve registrare una semplice fluttuazione statistica, ma modificare in modo persistente lo spazio topologico delle osservazioni future. Grazie all'Architettura Duale introdotta nella \cref{sec:4}, l'ontogenesi non avviene "alla cieca" sulle singole co-occorrenze, ma si configura come una risposta alla **deformazione progressiva del mezzo** operata dai fattori episodici in $\mathcal{G}_{\mathrm{epis}}$: la ricorrenza sedimenta bacini in $\mathbf{M}$ e $\mathbf{W}$, e l’ontogenesi interviene quando tali bacini possono essere assunti da cause comuni latenti dotate di comportamento non-lineare.

L’architettura si articola lungo quattro direttrici fondamentali:

1. **Genesi**: addizione di nuove unità latenti ($\zeta \in \mathcal{V}_{\mathrm{lat}}$) per aggregazione di fattori episodici in $\mathcal{X}$, o assimilazione di lacune d’interfaccia nell'osservabile $\mathcal{V}_{\mathrm{lex}}$.
2. **Mitosi**: divisione di un’unità sovraccarica in unità figlie distinte, guidata da fratture nei suoi archi di incidenza episodica.
3. **Coalescenza**: fusione endogena di unità divenute topologicamente e storicamente ridondanti.
4. **Apoptosi**: archiviazione o dissoluzione endogena di unità cronicamente inerti.

### Transizione di fase e periodo probatorio {#sec:8-1}

Il passaggio all’ontogenesi non è innescato dalla semplice novità di un contesto, ma dal fallimento diagnostico del regime parametrico (tensione di taglio, frustrazione in $\mathbf{W}$, saturazione in $\mathbf{M}$) e dall'accumulo di evidenza coerente nell'ipergrafo episodico $\mathcal{G}_{\mathrm{epis}}$.

Per evitare un’esplosione ontologica incontrollata, le trasformazioni subiscono un periodo probatorio; a questo si sovrappone la ricottura sistemica di 8.9, che ne raffredda endogenamente le soglie finché la struttura locale è ancora volatile. Le posizioni candidate si formano inizialmente come costrutti valutati a partire dai fattori episodici in $\mathcal{X}$, senza inquinare subito $\mathcal{V}$. Esse assumono due forme:

- l’**Unità Latente Candidata** $\zeta \notin \mathcal{V}$, originata quando la sedimentazione progressiva in $\mathbf{M}$ e $\mathbf{W}$ rivela una regolarità di campo ricorrente che può essere assunta da una causa comune latente non-lineare (si veda la \cref{sec:8-2});
- il **Nodo Ombra** $\vartheta_u \notin \mathcal{V}$, che funge da segnaposto per un elemento esterno ignoto ma ricorrente ($u \in \mathcal{U}$).

Una trasformazione candidata $\mathcal{O}$ viene promossa a modifica definitiva del grafo semantico stabile solo se soddisfa tre criteri valutati sul lungo periodo:
$$
\Delta \mathcal{L}_{\mathcal{O}} > 0 \quad \text{(guadagno descrittivo)},
$$
$$
\Delta \mathcal{T}^{-}_{\mathcal{O}} < 0 \quad \text{(rilassamento del conflitto)},
$$
$$
\Delta \mathcal{C}_{\mathcal{O}} > 0 \quad \text{(miglioramento di coerenza)}.
$$

### Genesi per aggregazione: causa comune latente non-lineare {#sec:8-2}

La Genesi per Aggregazione è il processo mediante cui una regolarità ricorrente nel mezzo viene stabilizzata come nuova causa comune latente $\zeta \in \mathcal{V}_{\mathrm{lat}}$. Il punto di partenza è una distinzione che la versione lineare della teoria lasciava implicita: un centroide del bacino fa la media di ciò che è già accaduto; una causa latente spiega perché certi nodi tendono ad apparire insieme e può ricostruire il pattern anche quando ne è presente solo una parte. Questa distinzione decide il meccanismo, i criteri di commit e la forma delle relazioni ereditate.

#### Doppia sedimentazione: bacino positivo e bacino di conflitto {#sec:8-2-1}

Ogni fattore episodico $\chi_i \in \mathcal{X}$ deposita contributi strutturali sul mezzo attraverso due canali separati.

Sul lato della co-mobilitazione, ciascun episodio rinforza la magnitudo strutturale tra i propri pivot:

$$
\Delta m_{uv}^{(i)} = \beta_i\, a_i(u)\, a_i(v), \qquad u,v \in \mathcal{P}_{C_i}, \quad u \neq v,
$$

dove $a_i(t) = \widetilde{\Sigma}_{C_i}(t)$ è la firma ristretta dell'episodio --- intesa come vettore sull'intero vocabolario $\mathcal{V}$, esteso con zeri fuori dai pivot $\mathcal{P}_{C_i}$, cosicché prodotti interni e norme tra episodi a supporto diverso siano ben definiti (cfr. 8.2.5 e 9.1) --- e $\beta_i$ è la sua affidabilità trasformativa, calcolata endogenamente e non assunta come oracolo esterno. Un'istanza canonica la deriva dal rapporto segnale-rumore fenomenologico dell'episodio: lo score grezzo $\widetilde{\beta}_i = M^*(\Psi_{C_i}) / N_{\mathrm{eff}}(\widetilde{\Sigma}_{C_i})$ coincide esattamente con la soglia di autoconsistenza $\varepsilon^{*}(\widetilde{\Sigma}_{C_i})$ valutata sulla firma ristretta dell'episodio **— intesa come massa per nodo efficace —,** alta per eventi concentrati e robusti, bassa per eventi dispersi o rumorosi. Poiché $\widetilde{\beta}_i$ scala con la magnitudo assoluta delle energie di campo, lo si normalizza in $(0,1)$ in modo invariante alla scala, ancorandolo a una media mobile fisiologica:

$$
\beta_i = \frac{\widetilde{\beta}_i}{\langle \widetilde{\beta} \rangle_{\mathrm{recent}} + \widetilde{\beta}_i}.
$$

Così $\beta_i \approx 0.5$ per un episodio tipico, tende a $1$ per eventi eccezionalmente a fuoco e a $0$ per eventi rumorosi, indipendentemente dall'ordine di grandezza assoluto delle energie del sistema (una saturazione fissa $\widetilde{\beta}_i/(1+\widetilde{\beta}_i)$ collasserebbe invece a $1$ ad alte energie, annullando il potere discriminante). Implementazioni alternative sono ammesse purché $\beta_i$ resti monotona crescente nella focalizzazione e nell'energia netta del segnale. La condizione $u \neq v$ riflette che $\mathbf{M}$ codifica relazioni fra unità distinte: gli auto-pesi sono nulli per costruzione, $m_{ii} = 0$. Se più episodi condividono un sottoinsieme di pivot, la loro magnitudo riceve rinforzo ripetuto: si forma un **bacino positivo** in $\mathbf{M}$.

Sul lato del conflitto, quando la presenza di certi pivot è sistematicamente accompagnata dalla soppressione di altri nodi, questo si accumula in $\mathbf{W}$ tramite il gating sulle PMI negative (\cref{sec:7-9}). Si forma così un **bacino di conflitto** in $\mathbf{W}$: una regione in cui la ricorrenza non avvicina i nodi, ma li rende strutturalmente incompatibili. Accanto al nucleo eccitatorio $\mathcal{K}_{\zeta}$ esiste quindi un insieme antagonista $\mathcal{A}_{\zeta}$ verso cui il bacino di conflitto si orienta (entrambi definiti formalmente in 8.2.5).

#### Perché il bacino non basta: il problema del centroide {#sec:8-2-2}

Un bacino positivo stabile potrebbe sembrare sufficiente per giustificare la nascita di $\zeta$ come "mentalizzazione" della regione. Questa intuizione è però parziale. Se $\zeta$ fosse inizializzata come combinazione lineare delle connessioni dei nodi del nucleo (il caricamento $R_{\zeta}^+$, anch'esso definito in 8.2.5, indica qui il peso dei nodi del nucleo):

$$
m_{\zeta r} = \sum_{t \in \mathcal{V}} R_{\zeta}^+(t)\, m_{tr},
$$

l'anello bidirezionale $\mathcal{K}_{\zeta} \to \zeta \to \mathcal{K}_{\zeta}$ che $\zeta$ introduce sarebbe algebricamente equivalente all'aggiunta di un termine di rango 1 alla matrice pairwise:

$$
\Delta x = \gamma\,(R_{\zeta}^+ R_{\zeta}^{+\top})\, x.
$$

In tal caso $\zeta$ è riassorbibile in $\mathbf{M}$: non introduce alcun grado di libertà nuovo, ma solo un'etichetta per la media esistente. Il criterio decisivo è:

> un anello lineare è riassorbibile come termine di rango 1 in $\mathbf{M}$; un anello non-lineare a soglia no.

#### $\zeta$ come causa comune latente non-lineare {#sec:8-2-3}

La formulazione corretta è quella di una **variabile latente con attivazione non-lineare a soglia**. Concettualmente, $\zeta$ non è il centroide del bacino, ma una causa comune che spiega la ricorrenza del pattern: dotata di un caricamento eccitatorio $R_{\zeta}^+$ e di uno inibitorio $R_{\zeta}^-$, essa scatta come unità quando una porzione sufficiente del proprio nucleo è attiva, e solo allora completa il resto del nucleo e sopprime gli antagonisti.

È la non-linearità, non la mera esistenza di un nodo nascosto, a costituire il grado di libertà nuovo: un nodo nascosto con accoppiamento *lineare* al nucleo collasserebbe in un termine pairwise di rango 1, perfettamente riassorbibile in $\mathbf{M}$, riducendo $\zeta$ a una macro (lo si dimostra in 8.2.2). L'attivazione a soglia, invece, produce uno scatto unitario --- il completamento di un pattern da evidenza parziale --- che nessuna riponderazione pairwise lineare può replicare.

Le due sottosezioni seguenti definiscono i caricamenti $(R_{\zeta}^+, R_{\zeta}^-)$ come prodotti della fattorizzazione e del taglio autoconsistente; l'equazione di attivazione $z_{\zeta} = \varphi(\langle R_{\zeta}^+, x\rangle - \langle R_{\zeta}^-, x\rangle - \theta_{\zeta}^{\mathrm{att}})$, con la sua soglia endogena $\theta_{\zeta}^{\mathrm{att}}$ e la sua integrazione nello scisma Potenziale/Campo, è presentata nella dinamica delle unità latenti (\cref{sec:9-1}), una volta che i caricamenti sono disponibili.

#### Fattorizzazione non-negativa locale: base e attivazione {#sec:8-2-4}

La regione satura individuata in 7.14 fornisce il seme; la causa latente si estrae fattorizzando localmente gli episodi del pool di richiamo, non costruendo a priori alcuna firma di partecipazione. Il passaggio dalla regione al pool viene formalizzato **per precludere la reintroduzione surrettizia di logiche di clustering arbitrario**. Sia $\mathcal{P}_{\mathrm{sat}} \subseteq \mathcal{V}$ la regione satura (i Pivot la cui sedimentazione in $\mathbf{M}$/$\mathbf{W}$ ha superato la capacità di assorbimento); il **pool locale** e l'insieme degli episodi che la toccano,

$$
\mathcal{X}_{\mathrm{loc}} = \{\, \chi_i \in \mathcal{X} \mid \mathcal{P}_{C_i} \cap \mathcal{P}_{\mathrm{sat}} \neq \emptyset \,\}.
$$

L'intersezione è calcolata sui *Pivot* $\mathcal{P}_{C_i}$ dell'episodio (i nodi che ne hanno superato il taglio di autoconsistenza), non sul supporto grezzo: un'attivazione spuria di ordine $10^{-6}$ su un nodo saturo non basta a includere l'episodio. La fattorizzazione si applica a $\{a_i \mid \chi_i \in \mathcal{X}_{\mathrm{loc}}\}$. Così $\mathcal{X}_{\mathrm{loc}}$ è definito dalla geometria della saturazione (non da una scelta intuitiva di famiglia), e la famiglia rilevante $\mathcal{H}_{\zeta}$ emerge solo dopo, come taglio autoconsistente sulle risonanze (8.2.5). Sia $\{a_i\}$ l'insieme dei vettori di incidenza episodica del pool locale. La causa comune si ottiene come **fattorizzazione non-negativa di rango 1**, che estrae *simultaneamente* la base spaziale e l'attivazione episodica:

$$
\min_{\rho_i \geq 0,\; \hat{R}_{\zeta}^+ \geq 0} \sum_{i} \beta_i \left\lVert a_i - \rho_i \hat{R}_{\zeta}^+ \right\rVert^2,
$$

risolta per Alternating Least Squares pesato. Per garantire la stabilità asintotica ed evitare derive di scala in floating-point, le regole di aggiornamento hanno denominatori espliciti:

$$
\rho_i = \frac{\langle a_i, \hat{R}_{\zeta}^+\rangle}{\lVert \hat{R}_{\zeta}^+ \rVert^2}, \qquad \hat{R}_{\zeta}^+(t) = \frac{\sum_i \beta_i \rho_i\, a_i(t)}{\sum_i \beta_i \rho_i^2}.
$$

La ponderazione per l'affidabilità $\beta_i$ impedisce che un episodio rumoroso devii la fattorizzazione quanto uno affidabile, in coerenza con il suo uso nella sedimentazione; la scala lasciata libera dall'ALS viene fissata a valle dalla normalizzazione del nucleo (8.2.5). Sotto vincoli di non-negatività e con pesi $\beta_i \geq 0$, nel caso strettamente di rango 1 l'errore quadratico pesato non cresce lungo l'iterazione: l'ALS converge monotonicamente a un punto stazionario dell'obiettivo *locale* (non si richiede un fattore globale in uno spazio ad alto rango, ma solo la componente principale non-negativa del bacino candidato). Ai denominatori si applica la convenzione dell'inverso generalizzato: se all'inizializzazione $\sum_i \beta_i \rho_i^2 = 0$, l'ipotesi latente è ortogonale all'evidenza, non possiede supporto empirico, e la candidatura $\zeta$ è rigettata nativamente --- non un errore numerico, ma un fallimento diagnostico. Questo risolve la circolarità delle formulazioni precedenti: il profilo spaziale $\hat{R}_{\zeta}^+$ (la loading grezza, definita sull'intero $\mathcal{V}$) e le risonanze $\rho_i$ non sono calcolati l'uno in funzione dell'altro in ordine sequenziale, ma convergono insieme come i due fattori della stessa decomposizione. La scelta della NMF, e non di una proiezione ortogonale, è obbligata: $\hat{R}_{\zeta}^+$ non è normalizzato in $L^2$ e un clip a non-negativo dopo proiezione violerebbe la coerenza della decomposizione. La località del fit è essenziale: una fattorizzazione su tutto $\mathcal{X}$ convergerebbe al fattore globalmente dominante della collezione, non alla famiglia specifica; è la regione satura a vincolare la NMF al bacino corretto. La fattorizzazione di rango 1 possiede un'ambiguità di gauge --- le trasformazioni $\rho_i \to \lambda \rho_i$, $\hat{R}_{\zeta}^+ \to \lambda^{-1}\hat{R}_{\zeta}^+$ lasciano invariato l'errore. L'estrazione del nucleo (8.2.5) è immune a tale ambiguità, poiché l'operatore $\mathcal{A}^{*}$ è per costruzione invariante alla scala. Le grandezze *estensive* che dipendono dalla scala (il fattore $c$, le masse $g_{\zeta}^{\pm}$, la soglia $\theta_{\zeta}^{\mathrm{att}}$) richiedono però di fissare il gauge: si adotta la normalizzazione $\sum_{t} R_{\zeta}^+(t) = 1$ sul nucleo, che determina univocamente $\lambda$ e con esso tutte le quantità scala-dipendenti.

#### Doppio taglio autoconsistente: nucleo $\mathcal{K}_{\zeta}$ e famiglia $\mathcal{H}_{\zeta}$ {#sec:8-2-5}

La fattorizzazione restituisce due campi non negativi --- la loading grezza $\hat{R}_{\zeta}^+$ sulla dimensione dei nodi e le risonanze $\{\rho_i\}$ sulla dimensione degli episodi. A entrambi si applica, simmetricamente, lo stesso operatore di autoconsistenza $\mathcal{A}^{*}$ della \cref{sec:8-10}.

Sulla dimensione spaziale, il taglio individua il **Nucleo Stabile** della causa latente:

$$
\mathcal{K}_{\zeta} = \mathcal{A}^{*}(\hat{R}_{\zeta}^+) = \{\, t \in \mathcal{V} \mid \hat{R}_{\zeta}^+(t) \geq \varepsilon^{*}(\hat{R}_{\zeta}^+) \,\}, \qquad \varepsilon^{*}(\hat{R}_{\zeta}^+) = \frac{\sum_t \hat{R}_{\zeta}^+(t)^2}{\sum_t \hat{R}_{\zeta}^+(t)}.
$$

Il caricamento eccitatorio definitivo è la loading rinormalizzata sul solo nucleo:

$$
R_{\zeta}^+(t) = \frac{\hat{R}_{\zeta}^+(t)}{\sum_{s \in \mathcal{K}_{\zeta}} \hat{R}_{\zeta}^+(s)} \quad \text{se } t \in \mathcal{K}_{\zeta}, \qquad 0 \text{ altrimenti}.
$$

Sulla dimensione episodica, lo stesso taglio individua la **famiglia storica rilevante**:

$$
\mathcal{H}_{\zeta} = \mathcal{A}^{*}(\rho) = \{\, \chi_i \mid \rho_i \geq \varepsilon^{*}(\rho) \,\}.
$$

$\mathcal{H}_{\zeta}$ è dunque un risultato della fattorizzazione, non una premessa di clustering: quali episodi appartengano alla famiglia è deciso dalla loro risonanza con il fattore emergente, in coerenza con quanto anticipato in 7.14. Il caricamento negativo $R_{\zeta}^-$ emerge in modo speculare dal blocco bipartito ricorrente in $\mathbf{W}$ tra il nucleo e i suoi antagonisti, con una costruzione del tutto parallela a quella positiva. Per ogni nodo candidato $j$ si misura la soppressione pesata sul nucleo, raccogliendo la sola parte negativa della polarità:

$$
\hat{R}_{\zeta}^-(j) = \sum_{i \in \mathcal{K}_{\zeta}} R_{\zeta}^+(i)\, \max\!\left(0,\, -w_{ij}\right).
$$

Una candidata ben formata richiede che nucleo e antagonisti siano disgiunti, $\mathcal{K}_{\zeta} \cap \mathcal{A}_{\zeta} = \emptyset$ (o, in forma flessibile, sovrapposizione trascurabile $\operatorname{ovlp}(\mathcal{K}_{\zeta}, \mathcal{A}_{\zeta}) < \varepsilon_{\mathrm{ovlp}}^*$). Se un nodo appartenesse a entrambi --- co-mobilitato e soppresso dalla stessa famiglia --- la candidata sarebbe internamente fratturata: in tal caso la Genesi per Aggregazione viene sospesa e il caso rinviato alla Mitosi Semantica (\cref{sec:8-4}) o a una rifattorizzazione locale, esattamente come per la frustrazione cronica. L'insieme antagonista è quindi il supporto autoconsistente di questa loading negativa grezza, e il caricamento inibitorio definitivo è la sua rinormalizzazione su tale supporto:

$$
\mathcal{A}_{\zeta} = \mathcal{A}^{*}(\hat{R}_{\zeta}^-), \qquad R_{\zeta}^-(j) = \frac{\hat{R}_{\zeta}^-(j)}{\sum_{k \in \mathcal{A}_{\zeta}} \hat{R}_{\zeta}^-(k)} \quad \text{se } j \in \mathcal{A}_{\zeta}, \qquad 0 \text{ altrimenti}.
$$

La costruzione è non circolare: nucleo $\mathcal{K}_{\zeta}$ e loading positiva $R_{\zeta}^+$ provengono dalla fattorizzazione (8.2.4); il lato inibitorio ne deriva applicando lo stesso operatore $\mathcal{A}^{*}$ al campo di soppressione $\hat{R}_{\zeta}^-$.

#### Migrazione del rango 1 ed eliminazione del doppio conteggio {#sec:8-2-6}

Quando $\zeta$ viene committata, le componenti di rango 1 che essa incarna devono migrare fuori dalle matrici pairwise per evitare doppio conteggio. I coefficienti $g_{\zeta}^+, g_{\zeta}^- > 0$ che seguono sono le **masse strutturali migrate** della causa latente, non guadagni dinamici: quantità estensive che bilanciano l'energia asportata dalle matrici pairwise (e che peseranno l'apoptosi in 8.6), distinte sia dal fattore di dissipazione $\gamma \in (0,1)$ sia dall'accoppiamento dinamico $\beta_{\mathrm{lat}}$ della \cref{sec:9-1}, con cui non vanno confuse. La decomposizione completa del mezzo è:

$$
\mathbf{M} \approx \mathbf{M}_{\mathrm{res}} + g_{\zeta}^+ R_{\zeta}^+ R_{\zeta}^{+\top}, \qquad \mathbf{W} \approx \mathbf{W}_{\mathrm{res}} - \frac{g_{\zeta}^-}{2}\left( R_{\zeta}^+ R_{\zeta}^{-\top} + R_{\zeta}^- R_{\zeta}^{+\top} \right).
$$

Il termine negativo è il prodotto incrociato simmetrizzato che cattura la soppressione collettiva: chi attiva il nucleo sopprime gli antagonisti. La simmetrizzazione $\tfrac{1}{2}(R_{\zeta}^+ R_{\zeta}^{-\top} + R_{\zeta}^- R_{\zeta}^{+\top})$ è obbligata, non estetica: la \cref{sec:9} assume $\mathbf{W}$ simmetrica, e un prodotto esterno fra due vettori distinti non lo è. La direzionalità della soppressione (dal nucleo verso gli antagonisti) non va dunque immagazzinata nella polarità, ma emerge dinamicamente attraverso l'operatore normalizzato $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$, in pieno accordo con il Principio dell'Asimmetria Emergente. Al commit la componente di rango 1 viene rimossa dalle matrici pairwise --- non *ripristinata*, ma migrata dentro $\zeta$. Poiché la NMF è un'approssimazione ai minimi quadrati, la sottrazione del blocco positivo da $\mathbf{M}$ può sovrastimare singole celle e produrre valori negativi, in violazione dell'assioma di non-negatività geometrica $\mathbf{M} \in \mathbb{R}_{\ge 0}^{N \times N}$ (\cref{sec:6-2}) --- valori che farebbero esplodere l'operatore canonico $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$ della \cref{sec:9}. La migrazione su $\mathbf{M}$ è quindi rettificata:

$$
\mathbf{M} \leftarrow \max\!\left(0,\; \mathbf{M} - g_{\zeta}^+ \mathcal{P}_{\mathrm{off}}\!\big(R_{\zeta}^+ R_{\zeta}^{+\top}\big)\right),
$$

dove $\mathcal{P}_{\mathrm{off}}$ annulla la diagonale ($\mathcal{P}_{\mathrm{off}}(A)_{ij} = A_{ij}$ per $i \neq j$, $0$ altrimenti): poiché $m_{ii} = 0$, la migrazione del rango 1 non deve toccare la diagonale.

I guadagni $g_{\zeta}^+, g_{\zeta}^-$ non sono iperparametri liberi: obbediscono a un **Principio di Conservazione dell'Energia Topologica**, che ne fissa il valore in modo che la massa rimossa dalle matrici pairwise eguagli quella *attualmente presente* nel mezzo al momento del commit. La massa va dunque letta dallo stato **corrente** di $\mathbf{M}$ --- non dalla storia accumulata --- proiettando il blocco nucleo$\times$nucleo osservato sul template di rango 1:

$$
g_{\zeta}^+ = \frac{\big\langle \mathbf{M},\; \mathcal{P}_{\mathrm{off}}(R_{\zeta}^+ R_{\zeta}^{+\top}) \big\rangle_F}{\big\lVert \mathcal{P}_{\mathrm{off}}(R_{\zeta}^+ R_{\zeta}^{+\top}) \big\rVert_F^2}.
$$

Non occorre estrarre la sottomatrice nucleo$\times$nucleo: poiché $R_{\zeta}^+$ è a supporto sparso (nullo fuori da $\mathcal{K}_{\zeta}$), il template $\mathcal{P}_{\mathrm{off}}(R_{\zeta}^+ R_{\zeta}^{+\top})$ è già nullo ovunque tranne il blocco $\mathcal{K}_{\zeta}\times\mathcal{K}_{\zeta}$ e agisce da maschera, sicché il prodotto di Frobenius con l'intera $\mathbf{M}$ è ben definito e seleziona esattamente quel blocco. Questa proiezione preleva esattamente l'energia topologica *sopravvissuta* all'oblio fisiologico $\lambda^M$ (\cref{sec:7-8}) fino all'istante del commit. La forma ingenua $c^2 \sum_{\chi_i \in \mathcal{H}_{\zeta}} \beta_i \rho_i^2$ misurerebbe invece la storia *non decaduta*: sottrarla da una $\mathbf{M}$ decaduta sovrastimerebbe l'asportazione, azzererebbe celle in modo scorretto e gonfierebbe $g_{\zeta}^+$, falsando a cascata l'Inerzia dell'Apoptosi (8.6) fino a causare morti per inedia premature.

In modo speculare, il guadagno inibitorio si ottiene proiettando il blocco di conflitto osservato sul template bipartito simmetrico. Sia $B_{\zeta}^- = [-\mathbf{W}]_+$ la componente inibitoria osservata nell'intero mezzo e $Q_{\zeta}^- = \tfrac{1}{2}(R_{\zeta}^+ R_{\zeta}^{-\top} + R_{\zeta}^- R_{\zeta}^{+\top})$ il template bipartito simmetrico (anch'esso a supporto sparso, nullo fuori dai blocchi $\mathcal{K}_{\zeta}\times\mathcal{A}_{\zeta}$ e $\mathcal{A}_{\zeta}\times\mathcal{K}_{\zeta}$, che maschera la proiezione senza richiedere estrazioni di sottomatrici). Allora

$$
g_{\zeta}^- = \max\!\left(0,\; \frac{\langle B_{\zeta}^-,\, Q_{\zeta}^-\rangle_F}{\lVert Q_{\zeta}^- \rVert_F^2}\right),
$$

ossia il coefficiente di rango 1 ottimo non negativo che fitta il template alla soppressione osservata. La forma è identica a quella positiva: anche $g_{\zeta}^+$ è la proiezione di Frobenius del blocco nucleo$\times$nucleo *corrente* di $\mathbf{M}$ sul proprio template. Entrambi i guadagni si leggono dallo stato attuale del mezzo, e il trattamento di $\mathbf{M}$ e $\mathbf{W}$ è perfettamente simmetrico: il lato inibitorio cessa di essere soltanto descrittivo. Questa identità garantisce che la massa rimossa orizzontalmente da $\mathbf{M}$ e $\mathbf{W}$ sia esattamente pari a quella conferita verticalmente a $\zeta$, impedendo fluttuazioni spurie della massa semantica totale; l'operatore $\max(0,\cdot)$ assorbe solo il piccolo errore di approssimazione della NMF.

Per $\mathbf{W}$, rimuovere un blocco negativo equivale a sommare il suo opposto, e $\mathbf{W}$ non richiede rettificazione di segno essendo per costruzione una matrice firmata:

$$
\mathbf{W} \leftarrow \mathbf{W} + \frac{g_{\zeta}^-}{2}\left( R_{\zeta}^+ R_{\zeta}^{-\top} + R_{\zeta}^- R_{\zeta}^{+\top} \right).
$$

Né richiede l'operatore off-diagonale $\mathcal{P}_{\mathrm{off}}$ usato per $\mathbf{M}$, e qui la geometria della teoria si chiude su se stessa: poiché in 8.2.5 si è imposta la disgiunzione dei supporti $\mathcal{K}_{\zeta} \cap \mathcal{A}_{\zeta} = \emptyset$, ogni elemento diagonale del template vale $\tfrac{1}{2}\big(R_{\zeta}^+(i) R_{\zeta}^-(i) + R_{\zeta}^-(i) R_{\zeta}^+(i)\big) = R_{\zeta}^+(i) R_{\zeta}^-(i) = 0$ --- poiché nessun nodo appartiene a entrambi i supporti. Il prodotto incrociato ha dunque diagonale *nativamente* nulla, e l'aggiornamento di $\mathbf{W}$ rispetta $w_{ii}=0$ senza alcuna rettificazione esplicita.

L'operatore $\max(0,\cdot)$ garantisce che gli inevitabili errori locali di approssimazione della fattorizzazione non violino la non-negatività rigorosa di $\mathbf{M}$. Va però imposta una conseguenza formale. La migrazione non si limita ad azzerare alcune celle di $\mathbf{M}$: più in generale ne *riduce* il valore (ad esempio da $0.8$ a $0.3$), e se la polarità $w_{ij}$ residua eccede la nuova magnitudo (ad esempio $|w_{ij}| = 0.7 > 0.3$) la condizione di compatibilità strutturale $|w_{ij}| \leq m_{ij}$ della \cref{sec:9} viene violata, facendo esplodere l'operatore $\mathbf{J}$. Non basta dunque azzerare le celle annullate: al termine della migrazione va applicato sull'intero blocco modificato l'operatore di proiezione già introdotto in 7.10,

$$
w_{ij} \leftarrow \operatorname{clip}\!\left(w_{ij},\, -m_{ij},\, +m_{ij}\right),
$$

che protegge indefinitamente la garanzia di contrazione di $\mathbf{J}$.

Tutte le grandezze prodotte dalla genesi sono **attributi persistenti** dell'unità latente, non quantità transitorie della migrazione. Al commit, $\zeta$ resta definita dalla tupla

$$
\zeta \;=\; \big(\, \mathcal{K}_{\zeta},\; R_{\zeta}^+,\; \mathcal{A}_{\zeta},\; R_{\zeta}^-,\; g_{\zeta}^+,\; g_{\zeta}^-,\; \theta_{\zeta}^{\mathrm{att}} \,\big),
$$

memorizzata come stato proprio del nodo. In particolare i guadagni $g_{\zeta}^+, g_{\zeta}^-$ vengono **congelati** al loro valore di nascita (l'energia di rango 1 migrata dal mezzo) e conservati: non sono ricalcolati a ogni passo, ma riletti dalla metrica di apoptosi (\cref{sec:8-6}, dove costituiscono l'onere topologico del nodo). Si noti che $g_{\zeta}^{\pm}$ non entrano nella spinta dinamica di 9.1, la quale è regolata dalla costante intensiva $\beta_{\mathrm{lat}}$: le masse misurano un costo, non una forza. Questo congelamento è coerente con la semantica dell'oblio: $g_{\zeta}^{\pm}$ rappresentano un investimento strutturale *sommerso*, sostenuto una volta per tutte alla nascita; se l'unità cessa di essere mobilitata, tale costo fisso non decade e fa convergere la sua Inerzia verso 1, candidandola all'apoptosi. Gli archi pairwise che $\zeta$ accumula in seguito verso nodi esterni (l'emancipazione di 8.2.8) sono invece grandezze dinamiche distinte, registrate nella riga di $\mathbf{M}$ e disgiunte da $g_{\zeta}^{\pm}$.

La simmetria del meccanismo è quadrupla:

$$
\underbrace{\mathbf{M} \;/\; R_{\zeta}^+ \;/\; \text{completamento}}_{\text{lato eccitatorio}} \qquad \underbrace{\mathbf{W} \;/\; R_{\zeta}^- \;/\; \text{soppressione}}_{\text{lato inibitorio}}.
$$

#### Criterio di commit: doppio test dinamico {#sec:8-2-7}

Il commit è giustificato solo se $\zeta$ produce un guadagno dinamico che nessuna riponderazione pairwise lineare può replicare. Il criterio è doppio.

**Test di completamento.** Per ciascuna maschera parziale $S \subsetneq \mathcal{K}_{\zeta}$ si definisce il guadagno di ricostruzione del sistema con $\zeta$ rispetto al controfattuale lineare di rango 1:

$$
\operatorname{Comp}_{\zeta}(S) = \operatorname{Rec}_{\mathrm{nonlin}}(\mathcal{K}_{\zeta} \setminus S \mid S) - \operatorname{Rec}_{\mathrm{rank\text{-}1}}(\mathcal{K}_{\zeta} \setminus S \mid S).
$$

Il criterio non deve dipendere da una maschera scelta ad hoc: si richiede che il guadagno sia positivo *in media* su una famiglia canonica di maschere $\mu_{\zeta}$ --- per default le maschere leave-one-out $S = \mathcal{K}_{\zeta} \setminus \{t\}$, una per ciascun nodo del nucleo, o un mascheramento più severo (per esempio dropout di Bernoulli al 50\% sul nucleo) che metta alla prova la capacità di $\zeta$ di rigenerare il pattern completo da frammenti gravemente incompleti --- con significatività valutata endogenamente:

$$
\mathbb{E}_{S \sim \mu_{\zeta}}\left[\operatorname{Comp}_{\zeta}(S)\right] > 0.
$$

**Test di soppressione.** Anche la soppressione va valutata sotto le stesse maschere parziali, dimostrando che $\zeta$ sopprime gli antagonisti $\mathcal{A}_{\zeta}$ in modo significativamente più deciso del blocco bipartito lineare *anche partendo da evidenza parziale*. Attivando una maschera $S \subsetneq \mathcal{K}_{\zeta}$:

$$
\operatorname{Supp}_{\zeta}(S) = \operatorname{Inh}_{\mathrm{nonlin}}(\mathcal{A}_{\zeta} \mid S) - \operatorname{Inh}_{\mathrm{rank\text{-}1}}(\mathcal{A}_{\zeta} \mid S).
$$

$\zeta$ viene committata solo se entrambi i test sono superati in media sulle maschere:

$$
\mathbb{E}_{S \sim \mu_{\zeta}}\left[C_{\zeta}(S)\right] \geq \varepsilon_C^* \quad \text{e} \quad \mathbb{E}_{S \sim \mu_{\zeta}}\left[S_{\zeta}(S)\right] \geq \varepsilon_S^* \quad \Rightarrow \quad \zeta \in \mathcal{V}_{\mathrm{lat}}.
$$

La soglia $> 0$ sarebbe troppo debole: un vantaggio infinitesimo, indistinguibile dal rumore numerico, autorizzerebbe il commit. È inoltre essenziale che *entrambi* i guadagni siano distribuzioni su un insieme di maschere e non singoli scalari: l'autoconsistenza di un solo valore $x$ è $x^2/x = x$, e il test $x \geq x$ sarebbe una tautologia vuota. Valutando anche la soppressione sulle maschere parziali, la significatività di entrambi i lati è resa endogena dallo stesso operatore. Posto $C_{\zeta}(S) = \max(0, \operatorname{Comp}_{\zeta}(S))$ e $S_{\zeta}(S) = \max(0, \operatorname{Supp}_{\zeta}(S))$, le soglie sono $\varepsilon_C^* = \frac{\sum_S C_{\zeta}(S)^2}{\sum_S C_{\zeta}(S)}$ e $\varepsilon_S^* = \frac{\sum_S S_{\zeta}(S)^2}{\sum_S S_{\zeta}(S)}$: il guadagno medio deve raggiungere il livello di significatività generato dalla morfologia della propria distribuzione, non un semplice scarto positivo. In accordo con la convenzione dell'inverso generalizzato, se $\sum_S C_{\zeta}(S) = 0$ o $\sum_S S_{\zeta}(S) = 0$ la soglia corrispondente è indefinita e la candidata fallisce automaticamente il test: una candidata che non produce alcun guadagno di completamento o di soppressione viene rigettata.

I criteri probatori generali $\Delta\mathcal{L}_{\zeta} > 0$, $\Delta\mathcal{T}^-_{\zeta} < 0$, $\Delta\mathcal{C}_{\zeta} > 0$ restano validi come condizioni necessarie di validità strutturale, ma il doppio test dinamico è la condizione sufficiente propria della Genesi per Aggregazione. Si noti l'ordine temporale: il doppio test è valutato a tempo di decisione, confrontando la $\zeta$ non-lineare candidata con il controfattuale lineare di rango 1; la migrazione di 8.2.6 --- e dunque la rimozione effettiva del rango 1 da $\mathbf{M}$ e $\mathbf{W}$ --- avviene solo *dopo* che entrambi i test sono superati. La sequenza corretta è dunque: test $\to$ commit $\to$ migrazione.

#### Residuo episodico e relazione tra $\chi_i$ e $\zeta$ {#sec:8-2-8}

Dopo il commit, gli episodi non vengono compressi né sostituiti. Ognuno acquista una doppia leggibilità:

$$
\chi_i \rightsquigarrow (\rho_i \zeta,\; r_i^{\zeta}), \qquad r_i^{\zeta}(t) = \max\{0,\, a_i(t) - \rho_i \hat{R}_{\zeta}^+(t)\}.
$$

L'errore di predizione si calcola sulla loading **grezza** $\hat{R}_{\zeta}^+$ ottimizzata dalla NMF, non sul caricamento rinormalizzato $R_{\zeta}^+$: i due svolgono ruoli distinti --- $\hat{R}_{\zeta}^+$ porta la scala della ricostruzione (e il vettore rispetto a cui la NMF ha minimizzato l'errore, con $\hat{R}_{\zeta}^+ = c\, R_{\zeta}^+$), mentre $R_{\zeta}^+$ è la direzione normalizzata usata nella geometria della soglia. Sottrarre $\rho_i R_{\zeta}^+$ (più piccolo di un fattore $c$) gonfierebbe artificialmente il residuo. Il residuo $r_i^{\zeta}$ rimane nell'episodio. Esso rappresenta la variante contestuale, l'eccezione, la tensione marginale --- ciò che non è ancora diventato causa latente e che forse un giorno ne genererà un'altra. Se residui di episodi diversi convergono in completamenti incompatibili e ricorrenti, possono innescare una Mitosi: $\zeta \to \zeta^{(1)}, \zeta^{(2)}$.

Al commit, la nuova unità viene aggiunta al lessico latente stabile come suo membro, $\mathcal{V}' = \mathcal{V} \cup \{\zeta\}$, ma **non** acquisisce righe lineari nelle matrici pairwise. Il suo accoppiamento al mezzo è dato interamente dai caricamenti $(R_{\zeta}^+, R_{\zeta}^-)$ attraverso la dinamica delle unità latenti non-lineari (\cref{sec:9-1}).

Dotare $\zeta$ di una riga lineare $m_{\zeta r} = \sum_t R_{\zeta}^+(t)\, m_{tr}$ *verso il proprio nucleo* sarebbe un errore. Tale riga, propagata dall'operatore canonico $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$, equivarrebbe per marginalizzazione a reintrodurre nel blocco nucleo$\times$nucleo proprio il termine di rango 1 fatto migrare fuori in 8.2.6, ricreando per via implicita la macro lineare esclusa in 8.2.2.

Il divieto va però delimitato con precisione, perché non è temporale ma **di dominio**, e deve essere permanente. Vietare a $\zeta$ *qualsiasi* arco pairwise la renderebbe una variabile sterile, incapace di integrarsi nel mezzo. La distinzione corretta è la seguente:

- verso il proprio nucleo generativo, $\zeta \leftrightarrow \mathcal{K}_{\zeta}$, l'accoppiamento resta **sempre** linearmente nullo: lì l'interazione è il caricamento non-lineare $(R_{\zeta}^+, R_{\zeta}^-)$, in perpetuo;
- verso le unità esterne al dominio generativo, $\zeta \leftrightarrow (\mathcal{V} \setminus \mathcal{K}_{\zeta})$, $\zeta$ è soggetta alla normale plasticità parametrica della \cref{sec:7}.

Questa asimmetria è cruciale e ha un fondamento dinamico. Il modello non apprende dall'input esterno $S_C$, ma dal Campo osservabile $\Psi_C$, cioè dallo stato fenomenologico emerso (\crefrange{sec:7-2}{sec:7-3}): l'apprendimento è basato su ciò che il sistema *percepisce dopo aver pensato*, non sulla stringa grezza. Di conseguenza, benché $\zeta$ non compaia mai nel vocabolario esterno $\mathcal{U}$, la sua attivazione non-lineare la fa emergere nel Campo, sopravvivere al taglio di autoconsistenza, diventare Pivot di un nuovo episodio e accumulare archi pairwise ordinari verso nodi esterni (per esempio, un concetto latente formatosi su un dominio può apprendere una relazione stabile con un nodo lessicale incontrato solo in seguito). Concretamente, poiché $\zeta$ rientra nel Campo $\Psi_C$, le normali equazioni parametriche ne processano la co-mobilitazione con un'unità esterna $u \notin \mathcal{K}_{\zeta}$ che partecipi allo stesso episodio, sedimentando un arco ordinario

$$
\Delta m_{\zeta u} = \eta^M \beta_C\, \widetilde{\Sigma}_C(\zeta)\, \widetilde{\Sigma}_C(u), \qquad u \notin \mathcal{K}_{\zeta}.
$$

Questo canale, vietato verso il nucleo ma libero verso l'esterno, è la forma analitica dell'apprendimento di ordine superiore: $\zeta$ nasce per spiegare un pattern passato, ma vive per associarsi alle novità future.

Resta un guardrail necessario. Poiché $\zeta$ scatta proprio quando il suo nucleo è attivo, $\zeta$ e i membri di $\mathcal{K}_{\zeta}$ co-occorrono nel Campo in modo sistematico: senza il vincolo permanente, la plasticità ordinaria della \cref{sec:7} ri-accumulerebbe $\Delta m_{\zeta,t}$ per $t \in \mathcal{K}_{\zeta}$, ricostruendo dalla porta di servizio la macro lineare vietata alla nascita. Operativamente, ciò si realizza come una **maschera di sedimentazione** sul blocco $\zeta \times \mathcal{K}_{\zeta}$ negli aggiornamenti di 7.8. Se la relazione di $\zeta$ con un membro del nucleo cambia in modo sostanziale e ricorrente --- segno che il concetto sta derivando --- la risposta corretta non è la ri-accrezione lineare silenziosa, ma una ri-fattorizzazione, eventualmente una Mitosi.

In sintesi, la Genesi per Aggregazione non comprime episodi né promuove centroidi. I fattori episodici restano tracce storiche separate, con i propri residui e le proprie tensioni marginali. La loro ricorrenza deforma il mezzo, sedimentando un bacino positivo in $\mathbf{M}$ e un bacino di conflitto in $\mathbf{W}$. Una nuova unità latente $\zeta$ è ammessa solo quando tali bacini possono essere interpretati come effetto di una causa comune latente: una variabile dotata di attivazione non-lineare a soglia, di un caricamento positivo $R_{\zeta}^+$ e di un caricamento negativo $R_{\zeta}^-$, le cui componenti di rango 1 migrano fuori dalla sedimentazione pairwise evitando ogni doppio conteggio. La giustificazione di $\zeta$ è puramente dinamica e doppia: essa deve permettere al sistema di completare il pattern da evidenza parziale e di sopprimere selettivamente i propri antagonisti, in misura non riproducibile da alcuna riponderazione pairwise lineare.

### Genesi per lacuna d’interfaccia e Nodo Ombra {#sec:8-3}

La Genesi per Lacuna d’Interfaccia è il processo mediante cui il sistema costruisce una rappresentazione interna stabile per un elemento esterno ricorrente che non possiede ancora un ancoraggio nel vocabolario semantico del mezzo. Essa non comprime una famiglia di fattori episodici già formata da unità note, come nella Genesi per Aggregazione; costruisce invece un posto interno per qualcosa che il sistema incontra attraverso l’interfaccia, ma che non sa ancora trattare come unità propria.

Sia $\mathcal{U}$ l’insieme degli elementi osservabili all’interfaccia linguistica o simbolica esterna. Si può assumere l’esistenza di una funzione parziale di ancoraggio:

$$
\operatorname{anc} : \mathcal{U} \rightharpoonup \mathcal{V}.
$$

Quando $\operatorname{anc}(u)$ è definita, l’elemento esterno $u$ dispone già di un referente interno stabile. Quando invece:

$$
u \in \mathcal{U}, \qquad \operatorname{anc}(u) \text{ non definita},
$$

il sistema incontra una lacuna d’interfaccia. L’elemento $u$ è osservabile nella sequenza esterna, ma non possiede ancora un nodo stabile in $\mathcal{V}$.

Per evitare che ogni elemento ignoto produca immediatamente una nuova unità, il sistema apre una posizione probatoria: il **Nodo Ombra** $\vartheta_u$. Il Nodo Ombra non appartiene al vocabolario semantico stabile:

$$
\vartheta_u \notin \mathcal{V}.
$$

Esso appartiene invece a uno spazio di sospensione, cioè a un insieme di posizioni provvisorie che accumulano evidenza senza modificare ancora la dimensionalità del mezzo. Il Nodo Ombra non è il significato di $u$; è il segnaposto della sua assenza interna.

Ogni volta che $u$ compare in un contesto $C$, il sistema osserva la risposta del mezzo noto alla presenza di tale elemento esterno. Poiché $u$ non ha ancora un nodo stabile, non viene trattato come una sorgente ordinaria del grafo semantico. Il sistema registra invece il campo prodotto dai nodi noti che co-occorrono con $u$, dalle perturbazioni contestuali circostanti e dalle eventuali soppressioni che la sua presenza induce.

Si definisce pertanto il **Campo Atteso** dell’elemento esterno $u$ come la famiglia delle tracce episodiche osservate nei contesti in cui $u$ appare:

$$
\mathbb{E}_u=
\left\{
\left(
\widetilde{\Sigma}_{C \mid u},
\widetilde{\Omega}_{C \mid u}^{-},
\mathcal{T}_{C \mid u}^{-}
\right)
\right\}_{C \in \mathcal{H}_u}.
$$

Qui $\mathcal{H}_u$ indica la storia degli episodi in cui $u$ è stato osservato; $\widetilde{\Sigma}_{C \mid u}$ è la Firma Ristretta positiva del campo prodotto dal contesto contenente $u$; $\widetilde{\Omega}_{C \mid u}^{-}$ è la firma negativa ristretta associata alle soppressioni rilevanti; $\mathcal{T}_{C \mid u}^{-}$ misura la Tensione Negativa prodotta dall’evento.

Il Campo Atteso non descrive ancora il significato interno di $u$. Descrive la forma della perturbazione che l’assenza di un nodo per $u$ lascia nel mezzo. In altri termini, il sistema non sa ancora cosa $u$ sia; osserva però quali regioni semantiche si accendono, quali vengono soppresse e quale tensione si produce ogni volta che $u$ compare.

Per valutare se questa perturbazione ricorrente possieda una forma stabile, si costruisce una **Firma di Partecipazione dell’Ombra**:

$$
\Pi_u(t)=
\frac{
\sum_{C \in \mathcal{H}_u}\beta_C\widetilde{\Sigma}_{C \mid u}(t)
}{
\sum_{C \in \mathcal{H}_u}\beta_C
}.
$$

I pesi $\beta_C$ rappresentano l’affidabilità dell’episodio: possono dipendere dalla chiarezza del Supporto Attivo, dalla bassa dispersione dissipativa, dalla coerenza del contesto o dalla riduzione attesa della tensione qualora $u$ venisse stabilizzato. Analogamente alla loading $\hat{R}_{\zeta}^+$ della Genesi per Aggregazione, $\Pi_u$ è un profilo storico costruito come media pesata di Firme Ristrette già normalizzate. Entrambe sono tuttavia campi storici non negativi e possono essere sottoposte allo stesso operatore di autoconsistenza.

La soglia endogena della lacuna è:

$$
\varepsilon_u^{*}=
\frac{
\sum_{t \in \mathcal{V}}\Pi_u(t)^2
}{
\sum_{t \in \mathcal{V}}\Pi_u(t)
}.
$$

Il **Nucleo Atteso Stabile** dell’elemento esterno $u$ è quindi:

$$
\mathcal{K}_u=
\{t \in \mathcal{V} \mid \Pi_u(t) \geq \varepsilon_u^{*}\}.
$$

La promozione non richiede che tutti gli episodi contenenti $u$ producano lo stesso campo. Richiede che, nella storia delle sue apparizioni, emerga una regione interna sufficientemente stabile da superare la propria coda morfologica. La lacuna diventa ontogeneticamente interessante quando il sistema osserva che l’assenza di $u$ genera sempre un vuoto della stessa forma.

Per inizializzare un eventuale nodo stabile, il sistema costruisce una firma prototipica della lacuna ristretta al Nucleo Atteso Stabile:

$$
R_u(t)=
\begin{cases}
\dfrac{\Pi_u(t)}{\sum_{s \in \mathcal{K}_u}\Pi_u(s)} & \text{se } t \in \mathcal{K}_u, \\
0 & \text{altrimenti.}
\end{cases}
$$

La firma $R_u$ non è una definizione lessicale di $u$, ma una stima del suo ruolo strutturale atteso: indica da quali regioni del mezzo il nuovo nodo dovrebbe ricevere il proprio primo ancoraggio.

La Genesi per Lacuna richiede anche di valutare se l’introduzione di una unità stabile riduca davvero il costo e la tensione del sistema. Il Nodo Ombra viene promosso solo se, durante il periodo probatorio, la trasformazione candidata soddisfa i criteri generali di commit:

$$
\Delta \mathcal{L}_{u}>0,
$$

$$
\Delta \mathcal{T}_{u}^{-}<0,
$$

$$
\Delta \mathcal{C}_{u}>0.
$$

Il primo criterio richiede che l’introduzione del nodo riduca il costo descrittivo degli episodi futuri contenenti $u$; il secondo richiede che diminuisca la tensione prodotta dalla lacuna; il terzo richiede che i campi associati a $u$ diventino più coerenti una volta stabilizzato l’ancoraggio.

Quando il commit è autorizzato, il Nodo Ombra cessa di essere una posizione probatoria e viene promosso a unità stabile:

$$
\mathcal{V}'=\mathcal{V}\cup{v_u}.
$$

Contestualmente, la funzione di ancoraggio viene estesa:

$$
\operatorname{anc}'(u)=v_u.
$$

La distinzione notazionale è importante. $u$ resta l’elemento esterno osservabile; $v_u$ è il suo rappresentante interno stabilizzato. Per abuso controllato di linguaggio, una volta avvenuto il commit si può dire che il sistema ha “appreso $u$”, ma formalmente ciò significa che ha creato un nodo interno $v_u$ ancorato a $u$.

I legami iniziali di $v_u$ vengono inferiti dal Campo Atteso attraverso la firma $R_u$:

$$
m_{v_u r}=\sum_{t \in \mathcal{V}}R_u(t)m_{tr},
$$

$$
w_{v_u r}=\sum_{t \in \mathcal{V}}R_u(t)w_{tr}.
$$

La distinzione notazionale ($v_u$ in luogo di $\zeta$) riflette uno scisma topologico rispetto alla Genesi per Aggregazione (8.2), non una mera differenza di nome. Il Nodo Ombra stabilizzato non è un operatore inferenziale non-lineare astratto, ma il **procuratore interno di un'entità lessicale esterna**: per questo entra legittimamente in $\mathcal{V}_{\mathrm{lex}}$ e, a differenza della causa latente $\zeta$, può e deve ereditare canali pairwise ordinari in $\mathbf{M}$ e $\mathbf{W}$, perché è attraverso quelle righe lineari che riceve la perturbazione diretta della sorgente contestuale $S_C$. Il divieto di righe lineari di 8.2.8 vale per la causa latente, priva di correlato esterno e attiva solo per scatto non-lineare; non per il nodo lessicale, che un correlato esterno ce l'ha.

Nel caso della Genesi per Lacuna, questi legami non sono un’eredità interna piena, come nella Genesi per Aggregazione. Sono **ancoraggi inferiti**: il nuovo nodo viene posizionato osservando gli effetti strutturali che la sua assenza produceva nel mezzo. Il sistema non copia il termine esterno nel proprio vocabolario; costruisce una posizione interna per assorbire una perturbazione ricorrente.

È possibile includere anche la componente negativa del Campo Atteso. Se la presenza di $u$ sopprime stabilmente una regione del mezzo, si può costruire una firma antagonista prototipica:

$$
R_u^{-}(t)=
\frac{1}{Z_u^{-}}
\sum_{C \in \mathcal{H}_u}\beta_C\widetilde{\Omega}_{C \mid u}^{-}(t),
$$

con $Z_u^{-}$ costante di normalizzazione sul supporto non nullo. Questa firma può contribuire all’inizializzazione della polarità inibitoria di $v_u$, distinguendo i casi in cui l’elemento nuovo è semplicemente associato a una regione semantica dai casi in cui esso entra come operatore di esclusione, contrasto o differenziazione.

La Genesi per Lacuna è dunque la forma con cui il mezzo trasforma una mancanza ricorrente in una unità. Essa non introduce un nodo perché una stringa è nuova; lo introduce quando l’assenza di un referente interno produce una perturbazione stabile, costosa e riducibile attraverso la creazione di un nuovo centro semantico.

### Mitosi Semantica: risoluzione della frattura dinamica {#sec:8-4}

La Mitosi interviene quando un nodo $x \in \mathcal{V}$ è dinamicamente sovraccarico: partecipa a configurazioni reciprocamente incompatibili, generando Tensione di Taglio Locale persistente ($\kappa_C^-(x) \gg 0$).

La separabilità non va diagnosticata tramite clustering intuitivo, ma con la stessa logica fattoriale della Genesi per Aggregazione, come confronto fra rango 1 e rango 2. Considerati gli episodi incidenti $\{a_i \mid \chi_i \ni x\}$, si confronta la fattorizzazione $a_i \approx \rho_i R$ con $a_i \approx \rho_i^{(1)} R_1 + \rho_i^{(2)} R_2 + r_i$, **tuttavia, poiché un modello a rango 2 ridurrebbe sistematicamente l'errore per puro sovradattamento (*overfitting*), un semplice guadagno scalare risulterebbe** tautologico. Si valuta perciò il **campo** dei guadagni episodici, pesato per l'affidabilità,

$$
\Delta_{\mathrm{mit}}(i) = \beta_i \big( \lVert a_i - \rho_i R \rVert^2 - \lVert a_i - (\rho_i^{(1)} R_1 + \rho_i^{(2)} R_2) \rVert^2 \big),
$$

e la Mitosi è autorizzata solo se il guadagno medio supera la soglia autoconsistente *aumentata della penalità descrittiva* per il grado di libertà introdotto, $\mathbb{E}_i[\Delta_{\mathrm{mit}}(i)] \geq \varepsilon_{\mathrm{mit}}^* + \Omega_{\mathrm{MDL}}$, e se i due fattori sono effettivamente antagonisti, $\langle R_1, \mathbf{W} R_2\rangle < 0$. La penalità $\Omega_{\mathrm{MDL}}$ impedisce le scissioni spurie premiate dal solo sovradattamento del rango 2. In tal caso la trasformazione divide la storia relazionale in due unità distinte $x^{(1)}$ e $x^{(2)}$.

Le figlie ereditano archi semantici proporzionalmente al cluster episodico che ha motivato la scissione. Per cristallizzare la risoluzione del conflitto, vengono inizializzate con una forte mutua inibizione in $\mathbf{W}$ ($w_{x^{(1)}x^{(2)}} \ll 0$), pur mantenendo contiguità geometrica in $\mathbf{M}$. La Mitosi trasforma così un conflitto storico in un'inibizione strutturale permanente.

### Coalescenza strutturale endogena {#sec:8-5}

La Coalescenza fonde unità divenute storicamente e funzionalmente ridondanti. Sfruttando l'architettura duale, la teoria elimina la necessità di parametri empirici (come una soglia prefissata $\theta_{\mathrm{coal}}$). Due unità sono ridondanti non se superano un limite imposto a priori dall'osservatore, ma se **condividono cronicamente la stessa topologia e la stessa storia episodica** rispetto alla distribuzione corrente.

Si definisce il **Campo di Ridondanza** su tutte le coppie candidate come il prodotto della similarità semantica strutturale e della sovrapposizione episodica:
$$
R_{\mathrm{coal}}(a,b) = \operatorname{sim}_{\mathrm{sem}}(a,b) \cdot \operatorname{sim}_{\mathrm{inc}}(a,b)
$$
dove $\operatorname{sim}_{\mathrm{inc}}(a,b)$ misura la similarità (es. similarità coseno) tra i vettori di incidenza temporale dei due nodi (ovvero a quali fattori $\chi$ essi partecipano simultaneamente in $\mathcal{X}$ all'interno dell'ipergrafo $\mathcal{G}_{\mathrm{epis}}$).

Per prevenire il collasso di termini antinomici (che occorrono negli stessi contesti ma con ruoli opposti), si definisce specularmente un **Campo Antagonista** $A_{\mathrm{coal}}(a,b)$, basato sull'antagonismo diretto ($-w_{ab}$) e sulla tensione di taglio storica ($\mathcal{K}_{ab}^{-}$).

A questi campi viene applicato l'operatore di autoconsistenza:
$$
\varepsilon_{\mathrm{coal}}^* = \frac{\sum_{a,b} R_{\mathrm{coal}}(a,b)^2}{\sum_{a,b} R_{\mathrm{coal}}(a,b)}, \quad \varepsilon_A^* = \frac{\sum_{a,b} A_{\mathrm{coal}}(a,b)^2}{\sum_{a,b} A_{\mathrm{coal}}(a,b)}
$$

Affinché due nodi si fondano nella nuova unità $\omega_{ab}$, la loro ridondanza deve emergere dal Campo stesso superando $\varepsilon_{\mathrm{coal}}^*$, e non devono presentare antagonismo significativo ($A_{\mathrm{coal}}(a,b) < \varepsilon_A^*$). Il modello fonde ciò che è sostituibile sulla base della propria metrica endogena del momento. La nuova unità si denota $\omega_{ab}$ (non $\zeta$, ormai riservato alle cause aggregative) per evitare ambiguità ontologica.

Se almeno uno dei nodi coalescenti è una causa latente aggregativa, la coalescenza non può limitarsi a fondere righe pairwise, **non essendo peraltro ammissibile l'intersezione diretta di maschere booleane** o supporti logicamente incompatibili. Si converte allora in una **Rifattorizzazione Unificante**: il sistema sospende le unità originarie e rilancia la procedura NMF (\cref{sec:8-2-4}) sull'unione dei rispettivi storici episodici $\mathcal{H}_{\zeta_a} \cup \mathcal{H}_{\zeta_b}$, generando da capo la nuova causa latente condivisa $\omega_{ab}$ con i suoi caricamenti, guadagni e soglia, e applicando l'oblio topologico ai vecchi fattori. Re-derivare la causa unificata dall'evidenza combinata è più corretto che sovrapporre due tuple eterogenee. La fusione di sole righe pairwise resta ammessa unicamente fra nodi ordinari.

### Apoptosi topologica per inedia: oblio endogeno {#sec:8-6}

L’Apoptosi topologica per inedia è il processo mediante cui una unità interna perde legittimità ontologica fino a essere disattivata, archiviata o rimossa. A differenza della soppressione dinamica in $V_C$, che è un fenomeno di frizione attiva e quindi testimonia ancora una rilevanza funzionale del nodo, l’apoptosi è una dissoluzione passiva: il nodo non è più mobilitato dagli eventi, non sostiene più trasformazioni, non organizza più tensioni e tuttavia continua a occupare capacità topologica nel mezzo.

Nell’architettura estesa, l’inedia non deve essere definita tramite soglie assolute di vitalità, come $\theta_\nu$ o $\theta_\mu$. Essa deve emergere come una discrepanza tra il costo strutturale di mantenere un nodo e la sua utilità episodica recente.

Sia dunque $M_{\mathrm{sem}}(t)$ la massa strutturale del nodo $t$ nel grafo semantico stabile $\mathcal{G}_{\mathrm{sem}}$:

$$
M_{\mathrm{sem}}(t)=
\begin{cases}
\sum_{r \in \mathcal{V}} m_{tr} & \text{se } t \in \mathcal{V}_{\mathrm{lex}}, \\
\sum_{r \in \mathcal{V}} m_{tr} + g_t^+ + g_t^- & \text{se } t \in \mathcal{V}_{\mathrm{lat}}.
\end{cases}
$$

Questa quantità misura il costo topologico del nodo: quanta struttura del mezzo resta impegnata dalla sua esistenza. Per le unità latenti il costo non può ridursi alla riga in $\mathbf{M}$: una causa latente appena nata ha riga nulla verso il proprio nucleo (8.2.8), e conteggiarne il costo come $\sum_r m_{\zeta r}$ la renderebbe a massa zero, dunque immortale all'apoptosi. La massa di una causa latente include perciò l'energia strutturale investita nei suoi caricamenti non-lineari, $g_t^+ + g_t^-$ --- la stessa massa migrata in essa al commit (8.2.6), qui contabilizzata come onere. I due contributi sono disgiunti (la massa verso il nucleo vive in $g_t^{\pm}$, quella verso i nodi esterni nella riga di $\mathbf{M}$), sicché non vi è doppio conteggio. Una causa latente che cessa di risuonare con nuovi episodi vede così la propria Inerzia convergere a 1, divenendo candidata all'apoptosi al pari di un nodo lessicale inerte. I termini $g_t^+, g_t^-$ sono contributi genealogici specifici delle cause aggregative: per i nodi lessicali, per i procuratori $v_u$ nati da Lacuna d'Interfaccia, per le unità di Coalescenza e in generale per ogni nodo non generato da Genesi per Aggregazione si pone $g_t^+ = g_t^- = 0$, salvo diversa genealogia ontogenetica esplicita.

Va scongiurata una **morte in culla**: una causa latente appena committata possiede massa strutturale $g_{\zeta}^+ + g_{\zeta}^- > 0$ ma volume di mobilitazione $V_{\mathrm{inc}}(\zeta) = 0$, sicché la sua Inerzia schizzerebbe a 1 e l'apoptosi la cancellerebbe al primo ciclo, prima ancora che possa mettersi alla prova. Per impedirlo, al momento del commit l'accumulatore di $\zeta$ viene inizializzato ereditando la risonanza storica che ne ha motivato la nascita,

$$
V_{\mathrm{inc}}^{(t_0)}(\zeta) = \sum_{\chi_i \in \mathcal{H}_{\zeta}} \beta_i\, \rho_i,
$$

dotazione che concede al concetto il tempo fisiologico di confermarsi sulle novità prima di essere valutato per l'inedia.

Sia invece $V_{\mathrm{inc}}(t)$ il volume di mobilitazione episodica recente del nodo nel layer episodico $\mathcal{G}_{\mathrm{epis}}$. Esso non deve contare soltanto l’attivazione positiva. Un nodo frequentemente soppresso, o coinvolto in tensioni di taglio, non è semanticamente morto: è ancora funzionale come polo antagonista, confine o operatore di esclusione. Per questo, $V_{\mathrm{inc}}(t)$ deve includere sia la partecipazione positiva sia la mobilitazione negativa:

$$
V_{\mathrm{inc}}(t)=
\sum_{\chi \in \mathcal{X}_{\mathrm{recent}}}
\left(a_{\chi}^{+}(t)+a_{\chi}^{-}(t)\right).
$$

Qui $a_{\chi}^{+}(t)$ misura la partecipazione positiva del nodo al fattore episodico $\chi$, mentre $a_{\chi}^{-}(t)$ misura la sua partecipazione antagonista o soppressiva. Se l’implementazione non materializza archi di incidenza negativi, $a_{\chi}^{-}(t)$ può essere ricavato dalla firma negativa ristretta associata all’episodio.

L'insieme $\mathcal{X}_{\mathrm{recent}}$ designa la finestra di storia episodica considerata "recente". La sua ampiezza non è una soglia semantica ma un **parametro di scala temporale** del sistema, analogo per natura alla viscosità $\lambda_d$: fissa l'orizzonte di memoria rispetto al quale si misura la mobilitazione, non un criterio di individuazione di significato. Nelle implementazioni continue non serve una finestra rigida: il volume di incidenza può essere tracciato da un accumulatore esponenziale decadente, che evita di conservare un log storico illimitato,

$$
V_{\mathrm{inc}}^{(t+1)}(u) = \lambda^V V_{\mathrm{inc}}^{(t)}(u) + a_C^{+}(u) + a_C^{-}(u),
$$

dove $\lambda^V \in (0,1)$ regola la scala temporale della memoria di mobilitazione. In entrambe le forme l'orizzonte va riconosciuto come grandezza di scala e non come iperparametro nascosto.

Per evitare rapporti dimensionalmente instabili tra massa strutturale e volume episodico, la teoria confronta le rispettive quote normalizzate nella popolazione corrente. Si definiscono:

$$
\widehat{M}_{\mathrm{sem}}(t)=
\begin{cases}
\dfrac{M_{\mathrm{sem}}(t)}{\sum_{s \in \mathcal{V}}M_{\mathrm{sem}}(s)} & \text{se } \sum_{s \in \mathcal{V}}M_{\mathrm{sem}}(s)>0, \\
0 & \text{altrimenti,}
\end{cases}
$$

$$
\widehat{V}_{\mathrm{inc}}(t)=
\begin{cases}
\dfrac{V_{\mathrm{inc}}(t)}{\sum_{s \in \mathcal{V}}V_{\mathrm{inc}}(s)} & \text{se } \sum_{s \in \mathcal{V}}V_{\mathrm{inc}}(s)>0, \\
0 & \text{altrimenti.}
\end{cases}
$$

L’inedia non coincide con la semplice grandezza di $M_{\mathrm{sem}}(t)$, né con la semplice piccolezza di $V_{\mathrm{inc}}(t)$. È invece un **eccesso di struttura non mobilitata**. Si definisce quindi il **Campo di Inerzia Relativa**:

$$
I(t)=
\begin{cases}
\max\left(0,
\dfrac{\widehat{M}_{\mathrm{sem}}(t)-\widehat{V}_{\mathrm{inc}}(t)}
{\widehat{M}_{\mathrm{sem}}(t)+\widehat{V}_{\mathrm{inc}}(t)}
\right) & \text{se } \widehat{M}_{\mathrm{sem}}(t)+\widehat{V}_{\mathrm{inc}}(t)>0, \\
0 & \text{altrimenti.}
\end{cases}
$$

Questa formulazione elimina la necessità di un termine artificiale $\epsilon$ nel denominatore. Il campo è limitato in $[0,1]$ e misura solo l’eccesso positivo di massa strutturale rispetto alla mobilitazione episodica. Se un nodo possiede molta struttura ma viene ancora mobilitato proporzionalmente alla sua massa, non appare inerte. Se invece occupa una quota rilevante del grafo stabile ma partecipa poco o nulla alla vita episodica recente, $I(t)$ tende verso $1$.

In forma compatta, le normalizzazioni precedenti possono essere riscritte usando l’inverso generalizzato scalare, analogo alla pseudo-inversa di Moore-Penrose. Per uno scalare non negativo $x$, si definisce:

$$
x^{+}=
\begin{cases}
\dfrac{1}{x} & \text{se } x>0, \\
0 & \text{se } x=0.
\end{cases}
$$

Allora:

$$
\widehat{M}_{\mathrm{sem}}(t)=M_{\mathrm{sem}}(t)\left(\sum_{s \in \mathcal{V}}M_{\mathrm{sem}}(s)\right)^{+},
$$

$$
\widehat{V}_{\mathrm{inc}}(t)=V_{\mathrm{inc}}(t)\left(\sum_{s \in \mathcal{V}}V_{\mathrm{inc}}(s)\right)^{+}.
$$

Questa forma è algebricamente equivalente alla definizione per casi e mantiene la stessa filosofia adottata per $\mathbf{D}_M^{+}$ nella dinamica canonica: nessun parametro di regolarizzazione teorico, ma semplice annullamento del contributo quando il supporto è nullo.

L’operatore apoptotico non deve tuttavia reagire a un singolo intervallo di inattività. L’inedia ontologica deve essere cronica. Per questo, il sistema estrae prima il supporto autoconsistente del campo di inerzia corrente:

$$
\varepsilon_I^{*}=
\frac{
\sum_{t \in \mathcal{V}}I(t)^2
}{
\sum_{t \in \mathcal{V}}I(t)
},
$$

con la convenzione che, se $\sum_{t \in \mathcal{V}}I(t)=0$, il supporto di inedia corrente è vuoto. Quando il campo non è nullo, il supporto di inedia corrente è:

$$
\mathcal{I}^{*}=
\{t \in \mathcal{V} \mid I(t) \geq \varepsilon_I^{*}\}.
$$

I nodi in $\mathcal{I}^{*}$ non vengono eliminati immediatamente. Essi alimentano un accumulatore di inedia:

$$
d_t \leftarrow \lambda_d d_t + I(t)\mathbf{1}_{t \in \mathcal{I}^{*}}.
$$

Il parametro $\lambda_d$ non è una soglia semantica: è una costante di scala temporale, cioè la viscosità con cui il mezzo conserva memoria dell’inedia. Regola quanto rapidamente il sistema perdona un periodo di inattività, non decide dall’esterno che cosa conti come significato.

Applicando nuovamente l’autoconsistenza al campo degli accumulatori, si ottiene la soglia endogena dell’inedia cronica:

$$
\varepsilon_d^{*}=
\frac{
\sum_{t \in \mathcal{V}}d_t^2
}{
\sum_{t \in \mathcal{V}}d_t
},
$$

anche qui con supporto vuoto se $\sum_t d_t=0$. I candidati apoptotici sono quindi:

$$
\mathcal{D}^{*}=
\{t \in \mathcal{V} \mid d_t \geq \varepsilon_d^{*}\}.
$$

La candidatura apoptotica non implica necessariamente cancellazione irreversibile. Il commit può assumere tre forme distinte:

1. **Ibernazione**, quando il nodo viene escluso dalla propagazione ordinaria ma resta riattivabile.
2. **Archiviazione**, quando il nodo viene rimosso dal vocabolario operativo ma conservato nella genealogia storica.
3. **Dissoluzione**, quando il nodo viene effettivamente sottratto da $\mathcal{V}$ e le sue relazioni vengono eliminate o redistribuite.

La scelta tra queste forme dipende dal costo genealogico, dalla reversibilità richiesta e dall’eventuale presenza di discendenti ontogenetici. Un nodo generatore di altre unità, o genealogicamente centrale, dovrebbe essere archiviato prima di essere dissolto.

L’apoptosi protegge il mezzo dalla fossilizzazione. Senza di essa, il vocabolario interno diventerebbe un cimitero di unità nate da fluttuazioni passate, non più sostenute dall’esperienza ma ancora capaci di consumare massa topologica e interferire con le dinamiche future. Con essa, invece, la teoria mantiene la propria plasticità senza introdurre soglie assolute: non viene eliminato ciò che è semplicemente raro, ma ciò che emerge come strutturalmente costoso, episodicamente non mobilitato e cronicamente inerte rispetto alla storia recente del sistema.

### Genealogia, reversibilità e interpretabilità {#sec:8-7}

L’ontogenesi altera l’algebra del mezzo. Per garantire stabilità e interpretabilità causale, la teoria richiede che ogni modifica dimensionale conservi in $\mathcal{G}_{\mathrm{sem}}$ una traccia genealogica:
$$
\operatorname{gen}(\zeta) = (\mathcal{O}_{\mathrm{type}}, \mathcal{H}_{\zeta}, \mathcal{K}_{\zeta}, \mathcal{A}_{\zeta}, R_{\zeta}^+, R_{\zeta}^-, g_{\zeta}^+, g_{\zeta}^-, \theta_{\zeta}^{\mathrm{att}}, \mu_{\zeta}, \operatorname{Comp}_{\zeta}, \operatorname{Supp}_{\zeta}, \Delta \mathcal{L}_\zeta, \Delta \mathcal{T}^-_\zeta, \Delta \mathcal{C}_\zeta).
$$
Conservare la matrice storica (l’operazione, l’insieme storico fondativo $\mathcal{H}_{\zeta}$, i caricamenti eccitatorio $R_{\zeta}^+$ e inibitorio $R_{\zeta}^-$, la soglia $\theta_{\zeta}^{\mathrm{att}}$, gli esiti del doppio test e i differenziali termodinamici) rende il modello neuro-simbolico intrinsecamente auditabile. Se una coalescenza degrada le prestazioni future, il modello può disfarla operando un rollback genealogico verso la struttura episodica originaria.

### Sintesi del regime ontogenetico {#sec:8-8}

Attraverso Genesi, Mitosi, Coalescenza e Apoptosi, il vocabolario abbandona lo statuto di inventario statico fornito a priori per divenire un *organismo topologico*. Il modello assimila l'ignoto, differenzia le fratture dinamiche persistenti, compatta le ridondanze strutturali ed elimina le zavorre basandosi esclusivamente sul dialogo autopoietico tra la struttura stabile passata ($\mathcal{G}_{\mathrm{sem}}$) e l'esperienza in atto ($\mathcal{G}_{\mathrm{epis}}$).

### Regime temporale dell'ontogenesi: la ricottura sistemica {#sec:8-9}

Le sezioni precedenti definiscono *quali* trasformazioni il mezzo può compiere; resta da stabilire *quando* gli sia lecito compierle. Il mezzo semantico non nasce maturo: all'avvio è una struttura giovane, poco differenziata e statisticamente fragile, in cui ogni input è sovra-perturbante. Se applicasse da subito le regole ontogenetiche di regime, consoliderebbe come concetti le correlazioni spurie del rumore iniziale. È il problema del **cold start**, ed è una declinazione del dilemma stabilità--plasticità: troppa plasticità e il sistema cristallizza strutture premature; troppa rigidità e resta bloccato, incapace di apprendere. La risposta è una **ricottura sistemica** (annealing): all'inizio il mezzo deve imparare molto e trasformarsi poco.

**L'approccio convenzionale imporrebbe** questa prudenza **tramite euristiche a fasi predefinite e interruttori globali (ad esempio, inibendo l'ontogenesi nella fase di burn-in e fissando soglie artificialmente elevate da abbassare poi manualmente)**. Sarebbe però l'unica eccezione esogena in una teoria interamente endogena: ovunque le soglie sono generate dalla morfologia della distribuzione osservata (operatore $\varepsilon^{*}$), mai imposte dall'esterno, e dei confini di fase A/B/C arbitrari contraddirebbero proprio questo principio. La ricottura va dunque resa endogena come tutto il resto.

**Temperatura del mezzo.** Si definisce una temperatura sistemica a partire dalla *volatilità della struttura stessa*: quanto $\mathbf{M}$ e $\mathbf{W}$ si stanno ancora riorganizzando per passo, in rapporto alla loro magnitudo.

$$
\mathcal{A}_{\mathrm{ann}}(t) = 1 + \frac{\lVert \Delta \mathbf{M}^{(t)} \rVert_F + \lVert \Delta \mathbf{W}^{(t)} \rVert_F}{\lVert \mathbf{M}^{(t)} \rVert_F + \lVert \mathbf{W}^{(t)} \rVert_F}.
$$

Questa temperatura modula moltiplicativamente *tutte* le soglie ontogenetiche endogene --- la saturazione d'innesco (8.1), le soglie del doppio test $\varepsilon_C^*, \varepsilon_S^*$ (8.2.7), la soglia di scissione $\varepsilon_{\mathrm{mit}}^*$ (8.4), e in generale ogni taglio $\varepsilon^{*}$ usato per autorizzare una trasformazione:

$$
\varepsilon^{*}_{\mathrm{eff}}(t) = \mathcal{A}_{\mathrm{ann}}(t)\cdot \varepsilon^{*}.
$$

Il meccanismo è autoritmato e privo di iperparametri. In un mezzo giovane e volatile, $\lVert \Delta \mathbf{M} \rVert_F$ è dello stesso ordine di $\lVert \mathbf{M} \rVert_F$: il fattore vale $\gtrsim 2$, le soglie raddoppiano e l'ontogenesi è di fatto soppressa. A maturità la struttura si stabilizza, $\lVert \Delta \rVert_F \to 0$, il fattore $\to 1$ e le soglie tornano *esattamente* ai valori autoconsistenti nudi delle sezioni precedenti. Non si introduce alcuna nuova costante né alcun confine di fase: la prudenza emerge dalla dinamica.

**Fondamento a due scale temporali.** La giustificazione è profonda. Il mezzo possiede due tempi caratteristici: il Campo veloce, che a ogni episodio rilassa verso il proprio punto fisso (\cref{sec:9}), e la struttura lenta, che sedimenta in $\mathbf{M}$ e $\mathbf{W}$ (\cref{sec:7}). La temperatura $\mathcal{A}_{\mathrm{ann}}$ misura la volatilità della *seconda*: non si conia un concetto mentre le relazioni che lo definirebbero sono ancora in tempesta. Il legame con la contrattività di \cref{sec:9} è diretto --- un mezzo "caldo" è lontano dall'equilibrio strutturale, uno "freddo" vi è prossimo --- e la ricottura impedisce all'ontogenesi di agire finché l'equilibrio non si è assestato.

**Forma locale (default).** Una temperatura globale bloccherebbe ogni nascita finché l'intero mezzo non si raffredda, paralizzando un sistema esposto a novità perenni. La forma canonica è perciò *locale*, ristretta alla regione satura che innesca la candidatura:

$$
\mathcal{A}_{\mathrm{ann}}(\mathcal{P}_{\mathrm{sat}}) = 1 + \frac{\lVert \Delta \mathbf{M}^{(t)}_{\mathcal{P}_{\mathrm{sat}}} \rVert_F + \lVert \Delta \mathbf{W}^{(t)}_{\mathcal{P}_{\mathrm{sat}}} \rVert_F}{\lVert \mathbf{M}^{(t)}_{\mathcal{P}_{\mathrm{sat}}} \rVert_F + \lVert \mathbf{W}^{(t)}_{\mathcal{P}_{\mathrm{sat}}} \rVert_F}.
$$

Così una regione che si è stabilizzata può ospitare una nascita anche se il mezzo globale è ancora giovane --- in piena coerenza con l'innesco per saturazione locale di 7.14: è la *stessa* regione satura a fornire il seme della genesi e a misurarne la maturità.

**Le fasi come regioni emergenti.** Le canoniche tre fasi della ricottura non sono stati cablati, ma regioni di un'unica curva di raffreddamento continua, utili a descriverne il comportamento:

| Regione | $\mathcal{A}_{\mathrm{ann}}$ | Apprendimento episodico | Plasticità parametrica | Ontogenesi |
|---|---|---|---|---|
| Burn-in (mezzo giovane) | $\gg 1$ | alto | bassa/moderata | soppressa dalle soglie gonfiate |
| Transizione | decrescente | alto | attiva | parzialmente abilitata, soglie in raffreddamento |
| Maturità | $\to 1$ | a regime | a regime | abilitata, solo con evidenza ricorrente |

Il sistema attraversa queste regioni non perché un orologio esterno lo comandi, ma perché la propria volatilità strutturale decresce man mano che accumula evidenza. La ricottura sistemica non è dunque una nota difensiva sul cold start, ma una proprietà architetturale del mezzo: l'ontogenesi è gated dal raffreddamento endogeno della struttura che essa stessa modifica.

### Principio di Autoconsistenza Multiscalare {#sec:8-10}

Le trasformazioni ontogenetiche descritte in questa sezione mostrano che la teoria non utilizza l’autoconsistenza soltanto come criterio locale di osservazione del campo. Lo stesso operatore riemerge a scale diverse ogni volta che il sistema deve individuare una forma semantica sopra una coda dissipativa, una ricorrenza instabile o un rumore di fondo.

Il principio può essere formulato così: dato un campo diagnostico non negativo $X_D$ definito su un dominio discreto $D$,

$$
X_D : D \to \mathbb{R}_{\geq 0},
$$

il sistema individua il supporto autoconsistente del campo tramite:

$$
\varepsilon^{*}(X_D)=
\frac{
\sum_{z \in D}X_D(z)^2
}{
\sum_{z \in D}X_D(z)
}.
$$

Il supporto autoconsistente è quindi:

$$
\mathcal{A}^{*}(X_D)=
{d \in D \mid X_D(d) \geq \varepsilon^{*}(X_D)}.
$$

L’operatore è definito solo per campi diagnostici non nulli. Se:

$$
\sum_{z \in D}X_D(z)=0,
$$

il campo non contiene alcuna massa osservativa e, per convenzione, il suo supporto autoconsistente è vuoto:

$$
\mathcal{A}^{*}(X_D)=\varnothing.
$$

Questa convenzione evita divisioni per zero e chiarisce un punto epistemologico: dove non esiste massa diagnostica, non esiste alcuna forma da individuare.

L’autoconsistenza non va intesa come l’operatore universale di ogni decisione del sistema. La teoria conserva parametri dinamici e sistemici, come $\alpha$, $\beta$, $\gamma$, $\lambda$ ed $\eta$, che definiscono intensità della sorgente, accoppiamento, dissipazione, memoria e plasticità. Si distinguano i diversi usi del simbolo $\beta$: $\beta$ è il coefficiente di accoppiamento della propagazione pairwise; $\beta_i$ l'affidabilità trasformativa endogena dell'episodio (8.2.1); $\beta_C$ la stessa affidabilità nel contesto corrente; $\beta_{\mathrm{lat}}$ la costante intensiva di accoppiamento delle cause latenti (9.1). Tali parametri non decidono però dall’esterno che cosa conti come oggetto semantico. Essi regolano la fisica del mezzo. L’operatore $\varepsilon^{*}$ svolge invece una funzione più specifica e più radicale: è l’**operatore canonico di individuazione semantica**.

Esso interviene quando il sistema deve rispondere a domande del tipo: esiste qui una forma che merita di essere trattata come unità operativa? La stessa struttura matematica compare in almeno sei passaggi fondamentali della teoria.

Nel campo positivo, l’operatore individua il Supporto Attivo dell’evento:

$$
\mathcal{A}_C^{*}=\mathcal{A}^{*}(\Psi_C).
$$

Qui la domanda è: *c’è un Segnale sopra la coda dissipativa dell’attivazione?*

Nel campo negativo, l’operatore individua il Nucleo Soppresso:

$$
\mathcal{S}_C^{*}=\mathcal{A}^{*}(\tau_C^{-}).
$$

Qui la domanda è: *c’è una soppressione strutturale autentica, distinta dal rumore negativo?*

Nella Genesi per Aggregazione, l’operatore individua il Nucleo Stabile di una famiglia episodica:

$$
\mathcal{K}_{\zeta}=\mathcal{A}^{*}(\hat{R}_{\zeta}^+).
$$

Qui la domanda è: *quale regione del mezzo costituisce il supporto strutturale autentico della causa latente emergente?*

Nella Genesi per Aggregazione, l’operatore individua anche il supporto degli episodi rilevanti:

$$
\mathcal{H}_{\zeta} = \mathcal{A}^*(\rho).
$$

Qui la domanda è: *quali episodi risuonano significativamente con il fattore latente emergente, e devono quindi contribuire alla sua firma prototipica?*

Nella Genesi per Lacuna, l’operatore individua il Nucleo Atteso Stabile di un elemento esterno ancora privo di ancoraggio:

$$
\mathcal{K}_u=\mathcal{A}^{*}(\Pi_u).
$$

Qui la domanda è: *c’è una forma interna stabile prodotta dall’assenza ricorrente di un referente per $u$?*

Nella Coalescenza, l’operatore può individuare le coppie che emergono come ridondanti rispetto alla popolazione corrente delle coppie candidate:

$$
\mathcal{C}_{\mathrm{coal}}^{*}=\mathcal{A}^{*}(R_{\mathrm{coal}}).
$$

Il commit resta però vincolato da un secondo campo diagnostico, quello antagonista. La coalescenza è ammessa soltanto quando una coppia emerge come ridondante senza emergere come oppositiva:

$$
R_{\mathrm{coal}}(a,b) \geq \varepsilon^{*}(R_{\mathrm{coal}})
\quad \text{e} \quad
A_{\mathrm{coal}}(a,b) < \varepsilon^{*}(A_{\mathrm{coal}}).
$$

Qui la domanda è: *c’è ridondanza strutturale non antagonista?*

Nell’Apoptosi topologica, l’operatore individua prima il supporto corrente dell’inerzia relativa e poi la cronicizzazione dell’inedia:

$$
\mathcal{I}^{*}=\mathcal{A}^{*}(I),
$$

$$
\mathcal{D}^{*}=\mathcal{A}^{*}(d).
$$

Qui la domanda non è se un nodo sia “morto” in senso assoluto, ma se esista una candidatura apoptotica: *c’è una inerzia ontologica cronica rispetto alla storia recente del mezzo?*

Questi casi non sono identici nel dominio di partenza. Il campo $\Psi_C$ è un campo di attivazione episodica; $\tau_C^{-}$ è un campo di soppressione; $\hat{R}_{\zeta}^+$ è la loading grezza di una fattorizzazione non-negativa; $\Pi_u$ è una impronta attesa media; $R_{\mathrm{coal}}$ è un campo di ridondanza su coppie; $I$ e $d$ sono campi diagnostici di inedia. Tuttavia, tutti condividono la stessa forma astratta: un insieme di valori non negativi, una coda dissipativa, una concentrazione quadratica e una soglia generata dal campo stesso.

Questa è l’autoconsistenza multiscalare della teoria. Non significa che il sistema sia privo di parametri, né che ogni scelta implementativa sia deducibile da $\varepsilon^{*}$. Significa piuttosto che le transizioni di individuazione semantica non dipendono da soglie assolute imposte dall’esterno. Quando il sistema deve stabilire se un evento, un conflitto, un pattern, una lacuna, una ridondanza o un’inedia siano abbastanza strutturati da diventare operativi, esso non applica un valore magico: lascia che sia la morfologia del campo diagnostico a determinare il proprio supporto.

Il principio può essere riassunto così:

$$
\text{ogni individuazione semantica è un taglio autoconsistente di un campo diagnostico.}
$$

Questa formulazione chiude il passaggio dalla semantica come luogo alla semantica come evento. Un concetto stabilizzato può essere interpretato come un evento di campo storicamente congelato; un evento, a sua volta, può essere interpretato come un’ontologia transitoria. L’ontogenesi non è quindi un’aggiunta accessoria alla teoria, ma il punto in cui la dinamica del significato diventa capace di trasformare il mezzo che la rende possibile.

Va precisato, dal punto di vista epistemologico, che $\varepsilon^{*}$ non è un filtro di *denoising* capace di fabbricare concentrazione dal nulla, bensì un selettore relativo che la *eredita*. Il suo potere discriminante è condizionato alla termodinamica del mezzo a monte (\cref{sec:9}): sono la focalizzazione della sorgente, la dissipazione $\gamma$, l'inibizione per conflitto e --- in modo cruciale --- la *normalizzazione del ricevente* in $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$ a garantire la concentrazione fenomenologica. Dividendo il segnale in ingresso per il proprio grado topologico, i nodi ad alta connettività (gli *hub* e le regioni di sfondo denso) fungono da pozzi dissipativi --- vengono sterilizzati dal proprio stesso peso strutturale --- e il rumore non invade il nucleo. L'autoconsistenza interviene solo alla fine, operando il taglio su una morfologia già assestata. Qualora l'input $S_C$ sia volutamente diffuso, la dinamica produce correttamente un campo piatto ($\mathrm{CV} \to 0$) e l'operatore si astiene dall'individuare un concetto inesistente: la condizionalità non è una fragilità, ma il *gate* che separa il significato dal rumore.


## Dinamiche ammissibili: una formulazione canonica {#sec:9}

La Teoria dello Spazio Semantico Continuo non prescrive un unico algoritmo computazionale, bensì definisce lo spazio di ammissibilità degli operatori che traducono l’incontro tra mezzo strutturale e sorgente in uno stato semantico interpretabile. Tuttavia, affinché la teoria sia operativamente falsificabile e simulabile, è necessario definirne una dinamica canonica di riferimento.

Nella formulazione estesa, una dinamica è ammissibile se rispetta lo scisma epistemologico tra Potenziale interno $V_C$ e Campo osservabile $\Psi_C$. Poiché l’architettura si fonda su un dualismo strutturale in cui la geometria $\mathbf{M}$ è separata dalla polarità $\mathbf{W}$, la propagazione non può avvenire in forma isotropa.

La matrice $\mathbf{M}$ registra la magnitudo storica dei canali semantici; la matrice $\mathbf{W}$ registra la direzione polarizzata dell’interazione lungo tali canali. Questa distinzione richiede una condizione di compatibilità strutturale:

$$
\operatorname{supp}(\mathbf{W}) \subseteq \operatorname{supp}(\mathbf{M}),
$$

ossia:

$$
w_{ij}=0 \quad \text{se} \quad m_{ij}=0.
$$

In forma più forte, è naturale richiedere che la polarità non ecceda la magnitudo del canale che la sostiene:

$$
|w_{ij}| \leq m_{ij}.
$$

Questa non è una riduzione di $\mathbf{M}$ a $|\mathbf{W}|$. Al contrario: $\mathbf{M}$ resta l’integrale storico del coinvolgimento strutturale, mentre $\mathbf{W}$ resta il differenziale polarizzato. La disuguaglianza assicura soltanto che una forza eccitatoria o inibitoria non possa propagarsi attraverso un canale topologicamente inesistente.

Affinché emerga la direzionalità semantica, ossia il Principio dell’Asimmetria Emergente, l’interazione dinamica è normalizzata rispetto all’orizzonte spaziale del nodo *ricevente*. Con la convenzione $\mathbf{J} = \mathbf{D}_M^{+}\mathbf{W}$ si ha infatti $J_{ij} = w_{ij}/d_i$, dove $d_i$ è il grado del ricevente $i$: ogni nodo aggrega i propri vicini come media pesata e normalizzata dalla propria connettività strutturale totale. Definita la matrice diagonale dei gradi geometrici pesati $\mathbf{D}_M$, con:

$$
(\mathbf{D}_M)_{ii}=d_i=\sum_j m_{ij},
$$

si introduce l’**operatore di interazione normalizzato**. Per gestire il caso di nodi isolati o di grado geometrico nullo, la regola formale più pulita consiste nell’intendere l’inversa come pseudo-inversa di Moore-Penrose. Poiché $\mathbf{D}_M$ è diagonale, la sua pseudo-inversa è definita da:

$$
(\mathbf{D}_M^{+})_{ii}=
\begin{cases}
\dfrac{1}{d_i} & \text{se } d_i>0, \\
0 & \text{se } d_i=0.
\end{cases}
$$

L’operatore canonico diventa quindi:

$$
\mathbf{J}=\mathbf{D}_M^{+}\mathbf{W}.
$$

In questa formulazione, un nodo privo di grado geometrico non produce singolarità e non necessita di un parametro artificiale di regolarizzazione: semplicemente non dispone di canali attraverso cui emettere propagazione. Dal punto di vista implementativo, è comunque possibile adottare una regolarizzazione numerica del tipo $d_i+\epsilon$ per prevenire instabilità finite-precision, ma tale scelta appartiene alla prassi computazionale e non alla definizione teorica dell’operatore.

Sebbene $\mathbf{W}$ sia simmetrica, l’operatore $\mathbf{J}$ risulta in generale non simmetrico. Infatti:

$$
J_{ij}=\frac{w_{ij}}{d_i}
\quad \text{se } d_i>0,
$$

mentre:

$$
J_{ji}=\frac{w_{ji}}{d_j}
\quad \text{se } d_j>0.
$$

Poiché in generale $d_i \neq d_j$, si ha $J_{ij} \neq J_{ji}$, e la direzionalità del flusso semantico emerge naturalmente. La normalizzazione riguarda la *suscettibilità del ricevente*: un nodo con elevata connettività strutturale totale in $\mathbf{M}$ è meno perturbabile da ogni singolo vicino --- la sua attivazione è la media normalizzata di un ampio contesto, e nessun legame isolato lo domina; un nodo periferico, al contrario, è fortemente sensibile ai pochi legami che possiede. Si tratta di una dinamica semanticamente plausibile, formalmente assimilabile alla normalizzazione di tipo random-walk ($\mathbf{D}^{-1}\mathbf{W}$) usata nelle reti su grafo. (Per normalizzare invece l'influenza dell'*emittente* occorrerebbe l'operatore trasposto $\mathbf{W}\mathbf{D}_M^{+}$, con prova di stabilità in norma 1; la presente teoria adotta la normalizzazione del ricevente, coerente con la prova di contrazione in norma infinito della \cref{sec:9}.)

L’evoluzione del Potenziale interno al passo temporale $t+1$ dell’episodio può essere descritta da un’equazione iterativa alle differenze finite:

$$
V_C^{(t+1)}=(1-\gamma)V_C^{(t)}+\alpha S_C+\beta\mathbf{J}\Psi_C^{(t)}.
$$

La rettificazione fenomenologica viene applicata a ogni passo:

$$
\Psi_C^{(t+1)}=\max\left(0,V_C^{(t+1)}\right).
$$

Qui $\gamma \in (0,1)$ è un fattore di dissipazione termodinamica locale, $\alpha$ modula la forzante continua della sorgente contestuale $S_C$, e $\beta$ governa il tasso di accoppiamento relazionale.

Dal punto di vista operativo, la sorgente $S_C$ agisce come una forzante mantenuta costante per la durata dell’episodio. Il processo iterativo si arresta al raggiungimento di una tolleranza di convergenza:

$$
\lVert \Psi_C^{(t+1)}-\Psi_C^{(t)}\rVert<\delta,
$$

oppure al raggiungimento di un numero massimo di iterazioni $T_{\max}$, che impedisce cicli indefiniti in casi di oscillazione residua.

La stabilità della dinamica può essere formulata distinguendo tra garanzia globale e controllo linearizzato. Definita la mappa iterativa:

$$
F(V)=(1-\gamma)V+\alpha S_C+\beta\mathbf{J}\operatorname{ReLU}(V),
$$

si osserva che la rettificazione $\operatorname{ReLU}(x)=\max(0,x)$ è un operatore non espansivo, cioè $1$-Lipschitziano:

$$
\lVert \operatorname{ReLU}(V)-\operatorname{ReLU}(U)\rVert \leq \lVert V-U\rVert.
$$

Pertanto, per una norma matriciale indotta, vale:

$$
\lVert F(V)-F(U)\rVert \leq \left((1-\gamma)+\beta\lVert \mathbf{J}\rVert\right)\lVert V-U\rVert.
$$

La mappa è dunque una contrazione globale quando:

$$
(1-\gamma)+\beta\lVert \mathbf{J}\rVert<1,
$$

ossia:

$$
\beta\lVert \mathbf{J}\rVert<\gamma.
$$

In tale regime, per il Teorema delle Contrazioni di Banach, la dinamica ammette un punto fisso unico e l’iterazione converge verso di esso. Questa garanzia copre il **regime parametrico ordinario** a dimensionalità costante --- propagazione pairwise senza cause latenti aggregative attive. L'estensione al regime inferenziale di ordine superiore, con unità latenti non-lineari $\zeta$ attive, è trattata subito sotto, includendo il contributo latente nel budget di Lipschitz complessivo.

La condizione di compatibilità $|w_{ij}| \leq m_{ij}$ consente una lettura più concreta in norma infinito. Per ogni riga non nulla:

$$
\sum_j |J_{ij}|=\sum_j \frac{|w_{ij}|}{d_i}\leq \sum_j \frac{m_{ij}}{d_i}=1.
$$

Quindi:

$$
\lVert \mathbf{J}\rVert_{\infty}\leq 1.
$$

In questo caso, una condizione sufficiente particolarmente semplice per la contrazione globale è:

$$
\beta<\gamma.
$$

Questa forma non sostituisce la condizione generale $\beta\lVert \mathbf{J}\rVert<\gamma$, ma mostra come il vincolo di dominanza geometrica renda il sistema naturalmente controllabile.

La condizione spettrale:

$$
\beta\rho(\mathbf{J})<\gamma
$$

(dove $\rho(\cdot)$ denota il raggio spettrale, da non confondere con la risonanza episodica $\rho_i$ della \cref{sec:8-2})

resta utile come criterio prudenziale nel regime linearizzato o locale, ma non deve essere confusa con una garanzia globale per la dinamica non lineare. La distinzione è essenziale: il raggio spettrale descrive il comportamento lineare dell’operatore, mentre la norma indotta, combinata con la non espansività della ReLU, fornisce il vincolo contrattivo globale.

In questa equazione, la propagazione del segnale nel grafo è demandata esclusivamente alla fenomenologia emersa $\Psi_C^{(t)}$. L’inibizione e il conflitto, veicolati dai valori negativi in $\mathbf{J}$, agiscono confinati all’interno di $V_C$, spingendo i nodi riceventi sotto lo zero. Tuttavia, poiché l’operatore di rettificazione interviene a ogni passo, un nodo soppresso cessa immediatamente di irradiare ulteriore inibizione. Questo accorgimento formale previene riverberi caotici e rispetta un vincolo epistemologico cruciale: il conflitto lavora nel profondo del Potenziale, ma l’evento semantico comunica con il resto del sistema solo attraverso la sua presenza positiva.

La dinamica canonica qui proposta non esaurisce lo spazio degli operatori ammissibili. Essa fornisce un caso di riferimento: una forma minima, simulabile e falsificabile, capace di mostrare come la teoria possa generare campi osservabili, nuclei attivi, soppressioni, tensioni e successive trasformazioni del mezzo.

### Dinamica delle unità latenti non-lineari {#sec:9-1}

Quando il mezzo contiene unità latenti $\zeta \in \mathcal{V}_{\mathrm{lat}}$ generate dall’Ontogenesi Semantica, la dinamica canonica si estende per incorporarne l’attivazione a soglia. A ogni passo dell’iterazione, dopo l’aggiornamento standard del Potenziale, ciascuna unità latente calcola la propria attivazione:

$$
z_{\zeta}^{(t)} = \varphi\!\left(\langle R_{\zeta}^+, \Psi_C^{(t)}\rangle - \langle R_{\zeta}^-, \Psi_C^{(t)}\rangle - \theta_{\zeta}^{\mathrm{att}}\right),
$$

e contribuisce al Potenziale interno tramite:

$$
V_C^{(t+1)}(u) \leftarrow V_C^{(t+1)}(u) + \sum_{\zeta} \mathbf{1}_{\{u = \zeta\}}\, z_{\zeta}^{(t)} + \beta_{\mathrm{lat}} \sum_{\zeta} \left[R_{\zeta}^+(u) - R_{\zeta}^-(u)\right] z_{\zeta}^{(t)}.
$$

L'influenza dinamica di $\zeta$ deve essere **intensiva**, non estensiva. Le masse migrate $g_{\zeta}^{\pm}$ (\cref{sec:8-2-6}) crescono con l'intera storia degli episodi fondativi: usarle come spinta dinamica farebbe iniettare a un concetto consolidato un potenziale enorme, polverizzando la sorgente $\alpha S_C$ e la propagazione $\beta\mathbf{J}$ e facendo divergere la costante di Lipschitz --- lo stesso errore che il modello evita normalizzando $\mathbf{M}$ in $\mathbf{J}$ tramite i gradi $\mathbf{D}_M$. Poiché i caricamenti $R_{\zeta}^{\pm}$ sono già distribuzioni normalizzate, l'accoppiamento dinamico passa per una costante adimensionale $\beta_{\mathrm{lat}} \in (0,1)$, perfettamente analoga al $\beta$ della propagazione pairwise. Le masse $g_{\zeta}^{\pm}$ restano così confinate ai loro ruoli propri --- bilanciare l'energia migrata (8.2.6) e pesare l'apoptosi (8.6) --- e non entrano mai nella spinta dinamica attiva.

Le somme su $\zeta$ corrono sulle sole **cause comuni aggregative**, le uniche unità dotate di attivazione $z_{\zeta}$ e di caricamenti $(R_{\zeta}^+, R_{\zeta}^-)$; i nodi lessicali e i procuratori $v_u$ non vi compaiono. Il primo termine, $\sum_{\zeta}\mathbf{1}_{\{u=\zeta\}} z_{\zeta}^{(t)}$ (in forma vettoriale $\sum_{\zeta} \mathbf{e}_{\zeta} z_{\zeta}^{(t)}$), è la **sorgente endogena** dell'unità latente stessa, ed è indispensabile. Senza di esso il nodo $\zeta$ non riceverebbe alcuna forzante --- non ha caricamento su se stesso ($R_{\zeta}^+(\zeta) = 0$), non riceve la sorgente esterna ($S_C(\zeta) = 0$, essendo latente) e alla nascita non ha righe in $\mathbf{J}$ --- sicché $V_C(\zeta)$ resterebbe rigorosamente nullo e $\zeta$ sarebbe un fantasma: capace di iniettare energia nel nucleo, ma privo di corpo fenomenologico, invisibile al taglio di Autoconsistenza Entropica. Iniettando lo scatto $z_{\zeta}$ nel proprio Potenziale, $\zeta$ si materializza nel Campo ($\Psi_C(\zeta) > 0$ quando scatta), può sopravvivere al taglio, diventare Pivot e accumulare archi pairwise verso nodi esterni: è questa la condizione che rende possibile l'emancipazione relazionale postulata in 8.2.8. Si noti che $z_{\zeta}$ dipende dal Campo del nucleo, non da $\Psi_C(\zeta)$, sicché l'iniezione non crea alcun anello di auto-amplificazione attraverso la soglia.

Questo contributo si affianca al termine di propagazione pairwise $\beta \mathbf{J} \Psi_C^{(t)}$. La sua presenza non lascia invariata la condizione di contrazione della \cref{sec:9}: pur essendo $\varphi$ non-espansiva, il termine latente introduce un guadagno proprio. La mappa iterativa completa diventa

$$
F(V) = (1-\gamma)V + \alpha S_C + \beta \mathbf{J}\,\mathrm{ReLU}(V) + \sum_{\zeta} \big(\mathbf{e}_{\zeta} + \beta_{\mathrm{lat}} R_{\zeta}^+ - \beta_{\mathrm{lat}} R_{\zeta}^-\big)\, \varphi\!\left(\langle R_{\zeta}^+ - R_{\zeta}^-,\, \mathrm{ReLU}(V)\rangle - \theta_{\zeta}^{\mathrm{att}}\right),
$$

la cui costante di Lipschitz latente è limitata da

$$
L_{\zeta} \leq \sum_{\zeta} \big\lVert \mathbf{e}_{\zeta} + \beta_{\mathrm{lat}}\big(R_{\zeta}^+ - R_{\zeta}^-\big) \big\rVert \cdot \big\lVert R_{\zeta}^+ - R_{\zeta}^- \big\rVert.
$$

Il versore $\mathbf{e}_{\zeta}$ rende esplicita, in forma vettoriale, la sorgente endogena $z_{\zeta}$ che materializza l'unità nel Campo; poiché $\mathbf{e}_{\zeta}$ è ortogonale al supporto di $R_{\zeta}^+ - R_{\zeta}^-$ (l'unità non appartiene al proprio nucleo), la norma resta limitata da $\sqrt{1 + \beta_{\mathrm{lat}}^2 \lVert R_{\zeta}^+ - R_{\zeta}^- \rVert^2}$.

La dinamica resta dunque una contrazione globale a condizione che le unità latenti consumino solo parte del margine già disponibile:

$$
(1-\gamma) + \beta \lVert \mathbf{J} \rVert + L_{\zeta} < 1.
$$

Valutando il bound nella stessa norma indotta $L^\infty$ della mappa globale (massima somma assoluta per righe) e usando $\lVert R_{\zeta}^+ \rVert_1 = \lVert R_{\zeta}^- \rVert_1 = 1$ con $\lVert \mathbf{e}_{\zeta} \rVert_1 = 1$, l'impatto di $K$ cause latenti simultaneamente attive su un singolo nodo è limitato da

$$
L_{\zeta} \leq 2 L_{\varphi}\, K \max(1, \beta_{\mathrm{lat}}).
$$

La contrazione $(1-\gamma)+\beta+L_{\zeta}<1$ impone allora un tetto al numero di cause latenti contemporaneamente attive:

$$
K < \frac{\gamma - \beta}{2 L_{\varphi} \max(1, \beta_{\mathrm{lat}})}.
$$

La disuguaglianza è un **limite di capacità inferenziale** del mezzo: la dinamica non può sostenere un numero arbitrario di cause latenti simultaneamente attive, e il budget dipende dal margine fra dissipazione $\gamma$ e propagazione orizzontale $\beta$. Il risultato fornisce un fondamento termodinamico-strutturale alla limitatezza della memoria di lavoro, in analogia con i limiti di capacità classici della cognizione (Legge di Miller), qui derivati non per postulato ma dalla contrattività del grafo.

La funzione $\varphi$ non è una singola funzione fissata ma una **famiglia ammissibile**, caratterizzata da: (i) $\varphi(x) = 0$ per $x \leq 0$ (silenzio sotto soglia); (ii) $\varphi(x) \geq 0$; (iii) non-linearità, con monotonia non-decrescente per $x > 0$ (così da escludere funzioni a gradino od oscillanti, che violerebbero la limitatezza della costante di Lipschitz); (iv) Lipschitz con costante $L_{\varphi}$ controllata; (v) non-espansività nel caso canonico, $L_{\varphi} \leq 1$. Lo "scatto unitario" va inteso come l'innesco a soglia (transizione netta da inattivo ad attivo), non come un salto discontinuo: la scelta entro la famiglia --- da una rettificazione $\varphi(x) = \max(0,x)$, che lascia una penombra graduale, a una saturazione $\varphi(x) = \min(1, \max(0,x))$, che impone uno scatto netto --- governa quanto bruscamente la causa latente si attiva. Si osservi che la non-negatività $z_{\zeta}^{(t)} \geq 0$ non interviene nella contrattività, la quale dipende dalla non-espansività e non dal segno dell'attivazione. L’inibizione prodotta da $R_{\zeta}^-$ agisce confinata all’interno di $V_C$, rispettando lo scisma epistemologico: il Campo osservabile $\Psi_C = \max(0, V_C)$ rimane non-negativo.

La soglia $\theta_{\zeta}^{\mathrm{att}}$ è endogena, ma non va posta sulla *media* delle attivazioni storiche: una soglia sulla media renderebbe il concetto cieco alla metà più debole dei propri episodi fondativi, distruggendone il recall a priori. La soglia deve invece mappare il **confine di fase** che ha definito la famiglia. Poiché $\mathcal{H}_{\zeta}$ è limitata inferiormente dal taglio $\rho_i \geq \varepsilon^{*}(\rho)$ (\cref{sec:8-2-5}) e l'attivazione $\langle R_{\zeta}^+, a_i\rangle$ è monotona nella risonanza $\rho_i$, la soglia si pone all'attivazione del membro di confine della famiglia:

$$
\theta_{\zeta}^{\mathrm{att}} = \min_{\chi_i \in \mathcal{H}_{\zeta}} \big(\langle R_{\zeta}^+, a_i\rangle - \langle R_{\zeta}^-, a_i\rangle\big),
$$

definita sulla risonanza *netta* $\langle R_{\zeta}^+, a_i\rangle - \langle R_{\zeta}^-, a_i\rangle$ (coerente con l'argomento della soglia in $z_{\zeta}$, che è netto), è immagine nello spazio dell'attivazione della soglia di risonanza $\varepsilon^{*}(\rho)$. Si usa il confine (il minimo sulla famiglia) e non la media: una soglia sulla media renderebbe $\zeta$ cieca alla metà più debole dei propri episodi fondativi. Includere il lato inibitorio garantisce inoltre la specificità --- un ingresso ricco di contenuto antagonista, pur attivando i nodi del nucleo, ha risonanza netta bassa e non innesca $\zeta$. Così $\zeta$ scatta per ogni ingresso almeno tanto risonante quanto il più debole episodio storicamente validato, garantendo il richiamo fenomenologico sull'intero supporto della famiglia e, al contempo, la specificità al di sotto di tale confine. La soglia di attivazione dinamica $\theta_{\zeta}^{\mathrm{att}}$ resta concettualmente distinta dalla soglia $\varepsilon^{*}(\hat{R}_{\zeta}^+)$ applicata alla loading per estrarre il nucleo (\cref{sec:8-2-5}): la prima vive nello spazio dell'attivazione dinamica, la seconda in quello della partecipazione storica.


## Sinergia neuro-simbolica: integrazione con i Large Language Models {#sec:10}

L’obiettivo della presente teoria non è porsi in contrapposizione alle moderne architetture basate su reti neurali profonde, e in particolare ai Large Language Models. Al contrario, la Teoria dello Spazio Semantico Continuo può essere intesa come uno strato complementare: una memoria semantica persistente, topologica e ispezionabile, capace di accumulare evidenza oltre la finestra di contesto senza richiedere l’aggiornamento diretto dei pesi neurali del modello.

I moderni LLM eccellono nell’estrazione di pattern contestuali, sintattici e pragmatici. Tuttavia, la loro ontologia operativa è in larga parte incorporata nei pesi pre-addestrati. Se un LLM incontra ripetutamente un neologismo, o deve operare una disambiguazione specifica per l’esperienza di un singolo utente, non può alterare stabilmente la propria struttura interna senza ricorrere a processi di fine-tuning, con costi e rischi di sovrascrittura, oppure affidarsi a database documentali esterni, che restano spesso memorie passive non fuse topologicamente con il modello generativo.

In un’architettura ibrida neuro-simbolica, LLM e TSSC possono assolvere funzioni complementari:

1. **LLM come corteccia fenomenologica.** La rete neurale agisce come interfaccia percettiva e linguistica. Di fronte a un input, l’LLM ne processa la sintassi, il contesto e l’attenzione semantica. Questo stato, proiettato su un vocabolario d’interfaccia, costituisce la **Sorgente Semantica** $S_C$.

2. **TSSC come memoria episodico-semantica.** L’innesco di $S_C$ attiva la dinamica nel mezzo persistente $\mathcal{G}$. Attraverso il Nodo Contesto Transitorio $\chi$, introdotto nel regime parametrico, il TSSC congela temporaneamente l’episodio, misura attivazioni $\mathcal{A}_C^*$, soppressioni $\mathcal{S}_C^*$, tensioni negative e nuclei trasformativi.

3. **Accumulo oltre la finestra di contesto.** Mentre l’LLM tratta l’episodio entro i limiti della propria finestra operativa, il TSSC conserva nel tempo le evidenze negli accumulatori duali $c^+$ e $c^-$. Il sistema può alterare le matrici $\mathbf{M}$ e $\mathbf{W}$, costruendo una memoria semantica a lungo termine personalizzata a dimensionalità inizialmente costante.

4. **Adattamento persistente senza retropropagazione neurale.** Se il sistema rileva tensioni di taglio irrisolte, può applicare una Mitosi Semantica; se riscontra lacune ricorrenti, può promuovere un Nodo Ombra. L’evoluzione ontogenetica del mezzo consente un adattamento persistente senza riscrivere direttamente i pesi del modello neurale.

In fase di output, il Campo Osservabile $\Psi_C$ del mezzo può essere retro-iniettato nell’LLM tramite prompt conditioning, retrieval strutturato, vincoli simbolici o modulazione dei logit. In questo modo, la generazione può essere orientata da traiettorie semantiche validate dalla topologia persistente del mezzo.

Questa integrazione non garantisce la piena interpretabilità dell’intero sistema ibrido, poiché la componente neurale resta opaca nei propri meccanismi interni. Tuttavia, rende auditabile la componente simbolico-topologica della decisione semantica: il sistema può ricondurre una modulazione dell’output alla genealogia dei campi, degli accumulatori, delle tensioni e delle trasformazioni ontogenetiche che l’hanno prodotta. In tal senso, la TSSC può potenzialmente ridurre derive allucinatorie di natura puramente associativa e aumentare la tracciabilità causale della memoria semantica utilizzata dal modello.

Il rapporto tra LLM e TSSC non è quindi di sostituzione, ma di complementarità architetturale. L’LLM fornisce fluidità linguistica e potenza inferenziale contestuale; il TSSC fornisce persistenza, plasticità ontogenetica e ispezionabilità topologica. Il primo eccelle nel generare stati fluidi; il secondo decide quali tracce meritino di sedimentare come struttura.


## Limiti computazionali e sviluppi futuri {#sec:11}

La conversione di un impianto teorico rigoroso in una piattaforma computazionale operante pone sfide implementative non banali. Queste sfide non indeboliscono la teoria, ma ne definiscono il programma di ricerca futuro.

### Costo computazionale della fase di ricottura {#sec:11-1}

La ricottura sistemica che governa il cold start non è un limite ma una scelta architetturale, trattata in 8.9 come raffreddamento endogeno delle soglie ontogenetiche. Sul piano computazionale essa ha un solo costo proprio: nella fase di burn-in il mezzo accumula evidenza episodica a pieno ritmo pur sopprimendo le trasformazioni strutturali, sicché per un transitorio iniziale si paga il costo dell'aggiornamento episodico e parametrico senza ancora beneficiare della compressione dimensionale che l'ontogenesi produrrà a maturità. Il transitorio è limitato: la temperatura $\mathcal{A}_{\mathrm{ann}}$ decade man mano che la struttura locale si stabilizza, e con essa il sovraccarico.

### Scalabilità e sparsità computazionale {#sec:11-2}

Il secondo limite risiede nella scalabilità algoritmica. In un sistema semantico maturo con un vocabolario di centinaia di migliaia di unità, una propagazione ingenua sull'intera matrice densa richiederebbe risorse di ordine quadratico $\mathcal{O}(N^2)$.

Tuttavia, l'architettura fornisce una via d'uscita algoritmica endogena: il taglio operato dalla Soglia $\varepsilon^{*}$ agisce come un meccanismo di *sparsificazione radicale*. Poiché la termodinamica confina la maggioranza del campo sotto la soglia fenomenologica, il vettore osservabile $\Psi_C$ risulta estremamente sparso. L'aggiornamento iterativo non richiede quindi moltiplicazioni dense, ma può essere risolto tramite operazioni **SpMV (Sparse Matrix-Vector multiplication)**. Questo abbatte la complessità da quadratica a **sub-quadratica, con un costo $\mathcal{O}(\mathrm{nnz})$ strettamente proporzionale al numero di archi (elementi non nulli) incidenti sul Supporto Attivo locale**, non al vocabolario complessivo.

Le implementazioni future dovranno quindi ricorrere a propagazione locale e politiche di attivazione circoscritte (dinamiche $k$-hop) attorno a $S_C$, aggiornando solo la regione del mezzo effettivamente perturbata. Questa limitazione non è soltanto computazionale, ma teorica: un evento semantico non dovrebbe necessariamente scuotere l’intera ontologia a ogni passo. La località dinamica è quindi al tempo stesso una necessità ingegneristica e una proprietà coerente con l’idea di campo perturbativo.

### Vocabulary Impedance e problema dell’ancoraggio {#sec:11-3}

Un limite particolarmente delicato riguarda la **Vocabulary Impedance**, cioè la non coincidenza tra i token sub-word usati dagli LLM e il vocabolario concettuale macroscopico $\mathcal{V}$ del mezzo continuo.

I tokenizer moderni operano spesso tramite unità sub-lessicali, come BPE o WordPiece. Il mezzo TSSC, invece, richiede nodi semanticamente interpretabili: concetti, unità mentali, aggregati, lacune, Pivot e forme emergenti. La proiezione tra questi due livelli non è banale.

Il problema dell’ancoraggio ha due direzioni:

1. **Proiezione dall’LLM al TSSC.** Lo stato contestuale del modello deve essere trasformato in una sorgente $S_C$ distribuita su $\mathcal{V}$. Questo richiede mappe stabili tra embedding, attention pattern, token, entità e nodi semantici persistenti.

2. **Retro-iniezione dal TSSC all’LLM.** Il Campo Osservabile $\Psi_C$ deve poter modulare la generazione neurale senza degradare la fluidità linguistica. Questa retro-iniezione può avvenire tramite prompt conditioning, retrieval strutturato, logit bias, memoria esterna o vincoli simbolici.

La qualità di questa interfaccia determinerà gran parte della riuscita applicativa del modello ibrido. Una TSSC formalmente elegante ma mal ancorata al sistema neurale rischierebbe di produrre una memoria interpretabile ma poco efficace. Viceversa, un ancoraggio stabile potrebbe trasformare il mezzo in una vera memoria semantica persistente sopra la dinamica fluida dell’LLM.

### Omeostasi dei parametri e stabilità ontogenetica {#sec:11-4}

La teoria mira a eliminare le soglie semantiche assolute, sostituendole con supporti autoconsistenti generati da campi diagnostici. Ciò non significa, tuttavia, eliminare ogni parametro. Restano necessari parametri sistemici come fattori di decadimento $\lambda$, tassi di apprendimento $\eta$, coefficienti di policy $\alpha$, dissipazione $\gamma$ e accoppiamento $\beta$.

Questi parametri non decidono dall’esterno che cosa conti come significato. Definiscono invece la fisica del mezzo: memoria, viscosità, plasticità, dissipazione, prudenza e velocità di adattamento. Il problema futuro non sarà dunque giustificare soglie semantiche arbitrarie, ma progettare un’omeostasi dei parametri sistemici.

Un sistema troppo plastico genererà ontogenesi premature, mitosi eccessive e coalescenze instabili. Un sistema troppo viscoso diventerà incapace di adattarsi a regolarità nuove. La stabilità ontogenetica richiederà quindi meccanismi di autoregolazione che modulino $\lambda$, $\eta$, $\gamma$ e $\beta$ in funzione dell’età del grafo, della densità del mezzo, della frequenza delle perturbazioni e della qualità degli esiti trasformativi.

Questa omeostasi rappresenta uno dei problemi più importanti per passare dalla teoria alla simulazione.

### Protocolli di valutazione empirica {#sec:11-5}

Infine, la teoria necessita di una validazione empirica rigorosa. Il passo successivo più immediato sarà la costruzione di un **Toy Model simulativo** capace di dimostrare algebricamente il ciclo di vita di una perturbazione: sorgente, propagazione, campo osservabile, supporto attivo, soppressione, tensione di taglio, trasformazione parametrica e, nei casi estremi, Mitosi Semantica o Genesi per lacuna.

Successivamente, sarà necessario definire benchmark oggettivi per valutare:

- mitigazione del catastrophic forgetting;
- apprendimento continuo su flussi non stazionari;
- disambiguazione semantica a lungo termine;
- gestione di neologismi e concetti emergenti;
- interpretabilità genealogica delle trasformazioni;
- qualità dell’integrazione con modelli neurali pre-addestrati.

La TSSC non deve essere valutata soltanto come modello di classificazione o retrieval. Il suo obiettivo è più specifico: mostrare se una memoria semantica topologica, dinamica e ontogenetica possa fornire capacità persistenti che le architetture neurali standard non possiedono nativamente.


## Tesi conclusiva {#sec:12}

Il significato non è una mappa inerte del mondo, né una coordinata congelata in uno spazio latente passivo. Il significato è un **evento di campo**: lo stato distribuito, firmato e misurabile che prende forma quando la variabilità inesauribile dell’esperienza entra in collisione con l’architettura di una memoria strutturata.

La Teoria dello Spazio Semantico Continuo mostra come, assumendo l’evento come oggetto primario dell’analisi, diventi possibile ripensare l’apprendimento semantico computazionale. Separando l’arena invisibile del Potenziale conflittuale dalla superficie fenomenologica del Campo osservabile, attraverso la topologia duale di $\mathbf{M}$ e $\mathbf{W}$, la teoria permette di calcolare non soltanto l’eccitazione associativa, ma anche l’inibizione, la frustrazione e il silenzio generato dalla soppressione attiva.

Ma la vera intelligenza di un sistema non si manifesta solo nella sua capacità di interpretare un evento. Si manifesta nella capacità di lasciarsi riprogettare dall’evento stesso. Introducendo la Trasformazione Parametrica e l’Ontogenesi Semantica, la teoria delinea un meccanismo formale con cui un sistema artificiale può superare i limiti di un vocabolario linguistico statico. Generando sintesi aggregative, scindendo unità frustrate, assimilando lacune d’interfaccia, fondendo ridondanze e archiviando ciò che è inerte, il sistema coltiva un lessico mentale autonomo, forgiato dalla storia dinamica dei propri fallimenti e delle proprie disambiguazioni.

In un’epoca dominata da intelligenze artificiali estremamente potenti ma concettualmente rigide nel loro assetto post-addestramento, la presente teoria propone un’infrastruttura topologica viva: un mezzo capace di conservare, trasformare e rendere ispezionabile la propria storia semantica. Il suo contributo non consiste nel sostituire le architetture neurali, ma nel fornire un possibile principio complementare per sistemi artificiali capaci di evoluzione semantica persistente, misurabile e interpretabile.

Il risultato più netto riguarda la natura del lessico interno. Esso non nasce dalla compressione degli episodi, ma dalla loro incapacità ricorrente di essere assorbiti a dimensionalità costante. L'episodio resta traccia storica ($\chi \neq \zeta$); il bacino sedimentato non è ancora un concetto ($B_{\zeta} \neq \zeta$); e l'unità latente aggregativa non è un centroide ($\zeta \neq$ centroide), ma una causa comune non-lineare dotata di soglia, completamento e soppressione selettiva. Solo quando un bacino positivo e conflittuale può essere spiegato da una tale causa, il sistema ne autorizza il commit. La mente interna non archivia semplicemente ciò che ha visto: costruisce operatori capaci di riconoscere ciò che manca.


## Riferimenti Bibliografici {.unnumbered}

- Aerts, D., Broekaert, J., Gabora, L., & Sozzo, S. (2013). Quantum structure and human thought. *Behavioral and Brain Sciences*, 36(3), 274-276.
- Anderson, J. R. (1983). *The Architecture of Cognition*. Harvard University Press.
- Brown, T., et al. (2020). Language models are few-shot learners. *NeurIPS*, 33, 1877-1901.
- Collins, A. M., & Loftus, E. F. (1975). A spreading-activation theory of semantic processing. *Psychological Review*, 82(6), 407-428.
- Fauconnier, G., & Turner, M. (1998). Conceptual integration networks. *Cognitive Science*, 22(2), 133-187.
- Firth, J. R. (1957). A synopsis of linguistic theory, 1930-1955. *Studies in Linguistic Analysis*.
- Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.
- Kipf, T. N., & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. *ICLR*.
- Mikolov, T., et al. (2013). Distributed representations of words and phrases and their compositionality. *NeurIPS*, 26.
- Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. *EMNLP*, 1532-1543.
- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., & Monfardini, G. (2008). The graph neural network model. *IEEE Transactions on Neural Networks*, 20(1), 61-80.
- Vartziotis, D. (2012). *Semantic Field Theory: Mathematical Formulation and Algorithmic Implementation*.
- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS*, 30.
