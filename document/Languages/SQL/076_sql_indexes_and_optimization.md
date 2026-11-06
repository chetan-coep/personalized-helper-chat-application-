---
id: "sql_076"
technology: "SQL"
category: "Languages"
title: "SQL Indexing: Concepts, CREATE INDEX Syntax, and Performance Optimization"
doc_order: 76
source_url: "https://www.postgresql.org/docs/current/sql-createindex.html"
language: "en"
retrieved_at: "2026-11-03 19:50:00"
content_hash: "sql_index_comprehensive_076"
---

# SQL Indexing: Concepts, Syntax, and Implementation

Source: https://www.postgresql.org/docs/current/sql-createindex.html

---

## What is Indexing in SQL Databases

An index in an SQL relational database is a separate, specialized data structure (most commonly a balanced tree, or B-tree) that maintains pointers to rows in a table. It acts like an index in the back of a book: instead of scanning every single page from beginning to end (a full table scan of O(N) complexity), the database engine navigates the index tree in logarithmic O(log N) time to locate exact rows.

Indexes are created on one or more columns of a table to accelerate data retrieval operations (SELECT queries) and enforce uniqueness constraints.

## Why Use Indexes in SQL Databases

- **Drastic Query Speedup**: Reduces search operations from sequential full table scans to binary or tree searches. For tables with millions of rows, query latency drops from seconds to single-digit milliseconds.
- **Fast Filtering & Sorting**: Speeds up queries containing `WHERE` clauses, `JOIN` conditions, `ORDER BY`, and `GROUP BY` operations on indexed columns.
- **Enforcing Uniqueness**: Unique indexes ensure that duplicate values cannot be entered into columns like email addresses, usernames, or identification numbers.
- **Primary Keys**: Relational database engines automatically build a unique clustered or B-tree index on the table's PRIMARY KEY.

## How to Implement Indexes: SQL Syntax

### 1. Basic Single-Column Index
To create a standard index on a single column:

```sql
-- Syntax:
CREATE INDEX idx_users_last_name
ON users (last_name);
```

### 2. Unique Index
To speed up lookups and prevent duplicate values:

```sql
-- Syntax:
CREATE UNIQUE INDEX idx_users_email
ON users (email);
```

### 3. Composite (Multi-Column) Index
When queries frequently filter by multiple columns together, create a composite index. The order of columns matters (leftmost prefix rule):

```sql
-- Syntax:
CREATE INDEX idx_orders_user_created
ON orders (user_id, created_at);
```

### 4. Conditional or Partial Index
An index that includes only rows satisfying a specific condition, saving disk space and memory:

```sql
-- PostgreSQL Syntax:
CREATE INDEX idx_orders_unprocessed
ON orders (created_at)
WHERE status = 'pending';
```

### 5. Verifying Index Usage with EXPLAIN
To inspect whether the query optimizer uses the index:

```sql
EXPLAIN ANALYZE
SELECT * FROM users
WHERE last_name = 'Smith';
```

### 6. Removing an Index
When an index is no longer needed:

```sql
DROP INDEX idx_users_last_name;
```

## Important Caveats & Best Practices

- **Write Overhead**: Every `INSERT`, `UPDATE`, and `DELETE` statement must update both the table and its associated indexes. Over-indexing degrades write throughput.
- **High vs Low Cardinality**: Index columns with high cardinality (many distinct values, e.g., user IDs, emails, timestamps). Avoid indexing columns with very low cardinality (e.g., boolean flags or gender), where full scans are often cheaper.
- **Leftmost Prefix Rule**: A composite index on `(user_id, created_at)` can accelerate queries on `user_id` alone or `user_id AND created_at`, but cannot be used for queries filtering only on `created_at`.

