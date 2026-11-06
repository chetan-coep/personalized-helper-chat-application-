---
id: "sql_042"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 42
source_url: "https://www.postgresql.org/about/press/presskit13/pl"
language: "en"
retrieved_at: "2026-11-01 21:57:26"
content_hash: "2b98f8ffbfc7c69a9508912204eda18270c8d3eec43afecb709d2de4fc2a3702"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit13/pl

---

**24 września 2020 —** Grupa PostgreSQL Global Development
  ogłosiła dzisiaj wydanie [PostgreSQL 13](https://www.postgresql.org/docs/13/release-13.html),
  najnowszej wersji [najbardziej zaawansowanej bazy danych open source](https://www.postgresql.org/).

PostgreSQL 13 zawiera znaczące ulepszenia systemów indeksowania i wyszukiwania, z których najbardziej skorzystają duże bazy danych, włączając w to m.in. oszczędność pamięci i lepszą wydajność indeksów, krótsze czasy odpowiedzi dla zapytań używających agregatów i partycji, a także lepsze planowanie zapytań dzięki rozszerzonym statystykom.

Wydanie to zawiera również bardzo oczekiwane funkcje, takie jak [równoległe czyszczenie (vacuum)](https://www.postgresql.org/docs/13/sql-vacuum.html)
  oraz [sortowanie przyrostowe](https://www.postgresql.org/docs/13/runtime-config-query.html#GUC-ENABLE-INCREMENTAL-SORT).
  PostgreSQL 13 zapewnia lepsze środowisko zarządzania danymi dla baz o dużym
  i małym obciążeniu, z optymalizacjami dla codziennego zarządzania bazami, a
  także więcej udogodnień dla twórców aplikacji oraz ulepszenia zabezpieczeń.

PostgreSQL 13 jest przykładem współpracy i zaangażowania naszej globalnej społeczności w rozwijaniu możliwości najbardziej zaawansowanej na świecie relacyjnej bazy danych typu open source" - powiedział Peter Eisentraut, członek zespołu PostgreSQL Core Team. "Innowacje, które niesie ze sobą każde wydanie, wraz z reputacją niezawodności i stabilności, jest powodem, dla którego coraz więcej osób decyduje się na używanie PostgreSQL w swoich aplikacjach.

[PostgreSQL](https://www.postgresql.org), to innowacyjny system
  zarządzania danymi znany ze swojej niezawodności i solidności. Rozwijany od
  ponad 25 lat jako open source przez [globalną społeczność programistów](https://www.postgresql.org/community/)
  stał się ulubioną relacyjną bazą danych open source wśród organizacji o różnej
  wielkości.

Kontynuując ulepszenia z poprzedniego wydania, PostgreSQL 13 może wydajnie obsługiwać
  [duplikowane dane w indeksach B-tree](https://www.postgresql.org/docs/13/btree-implementation.html#BTREE-DEDUPLICATION),
  które są standardowym typem indeksu. Dzięki temu zapotrzebowanie na pamięć
  używaną przez te indeksy zostało zmniejszone, co poprawia ogólną wydajność
  zapytań.

PostgreSQL 13 wprowadza sortowanie przyrostowe, w którym dane posortowane na
  wcześniejszym etapie wykonywania zapytania mogą zostać użyte do sortowania w
  późniejszym etapie. Dodatkowo PostgreSQL może teraz używać systemu
  [rozszerzonych statystyk](https://www.postgresql.org/docs/13/planner-stats.html#PLANNER-STATS-EXTENDED)
  (który jest dostępny poprzez [`CREATE STATISTICS`](https://www.postgresql.org/docs/13/sql-createstatistics.html)))
  do poprawienia planów zapytań wykorzystujących `OR` oraz w
  wyszukiwaniach `IN`/`ANY` działających na listach.

W PostgreSQL 13, więcej typów [agregatów](https://www.postgresql.org/docs/13/functions-aggregate.html)
  oraz [grupowania zbiorów](https://www.postgresql.org/docs/13/queries-table-expressions.html#QUERIES-GROUPING-SETS),
  może korzystać z wydajnej agregacji korzystającej z funkcji skrótu (hash
  aggregation), jako że zapytania z dużą liczbą agregatów nie muszą mieścić się
  całkowicie w pamięci. Zapytania z [partycjnowanymi tabelami](https://www.postgresql.org/docs/13/ddl-partitioning.html)
  zyskały lepszą wydajność dzięki zwiększeniu przypadków,
  w których partycje mogą być pominięte albo złączone.

[Czyszczenie (vacuum)](https://www.postgresql.org/docs/13/routine-vacuuming.html)
  jest istotną częścią administracji bazą PostgreSQL. Pozwala na odzyskanie miejsca
  zajmowanego przez zmienione albo usunięte wiersze. Proces ten również może być
  wyzwaniem dla administratorów, chociaż wcześniejsze wydania bazy PostgreSQL
  zmniejszały obciążenie związane z nim.

PostgreSQL 13 kontynuuje usprawnianie systemu czyszczenia poprzez wprowadzenie
  [równoległego czyszczenia dla indeksów](https://www.postgresql.org/docs/13/sql-vacuum.html).
  Poza zwiększoną wydajnością, użycie tej nowej funkcjonalności może być dostosowane
  do obciążenia bazy danych, ponieważ administratorzy mogą określić liczbę równolegle
  działających procesów. Dodatkowo, teraz wstawianie danych może również uruchamiać
  proces czyszczenia.

[Sloty replikacji](https://www.postgresql.org/docs/13/warm-standby.html#STREAMING-REPLICATION-SLOTS),
  używane do zapobiegania usuwania dzienników zapisu z
  wyprzedzeniem (write-ahead log - WAL) zanim otrzyma je replika bazy danych, mogą
  być dostosowane w PostgreSQL 13 poprzez określenie
  [maksymalnej liczby plików WAL do pozostawienia](https://www.postgresql.org/docs/13/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE),
  co pomoże w uniknięciu błędów zapełnienia dysku.

PostgreSQL 13 wprowadza również dodatkowe sposoby, dzięki którym administrator może
  monitorować aktywność bazy danych, włączając w to pokazanie statystyk użycia logów
  WAL w `EXPLAIN`, postęp strumieniowego robienia kopii bazy danych, a także postęp
  polecenia `ANALYZE`. Dodatkowo, można sprawdzić integralność
  działania polecenia [`pg_basebackup`](https://www.postgresql.org/docs/13/app-pgbasebackup.html)
  za pomocą nowego polecenia `pg_verifybackup`

PostgreSQL 13 pozwala na jeszcze łatwiejszą pracę z typami danych pochodzącymi z
  różnych źródeł. To wydanie dodaje funkcję
  [`datetime()`](https://www.postgresql.org/docs/13/functions-json.html#FUNCTIONS-SQLJSON-OP-TABLE)
  do zapytań używających ścieżek dla typu JSON (SQL/JSON path), która konwertuje
  różne typy czasu (np. w formacie ISO 8601) do wewnętrznych typów PostgreSQL.
  Dodatkowo, funkcja do generowania UUID v4 [`gen_random_uuid()`](https://www.postgresql.org/docs/13/functions-uuid.html)
  jest teraz dostępna bez potrzeby instalowania rozszerzeń.

System partycjonowania jest bardziej elastyczny, jako że partycjonowane tabele w pełni obsługują logiczną replikację oraz wyzwalacze wierszowe BEFORE.

Składnia [`FETCH FIRST`](https://www.postgresql.org/docs/13/sql-select.html#SQL-LIMIT) w
  PostgreSQL 13 jest rozszerzona i aktualnie zawiera klauzulę `WITH TIES`,
  która zawiera wszystkie wiersze, które, bazując na klauzuli `ORDER BY`,
  są związane z ostatnim wierszem wynikowego zbioru danych.

System rozszerzeń PostgreSQL jest kluczowym składnikiem stabilności bazy danych,
  jako że pozwala programistom rozszerzać jej funkcjonalność. W poprzednich wydaniach
  nowe rozszerzenia mogły być instalowane jedynie przez superużytkownika. W celu
  polepszenia rozszerzalności, PostgreSQL 13 dodaje koncepcję
  "[zaufanego rozszerzenia](https://www.postgresql.org/docs/13/sql-createextension.html)",
  która pozwala użytkownikom na instalowanie rozszerzeń, które zostały oznaczone
  przez superużytkownika jako "zaufane". Niektóre wbudowane rozszerzenia są domyślnie
  oznaczone jako zaufane, m.in.:
  [`pgcrypto`](https://www.postgresql.org/docs/13/pgcrypto.html),
  [`tablefunc`](https://www.postgresql.org/docs/13/tablefunc.html),
  [`hstore`](https://www.postgresql.org/docs/13/hstore.html).

Aplikacje, które wymagają bezpiecznego uwierzytelnienia, PostgreSQL 13 pozwala
  klientom na żądanie
  [channel binding](https://www.postgresql.org/docs/13/libpq-connect.html#LIBPQ-CONNECT-CHANNEL-BINDING)
  podczas używania
  [uwierzytelniania SCRAM](https://www.postgresql.org/docs/13/sasl-authentication.html#SASL-SCRAM-SHA-256).
  Dodatkowo, wrapper zewnętrznych danych PostgreSQL (foreign data wrapper)
  [`postgres_fdw`](https://www.postgresql.org/docs/13/postgres-fdw.html)
  może teraz korzystać z uwierzytelnienia opartego na certyfikatach.

[PostgreSQL](https://www.postgresql.org) to najbardziej zaawansowana baza danych
  open source na świecie, z globalną społecznością tysięcy użytkowników,
  współtwórców, firm i organizacji. PostgreSQL, bazujący na ponad trzydziestu latach
  pracy inżynierów, został zapoczątkowany na University of California w Berkeley.
  Późniejszy rozwój był kontynuowany z niezrównaną prędkością.
  Dojrzałe cechy PostgreSQLa nie tylko dorównują głównym komercyjnym systemom baz
  danych, ale w wielu przypadkach przewyższają je, jeśli chodzi o zaawansowane
  funkcjonalności, rozszerzalność, bezpieczeństwo i stabilność.

[PostgreSQL](https://www.postgresql.org) is the world's most
  advanced open source database, with a global community of thousands of users,
  contributors, companies and organizations. Built on over 30 years of
  engineering, starting at the University of California, Berkeley, PostgreSQL
  has continued with an unmatched pace of development. PostgreSQL's mature
  feature set not only matches top proprietary database systems, but exceeds
  them in advanced database features, extensibility, security, and stability.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

For explanations of the above features and others, please see the following resources:

There are several ways you can download PostgreSQL 13, including:

Other tools and extensions are available on the
  [PostgreSQL Extension Network](http://pgxn.org).

PostgreSQL 13 comes with HTML documentation HTML documentation as well as man
  pages, and you can also browse the documentation online in both
  [HTML](https://www.postgresql.org/docs/13/) and [PDF](https://www.postgresql.org/files/documentation/pdf/13/postgresql-13-US.pdf) formats.

PostgreSQL uses the [PostgreSQL License](https://www.postgresql.org/about/licence/), a
  BSD-like "permissive" license. This [OSI-certified license](http://www.opensource.org/licenses/postgresql/)
  is widely appreciated as flexible and business-friendly, since it does not
  restrict the use of PostgreSQL with commercial and proprietary applications.
  Together with multi-company support and public ownership of the code, our
  license makes PostgreSQL very popular with vendors wanting to embed a database
  in their own products without fear of fees, vendor lock-in, or changes in
  licensing terms.

Website

All logos are available for modification and redistribution under The
  [PostgreSQL Licence](https://www.postgresql.org/about/licence/).  The PostgreSQL name and
  logo are trademarks of The PostgreSQL Community Association of Canada.

PostgreSQL enjoys the support of numerous companies, who sponsor developers,
  provide hosting resources, and give us financial support.  See our
  [sponsors page](https://www.postgresql.org/about/sponsors/) for
  some of these project supporters.

There is also a large community of
  [companies offering PostgreSQL Support](https://www.postgresql.org/support/professional_support/)
  , from individual consultants to multinational companies.

If you wish to make a financial contribution to the PostgreSQL Global
  Development Group or one of the recognized community non-profit organizations,
  please visit our [donations](https://www.postgresql.org/about/donate/) page.