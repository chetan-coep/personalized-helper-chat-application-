---
id: "sql_041"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 41
source_url: "https://www.postgresql.org/about/press/presskit13/id"
language: "en"
retrieved_at: "2026-11-01 21:57:19"
content_hash: "81993ea66fd972ef134e9bfcd0b14fd9d810ccad321f981408b6af385b277d35"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit13/id

---

Grup PostgreSQL Global Development mengumumkan peluncuran
  [PostgreSQL 13](https://www.postgresql.org/docs/13/release-13.html), versi terbaru dari
  [database open source tercanggih](https://www.postgresql.org/) di dunia.

PostgreSQL 13 menyertakan peningkatan secara signifikan pada pengindeksan dan sistem pencarian yang sangat menguntungkan database berukuran besar, termasuk juga penghematan ruang penyimpanan dan peningkatan kinerja indeks, respon lebih cepat terhadap kueri yang menggunakan agregat atau partisi, perencanaan kueri yang lebih baik dengan menggunakan statistik yang disempurnakan, dan banyak lagi.

Bersama dengan fitur yang sudah ditunggu-tunggu seperti
  [proses vacuum secara parallel](https://www.postgresql.org/docs/13/sql-vacuum.html) dan
  [penyortiran bertahap](https://www.postgresql.org/docs/13/runtime-config-query.html#GUC-ENABLE-INCREMENTAL-SORT),
  PostgreSQL 13 memberikan pengalaman manajemen data yang lebih baik untuk beban
  kerja yang besar maupun kecil, beserta optimasi dalam administrasi harian,
  kemudahan untuk pengembang aplikasi dan berbagai peningkatan keamanan.

"PostgreSQL 13 menampilkan kolaborasi dan dedikasi komunitas global kami dalam memajukan kemampuan database relasional dan open source tercanggih di dunia", kata Peter Eisentraut, sebagai anggota tim inti PostgreSQL. "Inovasi dari setiap rilis bersama dengan reputasinya untuk keandalan dan stabilitas adalah alasan mengapa lebih banyak orang memilih untuk menggunakan PostgreSQL untuk aplikasi mereka".

[PostgreSQL](https://www.postgresql.org), sebuah sistem manajemen
  data yang inovatif dan diakui keandalan dan ketahanannya, telah memanfaatkan
  lebih dari 25 tahun pengembangan secara open source dari
  [global developer community](https://www.postgresql.org/community/) dan telah menjadi
  database relasional open source pilihan untuk semua bentuk organisasi.

Melalui pengembangan pekerjaan dari rilis PostgreSQL sebelumnya, PostgreSQL 13
  mampu menangani secara efisien
  [duplikat data pada B-tree indeks](https://www.postgresql.org/docs/13/btree-implementation.html#BTREE-DEDUPLICATION),
  yang merupakan indeks standard database. Dengan begitu, penggunaan keseluruhan
  ruang penyimpanan yang dibutuhkan B-tree indeks dapat berkurang sementara
  kinerja kueri secara keseluruhan semakin membaik.

PostgreSQL 13 memperkenalkan penyortiran inkremental, dimana di dalam sebuah
  kueri, data yang sudah diurutkan di langkah awal dapat mempercepat penyortiran
  di langkah selanjutnya. Selain itu, PostgreSQL dapat menggunakan sistem
  [statistik yang dilengkapi](https://www.postgresql.org/docs/13/planner-stats.html#PLANNER-STATS-EXTENDED)
  (diakses melalui [`CREATE STATISTICS`](https://www.postgresql.org/docs/13/sql-createstatistics.html))
  guna membuat rancangan yang lebih baik untuk kueri dengan klausa
  `OR` dan pencarian `IN` / `ANY` atas berbagai
  daftar.

Di dalam PostgreSQL 13, lebih banyak lagi tipe kueri
  [agregat](https://www.postgresql.org/docs/13/functions-aggregate.html) dan
  [kumpulan dari pengelompokan](https://www.postgresql.org/docs/13/queries-table-expressions.html#QUERIES-GROUPING-SETS)
  yang dapat memanfaatkan fungsionalitas agregasi hash yang efisien dari
  PostgreSQL. Hal ini dikarenakan kueri dengan agregat besar tidak harus
  sepenuhnya masuk ke dalam memori. Kueri dengan [tabel yang dipartisi](https://www.postgresql.org/docs/13/ddl-partitioning.html)
  telah memperoleh peningkatan kinerja, karena meningkatnya kasus dimana partisi
  dapat dipangkas dan dapat langsung digabungkan.

[Proses vacuum](https://www.postgresql.org/docs/13/routine-vacuuming.html) adalah bagian
  penting dari administrasi PostgreSQL, yang memungkinkan database untuk klaim
  ruang penyimpanan kembali setelah baris diperbarui dan dihapus. Proses ini
  masih menjadi tantangan administratif, meskipun rilis PostgreSQL sebelumnya
  telah berhasil meringankan overhead dari proses vacuum.

PostgreSQL 13 terus meningkatkan sistem vacuum dengan memperkenalkan
  [vacuum paralel untuk indeks](https://www.postgresql.org/docs/13/sql-vacuum.html). Selain
  meningkatkan kinerja dari proses vacuum, penggunaan dari fitur terbaru ini
  juga dapat disesuaikan terhadap beban kerja tertentu dengan cara memilih
  jumlah pekerja paralel yang ingin dijalankan. Selain manfaat kinerja sekarang
  adapun juga, penyisipan data dapat memicu proses autovacuum.

[Slot replikasi](https://www.postgresql.org/docs/13/warm-standby.html#STREAMING-REPLICATION-SLOTS),
  yang digunakan untuk mencegah Write-Ahead Logs (WAL) dihapus sebelum mereka
  diterima oleh replika, dapat dikonfigurasi di PostgreSQL 13 untuk menentukan
  [jumlah maksimum file WAL untuk disimpan](https://www.postgresql.org/docs/13/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE)
  dan membantu menghindari terjadinya penuhnya disk.

PostgreSQL 13 juga menambahkan lebih banyak cara bagi admin untuk memantau
  aktivitas database, termasuk mereferensikan statistik penggunaan WAL dari
  `EXPLAIN`, perkembangan streaming *base backup*, dan
  perkembangan perintah `ANALYZE`. Selain itu, integritas dari hasil
  perintah [`pg_basebackup`](https://www.postgresql.org/docs/13/app-pgbasebackup.html)
  dapat diperiksa menggunakan perintah baru yaitu
  [`pg_verifybackup`](https://www.postgresql.org/docs/13/app-pgverifybackup.html).

PostgreSQL 13 memudahkan untuk bekerja dengan tipe data PostgreSQL yang datang
  dari sumber data yang berbeda. Rilis ini menambahkan fungsi
  [`datetime()`](https://www.postgresql.org/docs/13/functions-json.html#FUNCTIONS-SQLJSON-OP-TABLE)
  ke dukungan jalur SQL/JSON-nya, guna mengubah format waktu yang valid
  (contohnya string ISO 8601) ke tipe natif PostgreSQL. Selain itu, fungsi
  generator UUID v4, [`gen_random_uuid()`](https://www.postgresql.org/docs/13/functions-uuid.html),
  sekarang tersedia tanpa harus memasang ekstensi apa pun.

Sistem partisi PostgreSQL sekarang lebih fleksibel, karena tabel yang dipartisi sepenuhnya mendukung logical replication dan trigger BEFORE di tingkat baris.

Sintaks [`FETCH FIRST`](https://www.postgresql.org/docs/13/sql-select.html#SQL-LIMIT)
  di PostgreSQL 13 sekarang diperluas untuk menyertakan klausa `WITH TIES`.
  Ketika ditentukan, `WITH TIES` akan menyertai baris yang "terikat"
  dengan baris terakhir dalam set hasil, berdasarkan klausa `ORDER BY`.

Sistem ekstensi PostgreSQL adalah kunci dari ketahanannya yang memungkinkan
  pengembang untuk memperluas fungsinya. Di dalam rilis sebelumnya, ekstensi
  baru hanya dapat dipasang oleh superuser database. Agar memudahkan pemanfaatan
  ekstensibilitas PostgreSQL, PostgreSQL 13 menambahkan konsep
  "[ekstensi tepercaya](https://www.postgresql.org/docs/13/sql-createextension.html)," yang
  memungkinkan pengguna database untuk memasang ekstensi yang ditandai oleh
  superuser sebagai "terpercaya." Adapula ekstensi bawaan yang sudah ditandai
  sebagai "terpercaya", termasuk [`pgcrypto`](https://www.postgresql.org/docs/13/pgcrypto.html),
  [`tablefunc`](https://www.postgresql.org/docs/13/tablefunc.html),
  [`hstore`](https://www.postgresql.org/docs/13/hstore.html), dan lainnya.

Untuk aplikasi yang membutuhkan metode otentikasi aman, PostgreSQL 13
  memperbolehkan klien untuk
  [meminta pengikatan saluran](https://www.postgresql.org/docs/13/libpq-connect.html#LIBPQ-CONNECT-CHANNEL-BINDING)
  saat menggunakan [otentikasi SCRAM](https://www.postgresql.org/docs/13/sasl-authentication.html#SASL-SCRAM-SHA-256),
  dan Foreign Data Wrapper PostgreSQL ([`postgres_fdw`](https://www.postgresql.org/docs/13/postgres-fdw.html))
  sekarang dapat menggunakan otentikasi berbasis sertifikat.

[PostgreSQL](https://www.postgresql.org) adalah database open
  source paling canggih di dunia, dengan komunitas global dari ribuan pengguna,
  kontributor, perusahaan dan organisasi. Dibangun melalui pengembangan selama
  lebih dari 30 tahun, dimulai di University of California, Berkeley, PostgreSQL
  telah berlangsung dengan kecepatan pengembangan yang tak tertandingi. Kumpulan
  fitur yang matang dari PostgreSQL tidak hanya bersaing dengan sistem database
  proprietary teratas, tetapi melampaui mereka dalam kecanggihan fitur database,
  ekstensibilitas, keamanan, dan stabilitas.

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