---
id: "sql_040"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 40
source_url: "https://www.postgresql.org/about/press/presskit13/he"
language: "en"
retrieved_at: "2026-11-01 21:57:08"
content_hash: "2b99642cb284c3f0fecf79732df09e8cc46b0cf10608b5c30cbaa860936293af"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit13/he

---

קבוצת הפיתוח הגלובלית של PostgreSQL הודיעה היום על שחרורה של
  [PostgreSQL 13](https://www.postgresql.org/docs/13/release-13.html)
  , הגרסה העדכנית ביותר של
   [מסד הנתונים המתקדם בעולם עם קוד פתוח](https://www.postgresql.org/) 

PostgreSQL 13 כולל שיפורים משמעותיים במערכת האינדקסים ומנועי חיפוש אשר מוסיפים יתרונות למסדי נתונים גדולים, כולל חיסכון באחסון שיפורי ביצועים לאינדקסים, זמני ביצוע מהירים יותר לשאילתות המשתמשות באגרגטים או מחיצות, תכנון שאילתות טוב יותר בעת שימוש בסטטיסטיקה משופרת ועוד.

לצד תכונות מבוקשות מאוד כמו
   [parallelized vacuuming](https://www.postgresql.org/docs/13/sql-vacuum.html) 
  ו
   [incremental sorting](https://www.postgresql.org/docs/13/runtime-config-query.html#GUC-ENABLE-INCREMENTAL-SORT) 
  מערכת מספקת חוויית ניהול נתונים טובה יותר לעומסי עבודה גדולים וקטנים, עם אופטימיזציות לניהול יומיומי, יותר נוחות למפתחי אפליקציות ושיפור האבטחה.

"PostgreSQL 13 מציגה את שיתוף הפעולה והמסירות של הקהילה הגלובלית שלנו לקידום היכולות של מסד נתונים יחסיים עם קוד פתוח המתקדם ביותר בעולם," אמר Peter Eisentraut, חבר בצוות הליבה של PostgreSQL. "החידושים שכל מהדורה מביאה יחד עם המוניטין שלה כאמינות ויציבות הם הסיבות לכך שאנשים רבים יותר בוחרים להשתמש ב- PostgreSQL עבור היישומים שלהם."

 [PostgreSQL](https://www.postgresql.org) 
  זאת מערכת ניהול נתונים חדשנית הידועה באמינותה ובחוסנה, נהנית ממעל 25 שנות פיתוח קוד פתוח מ
   [קהילת מפתחים עולמית](https://www.postgresql.org/community) 
  והפכה לבסיס נתונים רלציוני הפתוח המועדף על ארגונים מכל הגדלים.

בהתבסס על עבודה מהמהדורה הקודמת, PostgreSQL 13 יכולה לטפל ביעילות ב
   [נתונים כפולים ב B-tree אינדקסים](https://www.postgresql.org/docs/13/btree-implementation.html#BTREE-DEDUPLICATION) 
  , האינדקס הסטנדרטי של מסד הנתונים. זה מקטין את גודל האחסון שדרוש לאינדקס B-tree תוך שיפור ביצועי השאילתות הכוללים.

PostgreSQL 13 מציגה מיון מצטבר, כאשר נתונים ממוינים בשלב מוקדם בשאילתה ויכולים להאיץ את המיון בשלב מאוחר יותר. בנוסף, PostgreSQL יכולה כעת להשתמש
   [בסטטיסטיקה המורחבת](https://www.postgresql.org/docs/13/planner-stats.html#PLANNER-STATS-EXTENDED) 
   (נגישה באמצעות
   [\`CREATE STATISTICS\`](https://www.postgresql.org/docs/13/sql-createstatistics.html) 
  ) כדי ליצור תוכניות משופרות לשאילתות עם סעיפי 'OR' וחיפושים 'IN' / 'ANY' על פני רשימות.

ב- PostgreSQL 13, סוגים נוספים של
   [aggregate](https://www.postgresql.org/docs/13/functions-aggregate.htm) 
  ו
   [grouping set](https://www.postgresql.org/docs/13/queries-table-expressions.html#QUERIES-GROUPING-SETS) 
  כאשר שאילתות יכולות למנף את הפונקציונליות של hash aggregation יעילה של PostgreSQL, שכן שאילתות עם אגרגטים גדולים אינן צריכות להשתלב לחלוטין בזיכרון. שאילתות עם
   [partitioned tables](https://www.postgresql.org/docs/13/ddl-partitioning.htm) 
  קיבלו שיפור ביצועים, מכיוון שכעת ישנם מקרים נוספים בהם ניתן לגזום מחיצות ולחבר ישירות את המחיצות.

 [Vacuuming](https://www.postgresql.org/docs/13/routine-vacuuming.html) 
  הוא חלק חיוני בניהול של PostgreSQL, המאפשר לבסיס הנתונים להחזיר שטח אחסון לאחר עדכון ומחיקה של שורות. תהליך זה יכול גם להציב אתגרים ניהוליים, אם כי מהדורות קודמות של PostgreSQL עשו עבודה בכדי להקל על פעולה זו.

PostgreSQL 13 ממשיך לשפר את מערכת vacuuming עם
   [הכנסת vacuuming מקביל לאינדקסי](https://www.postgresql.org/docs/13/sql-vacuum.html) 
  . בנוסף ליתרונות ביצועי vacuuming שהיא מציעה, ניתן לכוון את השימוש בתכונה חדשה זו לעומסי עבודה ספציפיים שכן DBA יכולים לבחור את מספר תהליכים מקבילים להפעלה. בנוסף ליתרונות הביצועים הללו, הוספות נתונים יכולות כעת להפעיל את תהליך autovacuum.

 [Replication slots](https://www.postgresql.org/docs/13/warm-standby.html#STREAMING-REPLICATION-SLOTSl) 
   המשמשות למניעת הסרת WAL לפני שהתקבלו על ידי רפליקה, ניתנים לכוון ב- PostgreSQL 13 כדי לציין את
   [המספר המרבי של קבצי WAL שישמרו](https://www.postgresql.org/docs/13/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE) 
   לסייע למנוע שגיאות הקשורות לזמינות מקום בדיסק.

PostgreSQL 13 מוסיף גם דרכים נוספות שמנהל מערכת יכול להשתמש על מנת לפקח על פעילות מסדי נתונים, הכולל הפניה לסטטיסטיקה של שימוש ב- WAL מ- 'EXPLAIN', התקדמות streaming base backups והתקדמות פקודות ANALYZE. בנוסף, ניתן לבדוק את תקינות הפלט של הפקודה
   [\`pg\_basebackup\`](https://www.postgresql.org/docs/13/app-pgbasebackup.html) 
  באמצעות הפקודה החדשה
   [\`pg\_verifybackup\`](https://www.postgresql.org/docs/13/app-pgverifybackup.html) 
  .

PostgreSQL 13 מקל עוד יותר על העבודה עם סוגי נתונים של PostgreSQL המגיעים ממקורות נתונים שונים. מהדורה זו מוסיפה את הפונקציה
   [\`datetime()\`](https://www.postgresql.org/docs/13/functions-json.html#FUNCTIONS-SQLJSON-OP-TABLE) 
  לתמיכת ב SQL/JSON path שלה, אשר ממירה פורמטים תקפים של זמן (למשל
  מחרוזות ISO 8601) לסוגים מקוריים של PostgreSQL. בנוסף, פונקציית
   [\`gen\_random\_uuid()\`](https://www.postgresql.org/docs/13/functions-uuid.html) 
  ליצירה של UUID v4, זמינה כעת ללא צורך בהתקנת תוסף כלשהו.

מערכת חלוקת הטבלאות של PostgreSQL הפכה להיות גמישה יותר, מכיוון שטבלאות מחולקות תומכות באופן מלא ברפליקציה לוגית וBEFORE row-level triggers.

התחביר
   [\`FETCH FIRST\`](https://www.postgresql.org/docs/13/sql-select.html#SQL-LIMIT) 
   ב- PostgreSQL 13 מורחב כעת לכלול את הסעיף 'WITH TIES'. כאשר צוין, 'WITH TIES' כולל כל הרשומות , בהתבסס על סעיף 'ORDER BY',  אשר 'מקושרות' עם הרשומה האחרונה בסט התוצאות.

מערכת ההרחבות של PostgreSQL היא מרכיב מרכזי בחוסן שלה מכיוון שהיא מאפשרת למפתחים להרחיב את הפונקציונליות שלה. במהדורות קודמות, רק משתמש-על של מסד נתונים יכל היה להתקין הרחבות חדשות. כדי להקל על ניצול תכונה זו PostgreSQL 13 מוסיף את הרעיון של
   [trusted extension](https://www.postgresql.org/docs/13/sql-createextension.html) 
  , המאפשר למשתמשי מסד נתונים להתקין הרחבות שמשתמש-על סימן כ"אמינים". הרחבות מסוימות מובנות מסומנות ככה כברירת מחדל, כולל
   [\`pgcrypto\`](https://www.postgresql.org/docs/13/pgcrypto.html) 
   גם
   [\`tablefunc\`](https://www.postgresql.org/docs/13/tablefunc.html) 
  גם
   [\`hstore\`](https://www.postgresql.org/docs/13/hstore.html) 
   ואחרים.

עבור יישומים הדורשים שיטות אימות מאובטחות, PostgreSQL 13 מאפשר ללקוחות לדרוש
   [קשירת ערוצים](https://www.postgresql.org/docs/13/libpq-connect.html#LIBPQ-CONNECT-CHANNEL-BINDING) 
   בעת שימוש
   [באימות SCRAM](https://www.postgresql.org/docs/13/sasl-authentication.html#SASL-SCRAM-SHA-256) 
  .
  גם
   [עטיפת הנתונים הזרים](https://www.postgresql.org/docs/13/postgres-fdw.html) 
   של PostgreSQL יכולה כעת להשתמש באימות מבוסס תעודות.

 [PostgreSQL](https://www.postgresql.org/) 
  הוא מסד נתונים בקוד פתוח המתקדם ביותר בעולם, עם קהילה גלובלית של אלפי משתמשים, תורמים, חברות וארגונים. הפרויקט PostgreSQL נבנה על מעל 30 שנות הנדסה, החל באוניברסיטת קליפורניה, ברקלי, והמשיך להתפתח עם קצב ללא תחרות. ערכת התכונות הבשלות של PostgreSQL לא רק תואמת מערכות נתונים קנייניות מובילות, אלא עולה עליהן במאפיינים של מסדי נתונים מתקדמים ,הרחבה, אבטחה ויציבות.
  תרגומי הודעה לעיתונות

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