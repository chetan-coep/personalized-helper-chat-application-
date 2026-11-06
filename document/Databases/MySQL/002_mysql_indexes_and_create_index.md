---
id: "mysql_002"
technology: "MySQL"
category: "Databases"
title: "MySQL Optimization: CREATE INDEX, Clustered & Secondary Indexes"
doc_order: 2
source_url: "https://dev.mysql.com/doc/refman/8.4/en/create-index.html"
language: "en"
retrieved_at: "2026-11-03 19:50:00"
content_hash: "mysql_create_index_002"
---

# MySQL Indexing and Optimization

Source: https://dev.mysql.com/doc/refman/8.4/en/create-index.html

---

## What is an Index in MySQL

In MySQL (particularly when using the InnoDB storage engine), indexes are physical data structures that organize table rows for fast lookups. InnoDB uses B+Tree data structures where leaf nodes contain pointers or actual row data:

1. **Clustered Index**: Every InnoDB table has a clustered index based on the `PRIMARY KEY`. The data rows are physically stored in the leaf nodes of this index.
2. **Secondary Indexes**: Any index created on other columns (via `CREATE INDEX`) is a secondary index. In InnoDB, secondary index records store the indexed column values plus the corresponding primary key value.

## How to Implement Indexes in MySQL

### 1. Basic CREATE INDEX Statement
To create an index on an existing table:

```sql
CREATE INDEX idx_customers_country
ON customers (country);
```

### 2. Creating a Unique Index
Prevents duplicate entries and ensures data integrity:

```sql
CREATE UNIQUE INDEX idx_accounts_username
ON accounts (username);
```

### 3. Multi-Column (Composite) Index
Used when queries evaluate multiple columns in `WHERE` or `JOIN` conditions:

```sql
CREATE INDEX idx_customer_city_zip
ON customers (city, postal_code);
```

### 4. Inline Index Creation with CREATE TABLE
Indexes can be defined directly during table schema creation:

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    total_amount DECIMAL(10, 2),
    INDEX idx_orders_customer (customer_id),
    INDEX idx_orders_date (order_date)
) ENGINE=InnoDB;
```

### 5. Checking Index Usage with EXPLAIN
To check if MySQL uses your index or performs a `type: ALL` (full table scan):

```sql
EXPLAIN SELECT * FROM customers WHERE country = 'Germany';
```

### 6. Dropping an Index
To remove an index in MySQL:

```sql
DROP INDEX idx_customers_country ON customers;
```

## Why Use MySQL Indexes

- Prevents full table scans on large tables with hundreds of thousands or millions of records.
- Enables efficient index-only scans (covering indexes) where queries retrieve data directly from index nodes without touching table disk blocks.
- Drastically accelerates `JOIN` execution between foreign key and primary key columns.

