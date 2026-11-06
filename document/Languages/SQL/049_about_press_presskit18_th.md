---
id: "sql_049"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 49
source_url: "https://www.postgresql.org/about/press/presskit18/th"
language: "en"
retrieved_at: "2026-11-01 21:57:56"
content_hash: "61fcc3d7bb22876a94a8af8d807de3c80fbd30145752bb03b341a298b3be0a99"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit18/th

---

**25 กันยายน 2025** - [PostgreSQL Global Development Group](https://www.postgresql.org) วันนี้ประกาศการเปิดตัว [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html) เวอร์ชันล่าสุดของฐานข้อมูลโอเพนซอร์สที่ทันสมัยที่สุดในโลก

PostgreSQL 18 ปรับปรุงประสิทธิภาพสำหรับเวิร์กโหลดทุกขนาดผ่านระบบ I/O subsystem ใหม่ที่แสดงให้เห็นการปรับปรุงประสิทธิภาพสูงสุดถึง 3× เมื่ออ่านจากหน่วยเก็บข้อมูลและยังเพิ่มจำนวนกคิวรีที่สามารถใช้ดัชนีได้ การปล่อยเวอร์ชันใหม่นี้ทำให้การอัปเกรดเวอร์ชันหลักถูกรบกวนน้อยลง เร่งเวลา อัปเกรดและลดเวลาที่ต้องใช้เพื่อไปถึงประสิทธิภาพที่คาดหวังหลังจากอัปเกรดเสร็จสิ้น นักพัฒนายังได้รับประโยชน์จากฟีเจอร์ของ PostgreSQL 18 รวมถึงคอลัมน์ที่สร้างเสมือนที่คำนวณค่าในเวลาคิวรีและฟังก์ชัน `uuidv7()` ที่เป็นมิตรกับฐานข้อมูลซึ่งให้ประสิทธิภาพการจัดทำดัชนีและการอ่านที่ดีกว่าสำหรับ UUID PostgreSQL 18 ทำให้การผสมผสานรวมเข้ากับระบบ Single-Sign On (SSO) ง่ายขึ้นด้วยการรองรับ OAuth 2.0 Authentication

"ความพยายามของชุมชน Global Open Source ช่วยกำหนดทุกการปล่อย PostgreSQL และช่วยส่งมอบฟีเจอร์ที่ตอบสนองผู้ใช้ในที่ที่ข้อมูลของพวกเขาอยู่" โจนาธาน แคทซ์ สมาชิกทีมหลักของ PostgreSQL กล่าว "PostgreSQL 18 สร้างบนประวัติศาสตร์อันยาวนานและมั่งคั่งของโครงการในการส่งมอบประสบการณ์การจัดการข้อมูลที่เชื่อถือได้และแข็งแกร่ง ขณะเดียวกันยังคงขยายเวิร์กโหลดที่สามารถรองรับได้"

PostgreSQL ระบบจัดการข้อมูลเชิงนวัตกรรมที่ขึ้นชื่อเรื่องความเชื่อถือได้ ความทนทาน และความสามารถในการขยายได้รับประโยชน์จากการพัฒนาโอเพนซอร์สเกือบ 30 ปีจากชุมชนนักพัฒนาทั่วโลกและได้กลายเป็นฐานข้อมูลเชิงสัมพันธ์โอเพนซอร์สที่เป็นที่นิยมสำหรับองค์กรทุกขนาด

ก่อนหน้านี้ PostgreSQL อาศัย Operating System Readahead Mechanism เพื่อเร่งการเรียกข้อมูล อย่างไรก็ตาม เนื่องจากระบบปฏิบัติการขาดความเข้าใจในรูปแบบการเข้าถึงเฉพาะฐานข้อมูล พวกเขาจึงไม่สามารถคาดการณ์ข้อมูลที่จะต้องใช้ได้เสมอ ทำให้เกิดประสิทธิภาพที่ไม่เหมาะสมในเวิร์กโหลดหลายประเภท

PostgreSQL 18 แนะนำระบบ Asynchronous I/O (AIO) subsystem ใหม่ที่ออกแบบมาเพื่อจัดการกับข้อจำกัดนี้ AIO ให้ PostgreSQL ส่งคำขอ I/O หลายรายการพร้อมกันแทนที่จะรอให้แต่ละรายการเสร็จสิ้นตามลำดับ สิ่งนี้ขยายการอ่านล่วงหน้าที่มีอยู่และปรับปรุงปริมาณงานโดยรวม การดำเนินการ AIO ที่รองรับใน PostgreSQL 18 รวมถึง Sequential Scan, Bitmap Heap Scan และ Vacuum Benchmarking แสดงให้เห็นการเพิ่มประสิทธิภาพการทำงานสูงสุดถึง 3x ในบางสถานการณ์

การตั้งค่า [`io_method`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-IO-METHOD) ใหม่ให้คุณสลับระหว่างวิธี AIO รวมถึง `worker` และ `io_uring` หรือคุณสามารถเลือกรักษาพฤติกรรม PostgreSQL ปัจจุบันด้วยการตั้งค่า `sync` ตอนนี้มีตัวแปรกำหนดค่าเพิ่มเติมที่ต้องพิจารณาปรับแต่งกับ AIO ซึ่งคุณสามารถ[เรียนรู้เพิ่มเติมในเอกสารประกอบ](https://www.postgresql.org/docs/18/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-IO)

ฟีเจอร์สำคัญของ PostgreSQL คือการสร้างและจัดเก็บ[สถิติ](https://www.postgresql.org/docs/18/planner-stats.html)ที่ช่วย PostgreSQL เลือกแผนคิวรีที่มีประสิทธิภาพสูงสุด ก่อน PostgreSQL 18 สถิติเหล่านี้ไม่ถูกคงไว้ใน[อัปเกรดเวอร์ชันหลัก](https://www.postgresql.org/docs/18/pgupgrade.html) ซึ่งอาจทำให้ประสิทธิภาพของคิวรีลดลงอย่างมากในระบบไม่ว่างจนกว่า [`ANALYZE`](https://www.postgresql.org/docs/18/sql-analyze.html) จะทำงานเสร็จ PostgreSQL 18 แนะนำความสามารถในการเก็บแผนการวิเคราะห์ทางสถิติผ่านอัปเกรดเวอร์ชันหลักซึ่งช่วยให้คลัสเตอร์ที่อัปเกรดแล้วไปถึงประสิทธิภาพที่คาดหวังได้เร็วขึ้นหลังการอัปเกรด

นอกจากนี้ [`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html) ยูทิลิตี้ที่ทำ อัปเกรดเวอร์ชันหลักรวมการปรับปรุงหลายอย่างใน PostgreSQL 18 เช่น อัปเกรดที่เร็วขึ้นเมื่อฐานข้อมูลมีอ็อบเจ็กต์จำนวนมากเช่น ตารางและลำดับ เวอร์ชันนี้นี้ยังให้ `pg_upgrade` ประมวลผลการตรวจสอบแบบขนานตามการตั้งค่าของแฟล็ก `--jobs` และเพิ่มแฟล็ก `--swap` ที่สลับไดเรกทอรีอัปเกรดแทนการคัดลอก โคลน หรือเชื่อมโยงไฟล์

PostgreSQL 18 เร่งประสิทธิภาพกคิวรีเพิ่มเติมด้วยฟีเจอร์ที่ทำให้เวิร์กโหลดของคุณเร็วขึ้นโดยอัตโนมัติ เวอร์ชันนี้แนะนำการค้นหา "ข้ามสแกน" บน [Multicolumn B-tree Index](https://www.postgresql.org/docs/18/indexes-multicolumn.html)ที่ในการดำเนินการสำหรับการคิวรีที่ไม่มีเงื่อนไข `=` ในคอลัมน์ดัชนีคำนำหน้าหนึ่งหรือมากกว่า มันยังสามารถเพิ่มประสิทธิภาพคิวรีที่ใช้เงื่อนไข `OR` ใน `WHERE` เพื่อใช้ดัชนีทำให้การดำเนินการเร็วขึ้นอย่างมาก ยังมีการปรับปรุงมากมายในวิธีที่ PostgreSQL วางแผนและะดำเนินการการรวมตาราง ตั้งแต่เพิ่มประสิทธิภาพการรวมแฮช ไปจนถึงอนุญาตให้การรวมใช้การเรียงลำดับแบบเพิ่มหน่วย PostgreSQL 18 ยังรองรับการสร้างแบบคู่ขนานสำหรับ[ดัชนี GIN](https://www.postgresql.org/docs/18/gin.html) เข้าร่วมกับ B-tree และ[ดัชนี BRIN](https://www.postgresql.org/docs/current/brin.html)ในการรองรับความสามารถนี้

เวอร์ชันนี้ยังสร้างบนการรองรับ PostgreSQL สำหรับการเร่งความเร็วด้วยฮาร์ดแวร์รวมถึงการรองรับ ARM NEON และ SVE CPU intrinsic สำหรับฟังก์ชัน `popcount` ซึ่งใช้โดย [`bit_count`](https://www.postgresql.org/docs/18/functions-bitstring.html) และความสามารถภายในอื่น ๆ

PostgreSQL 18 แนะนำ[คอลัมน์ที่สร้างขึ้นเสมือน](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-STORED) ที่คำนวณค่าในเวลาคิวรีแทนที่จะเก็บไว้ ตอนนี้เป็นตัวเลือกเริ่มต้นสำหรับคอลัมน์ที่สร้างขึ้น นอกจากนี้คอลัมน์ที่สร้างขึ้นที่จัดเก็บไว้สามารถทำการจำลองแบบลอจิคัลได้อีกด้วย

เวอร์ชันนี้เพิ่มความสามารถในการเข้าถึงทั้งค่าก่อนหน้า (`OLD`) และค่าปัจจุบัน (`NEW`) ใน[คำสั่ง `RETURNING`](https://www.postgresql.org/docs/18/dml-returning.html) สำหรับคำสั่ง `INSERT`, `UPDATE`, `DELETE` และ `MERGE` นอกจากนี้ PostgreSQL 18 ยังเพิ่มการสร้าง UUIDv7 ผ่านฟังก์ชัน [`uuidv7()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE) ให้คุณคุณสร้าง UUID แบบสุ่มที่เรียงลำดับตามมค่าเวลาเเพื่อรองรับกลยุทธ์การแคชที่ดีกว่า PostgreSQL 18 ได้รวม[`uuidv4()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE) เป็นชื่อแทนสำหรับสำหรับ `gen_random_uuid()`

PostgreSQL 18 เพิ่มข้อจำกัดทางเวลา [temporal constraint](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-UNIQUE) -- ข้อจำกัดเหนือช่วง -- สำหรับทั้ง `PRIMARY KEY` และ `UNIQUE` constraint โดยใช้คำสั่ง `WITHOUT OVERLAPS` และในและข้อจำกัด `FOREIGN KEY` โดยใช้คำสั่ง `PERIOD`

สุดท้ายนี้ PostgreSQL 18 ทำให้การสร้างคำจำกัดความของโครงร่างของตารางภายนอกง่ายขึ้นโดยใช้คำจำกัดความของตารางภายในเครื่องด้วยคำสั่ง `CREATE FOREIGN TABLE ... LIKE`

PostgreSQL 18 ทำให้การประมวลผลข้อความง่ายและเร็วขึ้นด้วยการปรับปรุงใหม่หลายอย่าง เวอรํชันนี้ฟังก์ชันการจัดเรียงข้อมูล[`PG_UNICODE_FAST`](https://www.postgresql.org/docs/18/collation.html#COLLATION-MANAGING-STANDARD) ซึ่งให้ความหมาย Unicode เต็มรูปแบบสำหรับการแปลงตัวพิมพ์ใหญ่และเล็ก ขณะเดียวกันช่วยเร่งการเปรียบเทียบจำนวนมาก ซึ่งรวมถึงฟังก์ชันการเปรียบเทียบสตริง `upper` และ `lower` และฟังก์ชันใหม่[`casefold`](https://www.postgresql.org/docs/18/functions-string.html#FUNCTIONS-STRING-OTHER)สำหรับการเปรียบเทียบแบบไม่คำนึงถึงตัวพิมพ์ใหญ่และเล็ก นอกจากนี้ PostgreSQL 18 ตอนนี้รองรับการเปรียบเทียบแบบ `LIKE` บนข้อความที่ใช้[การจัดเรียงแบบไม่กำหนด](https://www.postgresql.org/docs/18/collation.html#COLLATION-NONDETERMINISTIC) ซึ่งทำให้วิธีการจับคู่รูปแบบที่ซับซ้อนยิ่งขึ้นง่ายขึ้น การเปิดตัวนี้ยังเปลี่ยนแปลงการค้นหาข้อความแบบเต็ม เวอร์ชันนี้ นี้ยังเปลี่ยน[การค้นหาข้อความแบบเต็ม](https://www.postgresql.org/docs/18/textsearch.html)ใเพื่อใช้ผู้ให้บริการการจัดเรียงเริ่มต้นของคลัสเตอร์แทนที่จะใช้ Libc เสมอ ซึ่งอาจต้องให้คุณสร้างดัชนีใหม่ทั้งหมด [การค้นหาข้อความแบบเต็ม](https://www.postgresql.org/docs/18/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX)และ[`pg_trgm`](https://www.postgresql.org/docs/18/pgtrgm.html#PGTRGM-INDEX) หลังจากรันดัชนี `pg_upgrade`

PostgreSQL 18 รองรับการรายงานข้อขัดแย้งในการเขียนข้อมูลการจำลองแบบลอจิคัลในบันทึกและในมุมมอง[`pg_stat_subscription_stats`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-SUBSCRIPTION-STATS) นอกจากนี้[`สร้างการสมัครสมาชิก`](https://www.postgresql.org/docs/18/sql-createsubscription.html)ตยังได้ตั้งค่าเริ่มต้นให้ใช้การสตรีมแบบขนานสำหรับการใช้ธุรกรรม ซึ่งจะช่วยปรับปรุงประสิทธิภาพการทำงาน ยูทิลิตี้ [`pg_createsubscriber`](https://www.postgresql.org/docs/18/app-pgcreatesubscriber.html) ตอนนี้มีแฟล็ก `--all` เพื่อให้คุณสร้าง สร้างแบบจำลองเชิงตรรกะสำหรับฐานข้อมูลทั้งหมดในอินสแตนซ์ได้ด้วยคำสั่งเดียว PostgreSQL 18 ยังให้คุณ[ลบสล็อตการจำลองแบบว่างโดยอัตโนมัติ](https://www.postgresql.org/docs/18/runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT) เพื่อช่วยป้องกันไม่ให้มีการจัดเก็บไฟล์บันทึกการเขียนล่วงหน้ามากเกินไปใน Publisher

PostgreSQL 18 ปรับปรุงกลยุทธ์ [การดูดสูญญากาศ](https://www.postgresql.org/docs/18/routine-vacuuming.html) โดยการแช่แข็งหน้าต่าง ๆ มากขึ้นหน้าเพิ่มเติมในระหว่างการดูดสูญญากาศปกติ ลดค่าใช้จ่าย และช่วยเหลือในสถานการณ์ที่ต้องใช้การดูดสูญญากาศอย่างเข้มงวด

PostgreSQL 18 เพิ่มรายละเอียดเพิ่มเติมให้[`EXPLAIN`](https://www.postgresql.org/docs/18/using-explain.html) ซึ่งให้ข้อมูลเกี่ยวกับการดำเนินการตามแผนคิวรีและตั้งแต่เวอร์ชันนี้เป็นต้นไป จะแสดงจำนวนบัฟเฟอร์ (หน่วยพื้นฐานของการจัดเก็บข้อมูล) ที่เข้าถึงโดยอัตโนมัติเมื่อดำเนินการ `EXPLAIN ANALYZE` นอกจากนี้ `EXPLAIN ANALYZE` ยังแสดงจำนวนการค้นหาดัชนีที่เกิดขึ้นระหว่างการสแกนดัชนี และ `EXPLAIN ANALYZE VERBOSE` ยังรวมสถิติการอ่าน CPU, WAL และค่าเฉลี่ย PostgreSQL 18 มีข้อมูลเพิ่มเติมใน [`pg_stat_all_tables`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW) เกี่ยวกับเวลาที่ใช้ในการล้างข้อมูลและการดำเนินการที่เกี่ยวข้อง รวมถึงสถิติการใช้งาน I/O และ WAL ต่อการเชื่อมต่อ

ฐานข้อมูลที่เริ่มต้นด้วย PostgreSQL 18 [`initdb`](https://www.postgresql.org/docs/18/app-initdb.html) จะมีการเปิดใช้งาน checksum ของหน้าไว้ตามค่าเริ่มต้น ซึ่งอาจส่งผลต่อการอัปเกรดจากคลัสเตอร์ที่ไม่ได้เปิดใช้งาน checksum ซึ่งคุณจะต้องสร้างคลัสเตอร์ PostgreSQL 18 ใหม่โดยใช้ตัวเลือก `--no-data-checksums` เมื่อใช้`pg_upgrade`

PostgreSQL 18 ยังได้แนะนำโปรโตคอล PostgreSQL wire เวอร์ชันใหม่ (3.2) ซึ่งเป็นเวอร์ชันโปรโตคอลใหม่เวอร์ชันแรกนับตั้งแต่ PostgreSQL 7.4 (2003) [`libpq`](https://www.postgresql.org/docs/18/libpq-connect.html) ยังคงใช้เวอร์ชัน 3.0 ตามค่าเริ่มต้น ในขณะที่ไคลเอนต์ (เช่น ไดรเวอร์ พูลเลอร์ พร็อกซี) เพิ่มการรองรับสำหรับเวอร์ชันโปรโตคอลใหม่

ฟีเจอร์และการปรับปรุงใหม่อื่น ๆ อีกมากมายได้ถูกเพิ่มเข้าใน PostgreSQL 18 ซึ่งอาจเป็นประโยชน์สำหรับการใช้งานของคุณ โปรดดู [หมายเหตุเวอร์ชันใหม่](https://www.postgresql.org/docs/18/release-18.html)เพื่อดูรายการฟีเจอร์ใหม่และฟีเจอร์ที่เปลี่ยนแปลงทั้งหมด

[PostgreSQL](https://www.postgresql.org) เป็นฐานข้อมูลโอเพนซอร์สที่ทันสมัยที่สุดในโลก มีชุมชนผู้ใช้ ผู้สนับสนุน บริษัท และองค์กรทั่วโลกหลายพันราย นับตั้งแต่ก่อตั้งที่มหาวิทยาลัยแคลิฟอร์เนีย เบิร์กลีย์ เมื่อกว่า 40 ปีที่แล้ว PostgreSQL ยังคงพัฒนาอย่างต่อเนื่องด้วยความเร็วที่ไม่มีใครเทียบได้ ชุดคุณสมบัติที่ครบครันของ PostgreSQL ไม่เพียงแต่เทียบเท่ากับระบบฐานข้อมูลที่เป็นกรรมสิทธิ์ชั้นนำเท่านั้น แต่ยังเหนือกว่าในด้านคุณสมบัติฐานข้อมูลขั้นสูง ความสามารถในการขยาย ความปลอดภัย และความเสถียรอีกด้วย

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

สำหรับคำอธิบายของฟีเจอร์ข้างต้นและอื่น ๆ โปรดดู resource ต่อไปนี้:

มีหลายวิธีที่คุณสามารถดาวน์โหลด PostgreSQL 18 รวมถึง:

มีเครื่องมือและส่วนขยายอื่น ๆ อยู่บน [เครือข่ายส่วนขยาย PostgreSQL](http://pgxn.org/)

PostgreSQL 18 มาพร้อมกับเอกสาร HTML เช่นเดียวกับหน้าคู่มือ และคุณยังสามารถเรียกดูเอกสารออนไลน์ได้ทั้งในรูปแบบ [HTML](https://www.postgresql.org/docs/18/) และ [PDF](https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-US.pdf)

PostgreSQL ใช้ [ใบอนุญาต PostgreSQL](https://www.postgresql.org/about/licence/) ซึ่งเป็นใบอนุญาตแบบ "อนุญาต" คล้ายกับ BSD ใบอนุญาต [ใบอนุญาตที่ได้รับการรับรอง OSI](http://www.opensource.org/licenses/postgresql/) นี้ได้รับการยอมรับอย่างกว้างขวางว่ามีความยืดหยุ่นและเป็นมิตรต่อธุรกิจ เนื่องจากไม่จำกัดการใช้ PostgreSQL กับแอปพลิเคชันเชิงพาณิชย์และแอปพลิเคชันที่เป็นกรรมสิทธิ์ ด้วยการสนับสนุนจากหลายบริษัทและการเป็นเจ้าของโค้ดโดยสาธารณะ ใบอนุญาตของเราจึงทำให้ PostgreSQL เป็นที่นิยมอย่างมากในหมู่ผู้จำหน่ายที่ต้องการฝังฐานข้อมูลในผลิตภัณฑ์ของตนเอง โดยไม่ต้องกลัวค่าธรรมเนียม การผูกขาดกับผู้จำหน่าย หรือการเปลี่ยนแปลงเงื่อนไขใบอนุญาต

เว็บไซต์

อีเมล

โลโก้ Postgres, PostgreSQL และ Elephant (Slonik) ล้วนเป็นเครื่องหมายการค้าจดทะเบียนของ [PostgreSQL Community Association](https://www.postgres.ca) หากท่านต้องการใช้เครื่องหมายเหล่านี้ ท่านต้องปฏิบัติตาม [นโยบายเครื่องหมายการค้า](https://www.postgresql.org/about/policies/trademarks/)

PostgreSQL ได้รับการสนับสนุนจากบริษัทมากมาย ทั้งผู้สนับสนุนนักพัฒนา ผู้ให้บริการโฮสติ้ง และการสนับสนุนทางการเงิน ดูรายชื่อผู้สนับสนุนโครงการเหล่านี้ได้ที่หน้า [ผู้สนับสนุน](https://www.postgresql.org/about/sponsors/)

นอกจากนี้ยังมีชุมชนขนาดใหญ่ของ [บริษัทต่างๆ ที่ให้การสนับสนุน PostgreSQL](https://www.postgresql.org/support/professional_support/) ตั้งแต่ที่ปรึกษาส่วนบุคคลไปจนถึงบริษัทข้ามชาติ

หากท่านต้องการบริจาคเงินให้กับ PostgreSQL Global Development Group หรือองค์กรไม่แสวงหาผลกำไรที่ได้รับการยอมรับในชุมชน โปรดเยี่ยมชมหน้า[การบริจาค](https://www.postgresql.org/about/donate/) ของเรา