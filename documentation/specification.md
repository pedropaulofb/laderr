# How to Write LaDeRR Specifications

PLEASE BE AWARE THAT THIS IS A VERSION STILL UNDER DEVELOPMENT. USE IT CAREFULLY.

## Table of Contents

<!-- TOC -->

- [How to Write LaDeRR Specifications](#how-to-write-laderr-specifications)
    - [Table of Contents](#table-of-contents)
    - [1. Introduction](#1-introduction)
    - [2. General Structure of a LaDeRR Specification](#2-general-structure-of-a-laderr-specification)
        - [2.1. Access to LaDeRR Specification Examples and Results](#21-access-to-laderr-specification-examples-and-results)
    - [3. Specification Metadata](#3-specification-metadata)
        - [3.1. Required Fields and Defaults](#31-required-fields-and-defaults)
        - [3.2. Complete Example of a Valid Metadata Specification](#32-complete-example-of-a-valid-metadata-specification)
    - [4. Defining Constructs](#4-defining-constructs)
        - [4.1 Common Aspects of LaDeRR Constructs](#41-common-aspects-of-laderr-constructs)
            - [4.1.1 Example of a General Construct Specification](#411-example-of-a-general-construct-specification)
- [Without a defined label, this construct will have 'label = reinforceddesign'. The label's default value equals the id.](#without-a-defined-label-this-construct-will-have-label--reinforceddesign-the-labels-default-value-equals-the-id)
            - [4.1.2 Constructs' Attributes](#412-constructs-attributes)
        - [4.2 Entities](#42-entities)
            - [4.2.1 Assets](#421-assets)
                - [Additional Attributes of Assets](#additional-attributes-of-assets)
                - [Example of an Asset Specification](#example-of-an-asset-specification)
            - [4.2.2 Threats](#422-threats)
                - [Additional Attributes of Threats](#additional-attributes-of-threats)
                - [Example of a Threat Specification](#example-of-a-threat-specification)
            - [4.2.3 Control Mechanisms](#423-control-mechanisms)
                - [Additional Attributes of Controls](#additional-attributes-of-controls)
                - [Example of a Control Specification](#example-of-a-control-specification)
        - [4.3 Dispositions](#43-dispositions)
            - [4.3.1 Capabilities](#431-capabilities)
                - [Additional Attributes of Capabilities](#additional-attributes-of-capabilities)
                - [Example of a Capability Specification](#example-of-a-capability-specification)
            - [4.3.2 Vulnerabilities](#432-vulnerabilities)
                - [Additional Attributes of Vulnerabilities](#additional-attributes-of-vulnerabilities)
                - [Example of a Vulnerability Specification](#example-of-a-vulnerability-specification)
        - [4.4 Resilience](#44-resilience)
            - [Attributes and Relationships](#attributes-and-relationships)
            - [Example of a Resilience Specification](#example-of-a-resilience-specification)
    - [5. Logical Rules of LaDeRR](#5-logical-rules-of-laderr)
        - [5.1 Dispositions and Their Relationships](#51-dispositions-and-their-relationships)
        - [5.2 Entity Interactions](#52-entity-interactions)
        - [5.3 Resilience Rules](#53-resilience-rules)
        - [5.4 Damage Success and Failure](#54-damage-success-and-failure)
        - [5.5 Scenario Resilience Determination](#55-scenario-resilience-determination)
        - [5.6 Vulnerability-Capability Relationship](#56-vulnerability-capability-relationship)
    - [6. LaDeRR Engine](#6-laderr-engine)
        - [6.1 Writing a LaDeRR Specification with LaDeRR Engine](#61-writing-a-laderr-specification-with-laderr-engine)
            - [6.1.1 Automatic Inference](#611-automatic-inference)
            - [Automatic Resilience Generation](#automatic-resilience-generation)
            - [6.1.3 Simplified Specification Example](#613-simplified-specification-example)
        - [6.2 Engine Output and Inferred Model](#62-engine-output-and-inferred-model)
    - [7. Complete Example](#7-complete-example)
        - [7.1 Explicit Specification](#71-explicit-specification)
        - [7.2 Simplified Specification with LaDeRR Engine](#72-simplified-specification-with-laderr-engine)
        - [7.3 Inferred Output by LaDeRR Engine](#73-inferred-output-by-laderr-engine)

<!-- /TOC -->

## 1. Introduction

The [Language for Describing Risk and Resilience (LaDeRR)](https://w3id.org/laderr/git) is an ontology-based domain-specific language (DSL) designed to specify resilience scenarios. Built over [ResiliOnt](https://github.com/pedropaulofb/resiliont/), it provides a structured approach to defining entities, capabilities, vulnerabilities, and their interrelations. LaDeRR integrates formal modeling with computational representations, ensuring precision in resilience representation.

This document serves as a guide for writing LaDeRR specifications using its concrete syntax in [TOML format](https://toml.io/en/). It outlines the essential components, rules, and best practices for creating valid and meaningful specifications. Each section introduces a key concept of the LaDeRR language, presents its corresponding metamodel representation, explains any associated logical rules, and provides a concrete example of how to specify it in practice.

The LaDeRR metamodel defines the core structural elements of the language, establishing the conceptual foundation for resilience and risk scenario modeling. To ensure clarity and precision, it is presented in separate UML class diagrams, each representing a distinct aspect of LaDeRR and illustrating the relationships between its components.

In the following sections, we will systematically cover all core elements of a LaDeRR specification. Each component will be accompanied by:
- **Concept Overview**: A brief explanation of the purpose and role of the component within a LaDeRR specification.
- **Metamodel Representation**: A UML class diagram illustrating the structure and relationships within the metamodel.
- **Rules and Constraints (if applicable)**: Formal constraints and derivations governing the use of the component, ensuring compliance with the LaDeRR framework.
- **Specification Example**: A fully annotated TOML snippet demonstrating a correct way to specify the component within a LaDeRR model.

Each UML diagram follows a color-coding and formatting scheme:

- **Blue**: Represents classes that are defined within the specific diagram being presented.
- **Gray**: Represents classes that are defined in other diagrams and are shown only to indicate relationships.
- **White**: Represents enumerations, which define a set of predefined values.
- **Red**: Represents notes that provide additional constraints, rules, or clarifications.

## 2. General Structure of a LaDeRR Specification

A LaDeRR specification defines **resilience scenarios** using a structured format that consists of two main components:

- **Metadata**: Provides general information about the specification, including authorship, versioning, and scenario type.
- **Constructs**: Define the key elements of the resilience scenario and their relationships. The main constructs include:
  - **Assets**: Represent entities that need protection or have resilience capabilities.
  - **Capabilities**: Define the functional strengths of an entity, such as protective mechanisms.
  - **Vulnerabilities**: Represent weaknesses that can be exploited by threats.
  - **Threats**: Entities or conditions that can exploit vulnerabilities.
  - **Resilience**: Mechanisms that mitigate or counteract threats and vulnerabilities.
  - **Control**: Entities that inhibit threats, creating resilience.

Each construct is interconnected, governed by logical constraints, and formally structured in TOML format. These constraints ensure consistency and are enforced through formal rules, as described in Section 5. The following sections detail each construct, presenting its concept, metamodel representation, applicable rules, and a valid example of how to specify it in a LaDeRR model.

### 2.1. Access to LaDeRR Specification Examples and Results

All **LaDeRR specifications** presented in this document, including every example and fragment, are available in the [examples](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples) folder of the LaDeRR repository.

For each LaDeRR specification included in this documentation, the following additional resources are provided:

- The original specification file as presented in this document.
- Validation and inference reports:
  - Pre-Inference Validation: Ensures that the input specification conforms to the LaDeRR metamodel and does not contain missing required fields or incorrect relationships.
  - Post-Inference Validation: After inference, checks that the inferred constructs and relationships maintain logical consistency within the model.
- The generated graph data:
  - The graph structure before inference.
  - The graph structure after inference.  
- Graph-based visualizations of the specification:
  - A visualization of the graph before inference.
  - A visualization of the graph after inference.

These resources allow users to verify how the LaDeRR Engine interprets and processes each specification. Links to these files are provided alongside the corresponding examples in this documentation, ensuring full access to both the input specifications and the processed results.


## 3. Specification Metadata

The metadata defines global properties of a LaDeRR specification. These fields establish essential information about the specification, including its identity, authorship, and operational scenario. The UML diagram below illustrates the metadata structure:

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/LaderrSpecification.png" width="750"></p>

### 3.1. Required Fields and Defaults

| Field        | Type         | Required | Default Value            | Description |
|-------------|-------------|----------|--------------------------|-------------|
| **baseURI**  | URIRef [1]  | Yes      | `https://laderr.laderr#` | Unique identifier for the specification. |
| **title**    | string [1]  | Yes      | N/A                      | Title of the specification. |
| **description** | string [0..1] | No | None | Brief explanation of the specification. |
| **version**  | string [1]  | Yes      | N/A | Version identifier of the specification. |
| **createdBy** | string [1..*] | Yes | N/A | Author(s) responsible for the specification. |
| **createdOn** | datetime [1] | Yes | N/A | Creation timestamp. |
| **modifiedOn** | datetime [0..1] | No | None | Timestamp of the last modification. |
| **scenario** | `ScenarioType [1]` | Yes | `operational` | Defines the operational context of the specification. Can be `operational` or `incident`. The values `resilient` and `not_resilient` are computed and cannot be explicitly set. |

### 3.2. Complete Example of a Valid Metadata Specification

```toml
baseURI = "https://example.org#"
title = "Flood Risk and Resilience Model"
description = "A socio-ecological system model for flood risk and resilience."
version = "1.1"
createdBy = "Pedro Paulo F. Barcelos"
createdOn = "2025-02-10T14:30:00Z"
modifiedOn = "2025-03-01T10:15:00Z"
scenario = "operational"
```
<!-- see example_doc_01 -->

## 4. Defining Constructs

### 4.1 Common Aspects of LaDeRR Constructs

All elements within a LaDeRR specification are instances of **LaderrConstruct**, which serves as the base class for all constructs. This includes **Assets, Capabilities, Vulnerabilities, Threats, Resilience**, and **Control Mechanisms**. Each construct shares a common structure with the following attributes:

- **id** (*string, required, unique*): The unique identifier of the construct. This value is used to reference the construct throughout the specification.
- **label** (*string, required*): A human-readable name for the construct. If not explicitly provided, it defaults to the `id`.
- **description** (*string, optional*): A textual explanation of the construct.

The UML diagram below illustrates the **LaderrConstruct** class and its relationship to other elements.

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/LaderrConstructs.png" width="750"></p>

#### 4.1.1 Example of a General Construct Specification

The following TOML snippet demonstrates how to define constructs using the common attributes.

```toml
[Asset.bridge]
label = "Main River Bridge"
description = "A key transportation infrastructure that requires protection."

[Capability.structural_integrity]
label = "Structural Integrity"
description = "The ability of the bridge to withstand external forces."

[Vulnerability.material_fatigue]
label = "Material Fatigue"
description = "Structural weakening due to repeated stress."

[Threat.earthquake]
label = "Earthquake"
description = "Seismic activity that could compromise the bridge’s structure."

[Resilience.reinforced_design]
description = "A structural reinforcement method to improve resilience."
# Without a defined label, this construct will have 'label = reinforced_design'. The label's default value equals the id.

[Control.maintenance_program]
label = "Routine Maintenance Program"
description = "Scheduled inspections and repairs to prevent material fatigue."
```

#### 4.1.2 Constructs' Attributes

| Attribute      | Type   | Required | Default Value | Description |
|---------------|--------|----------|--------------|-------------|
| **id**        | string | Yes      | None         | Unique identifier for the construct. |
| **label**     | string | No       | Same as `id` | Human-readable name for the construct. |
| **description** | string | No       | None         | Explanation of the construct's role. |

These attributes provide a standardized way to define all constructs, ensuring consistency across LaDeRR specifications. The following subsections detail specific construct types and their additional attributes.


### 4.2 Entities

An **Entity** represents a core component within a LaDeRR specification. Entities can assume different roles in resilience scenarios, including **Assets**, **Threats**, and **Control Mechanisms**. Each entity is associated with **Capabilities** and **Vulnerabilities**, defining its strengths and weaknesses.

The UML diagram below illustrates the **Entity** class and its relationships.

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Entities.png" width="750"></p>

#### 4.2.1 Assets

An **Asset** is an entity that requires protection and plays a crucial role in resilience scenarios. Assets are typically infrastructure, organizations, or systems that must be safeguarded against threats.

##### Additional Attributes of Assets

- **resiliences** (*list of strings, optional*): References to resilience mechanisms protecting the asset.

##### Example of an Asset Specification

```toml
[Asset.power_grid]
label = "Regional Power Grid"
description = "A critical infrastructure providing electricity."
capabilities = ["load_balancing", "fault_tolerance"]
vulnerabilities = ["cyber_attack", "equipment_failure"]
resiliences = ["distributed_generation"]
```

#### 4.2.2 Threats

A **Threat** is an entity that exploits vulnerabilities in assets, challenging their resilience. Threats can be natural, technical, or human-driven.

##### Additional Attributes of Threats

- **threatens** (*list of strings, required*): References to the assets that the threat targets.
- **failedToDamage** (*list of strings, optional*): Assets that the threat attempted but failed to damage.

##### Example of a Threat Specification

```toml
[Threat.hacker_group]
label = "Advanced Persistent Threat Group"
description = "A cybercriminal organization targeting infrastructure."
capabilities = ["cyber_attack"]
threatens = ["power_grid"]
failedToDamage = ["hospital_network"]
```

#### 4.2.3 Control Mechanisms

A **Control** is an entity that mitigates or inhibits threats, preventing them from exploiting vulnerabilities.

##### Additional Attributes of Controls

- **protects** (*list of strings, required*): References to the assets the control safeguards.
- **inhibits** (*list of strings, optional*): References to threats neutralized or reduced by the control.

##### Example of a Control Specification

```toml
[Control.firewall_system]
label = "Network Firewall"
description = "A security system preventing unauthorized access."
capabilities = ["intrusion_prevention"]
protects = ["hospital_network"]
inhibits = ["hacker_group"]
```

These three types of entities define the fundamental actors in LaDeRR resilience scenarios, linking capabilities, vulnerabilities, and resilience mechanisms.


### 4.3 Dispositions

Dispositions represent the inherent tendencies of entities within a LaDeRR specification. They encompass both **Capabilities** (positive dispositions that enable resilience) and **Vulnerabilities** (negative dispositions that introduce risk). These elements are critical for modeling how assets function under different conditions and how they respond to threats.

Each disposition has a **state**, which can be either `enabled` or `disabled`. By default, all dispositions are set to `enabled`, meaning they actively contribute to the resilience or vulnerability of an entity.

The UML diagram below illustrates the **Disposition** metamodel and its relationships with other constructs:

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Dispositions.png" width="750"></p>

#### 4.3.1 Capabilities

A **Capability** is a positive disposition that enables an entity to perform functions that contribute to resilience. Capabilities can sustain resilience mechanisms and disable vulnerabilities. 

##### Additional Attributes of Capabilities

- **state** (*string, required, default: `"enabled"`*): Specifies whether the capability is active (`enabled`) or inactive (`disabled`).
- **sustains** (*list of strings, optional*): References to resilience mechanisms supported by this capability.
- **disables** (*list of strings, optional*): Vulnerabilities that are mitigated by this capability.

##### Example of a Capability Specification

```toml
[Capability.fire_resistance]
label = "Fire Resistance"
description = "An advanced coating that protects against high temperatures."
state = "enabled"
sustains = ["fire_safety_measures"]
disables = ["flammable_material"]
```

#### 4.3.2 Vulnerabilities

A **Vulnerability** is a negative disposition that exposes an entity to threats. Vulnerabilities can be exploited by threats and can expose capabilities that belong to the same entity.

##### Additional Attributes of Vulnerabilities

- **state** (*string, required, default: `"enabled"`*): Specifies whether the vulnerability is active (`enabled`) or has been mitigated (`disabled`).
- **exposes** (*list of strings, required*): References to capabilities that are negatively affected by this vulnerability. A vulnerability can only expose capabilities within the same entity.
- **exploits** (*list of strings, optional*): References to threats that exploit this vulnerability.

##### Example of a Vulnerability Specification

```toml
[Vulnerability.unpatched_software]
label = "Unpatched Software"
description = "A known software vulnerability that can be exploited by attackers."
state = "enabled"
exposes = ["system_integrity"]
exploits = ["malware"]
```

Capabilities and vulnerabilities define the operational characteristics of assets, influencing how resilience mechanisms interact with threats in a LaDeRR specification.


### 4.4 Resilience

**Resilience** represents mechanisms that help preserve capabilities and mitigate the effects of threats and vulnerabilities. Resilience mechanisms act as safeguards that ensure an entity can maintain its functions despite adverse conditions. They can be associated with **Assets**, **Capabilities**, and **Vulnerabilities**, defining structured ways to counteract risks.

The UML diagram below illustrates the **Resilience** construct and its relationships:

<p align="center"><img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Resilience.png" width="750"></p>

#### Attributes and Relationships

A **Resilience** construct is defined by its relationships to other elements:

- **preserves** (*list of strings, required*): The capabilities that are maintained by this resilience mechanism.
- **preservesAgainst** (*list of strings, optional*): Threats that the resilience mechanism helps to counteract.
- **preservesDespite** (*list of strings, optional*): Vulnerabilities that do not compromise the effectiveness of this resilience mechanism.
- **sustains** (*list of strings, optional*): Capabilities that actively support the resilience mechanism.

#### Example of a Resilience Specification

```toml
[Resilience.flood_protection]
label = "Flood Protection Measures"
description = "A set of structural and non-structural measures to prevent flood damage."
preserves = ["housing_infrastructure"]
preservesAgainst = ["river_overflow"]
preservesDespite = ["weak_levees"]
sustains = ["levee_reinforcement"]
```

Resilience mechanisms play a crucial role in ensuring that capabilities remain functional under threat. They provide a structured way to model how systems

## 5. Logical Rules of LaDeRR

In addition to the metamodel, LaDeRR specifications must comply with a set of formal rules that govern the relationships between constructs. These rules ensure logical consistency and define how elements such as capabilities, vulnerabilities, threats, and resilience mechanisms interact within a resilience scenario.

The following rules provide a structured foundation for defining resilience and risk mitigation strategies. Each rule is presented with:
- **A human-readable explanation**: Describing the logic behind the rule.
- **A formal logical representation**: Using first-order logic notation to specify the constraints.

### 5.1 Dispositions and Their Relationships

1. **Enabling and Disabling of Dispositions**  
   If a Disposition disables another Disposition, the first must be in an `ENABLED` state, and the second must be `DISABLED`.  
   **Formal Rule:**  
   $$\forall d1, d2 ( Disposition(d1) \land Disposition(d2) \land disables(d1, d2) \rightarrow state(d1) = ENABLED \land state(d2) = DISABLED )$$  

### 5.2 Entity Interactions

2. **Protection Rule**  
   An entity protects another if and only if the second entity has a Capability that disables a Vulnerability of the first entity.  
   **Formal Rule:**  
   $$\forall o1, o2 ( Entity(o1) \land Entity(o2) \land \exists v1, c2 ( Vulnerability(v1) \land Capability(c2) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land disables(c2, v1) ) \leftrightarrow protects(o2, o1) )$$  

3. **Inhibition Rule**  
   An entity inhibits another if it has a capability that disables a vulnerability, while the inhibited entity has a capability that exploits the same vulnerability.  
   **Formal Rule:**  
   $$\forall o2, o3 ( Entity(o2) \land Entity(o3) \land \exists c2, c3, v1 ( Capability(c2) \land Capability(c3) \land capabilities(o2, c2) \land capabilities(o3, c3) \land Vulnerability(v1) \land disables(c2, v1) \land exploits(c3, v1) ) \leftrightarrow inhibits(o2, o3) )$$  

4. **Threatening Rule**  
   An entity threatens another if and only if it has a Capability that exploits a Vulnerability in the other entity.  
   **Formal Rule:**  
   $$\forall o1, o3 ( Entity(o1) \land Entity(o3) \land \exists v1, c3 ( Vulnerability(v1) \land Capability(c3) \land vulnerabilities(o1, v1) \land capabilities(o3, c3) \land exploits(o3, v1) ) \leftrightarrow threatens(o3, o1) )$$  

### 5.3 Resilience Rules

5. **Resilience Requirement Rule**  
   If an entity has a Capability and a Vulnerability, and another entity has an `ENABLED` Capability that disables the Vulnerability, and the Vulnerability exposes the first entity’s Capability while being exploited by a third entity’s Capability, then there must exist exactly one Resilience construct that preserves the first Capability and is sustained by the second entity’s Capability.  
   **Formal Rule:**  
   $$\forall o1, c1, v1, o2, c2, o3, c3 ( Entity(o1) \land Entity(o2) \land Entity(o3) \land Capability(c1) \land Capability(c2) \land Capability(c3) \land Vulnerability(v1) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land capabilities(o3, c3) \land state(c2) = ENABLED \land disables(c2, v1) \land exposes(v1, c1) \land exploits(c3, v1) \rightarrow \exists! r ( Resilience(r) \land resiliences(o1, r) \land preserves(r, c1) \land preservesAgainst(r, c3) \land preservesDespite(r, v1) \land sustains(c2, r) ) )$$  

### 5.4 Damage Success and Failure

6. **Success of Damage Rule**  
   If an entity succeeds in damaging another, it means the attacking entity has an `ENABLED` Capability that exploits a Vulnerability in the other entity, and both the Capability and Vulnerability are active.  
   **Formal Rule:**  
   $$\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = ENABLED \land state(c2) = ENABLED ) ) \leftrightarrow succeededToDamage(o2, o1) )$$  

7. **Failure of Damage Rule**  
   If an entity fails to damage another, it means the attacking entity’s Capability is `ENABLED`, but the targeted Vulnerability is `DISABLED`.  
   **Formal Rule:**  
   $$\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = DISABLED \land state(c2) = ENABLED ) ) \leftrightarrow failedToDamage(o2, o1) )$$  

### 5.5 Scenario Resilience Determination

8. **Scenario is NOT_RESILIENT Rule**  
   A LaDeRR specification scenario is considered `NOT_RESILIENT` if there is at least one entity that succeeded in damaging another.  
   **Formal Rule:**  
   $$\forall ls ( LaderrSpecification(ls) \land scenario(ls) = NOT_RESILIENT \leftrightarrow \exists o1, o2 ( Entity(o1) \land Entity(o2) \land constructs(ls, o1) \land constructs(ls, o2) \land succeededToDamage(o1, o2) ) )$$  

9. **Scenario is RESILIENT Rule**  
   If a scenario is an `INCIDENT`, and every Vulnerability in its Entities is either `DISABLED`, protected by a Resilience (preservesDespite), or not exploited by any threat, then the scenario is considered `RESILIENT`.  
   **Formal Rule:**  
   $$\forall ls ( LadderSpecification(ls) \land scenario(ls) = INCIDENT \land \neg \exists o1, v1 ( constructs(ls, o1) \land vulnerabilities(o1, v1) \land \neg ( state(v1) = DISABLED \lor \exists r (Resilience(r) \land preservesDespite(r, v1)) \lor \neg \exists c1 (Capability(c1) \land exploits(c1, v1)) ) ) \rightarrow scenario(ls) = RESILIENT )$$  

### 5.6 Vulnerability-Capability Relationship

10. **Vulnerability Exposure Rule**  
   A Vulnerability can expose a Capability only if both belong to the same Entity.  
   **Formal Rule:**  
   $$\forall v, c ( Vulnerability(v) \land Capability(c) \land exposes(v, c) \rightarrow \exists! o ( Entity(o) \land vulnerabilities(o, v) \land capabilities(o, c) ) )$$  

These rules complement the metamodel, ensuring that LaDeRR specifications are logically consistent and that resilience mechanisms, vulnerabilities, and threats interact correctly within the modeled scenarios.


Validation occurs through the **LaDeRR Engine**, which ensures compliance with these constraints.

## 6. LaDeRR Engine

The **LaDeRR Engine** is a Python-based software tool that provides validation and inference capabilities for LaDeRR specifications. It consists of:
- **A library** for programmatic use and integration into applications.
- **A command-line script** for executing and processing LaDeRR models.

The engine ensures that specifications comply with the metamodel rules and derives implicit knowledge based on logical inference. More details about the engine, including installation and usage instructions, can be found at [w3id.org/laderr/engine/git](https://w3id.org/laderr/engine/git).

### 6.1 Writing a LaDeRR Specification with LaDeRR Engine

The LaDeRR Engine allows users to write **simplified** specifications by omitting explicit declarations that can be **inferred** by the system. This reduces the effort needed to create a model while maintaining correctness.

#### 6.1.1 Automatic Inference

The LaDeRR Engine infers various relationships and properties based on the formal rules defined in the LaDeRR framework. Some key inferences include:

1. **Entity Types are Inferred**  
   - Users do not need to specify whether an entity is an **Asset, Threat, or Control**.  
   - The composition of **capabilities, vulnerabilities, and their interplay** determines the entity type.

2. **Default Values are Assigned Automatically**  
   - Attributes with default values do not need to be explicitly written in the specification.  
   - For example, if a `scenario` attribute is missing, it defaults to `"operational"`.

3. **Implicit Relationships are Derived**  
   - Many relations between constructs are inferred instead of being explicitly defined by the user.  
   - Examples:
     - **Protection**: If an entity has a capability that disables a vulnerability in another entity, the **protects** relation is inferred.
     - **Threats**: If an entity has a capability that exploits a vulnerability, the **threatens** relation is inferred.
     - **Resilience Mechanisms are Automatically Created**: If an entity has a **capability** that is at risk due to a **threat exploiting a vulnerability**, and another **capability exists that can sustain resilience**, the **engine automatically introduces a resilience mechanism** to preserve the first capability.

Since resilience inference is a key feature of the LaDeRR Engine, the next subsection describes the conditions under which resilience mechanisms are automatically generated.

#### Automatic Resilience Generation

A key feature of the LaDeRR Engine is its ability to **automatically generate resilience mechanisms** when conditions for resilience exist. Instead of requiring users to explicitly define resilience constructs, the engine:

- **Identifies** when a resilience construct should exist based on the interplay between vulnerabilities, capabilities, and threats.
- **Instantiates** the resilience construct.
- **Establishes the necessary relations**, such as `preserves`, `preservesDespite`, and `preservesAgainst`.

For example, if an **Asset** has a **Capability** that is at risk due to a **Threat exploiting a Vulnerability**, and another **Capability exists that can sustain resilience**, the engine **automatically introduces a resilience mechanism**.

This behavior is formally defined by the **Resilience Requirement Rule** in **Section 5.3 (Resilience Rules)**, which states:

> "If an entity has a **Capability** and a **Vulnerability**, and another entity has an **ENABLED Capability** that disables the Vulnerability, and the Vulnerability exposes the first entity’s Capability while being exploited by a third entity’s Capability, then there must exist exactly **one Resilience construct** that preserves the first Capability and is sustained by the second entity’s Capability."

By leveraging this inference mechanism, users can **omit explicit resilience definitions** in their specifications, allowing the LaDeRR Engine to dynamically determine and instantiate them when applicable. For further details, refer to **Section 5.3**.


#### 6.1.3 Simplified Specification Example

A **manually defined** LaDeRR specification might look like this:

```toml
[Asset.bridge]
label = "Main River Bridge"
description = "A key infrastructure requiring protection."
capabilities = ["structural_integrity"]
vulnerabilities = ["material_fatigue"]

[Capability.structural_integrity]
label = "Structural Integrity"
description = "Ability to withstand forces."
disables = ["material_fatigue"]

[Vulnerability.material_fatigue]
label = "Material Fatigue"
description = "Structural weakening due to repeated stress."

[Threat.earthquake]
label = "Earthquake"
capabilities = ["seismic_force"]
threatens = ["bridge"]

[Capability.seismic_force]
label = "Seismic Force"
description = "High-intensity vibrations that stress structures."
exploits = ["material_fatigue"]

[Resilience.reinforced_design]
label = "Reinforced Design"
preserves = ["structural_integrity"]
preservesDespite = ["material_fatigue"]
```

However, when using **LaDeRR Engine**, the user can omit explicitly defining inferred relations, such as `threatens` and `protects`, and even the **Resilience construct itself**, as the **engine** will infer and generate it when applicable.

A **simplified version** of the specification:

```toml
[Asset.bridge]
capabilities = ["structural_integrity"]
vulnerabilities = ["material_fatigue"]

[Capability.structural_integrity]
disables = ["material_fatigue"]

[Vulnerability.material_fatigue]

[Threat.earthquake]
capabilities = ["seismic_force"]

[Capability.seismic_force]
exploits = ["material_fatigue"]
```

In this version:
- **The resilience mechanism (`reinforced_design`) is omitted** because the engine can infer its existence.
- **Unnecessary attributes** such as `label` and `description` are omitted.
- **Relations like "threatens" and "protects" are inferred** automatically.
- **Scenario resilience is evaluated dynamically**.

### 6.2 Engine Output and Inferred Model

When processed by **LaDeRR Engine**, the missing relations and resilience mechanisms are inferred, producing an expanded version of the specification. The resulting enriched model includes:
- **Threats are automatically linked to assets** (e.g., `threatens` relation is inferred between `earthquake` and `bridge`).
- **Protection relations are established** (e.g., `structural_integrity` protecting `bridge`).
- **Resilience mechanisms are instantiated** if the model meets the resilience conditions.
- **Scenario resilience is evaluated**, determining if threats are effectively mitigated.

This makes the **LaDeRR Engine** a powerful tool for simplifying specifications while ensuring correctness through logical inference.

## 7. Complete Example

This section provides a complete LaDeRR specification example. The first version explicitly defines all relevant elements, while the second version demonstrates how the **LaDeRR Engine** infers implicit relationships and resilience mechanisms.

### 7.1 Explicit Specification

The following specification fully defines an **operational** scenario, explicitly declaring all relationships.

```toml
baseURI = "https://example.org#"
createdBy = "Author Name"
createdOn = "2025-02-10T14:30:00Z"
description = "Example resilience model."
scenario = "operational"
title = "Example Model"
version = "1.1"

[Asset.city]
capabilities = ["defense_system"]
resiliences = ["resilience1"]
vulnerabilities = ["cyber_attack"]

[Capability.defense_system]
disables = ["cyber_attack"]
state = "enabled"

[Vulnerability.cyber_attack]
exposes = ["defense_system"]
state = "enabled"

[Threat.hacker_group]
capabilities = ["hacking"]
threatens = ["city"]

[Capability.hacking]
exploits = ["cyber_attack"]

[Resilience.resilience1]
preserves = ["defense_system"]
preservesDespite = ["cyber_attack"]
preservesAgainst = ["hacker_group"]
```

### 7.2 Simplified Specification with LaDeRR Engine

Using the **LaDeRR Engine**, users can omit certain elements that are **automatically inferred**. The engine derives **threats, protections, and resilience mechanisms** based on the existing capabilities, vulnerabilities, and their interactions.

```toml
baseURI = "https://example.org#"
createdBy = "Author Name"
createdOn = "2025-02-10T14:30:00Z"
scenario = "operational"
title = "Example Model"
version = "1.1"

[Asset.city]
capabilities = ["defense_system"]
vulnerabilities = ["cyber_attack"]

[Capability.defense_system]
disables = ["cyber_attack"]

[Vulnerability.cyber_attack]

[Threat.hacker_group]
capabilities = ["hacking"]

[Capability.hacking]
exploits = ["cyber_attack"]
```

### 7.3 Inferred Output by LaDeRR Engine

When processed by the **LaDeRR Engine**, the simplified specification is expanded, adding inferred relationships and resilience constructs:

- **Resilience mechanisms are created** when conditions for resilience are met.
- **Threats are linked to their target assets** (e.g., `threatens` relation is inferred between `hacker_group` and `city`).
- **Protection mechanisms are inferred** if a capability neutralizes a vulnerability.
- **Scenario resilience is evaluated**.

The resulting expanded model ensures consistency with the LaDeRR framework while reducing manual specification effort.
