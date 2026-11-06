---
id: "sql_052"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 52
source_url: "https://www.postgresql.org/about/press/presskit96/it"
language: "en"
retrieved_at: "2026-11-01 21:58:01"
content_hash: "71689f2d64675a71c6e16899a2c4001f1b64b4513f77e7d14328ae6ed6c31ae8"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit96/it

---

29 SETTEMBRE 2016: PostgreSQL 9.6, l'ultima versione del più avanzato database SQL open source, è stato rilasciato oggi dal PostgreSQL Global Development Group. Questa release migliora la scalabilità verticale e orizzontale di database con alti requisiti di performance. Le nuove funzionalità comprendono query parallele, maggior controllo nella replica sincrona, ricerche di frasi, oltre ai consueti miglioramenti in ambito di prestazioni e di usabilità.

**Scalabilità verticale tramite query parallele**

PostgreSQL 9.6 introduce il supporto per la parallelizzazione delle query, consentendo di sfruttare più processori di uno stesso server e di velocizzarne l'esecuzione. Questa release include il supporto per *sequential scan* di una tabella, *aggregazioni* e *join*.
A seconda del numero di processori a disposizione, la parallelizzazione può ridurre i tempi di esecuzione di query in ambito big data fino a 32 volte.


**Scalabilità orizzontale tramite replica sincrona e postgres\_fdw**

Sono state aggiunte due nuove opzioni alla replica sincrona di PostgreSQL che permettono di scalare le letture su più nodi di un cluster, assicurandone la consistenza fra loro. Finora non era possibile mantenere più repliche sincrone. Adesso, con l'introduzione della modalità 'remote\_apply', è possibile mantenere una vista consistente su più nodi. Tramite la replica sincrona, si potranno avere diversi nodi "identici" ed effettuare \*load balancing\* in lettura.

In aggiunta, postgres\_fdw, il driver per la federazione dei dati tra database PostgreSQL, permette adesso la propagazione (in gergo tecnico *"push down"*) di ordinamenti, *join* e aggiornamenti batch di dati sul server remoto. In questo modo, gli utenti potranno distribuire il carico su diversi nodi PostgreSQL. Presto queste operazioni saranno estese anche ad altri driver FDW.

"Grazie all'esecuzione remota di JOIN, UPDATE e DELETE, i *Foreign Data Wrapper* rappresentano adesso una soluzione completa per la distribuzione dei dati tra altri database e PostgreSQL. Per esempio, PostgreSQL può essere usato per gestire dati in ingresso verso due o più differenti tipi di database", ha detto Julyanto Sutandang, Direttore *Business Solution* di Equnix.

**Miglior ricerca testuale con le frasi**

Il *full text search* di PostgreSQL supporta adesso la ricerca a livello di "frase". Gli utenti saranno in grado di ricercare con *match* esatto intere frasi, oppure parole con una certa prossimità fra loro, usando la veloce indicizzazione GIN. Combinata con le nuove funzionalità di maggior controllo delle opzioni di ricerca testuale, PostgreSQL si conferma essere la prima scelta per "ricerche ibride" che includono l'approccio relazionale, NOSQL (col supporto JSON), e *full text*.

**Più armonioso, veloce e semplice da usare**

Grazie al feedback ricevuto dagli utenti che utilizzano in produzione database PostgreSQL su grandi volumi, questa nuova versione ha visto notevoli miglioramenti in termini di prestazioni e usabilità. Replica, aggregazioni, indicizzazioni, ordinamenti e procedure sono stati resi più efficienti. PostgreSQL adesso riesce a sfruttare meglio le risorse delle recenti versioni di kernel Linux. Anche l'impatto di amministrazione ordinaria di tabelle di grandi dimensioni e in presenza di carichi di lavoro complessi è stato ridotto, soprattutto attraverso il potenziamento del 'VACUUM'.

Per spiegazioni sulle funzionalità elencate sopra e per ulteriori informazioni, si rimanda alle seguenti risorse:

