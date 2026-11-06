---
id: "sql_048"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 48
source_url: "https://www.postgresql.org/about/press/presskit18/it"
language: "en"
retrieved_at: "2026-11-01 21:57:32"
content_hash: "2b9666f6f5180c659d0e973b672dc287a52be7a274f3d11111a6b55ba94953ed"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit18/it

---

**25 settembre 2025** - Il [PostgreSQL Global Development Group](https://www.postgresql.org) ha annunciato oggi il rilascio di [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html), l'ultima versione del database open source più avanzato al mondo.

PostgreSQL 18 migliora le prestazioni per carichi di lavoro di tutte le dimensioni attraverso un nuovo sottosistema di I/O che ha dimostrato miglioramenti delle prestazioni fino a 3× durante la lettura dallo storage, e aumenta inoltre il numero di query che possono utilizzare gli indici. Questa release rende gli upgrade di major version meno distruttivi, accelerando i tempi di aggiornamento e riducendo il tempo necessario per raggiungere le prestazioni attese dopo il completamento di un upgrade. Anche gli sviluppatori beneficiano delle funzionalità di PostgreSQL 18, tra cui colonne generate virtuali che calcolano i valori al momento della query e la funzione `uuidv7()` ottimizzata per il database che fornisce migliori prestazioni di indicizzazione e lettura per gli UUID. PostgreSQL 18 semplifica l'integrazione con i sistemi single-sign on (SSO) con il supporto per l'autenticazione OAuth 2.0.

"Lo sforzo della comunità open source globale plasma ogni release di PostgreSQL e aiuta a fornire funzionalità che incontrano le esigenze degli utenti dove risiedono i loro dati", ha dichiarato Jonathan Katz, membro del team core di PostgreSQL. "PostgreSQL 18 si basa sulla lunga e ricca storia del progetto nel fornire un'esperienza di gestione dei dati affidabile e robusta, continuando al contempo ad espandere i carichi di lavoro che può supportare."

PostgreSQL, un innovativo sistema di gestione dei dati noto per affidabilità, robustezza ed estendibilità, beneficia di quasi 30 anni di sviluppo open source da parte di una comunità mondiale di sviluppatori ed è diventato il database relazionale open source preferito da organizzazioni di tutte le dimensioni.

In passato PostgreSQL si affidava ai meccanismi di readahead del sistema operativo per accelerare il recupero dei dati. Tuttavia, poiché i sistemi operativi non hanno visibilità sui modelli di accesso specifici delle basi dati, non possono sempre anticipare quali dati saranno necessari, portando a prestazioni subottimali in molti carichi di lavoro.

PostgreSQL 18 introduce un nuovo sottosistema di I/O asincrono (AIO) progettato per affrontare questa limitazione. L'AIO consente a PostgreSQL di inviare più richieste I/O in parallelo invece di attendere che ciascuna termini in sequenza. Questo amplia il readahead esistente e migliora il throughput complessivo. Le operazioni AIO supportate in PostgreSQL 18 includono scansioni sequenziali, bitmap heap scans e vacuum. I benchmark hanno dimostrato guadagni di prestazioni fino a 3× in determinati scenari.

La nuova impostazione `io_method` permette di scegliere tra i metodi AIO, inclusi `worker` e `io_uring`, oppure è possibile mantenere il comportamento corrente di PostgreSQL con l'impostazione `sync`. Ci sono ora più parametri da considerare per il tuning con AIO, di cui puoi [informarti nella documentazione](https://www.postgresql.org/docs/18/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-IO).

Una caratteristica chiave di PostgreSQL è la generazione e la memorizzazione di [statistiche](https://www.postgresql.org/docs/18/planner-stats.html) che aiutano il planner di PostgreSQL a scegliere il piano di esecuzione più efficiente. Prima di PostgreSQL 18, queste statistiche non venivano mantenute durante un [major version upgrade](https://www.postgresql.org/docs/18/pgupgrade.html), il che poteva causare significative degradazioni delle prestazioni delle query su sistemi molto carichi fino al completamento dell'`ANALYZE`. PostgreSQL 18 introduce la possibilità di preservare le statistiche del planner durante un major upgrade, aiutando un cluster aggiornato a raggiungere più rapidamente le prestazioni attese.

Inoltre, `pg_upgrade`, l'utility che esegue gli upgrade di major version, include diversi miglioramenti in PostgreSQL 18, come upgrade più rapidi quando un database contiene molti oggetti (ad esempio tabelle e sequence). Questa release permette anche a `pg_upgrade` di eseguire i propri controlli in parallelo basandosi sull'impostazione del flag `--jobs`, e aggiunge il flag `--swap` che scambia le directory di upgrade invece di copiare, clonare o collegare i file.

PostgreSQL 18 accelera ulteriormente le prestazioni delle query con funzionalità che rendono i carichi di lavoro automaticamente più veloci. Questa release introduce ricerche "skip scan" sugli [indici B-tree multicolonna](https://www.postgresql.org/docs/18/indexes-multicolumn.html) che migliorano i tempi di esecuzione per query che omettono una condizione `=` su una o più colonne prefisso dell'indice. Può inoltre ottimizzare query che utilizzano condizioni `OR` in una clausola `WHERE` per sfruttare un indice, portando a esecuzioni significativamente più veloci. Ci sono anche numerosi miglioramenti nella pianificazione e nell'esecuzione delle join tra tabelle, dal potenziamento delle prestazioni delle hash join alla possibilità per le merge join di usare ordinamenti incrementali. PostgreSQL 18 supporta inoltre la costruzione parallela per gli [indici GIN](https://www.postgresql.org/docs/18/gin.html), unendo B-tree e [BRIN index](https://www.postgresql.org/docs/current/brin.html) nel supportare questa capacità.

Questa release amplia anche il supporto per l'accelerazione hardware, includendo il supporto per gli intrinsic CPU ARM NEON e SVE per la funzione `popcount`, che è utilizzata da `bit_count` e altre funzionalità interne.

PostgreSQL 18 introduce [colonne generate virtuali](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-STORED) che calcolano i valori al momento della query invece di memorizzarli. Questa è ora l'opzione predefinita per le colonne generate. Inoltre, le colonne generate memorizzate possono ora essere replicate logicamente.

Questa release aggiunge la possibilità di accedere sia ai valori precedenti (`OLD`) che ai valori correnti (`NEW`) nella clausola `RETURNING` per i comandi `INSERT`, `UPDATE`, `DELETE` e `MERGE`. PostgreSQL 18 aggiunge anche la generazione UUIDv7 tramite la funzione `uuidv7()`, permettendo di generare UUID casuali ordinati per timestamp per supportare strategie di caching migliori. PostgreSQL 18 include `uuidv4()` come alias per `gen_random_uuid()`.

PostgreSQL 18 aggiunge i [vincoli temporali](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-UNIQUE) — vincoli su intervalli — sia per i vincoli `PRIMARY KEY` che `UNIQUE` utilizzando la clausola `WITHOUT OVERLAPS`, e sui vincoli `FOREIGN KEY` utilizzando la clausola `PERIOD`.

Infine, PostgreSQL 18 facilita la creazione della definizione di schema di una foreign table usando la definizione di una tabella locale con il comando `CREATE FOREIGN TABLE ... LIKE`.

PostgreSQL 18 semplifica e accelera l'elaborazione del testo con diversi miglioramenti. Questa release aggiunge la collation `PG_UNICODE_FAST`, che fornisce piena semantica Unicode per le trasformazioni di case (maiuscole/minuscole) accelerando molte comparazioni. Questo include le funzioni di confronto `upper` e `lower` e la nuova funzione `casefold` per confronti case-insensitive. Inoltre, PostgreSQL 18 ora supporta le comparazioni `LIKE` su testi che utilizzano una collation nondeterministica, semplificando come eseguire confronti di pattern più complessi. Questa release cambia anche la ricerca full-text per usare il provider di collation predefinito di un cluster invece di usare sempre libc, il che potrebbe richiedere di reindicizzare tutti gli indici di ricerca full-text e gli indici `pg_trgm` dopo aver eseguito `pg_upgrade`.

PostgreSQL 18 introduce l'autenticazione `oauth`, che consente agli utenti di autenticarsi usando meccanismi OAuth 2.0 supportati tramite estensioni di PostgreSQL. Inoltre, PostgreSQL 18 include validazione per la [modalità FIPS](https://www.postgresql.org/docs/18/pgcrypto.html#PGCRYPTO-OPENSSL-SUPPORT-FUNCS) e aggiunge il parametro `ssl_tls13_ciphers` per configurare le suite di cipher TLS v1.3 lato server.

Questa release depreca l'autenticazione delle password basata su `md5`, che sarà rimossa in una release futura. Se necessiti dell'autenticazione tramite password in PostgreSQL, usa l'autenticazione `SCRAM`. PostgreSQL 18 supporta inoltre il passthrough SCRAM sia con `postgres_fdw` che con `dblink` per l'autenticazione verso istanze PostgreSQL remote. Inoltre, `pgcrypto` ora supporta SHA-2 per l'hashing delle password.

PostgreSQL 18 supporta la segnalazione dei conflitti di scrittura della replica logica nei log e nella vista `pg_stat_subscription_stats`. Inoltre, `CREATE SUBSCRIPTION` ora usa per impostazione predefinita lo streaming parallelo per l'applicazione delle transazioni, il che può aiutare a migliorare le prestazioni. L'utility `pg_createsubscriber` ora dispone del flag `--all` per creare repliche logiche per tutte le basi dati in un'istanza con un unico comando. PostgreSQL 18 consente anche di [eliminare automaticamente gli slot di replica inattivi](https://www.postgresql.org/docs/18/runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT) per aiutare a prevenire l'accumulo di troppi file WAL su un publisher.

PostgreSQL 18 migliora la strategia di `vacuum` congelando proattivamente più pagine durante i vacuum regolari, riducendo l'overhead e aiutando in situazioni che richiedono vacuum aggressivi.

PostgreSQL 18 aggiunge maggiori dettagli a `EXPLAIN`, che fornisce informazioni sull'esecuzione dei piani di query, e da questa release mostra automaticamente quante buffer (l'unità fondamentale di memorizzazione dei dati) vengono letti durante `EXPLAIN ANALYZE`. Inoltre, `EXPLAIN ANALYZE` ora mostra quante ricerche su indice si verificano durante una index scan, e `EXPLAIN ANALYZE VERBOSE` include statistiche medie su CPU, WAL e letture. PostgreSQL 18 include maggiori informazioni in `pg_stat_all_tables` sul tempo speso in vacuum e operazioni correlate, così come statistiche per connessione su I/O e utilizzo del WAL.

Le basi dati inizializzate con `initdb` di PostgreSQL 18 ora hanno i checksum delle pagine abilitati per impostazione predefinita. Questo può influenzare gli upgrade da cluster non abilitati ai checksum, nel qual caso potrebbe essere necessario creare un nuovo cluster PostgreSQL 18 con l'opzione `--no-data-checksums` quando si usa `pg_upgrade`.

PostgreSQL 18 introduce anche una nuova versione (3.2) del protocollo wire di PostgreSQL, la prima nuova versione del protocollo dalla 7.4 (2003). `libpq` continua a usare per default la versione 3.0 mentre i client (ad esempio driver, pooler, proxy) aggiungono il supporto per la nuova versione del protocollo.

Molte altre nuove funzionalità e miglioramenti sono state aggiunte a PostgreSQL 18 che potrebbero essere utili per i tuoi casi d'uso. Consulta le [note di rilascio](https://www.postgresql.org/docs/18/release-18.html) per l'elenco completo delle funzionalità nuove e cambiate.

[PostgreSQL](https://www.postgresql.org) è il database open source più avanzato al mondo, con una comunità globale di migliaia di utenti, contributori, aziende e organizzazioni. Dalle sue origini all'Università della California, Berkeley, oltre 40 anni fa, PostgreSQL ha continuato a svilupparsi a un ritmo ineguagliabile. L'insieme maturo di funzionalità di PostgreSQL non solo è paragonabile ai migliori sistemi database proprietari, ma li supera in funzionalità avanzate, estendibilità, sicurezza e stabilità.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

Per spiegazioni delle funzionalità sopra elencate e altre, consulta le seguenti risorse:

Ci sono diversi modi per scaricare PostgreSQL 18, tra cui:

Altri strumenti ed estensioni sono disponibili su [PostgreSQL Extension Network](http://pgxn.org/).

PostgreSQL 18 è fornito con documentazione HTML e pagine man, e puoi consultare la documentazione online sia in [HTML](https://www.postgresql.org/docs/18/) che in [PDF](https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-US.pdf).

PostgreSQL utilizza la [PostgreSQL License](https://www.postgresql.org/about/licence/), una licenza permissiva simile alla BSD. Questa [licenza certificata OSI](http://www.opensource.org/licenses/postgresql/) è apprezzata per la sua flessibilità e compatibilità con l'uso commerciale e proprietario. Insieme al supporto multi-azienda e alla proprietà pubblica del codice, la nostra licenza rende PostgreSQL molto popolare tra i vendor che desiderano includere un database nei loro prodotti senza timori di costi, lock-in o cambiamenti nelle condizioni di licenza.

Sito web

Postgres, PostgreSQL e l'elefante logo (Slonik) sono tutti marchi registrati della [PostgreSQL Community Association](https://www.postgres.ca). Se desideri utilizzare questi marchi, devi rispettare la [policy sui marchi](https://www.postgresql.org/about/policies/trademarks/).

PostgreSQL gode del supporto di numerose aziende, che sponsorizzano sviluppatori, forniscono risorse di hosting e offrono supporto finanziario. Consulta la pagina dei [sponsor](https://www.postgresql.org/about/sponsors/) per alcuni di questi sostenitori del progetto.

Esiste inoltre una vasta comunità di [aziende che offrono supporto PostgreSQL professionale](https://www.postgresql.org/support/professional_support/), da consulenti individuali a società multinazionali.

Se desideri effettuare un contributo finanziario al PostgreSQL Global Development Group o a una delle organizzazioni non-profit riconosciute dalla comunità, visita la pagina [donazioni](https://www.postgresql.org/about/donate/).