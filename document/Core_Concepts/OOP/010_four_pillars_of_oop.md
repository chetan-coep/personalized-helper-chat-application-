---
id: "oop_010"
technology: "OOP"
category: "Core Concepts"
title: "The Four Pillars of Object-Oriented Programming (OOP): Encapsulation, Abstraction, Inheritance, and Polymorphism"
doc_order: 10
source_url: "https://docs.oracle.com/javase/tutorial/java/concepts/index.html"
language: "en"
retrieved_at: "2026-11-03 19:55:00"
content_hash: "oop_four_pillars_comprehensive_010"
---

# The Four Pillars of Object-Oriented Programming (OOP)

Source: https://docs.oracle.com/javase/tutorial/java/concepts/index.html

---

## Overview: The Four Fundamental Pillars of OOP

Object-Oriented Programming (OOP) is a programming paradigm organized around real-world entities termed "objects" and "classes". The entire architecture of OOP rests upon **Four Pillars**:

1. **Encapsulation**: Bundling state (variables) and behavior (methods) together while restricting direct access to internal details (data hiding).
2. **Abstraction**: Exposing only essential high-level interfaces to the outside world while concealing internal execution logic.
3. **Inheritance**: Creating a hierarchy where child classes inherit properties, fields, and methods from existing parent classes, promoting code reuse.
4. **Polymorphism**: The ability of a single interface, function, or method name to perform different underlying operations based on the object calling it.

---

## 1. Encapsulation (Data Hiding and Security)

Encapsulation is the technique of keeping an object's fields private and providing access only through controlled public getter and setter methods. This prevents unauthorized direct modification of internal state and guarantees data validation.

```java
// Example in Java
public class BankAccount {
    // Private state - hidden from outside access
    private double balance;

    // Public constructor
    public BankAccount(double initialBalance) {
        if (initialBalance >= 0) {
            this.balance = initialBalance;
        }
    }

    // Controlled getter
    public double getBalance() {
        return this.balance;
    }

    // Controlled setter with validation rules
    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
}
```

```python
# Example in Python
class BankAccount:
    def __init__(self, initial_balance: float):
        self._balance = initial_balance  # Encapsulated attribute

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit must be positive")
```

---

## 2. Abstraction (Hiding Complexity)

Abstraction means displaying only essential information to the developer and hiding background complexity. In programming, abstraction is achieved using **abstract classes** and **interfaces**. The user knows *what* an object does, but does not need to know *how* it does it.

```java
// Example in Java: Interface defines the contract
public interface PaymentProcessor {
    void processPayment(double amount);
}

public class StripePaymentProcessor implements PaymentProcessor {
    @Override
    public void processPayment(double amount) {
        // Complex Stripe API tokenization, SSL encryption, HTTP requests
        System.out.println("Processing $" + amount + " via Stripe API");
    }
}
```

```python
# Example in Python using abc module
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> None:
        """Abstract contract - subclasses must implement"""
        pass

class EmailNotification(NotificationService):
    def send_notification(self, recipient: str, message: str) -> None:
        print(f"Sending Email to {recipient}: {message}")
```

---

## 3. Inheritance (Code Reuse and Hierarchy)

Inheritance is the mechanism by which a new class (subclass or derived class) inherits fields and methods from an existing class (superclass or base class). This models "is-a" relationships and eliminates duplicate code across systems.

```java
// Superclass (Base)
public class Vehicle {
    protected String brand;

    public Vehicle(String brand) {
        this.brand = brand;
    }

    public void startEngine() {
        System.out.println(brand + " engine is running.");
    }
}

// Subclass (Derived)
public class ElectricCar extends Vehicle {
    private int batteryCapacity;

    public ElectricCar(String brand, int batteryCapacity) {
        super(brand); // Call superclass constructor
        this.batteryCapacity = batteryCapacity;
    }

    public void charge() {
        System.out.println("Charging " + brand + " battery (" + batteryCapacity + " kWh)");
    }
}
```

```python
# Example in Python
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def start_engine(self) -> str:
        return f"{self.brand} engine started."

class ElectricCar(Vehicle):
    def __init__(self, brand: str, battery_kwh: int):
        super().__init__(brand)
        self.battery_kwh = battery_kwh
```

---

## 4. Polymorphism (Multiple Forms)

Polymorphism translates literally from Greek as "many forms". It allows objects of different subclasses to be treated through a single common superclass or interface, with the correct subclass implementation executed at runtime (Dynamic Method Dispatch).

There are two primary types of polymorphism:
1. **Compile-time Polymorphism (Method Overloading)**: Methods in the same class sharing the same name but with different parameter lists or types.
2. **Runtime Polymorphism (Method Overriding)**: A subclass providing a specific implementation of a method already defined in its superclass.

```java
// Runtime Polymorphism Example in Java
public class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark bark");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow meow");
    }
}

// Usage: Polymorphic collection
Animal myDog = new Dog();
Animal myCat = new Cat();
myDog.makeSound(); // Prints "Bark bark"
myCat.makeSound(); // Prints "Meow meow"
```

---

## Summary of the 4 Pillars of OOP

| Pillar | Primary Purpose | How It Is Implemented | Major Benefit |
| :--- | :--- | :--- | :--- |
| **Encapsulation** | Protect and bundle internal state | `private`/`protected` modifiers, getters/setters | Data security, preventing bugs, validation |
| **Abstraction** | Hide unnecessary background complexity | `interface`, `abstract class`, `abstractmethod` | Simple public APIs, decoupled design |
| **Inheritance** | Form parent-child relationships ("is-a") | `extends`, `class Sub(Super):` | Code reuse, eliminates duplicated logic |
| **Polymorphism** | Treat multiple classes through a shared API | Method overriding (`@Override`), dynamic dispatch | Extensible architecture, easy plug-and-play |