La documentazione in formato HTML ed il manuale in formato *man* sono installati contestualmente a PostgreSQL. Tuttavia è estremamente consigliato navigare, ricercare e lasciare commenti sulla [documentazione online](https://www.postgresql.org/docs/9.6/) interattiva.

PostgreSQL utilizza la [Licenza PostgreSQL](https://www.postgresql.org/about/licence), una licenza in stile BSD molto permissiva.
Questa [licenza certificata da OSI](http://www.opensource.org/licenses/postgresql) è unanimemente apprezzata per la sua natura flessibile e *business-friendly*, in quanto non limita l'impiego di PostgreSQL in applicazioni proprietarie e commerciali. Insieme al supporto multi-azienda ed alla proprietà diffusa e pubblica del codice, la nostra licenza rende PostgreSQL molto popolare con i *vendor* che intendono incorporare il database all'interno dei loro prodotti senza alcun timore di incappare in costi, forme di lock-in o cambi nei termini e nelle condizioni di licenza.

Riferimenti sul web

Contatto per la stampa

Gabriele Bartolini

[it@postgresql.org](mailto:it@postgresql.org)

Ufficio: +39 0574 159 3000

Mobile: +39 338 1566217

Tutti i logo sono disponibili per modifiche e redistribuzione secondo la "PostgreSQL License". Il nome ed il logo di PostgreSQL sono marchi registrati di "PostgreSQL Community Association of Canada".

PostgreSQL è il principale sistema di gestione di database open source, con una comunità internazionale costituita da migliaia di utenti e sviluppatori nonché decine di aziende ed enti provenienti da tutte le parti del mondo. Il progetto PostgreSQL si porta dietro oltre 25 anni di attività di ingegneria del software, a partire dal campus di Berkeley dell'Università di California, ed oggi può vantare un ritmo di sviluppo senza uguali. La gamma di funzionalità mature messe a disposizione da PostgreSQL non soltanto è in grado di competere con quelle offerte da sistemi di database proprietari, ma le migliora in termini  di funzionalità avanzate, estensibilità, sicurezza e stabilità. Scopri maggiori informazioni su PostgreSQL e partecipa attivamente alla nostra comunità sul sito [PostgreSQL.org](https://www.postgresql.org) e, per l'Italia, [ITPUG](http://www.itpug.org).

"In qualità di *chief database architect* per Synthetic Genomics, sono rimasto oltremodo stupito dalla potenza, dalla flessibilità e dalla ricchezza di interfacce di programmazione per PostgreSQL 9.5. Abbiamo migrato la totalità dei genomi immagazzinati nella nostra piattaforma - complessivamente 25 miliardi di righe in MySQL - su di un singolo database PostgreSQL, sfruttando la possibilità di compressione dello spazio occupato dalle righe (grazie al tipo di dato 'JSONB' e alle eccellenti indicizzazioni 'GIN', 'BRIN' e 'B-tree') e l'incredibilmente esteso linguaggio di programmazione PL/pgSQL per le *stored procedure*. Adesso, con la versione 9.6, mi aspetto di sfruttare a pieno le query parallele ed aumentare così la scalabilità del nostro database, composto da tabelle piuttosto grandi. PostgreSQL 9.5 ha dimostrato di essere estremamente stabile, di avere prestazioni considerevoli, e di essere in questo momento, almeno secondo la mia opinione, il miglior motore sul mercato per la memorizzazione ibrida di dati relazionali e non strutturati", ha detto Mike Sofen, Chief Database Architect di Synthetic Genomics.

[Synthetic Genomics, Inc.](https://www.syntheticgenomics.com/) (SGI) è leader mondiale nel campo della biologia sintetica.
Contatto in inglese: [media@syntheticgenomics.com](mailto:media@syntheticgenomics.com).

[Equnix](http://www.equnix.co.id/) è un provider di soluzioni IT per aziende che si basa su ricerca, sviluppo e open source. Equnix è un'azienda che supporta PostgreSQL. Contatto in inglese: [Info@equnix.co.id](mailto:info@equnix.co.id).

PostgreSQL gode del supporto di tante aziende pronte a sponsorizzare sviluppatori, a fornire servizi di hosting e a contribuire economicamente al progetto. Il sito comprende una [pagina di sponsor](https://www.postgresql.org/about/sponsors/) principali del progetto PostgreSQL.

Esiste anche un vasto gruppo di [aziende che offrono supporto professionale a PostgreSQL](https://www.postgresql.org/support/professional_support), da liberi professionisti e consulenti fino a aziende multinazionali.

[Donazioni](https://www.postgresql.org/about/donate) sono bene accette e gradite.

Oppure potete acquistare il nostro elegante merchandise dal nostro [Zazzle PostgreSQL Store](http://www.zazzle.com/postgresql).