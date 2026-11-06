---
id: "oop_005"
technology: "OOP"
category: "Core Concepts"
title: "What Is Inheritance? (The Java™ Tutorials >"
doc_order: 5
source_url: "https://docs.oracle.com/javase/tutorial/java/concepts/inheritance.html"
language: "en"
retrieved_at: "2026-11-03 17:59:57"
content_hash: "6ff516e62f4452ddec8103964293652b58f7fa9c06e8cceb52ba790a53fc4a0d"
---

# What Is Inheritance? (The Java™ Tutorials >        
            Learning the Java Language > Object-Oriented Programming Concepts)

Source: https://docs.oracle.com/javase/tutorial/java/concepts/inheritance.html

---

Different kinds of objects often have a certain amount in common with each other. Mountain bikes, road bikes, and tandem bikes, for example, all share the characteristics of bicycles (current speed, current pedal cadence, current gear). Yet each also defines additional features that make them different: tandem bicycles have two seats and two sets of handlebars; road bikes have drop handlebars; some mountain bikes have an additional chain ring, giving them a lower gear ratio.

Object-oriented programming allows classes to *inherit* commonly used state and behavior from other classes. In this example, `Bicycle` now becomes the *superclass* of `MountainBike`, `RoadBike`, and `TandemBike`. In the Java programming language, each class is allowed to have one direct superclass, and each superclass has the potential for an unlimited number of *subclasses*:

A hierarchy of bicycle classes.

The syntax for creating a subclass is simple. At the beginning of your class declaration, use the `extends` keyword, followed by the name of the class to inherit from:

class MountainBike **extends** Bicycle {
    // new fields and methods defining 
    // a mountain bike would go here
}

This gives `MountainBike` all the same fields and methods as `Bicycle`, yet allows its code to focus exclusively on the features that make it unique. This makes code for your subclasses easy to read. However, you must take care to properly document the state and behavior that each superclass defines, since that code will not appear in the source file of each subclass.