---
id: "sql_047"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 47
source_url: "https://www.postgresql.org/about/press/presskit18/id"
language: "en"
retrieved_at: "2026-11-01 21:57:46"
content_hash: "fe03b708da3375c2c419044be420f756dec124ee9f8dcf51960900e0bcde4f81"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit18/id

---

**25 September 2025** - [PostgreSQL Global Development Group](https://www.postgresql.org) hari ini mengumumkan perilisan [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html), versi terbaru dari database open source paling canggih di dunia.

PostgreSQL 18 meningkatkan performa untuk workload dengan berbagai skala melalui subsistem I/O baru yang telah menunjukkan peningkatan performa hingga 3× saat membaca dari storage, serta meningkatkan jumlah query yang dapat menggunakan indeks. Rilis ini membuat upgrade versi mayor menjadi lebih mulus, mempercepat waktu upgrade dan mengurangi waktu yang diperlukan untuk mencapai performa yang diharapkan setelah upgrade selesai. Developer juga mendapat manfaat dari fitur-fitur PostgreSQL 18, termasuk virtual generated columns yang menghitung nilai pada saat query dieksekusi, dan fungsi `uuidv7()` yang lebih ramah terhadap database serta memberikan performa indexing dan read yang lebih baik untuk UUID. PostgreSQL 18 juga mempermudah integrasi dengan sistem Single-Sign On (SSO) melalui dukungan autentikasi OAuth 2.0.

"Upaya komunitas Open Source global membentuk setiap rilis PostgreSQL dan membantu menghadirkan fitur yang relevan dengan kebutuhan pengguna di mana data mereka berada," ujar Jonathan Katz, anggota tim inti PostgreSQL. "PostgreSQL 18 dibangun berdasarkan proyek panjang dan kaya akan sejarah dalam menghadirkan pengalaman manajemen data yang andal dan kuat, sambil terus memperluas jenis workload yang dapat didukung."

PostgreSQL, sebuah sistem manajemen data inovatif yang dikenal karena keandalan, ketangguhan, dan ekstensibilitasnya, mendapat manfaat dari hampir 30 tahun pengembangan Open Source dari komunitas developer global dan telah menjadi database relasional Open Source pilihan untuk berbagai skala organisasi.

Sebelumnya, PostgreSQL mengandalkan mekanisme readahead pada sistem operasi untuk mempercepat pengambilan data. Namun, karena sistem operasi tidak mengenali pola akses spesifik database, sering kali data yang diperlukan tidak terantisipasi yang menyebabkan performa yang tidak optimal pada banyak workload.

PostgreSQL 18 memperkenalkan subsistem asynchronous I/O (AIO) baru yang dirancang untuk mengatasi keterbatasan ini. AIO memungkinkan PostgreSQL mengeluarkan beberapa permintaan I/O sekaligus alih-alih menunggu satu per satu selesai. Hal ini memperluas kemampuan readahead yang ada dan meningkatkan throughput keseluruhan. Operasi AIO yang didukung dalam PostgreSQL 18 meliputi sequential scan, bitmap heap scan, dan vacuum. Benchmarking telah menunjukkan peningkatan performa hingga 3x dalam skenario tertentu.

Pengaturan baru [`io_method`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-IO-METHOD) memungkinkan Anda memilih metode AIO, termasuk `worker` dan `io_uring`, atau tetap menggunakan metode PostgreSQL saat ini dengan pengaturan `sync`. Kini ada lebih banyak parameter yang perlu dipertimbangkan untuk tuning dengan AIO, yang dapat [Anda pelajari lebih lanjut dalam dokumentasi](https://www.postgresql.org/docs/18/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-IO).

Salah satu fitur kunci PostgreSQL adalah pembuatan dan penyimpanan [statistics](https://www.postgresql.org/docs/18/planner-stats.html) yang membantu PostgreSQL memilih query plan yang paling efisien. Sebelum PostgreSQL 18, statistics ini tidak terbawa saat [upgrade versi mayor](https://www.postgresql.org/docs/18/pgupgrade.html), yang dapat menyebabkan degradasi performa query signifikan pada sistem yang sibuk sampai [`ANALYZE`](https://www.postgresql.org/docs/18/sql-analyze.html) selesai berjalan. PostgreSQL 18 memperkenalkan kemampuan untuk mempertahankan statistics planner saat terjadi upgrade versi mayor, sehingga cluster yang di-upgrade dapat lebih cepat mencapai performa yang diharapkan.

Selain itu, [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html), utilitas yang melakukan upgrade versi mayor, menyertakan sejumlah peningkatan dalam PostgreSQL 18, antara lain upgrade yang lebih cepat ketika database berisi banyak objek seperti tabel dan sequence. Rilis ini juga memungkinkan `pg_upgrade` memproses pemeriksaannya secara paralel berdasarkan pengaturan flag `--jobs`, dan menambahkan flag `--swap` yang menukar direktori upgrade alih-alih menyalin, mengkloning, atau menghubungkan file.

PostgreSQL 18 semakin mempercepat performa query dengan fitur yang secara otomatis membuat workload Anda lebih cepat. Rilis ini memperkenalkan pencarian "skip scan" pada [indeks B-tree multikolom](https://www.postgresql.org/docs/18/indexes-multicolumn.html) yang meningkatkan waktu eksekusi untuk query tanpa kondisi `=` pada satu atau lebih kolom indeks prefiks. Lookup ini juga dapat mengoptimalkan query yang menggunakan kondisi `OR` dalam `WHERE` untuk menggunakan indeks, menghasilkan eksekusi yang jauh lebih cepat. Ada juga banyak peningkatan dalam cara PostgreSQL merencanakan dan mengeksekusi table join, mulai dari meningkatkan performa hash join hingga memungkinkan merge join menggunakan incremental sort. PostgreSQL 18 kini juga mendukung pembuatan paralel untuk [indeks GIN](https://www.postgresql.org/docs/18/gin.html), menyusul indeks B-tree dan [BRIN](https://www.postgresql.org/docs/current/brin.html) yang telah mendukung kapabilitas ini.

Rilis ini juga memperluas dukungan PostgreSQL untuk akselerasi hardware, termasuk dukungan intrinsik CPU ARM NEON dan SVE untuk fungsi `popcount` yang digunakan oleh [`bit_count`](https://www.postgresql.org/docs/18/functions-bitstring.html) dan kemampuan internal lainnya.

PostgreSQL 18 memperkenalkan [virtual generated columns](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-STORED) yang menghitung nilai pada saat query dijalankan alih-alih menyimpannya. Opsi ini kini menjadi default untuk generated columns. Selain itu, stored generated columns kini dapat direplikasi secara logical.

Rilis ini menambahkan kemampuan untuk mengakses nilai sebelumnya (`OLD`) dan nilai saat ini (`NEW`) dalam [klausa `RETURNING`](https://www.postgresql.org/docs/18/dml-returning.html) untuk perintah `INSERT`, `UPDATE`, `DELETE` dan `MERGE`. PostgreSQL 18 juga menambahkan pembuatan UUIDv7 melalui fungsi [`uuidv7()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE), memungkinkan Anda menghasilkan UUID acak yang diurutkan berdasarkan timestamp untuk mendukung strategi caching yang lebih baik. PostgreSQL 18 menyertakan [`uuidv4()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE) sebagai alias untuk `gen_random_uuid()`.

PostgreSQL 18 menambahkan [temporal constraints](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-UNIQUE) -- pembatasan atas rentang -- untuk constraint `PRIMARY KEY` dan `UNIQUE` menggunakan klausa `WITHOUT OVERLAPS`, dan pada constraint `FOREIGN KEY` menggunakan klausa `PERIOD`.

Akhirnya, PostgreSQL 18 memudahkan pembuatan definisi schema dari foreign table menggunakan definisi tabel lokal dengan perintah [`CREATE FOREIGN TABLE ... LIKE`](https://www.postgresql.org/docs/18/sql-createforeigntable.html).

PostgreSQL 18 membuat pemrosesan teks lebih mudah dan cepat dengan sejumlah peningkatan baru. Rilis ini menambahkan collation [`PG_UNICODE_FAST`](https://www.postgresql.org/docs/18/collation.html#COLLATION-MANAGING-STANDARD), yang menyediakan semantik Unicode penuh untuk transformasi huruf sambil membantu mempercepat banyak perbandingan. Hal ini mencakup fungsi perbandingan string `upper` dan `lower`, serta fungsi [`casefold`](https://www.postgresql.org/docs/18/functions-string.html#FUNCTIONS-STRING-OTHER) baru untuk perbandingan yang tidak peka besar-kecilnya huruf. Selain itu, PostgreSQL 18 sekarang mendukung perbandingan `LIKE` pada teks yang menggunakan [nondeterministic collation](https://www.postgresql.org/docs/18/collation.html#COLLATION-NONDETERMINISTIC), sehingga memudahkan pencocokan pola yang lebih kompleks. Rilis ini juga mengubah [full text search](https://www.postgresql.org/docs/18/textsearch.html) untuk menggunakan penyedia collation default (bawaan) dari cluster alih-alih selalu menggunakan libc, yang mungkin mengharuskan Anda untuk melakukan reindex pada semua indeks [full text search](https://www.postgresql.org/docs/18/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX) dan [`pg_trgm`](https://www.postgresql.org/docs/18/pgtrgm.html#PGTRGM-INDEX) setelah menjalankan [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html).

PostgreSQL 18 mendukung pelaporan konflik penulisan logical replication dalam log dan dalam tampilan [`pg_stat_subscription_stats`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-SUBSCRIPTION-STATS). Selain itu, [`CREATE SUBSCRIPTION`](https://www.postgresql.org/docs/18/sql-createsubscription.html) kini secara default menggunakan parallel streaming untuk menerapkan transaksi, yang dapat membantu meningkatkan performa. Utilitas [`pg_createsubscriber`](https://www.postgresql.org/docs/18/app-pgcreatesubscriber.html) sekarang memiliki flag `--all` sehingga Anda dapat membuat replika logical untuk semua database dalam instance dengan satu perintah. PostgreSQL 18 juga memungkinkan Anda secara otomatis [menghapus idle replication slot](https://www.postgresql.org/docs/18/runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT) untuk membantu mencegah penyimpanan terlalu banyak file write-ahead log pada publisher.

PostgreSQL 18 meningkatkan strategi [vacuum](https://www.postgresql.org/docs/18/routine-vacuuming.html) dengan secara proaktif membekukan lebih banyak halaman selama vacuum reguler, mengurangi overhead dan membantu dalam situasi yang memerlukan vacuum agresif.

PostgreSQL 18 menambahkan lebih banyak detail pada [`EXPLAIN`](https://www.postgresql.org/docs/18/using-explain.html), yang menyediakan informasi tentang eksekusi query plan, dan mulai rilis ini secara otomatis menampilkan berapa banyak buffer (unit fundamental dari penyimpanan data) yang diakses saat mengeksekusi `EXPLAIN ANALYZE`. Selain itu, `EXPLAIN ANALYZE` kini menunjukkan berapa banyak pencarian indeks (index lookup) yang terjadi selama index scan, dan `EXPLAIN ANALYZE VERBOSE` mencakup statistik CPU, WAL, dan rata-rata pembacaan (read). PostgreSQL 18 juga menambahkan lebih banyak informasi dalam [`pg_stat_all_tables`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW) mengenai waktu yang dihabiskan untuk vacuum dan operasi terkait, serta statistik per koneksi tentang pemanfaatan I/O dan WAL.

Database yang diinisialisasi dengan [`initdb`](https://www.postgresql.org/docs/18/app-initdb.html) PostgreSQL 18 sekarang memiliki page checksum yang aktif secara default. Hal ini dapat memengaruhi upgrade dari cluster tanpa checksum, yang akan mengharuskan Anda membuat cluster PostgreSQL 18 baru dengan opsi `--no-data-checksums` saat menggunakan [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html).

PostgreSQL 18 juga memperkenalkan PostgreSQL wire protocol 3.2, protokol versi terbaru pertama sejak PostgreSQL 7.4 (2003). [`libpq`](https://www.postgresql.org/docs/18/libpq-connect.html) masih menggunakan versi 3.0 secara default sementara client (seperti driver, pooler, proxy) menambahkan dukungan untuk versi protokol baru.

Banyak fitur dan peningkatan baru lainnya telah ditambahkan ke PostgreSQL 18 yang mungkin juga berguna untuk kasus penggunaan Anda. Silakan lihat [catatan rilis](https://www.postgresql.org/docs/18/release-18.html) untuk daftar lengkap fitur baru dan fitur yang diubah.

[PostgreSQL](https://www.postgresql.org) adalah database Open Source paling canggih di dunia, dengan komunitas global ribuan pengguna, kontributor, perusahaan, dan organisasi. Sejak awal dikembangkan di University of California, Berkeley lebih dari 40 tahun yang lalu, PostgreSQL terus berkembang dengan kecepatan yang tak tertandingi. Kumpulan fiturnya yang matang tidak hanya menyamai sistem database proprietary teratas, tetapi juga melampaui dalam hal fitur database tingkat lanjut, ekstensibilitas, keamanan, dan stabilitas.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

Untuk penjelasan fitur di atas dan lainnya, silakan lihat sumber-sumber berikut:

Ada beberapa cara Anda dapat mendownload PostgreSQL 18, termasuk:

Tool dan extension lainnya tersedia di [PostgreSQL Extension Network](http://pgxn.org/).

PostgreSQL 18 dilengkapi dengan dokumentasi HTML serta manual. Anda juga dapat menjelajahi dokumentasi secara online dalam format [HTML](https://www.postgresql.org/docs/18/) dan [PDF](https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-US.pdf).

PostgreSQL menggunakan [PostgreSQL License](https://www.postgresql.org/about/licence/), sebuah lisensi "permisif" yang mirip seperti BSD. [Lisensi bersertifikat OSI](http://www.opensource.org/licenses/postgresql/) ini sangat dihargai karena fleksibel dan ramah bisnis, tidak membatasi penggunaan PostgreSQL dengan aplikasi komersial dan proprietary. Bersama dengan dukungan dari berbagai perusahaan dan kepemilikan publik atas kode, lisensi kami membuat PostgreSQL sangat populer di kalangan vendor yang ingin menanamkan database dalam produk mereka sendiri tanpa khawatir akan biaya, vendor lock-in, atau perubahan ketentuan lisensi.

Website

Postgres, PostgreSQL, dan Logo Gajah (Slonik) semuanya merupakan merek dagang terdaftar dari [PostgreSQL Community Association](https://www.postgres.ca). Jika Anda ingin menggunakan merek ini, Anda harus mematuhi [kebijakan merek dagang](https://www.postgresql.org/about/policies/trademarks/).

PostgreSQL mendapat dukungan dari banyak perusahaan, yang mensponsori developer, menyediakan sumber daya hosting, dan memberikan dukungan finansial kepada kami. Lihat halaman [sponsor](https://www.postgresql.org/about/sponsors/) kami untuk beberapa pendukung proyek ini.

Ada juga komunitas besar [perusahaan yang menawarkan Dukungan PostgreSQL](https://www.postgresql.org/support/professional_support/), dari konsultan individu hingga perusahaan multinasional.

Jika Anda ingin memberikan kontribusi finansial kepada PostgreSQL Global Development Group atau salah satu organisasi nirlaba komunitas yang diakui, silakan kunjungi halaman [donasi](https://www.postgresql.org/about/donate/) kami.