---
id: "prisma_orm_004"
technology: "Prisma ORM"
category: "Backend & APIs"
title: "Prisma ORM"
doc_order: 4
source_url: "https://www.prisma.io/apollo"
language: "en"
retrieved_at: "2026-11-01 22:18:08"
content_hash: "0925d0966f8248570a523efce18831bb3fb2cc9f56b32e62a2fe6e58601e5d4f"
---

# Prisma ORM

Source: https://www.prisma.io/apollo

---

# Easy, type-safe database access with Prisma & Apollo

Query data from MySQL, PostgreSQL & SQL Server databases in GraphQL with Prisma – a better ORM for JavaScript and TypeScript.

## Why Prisma and Apollo?

### End-to-end type safety

Get coherent typings for your application, from database to frontend, to boost productivity and avoid errors.

### Optimized database queries

Prisma's built-in dataloader ensures optimized and performant database queries, even for N+1 queries.

### Type-safe database client

Prisma Client ensures fully type-safe database queries with benefits like autocompletion - even in JavaScript.

### Intuitive data modeling

Prisma's modeling language is inspired by GraphQL SDL and lets you intuitively describe your database schema.

### Easy database migration

Map your Prisma schema to the database so you don't need to write SQL to manage your database schema.

### Filters, pagination & ordering

Prisma Client reduces boilerplates by providing convenient APIs for common database features.

## How Prisma and Apollo fit together

#### Apollo Server — SDL-First

When using Apollo's native SDL-first approach for constructing your GraphQL schema, you provide your GraphQL schema definition as a string and a resolver map that implement this definition.

Inside your resolvers, you can use Prisma Client to read and write data in your database in order to resolve the incoming GraphQL queries and mutations.

```
import { PrismaPg } from '@prisma/adapter-pg';
import { PrismaClient } from '../generated/client';
import { ApolloServer } from 'apollo-server'
const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL,
});
const prisma = new PrismaClient({ adapter });
const typeDefs = `
  type User {
    email: String!
    name: String
  }
  type Query {
    allUsers: [User!]!
  }
`;
const resolvers = {
  Query: {
    allUsers: () => {
      return prisma.user.findMany();
    }
  }
};
const server = new ApolloServer({ resolvers, typeDefs });
server.listen({ port: 4000 });
```
## Featured Prisma & Apollo examples

### How to build and deploy a GraphQL API

A comprehensive tutorial that explains how to build a GraphQL API with Apollo Server and Prisma and deploy it to DigitalOcean's App Platform.

### SDL-first starter kit

A ready-to-run example project with an SDL-first schema and a Postgres database

### Nexus starter kit

A ready-to-run example project with Nexus (code-first) and a SQLite database