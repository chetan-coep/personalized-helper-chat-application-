---
id: "sql_046"
technology: "SQL"
category: "Languages"
title: "SQL"
doc_order: 46
source_url: "https://www.postgresql.org/about/press/presskit18/he"
language: "en"
retrieved_at: "2026-11-01 21:57:34"
content_hash: "cb29d7448b466b445e4538e58c5daf91091833eb6eaa2fba195342a26ee005c0"
---

# SQL

Source: https://www.postgresql.org/about/press/presskit18/he

---

25 בספטמבר 2025 – 
[קבוצת הפיתוח הגלובלית של PostgreSQL](https://www.postgresql.org)
מודיעה היום על שחרור 
[PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html)
,
הגרסה העדכנית ביותר של מסד הנתונים בקוד פתוח המתקדם בעולם.

PostgreSQL 18 משפרת את הביצועים עבור עומסי עבודה בכל הגדלים באמצעות תת־מערכת I/O חדשה,
שהדגימה שיפורי ביצועים של עד פ 3 בקריאות מהאחסון, ומגדילה גם את מספר השאילתות היכולות להשתמש באינדקסים.
מהדורה זו מצמצמת את ההפרעה בתהליכי שדרוג גרסה ראשית, מקצרת את זמני השדרוג ומפחיתה את הזמן הנדרש להגיע לביצועים הצפויים לאחר סיום השדרוג.
מפתחים מרוויחים מתכונות חדשות ב‑PostgreSQL 18, כולל עמודות מחושבות וירטואליות (Virtual Generated Columns) שמחשבות ערכים בזמן שאילתה,
ופונקציית
    `uuidv7()` 
הידידותית למסדי נתונים המספקת אינדוקס וקריאה מהירים יותר עבור UUID.
PostgreSQL 18 גם מקלה על אינטגרציה עם מערכות
SSO (Single‑Sign On)
    בעזרת תמיכה באימות OAuth 2.0.

"המאמץ של קהילת הקוד הפתוח הגלובלית מעצב כל מהדורה של PostgreSQL ועוזר לה לספק תכונות שמגיעות אל המשתמשים היכן שהנתונים שלהם נמצאים", אמר Jonathan Katz, חבר ב‑PostgreSQL Core Team. "PostgreSQL 18 נבנה על ההיסטוריה הארוכה והעשירה של הפרויקט במתן חוויית ניהול נתונים אמינה וחסינה, תוך המשך הרחבת מגוון עומסי העבודה שהוא יכול לתמוך בהם."

PostgreSQL זאת מערכת ניהול נתונים חדשנית הידועה באמינות, בחוסנה וביכולת הרחבה שלה, נהנית ממעל 25 שנות פיתוח קוד פתוח מקהילת המפתחים העולמית והפכה לבסיס נתונים רלציוני הפתוח המועדף על ארגונים מכל הגדלים.

PostgreSQL הסתמכה בעבר על מנגנוני readahead של מערכת ההפעלה כדי להאיץ שליפת נתונים. עם זאת, מכיוון שלמערכות ההפעלה אין ידע על דפוסי הגישה הייחודיים למסד הנתונים, הן אינן תמיד מסוגלות לצפות אילו נתונים יידרשו, מה שמוביל לביצועים פחות מיטביים תחת עומסי עבודה רבים.

PostgreSQL 18 מציגה תת־מערכת חדשה של קלט/פלט אסינכרוני (AIO) שנועדה לטפל במגבלה הזו.
AIO מאפשרת ל-PostgreSQL להנפיק כמה בקשות I/O במקביל, במקום להמתין שכל בקשה תסתיים ברצף. בכך היא מרחיבה את מנגנון ה-readahead הקיים ומשפרת את התפוקה הכוללת.
ב-PostgreSQL 18 נתמכות פעולות AIO כגון סריקות רציפות (sequential scans), סריקות bitmap של ערימת הטבלה (bitmap heap scans) ו-
    `VACUUM`
.
מדדי ביצועים הראו שיפורים של עד פי 3 בתרחישים מסוימים.

הגדרת
[`io_method`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-IO-METHOD)
החדשה מאפשרת לבחור בין שיטות AIO, כולל 
    `worker`
    ו-
    `io_uring`
, או לשמור על ההתנהגות הנוכחית של PostgreSQL באמצעות ההגדרה
    `sync`
.
כעת קיימים עוד פרמטרים שכדאי לשקול לכייל יחד עם AIO, ועליהם ניתן לקרוא ב
[תיעוד](https://www.postgresql.org/docs/18/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-IO).

מאפיין מרכזי ב‑PostgreSQL הוא יצירה ואחסון של 
[סטטיסטיקות](https://www.postgresql.org/docs/18/planner-stats.html)
המסייעות לבחור את תכנית השאילתה היעילה ביותר.
לפני PostgreSQL 18, סטטיסטיקות אלה לא נשמרו בעת 
[שדרוג גרסה ראשית](https://www.postgresql.org/docs/18/pgupgrade.html),
מה שעלול היה לגרום לירידה זמנית בביצועי שאילתות במערכות עמוסות עד לסיום
[`ANALYZE`](https://www.postgresql.org/docs/18/sql-analyze.html).
ב‑PostgreSQL 18 ניתן לשמר את סטטיסטיקות של המתכנן במהלך שדרוג גרסה ראשית, ובכך לסייע לבסיס הנתונים המשודרג להגיע מהר יותר לביצועים הצפויים.

בנוסף, כלי השדרוג 
[`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html)
    קיבל מספר שיפורים ב‑PostgreSQL 18,
לרבות שדרוגים מהירים יותר כאשר במסד הנתונים יש הרבה אובייקטים (כגון טבלאות ורצפים).
מהדורה זו גם מאפשרת ל‑
`pg_upgrade` 
להריץ בדיקות במקביל בהתאם לפרמטר 
`--jobs`
, ומוסיפה את הדגל 
`--swap`
שמבצע החלפה בין ספריות השדרוג במקום העתקה, שכפול או קישור קבצים.

PostgreSQL 18 ממשיכה להאיץ את ביצועי השאילתות בעזרת יכולות שמזרזות את העומסים שלכם באופן אוטומטי. 
מהדורה זו מציגה חיפושי “skip scan” על 
[אינדקסי B-tree מרובי עמודות](https://www.postgresql.org/docs/18/indexes-multicolumn.html)
, המשפרים את זמן הביצוע עבור שאילתות שמדלגות על תנאי = באחת או יותר עמודת הפריפיקס של האינדקס.
היא יכולה גם לאפטם שאילתות המשתמשות בתנאי 
`OR`
    
    בתוך סעיף 
`WHERE`
    כך שיוכלו להשתמש באינדקס, דבר שמוביל לביצוע מהיר משמעותית.
נוסף על כך, בוצעו שיפורים רבים באופן שבו PostgreSQL מתכננת ומבצעת חיבורים בין טבלאות (joins) — מהאצת
`hash join`
    ועד מתן אפשרות ל-
`merge join`
    להשתמש במיונים אינקרמנטליים.
PostgreSQL 18 תומכת גם בבנייה מקבילית של 
[אינדקסי GIN](https://www.postgresql.org/docs/18/gin.html)
, ומצטרפת בכך לאינדקסי B-tree ו-
    שכבר תומכים ביכולת זו.

מהדורה זו גם מרחיבה את התמיכה של PostgreSQL בהאצת חומרה, כולל תמיכה באינטרינזיקות מעבד ARM NEON ו-SVE עבור הפונקציה
`popcount`
, המשמשת את
[`bit_count`](https://www.postgresql.org/docs/18/functions-bitstring.html)
    ויכולות פנימיות נוספות.

PostgreSQL 18 מציגה עמודות מחושבות וירטואליות (Virtual Generated Columns) שמחשבות ערכים בזמן הרצת השאילתה במקום לאחסן אותם. זהו כעת ברירת המחדל עבור עמודות מחושבות. בנוסף, ניתן כעת לשכפל לוגית עמודות מחושבות מאוחסנות.

מהדורה זו מוסיפה אפשרות לגשת גם לערכים הקודמים (
`OLD`
) וגם לערכים הנוכחיים (
`NEW`
) בסעיף
[`RETURNING`](https://www.postgresql.org/docs/18/dml-returning.html)
עבור הפקודות
`INSERT`
,
`UPDATE`
,
`DELETE`
ו-
`MERGE`
.
PostgreSQL 18 מוסיפה גם יצירת UUIDv7 באמצעות הפונקציה
[`uuidv7()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE)
    , המאפשרת להפיק מזהי UUID אקראיים המסודרים לפי חותמת זמן, לטובת אסטרטגיות קאשינג יעילות יותר.
PostgreSQL 18 כוללת את
[`uuidv4()`](https://www.postgresql.org/docs/18/functions-uuid.html#FUNC_UUID_GEN_TABLE)
    ככינוי ל-
`gen_random_uuid()`
.

PostgreSQL 18 מוסיפה
 [אילוצים טמפורליים](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-UNIQUE)
    - אילוצים על פני תחומים- ל-
`PRIMARY KEY`
    ול-
`UNIQUE`
- באמצעות הסעיף
`WITHOUT OVERLAPS`
, וכן ל-
`FOREIGN KEY`
    באמצעות הסעיף
`PERIOD`
.

לבסוף, PostgreSQL 18 מקלה על יצירת הגדרת הסכימה של טבלת חוץ (foreign table) על בסיס ההגדרה של טבלה מקומית באמצעות הפקודה
[`CREATE FOREIGN TABLE ... LIKE`](https://www.postgresql.org/docs/18/sql-createforeigntable.html)
.

PostgreSQL 18 מקלה ומאיצה את עיבוד הטקסט בעזרת מספר שיפורים חדשים. 
מהדורה זו מוסיפה את המיון
[`PG_UNICODE_FAST`](https://www.postgresql.org/docs/18/collation.html#COLLATION-MANAGING-STANDARD)
, המספק סמנטיקה מלאה של Unicode להמרות רישיות (case) ובמקביל מסייע להאיץ השוואות רבות.
זה כולל את פונקציות
`upper`
    ו-
`lower`
, וכן את הפונקציה החדשה
[`casefold`](https://www.postgresql.org/docs/18/functions-string.html#FUNCTIONS-STRING-OTHER)
    להשוואות שאינן תלויות רישיות.
בנוסף, PostgreSQL 18 תומכת כעת בביצוע השוואות
`LIKE`
    על טקסט המשתמש ב
[מיון לא-דטרמיניסטי](https://www.postgresql.org/docs/18/collation.html#COLLATION-NONDETERMINISTIC)
, מה שמפשט ביצוע התאמות תבנית מורכבות יותר.
מהדורה זו גם משנה את
[חיפוש הטקסט המלא](https://www.postgresql.org/docs/18/textsearch.html)
    כך שישתמש בספק המיון (collation provider) ברירת-המחדל של בסיס נתונים במקום תמיד להשתמש ב-
`libc`
, שינוי שעשוי לדרוש אינדוקס מחדש של כל אינדקסי
 [חיפוש הטקסט המלא](https://www.postgresql.org/docs/18/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX)
    ואינדקסי
[`pg_trgm`](https://www.postgresql.org/docs/18/pgtrgm.html#PGTRGM-INDEX)
    לאחר הרצת
[`pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html)
.

PostgreSQL 18 מציגה אימות
[`oauth`](https://www.postgresql.org/docs/18/auth-oauth.html)
, המאפשר למשתמשים לבצע אימות באמצעות מנגנוני OAuth 2.0 הנתמכים דרך הרחבות PostgreSQL.
בנוסף, PostgreSQL 18 כוללת ולידציה עבור
[מצב FIPS](https://www.postgresql.org/docs/18/pgcrypto.html#PGCRYPTO-OPENSSL-SUPPORT-FUNCS)
, ומוסיפה את הפרמטר
[`ssl_tls13_ciphers`](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-SSL-TLS13-CIPHERS)
    להגדרת מערכי הצפנים (cipher suites) של TLS v1.3 בצד השרת.

מהדורה זו מכריזה על מנגנון האימות בסיסמה
`md5`
    כמיושן (deprecated), והוא יוסר באחת המהדורות הבאות. 
אם נדרש לכם אימות מבוסס סיסמה ב-PostgreSQL, השתמשו באימות 
[`SCRAM`](https://www.postgresql.org/docs/18/auth-password.html)
של PostgreSQL 18.

SCRAM תומכת גם ב-SCRAM passthrough הן עם
[`postgres_fdw`](https://www.postgresql.org/docs/18/postgres-fdw.html)
    והן עם
[`dblink`](https://www.postgresql.org/docs/18/dblink.html)
    לצורך אימות מול מופעי PostgreSQL מרוחקים.
    בנוסף, 
[`pgcrypto`](https://www.postgresql.org/docs/18/pgcrypto.html)
    תומכת כעת ב
[SHA-2 לצורך גיבוב סיסמאות](https://www.postgresql.org/docs/18/pgcrypto.html#PGCRYPTO-CRYPT-ALGORITHMS)
.

PostgreSQL 18 תומכת בדיווח על התנגשויות כתיבה בשכפול לוגי (logical replication write conflicts) ביומנים (logs) ובתצוגה
[`pg_stat_subscription_stats`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-SUBSCRIPTION-STATSl)
. 
בנוסף,
[`CREATE SUBSCRIPTION`](https://www.postgresql.org/docs/18/sql-createsubscription.html)
    משתמשת כעת כברירת מחדל בהזרמה מקבילית (parallel streaming) ליישום עסקאות, מה שיכול לשפר את הביצועים. 
לכלי 
[`pg_createsubscriber`](https://www.postgresql.org/docs/18/app-pgcreatesubscriber.html)
    נוסף הדגל
`--all`
, כך שניתן ליצור רפליקות לוגיות לכל מסדי הנתונים במופע בפקודה אחת.
PostgreSQL 18 מאפשרת גם
[להסיר אוטומטית סלוטי שכפול לא פעילים (idle replication slots)](https://www.postgresql.org/docs/18/runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT)
    כדי לסייע במניעת אגירה של יותר מדי קובצי WAL בצד המפרסם.

PostgreSQL 18 משפרת את אסטרטגיית ה- 
[`VACUUM`](https://www.postgresql.org/docs/18/routine-vacuuming.html)
- על-ידי הקפאה יזומה של יותר דפים במהלך פעולות
`VACUUM`
    רגילות, מה שמפחית תקורה ותורם במצבים הדורשים פעולות
`VACUUM`
    אגרסיביות.

PostgreSQL 18 מוסיפה פרטים נוספים ל-
[`EXPLAIN`](https://www.postgresql.org/docs/18/using-explain.html)
, המספק מידע על ביצוע תוכנית השאילתה, וכעת מציגה אוטומטית כמה באפרים (יחידת האחסון הבסיסית) נגישים בעת הרצת
`EXPLAIN ANALYZE`
. 
בנוסף,
`EXPLAIN ANALYZE`
    מציג כעת כמה פניות לאינדקס מתבצעות במהלך סריקת אינדקס, ו-
`EXPLAIN ANALYZE VERBOSE`
    כולל סטטיסטיקות על CPU, WAL וזמני קריאה ממוצעים.
PostgreSQL 18 כוללת יותר מידע ב
[`pg_stat_all_tables`](https://www.postgresql.org/docs/18/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW)
- על זמן שהוקדש ל-
`VACUUM`
    ולפעולות קשורות, וכן סטטיסטיקות לפי-חיבור על ניצול I/O ו-WAL.

מסדי נתונים שמאותחלים עם
[`initdb`](https://www.postgresql.org/docs/18/app-initdb.html)
    של PostgreSQL 18 מופעלים כברירת־מחדל עם בדיקות page checksums. 
הדבר עשוי להשפיע על שדרוגים מבסיסי נתונים שבהם בדיקות page checksums אינן מופעלות: במקרה כזה, בעת שימוש ב
[`־pg_upgrade`](https://www.postgresql.org/docs/18/pgupgrade.html)
יהיה צורך ליצור בסיס נתונים PostgreSQL 18 חדש עם האפשרות
`--no-data-checksums`
.

PostgreSQL 18 מציגה גם גרסה חדשה (3.2) של פרוטוקול ה-WIRE של PostgreSQL - הגרסה החדשה הראשונה מאז 
PostgreSQL 7.4 (2003). 
הספרייה
[`libpq`](https://www.postgresql.org/docs/18/libpq-connect.html)
    עדיין משתמשת בגרסה 3.0 כברירת־מחדל, בעוד ש clients (למשל דרייברים, מאגרים, פרוקסים) מוסיפים תמיכה בגרסת הפרוטוקול החדשה.

תכונות חדשות ושיפורים רבים אחרים נוספו ל‑PostgreSQL 18 שעשויים גם להועיל למקרי השימוש שלכם.
אנא עיינו ב-
[הערות המהדורה](https://www.postgresql.org/docs/18/release-18.html)
    לקבלת רשימה מלאה של תכונות חדשות ושונות.

[PostgreSQL](https://www.postgresql.org/)
    הוא מסד נתונים בקוד פתוח המתקדם ביותר בעולם, עם קהילה גלובלית של אלפי משתמשים, תורמים, חברות וארגונים. 
הפרויקט PostgreSQL נבנה על מעל 40 שנות הנדסה, החל באוניברסיטת קליפורניה, ברקלי, והמשיך להתפתח עם קצב ללא תחרות. 
ערכת התכונות הבשלות של PostgreSQL לא רק תואמת מערכות נתונים קנייניות מובילות, אלא עולה עליהן במאפיינים של מסדי נתונים מתקדמים ,יכולות הרחבה, אבטחה ויציבות.

Learn more about PostgreSQL and participate in our community at
  [PostgreSQL.org](https://www.postgresql.org/).

להסברים על התכונות שלעיל ואחרות, עיינו במשאבים הבאים:

ישנן מספר דרכים להוריד את PostgreSQL18, כולל:

כלים והרחבות נוספים זמינים ב-
[PostgreSQL Extension Network](http://pgxn.org/)
.

PostgreSQL 18 מגיע עם תיעוד HTML וכן דפי man. 
ניתן לעיין בתיעוד גם באופן מקוון בפורמט
[HTML](https://www.postgresql.org/docs/18/)
ובפורמט
[PDF](https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-US.pdf)
.

PostgreSQL משתמשת ב
[רישיון PostgreSQL](https://www.postgresql.org/about/licence/)
    , רישיון “מתירני” הדומה ל-BSD. 
רישיון זה, 
[המאושר על-ידי OSI](http://www.opensource.org/licenses/postgresql/)
, מוערך כגמיש וידידותי לעסקים, שכן הוא אינו מגביל את השימוש ב-PostgreSQL יחד עם יישומים מסחריים וקנייניים. 
בשילוב עם תמיכה של חברות רבות ובעלות ציבורית על הקוד, רישיוננו הופך את PostgreSQL לפופולרית מאוד בקרב ספקים המבקשים לשלב מסד נתונים במוצריהם ללא חשש מעמלות, נעילת ספקים או שינויי תנאי רישוי.

אתר:

אימייל:

Postgres ו-PostgreSQL ולוגו הפיל (Slonik) הם כולם סימנים מסחריים רשומים של 
[PostgreSQL Community Association](https://www.postgres.ca)
. אם ברצונך להשתמש בסימנים אלה, עליך לציית ל
[מדיניות הסימנים המסחריים](https://www.postgresql.org/about/policies/trademarks/)
.

PostgreSQL נהנית מתמיכתן של חברות רבות, שנותנות חסות למפתחים, מספקות משאבי אירוח ונותנות לנו תמיכה כספית. עיין בדף 
[נותני החסות](https://www.postgresql.org/about/sponsors/)
שלנו עבור חלק מתומכי הפרויקט הללו.

יש גם קהילה גדולה של 
[חברות המציעות תמיכה ב-PostgreSQL](https://www.postgresql.org/support/professional_support/)
, מיועצים בודדים ועד לחברות רב לאומיות.

אם ברצונך לתרום תרומה כספית לקבוצת הפיתוח העולמית PostgreSQL או לאחד מארגוני הקהילה המוכרים ללא מטרות רווח, אנא בקר ב
[דף התרומות](https://www.postgresql.org/about/donate/)
שלנו.