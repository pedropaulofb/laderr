# How to Write LaDeRR Specifications

**WORK IN PROGRESS: PLEASE BE AWARE THAT THIS DOCUMENT IS STILL UNDER DEVELOPMENT. USE IT CAREFULLY.**

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. General Structure of a LaDeRR Specification](#2-general-structure-of-a-laderr-specification)
  - [2.1. Access to LaDeRR Specification Examples and Results](#21-access-to-laderr-specification-examples-and-results)
- [3. Specification Metadata](#3-specification-metadata)
  - [3.1. Required Fields and Defaults](#31-required-fields-and-defaults)
  - [3.2. Scenario Classification and Determination](#32-scenario-classification-and-determination)
  - [3.3. Example of a Valid Metadata Specification](#33-example-of-a-valid-metadata-specification)
- [4. Defining Constructs](#4-defining-constructs)
  - [4.1. Common Aspects of LaDeRR Constructs](#41-common-aspects-of-laderr-constructs)
  - [4.2. Entities](#42-entities)
  - [4.3. Dispositions](#43-dispositions)
  - [4.4. Resilience](#44-resilience)
- [5. LaDeRR Engine](#5-laderr-engine)
  - [5.1. Writing a LaDeRR Specification with LaDeRR Engine](#51-writing-a-laderr-specification-with-laderr-engine)
  - [5.2. Engine Output and Inferred Model](#52-engine-output-and-inferred-model)
- [6. Complete Example](#6-complete-example)
  - [6.1. Explicit Specification](#61-explicit-specification)
  - [6.2. Simplified Specification with LaDeRR Engine](#62-simplified-specification-with-laderr-engine)
  - [6.3. Inferred Output by LaDeRR Engine](#63-inferred-output-by-laderr-engine)

## 1. Introduction

The [Language for Describing Risk and Resilience (LaDeRR)](https://w3id.org/laderr/git) is an ontology-based domain-specific language (DSL) designed to specify resilience scenarios. Built over [ResiliOnt](https://github.com/pedropaulofb/resiliont/), it provides a structured approach to defining entities, capabilities, vulnerabilities, and their interrelations.

This document serves as a guide for writing LaDeRR specifications using its concrete syntax in [TOML format](https://toml.io/en/). It outlines the essential components, rules, and best practices for creating valid specifications. Each section introduces a key concept of the LaDeRR language, presents its corresponding metamodel representation, explains any associated logical rules, and provides a concrete example of how to specify it in practice.

The LaDeRR metamodel defines the core structural elements of the language, establishing the conceptual foundation for resilience and risk scenario modeling. It is presented in separate UML class diagrams, each representing a distinct aspect of LaDeRR.

In the following sections, we will cover all core elements of a LaDeRR specification. Each component will be accompanied by:

- **Concept Overview**: A brief explanation of the purpose and role of the component within a LaDeRR specification.
- **Metamodel Representation**: A UML class diagram illustrating the structure and relationships of the language's elements.
- **Rules and Constraints (if applicable)**: Formal constraints and derivations governing the use of the component.
- **Specification Example**: A LaDeRR specification snippet in TOML format, demonstrating a correct way to specify the component.

The UML metamodel follows a color-coding and formatting scheme:

- **Blue**: Represents classes that are defined within the specific diagram being presented.
- **Gray**: Represents classes that are defined in other diagrams and are shown only to indicate relationships.
- **White**: Represents enumerations, which define a set of predefined values.
- **Red**: Represents notes that provide additional constraints, rules, or clarifications.

## 2. General Structure of a LaDeRR Specification

A LaDeRR specification defines **resilience scenarios** using a structured format that consists of two main components:

- **Metadata**: Provides general information about the specification, including authorship, versioning, and the type of the resilience scenario being specified.
- **Constructs**: Define the elements of the resilience scenario and their relationships. The main constructs include:
  - **Assets**: Represent entities that have value and are subject to potential risks and threats.
  - **Capabilities**: Define the "positive" dispositions of an entity, enabling the entity to perform specific functions.
  - **Vulnerabilities**: Represent weaknesses that can be exploited by threats.
  - **Threats**: Entities with capabilities that can exploit vulnerabilities.
  - **Resilience**: Resilience preserves an entity's value despite vulnerabilities, preventing threats from causing damage.
  - **Control**: Entities that inhibit threats, creating resilience.

Each construct is interconnected, governed by logical constraints. These constraints ensure consistency and are enforced through formal rules, as described in Section 5. The following sections detail each construct, presenting its concept, metamodel representation, applicable rules, and an example of how to specify it in a LaDeRR model.

### 2.1. Access to LaDeRR Specification Examples and Results

All LaDeRR specifications presented in this document, including every example and fragment, are available in the [examples](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples) folder of the LaDeRR repository.

For each LaDeRR specification included in this documentation, the following additional resources are provided:

- The original specification TOML file, as presented in this document.
- Validation and inference reports:
  - Pre-Inference Validation: Ensures that the input specification conforms to the LaDeRR metamodel and does not contain missing required fields or incorrect relationships.
  - Post-Inference Validation: After inference, checks that the inferred constructs and relationships maintain logical consistency within the model.
- The generated graph data:
  - The graph structure before inference.
  - The graph structure after inference.
- Graph-based visualizations of the specification:
  - A visualization of the graph before inference.
  - A visualization of the graph after inference.

These resources allow users to verify how the [**LaDeRR Engine**](#5-laderr-engine) interprets and processes each specification. Links to these files are provided alongside the corresponding examples in this documentation.

## 3. Specification Metadata

The metadata defines global properties of a LaDeRR specification. These fields establish essential information about the specification, including its identity, authorship, and the type of the resilience scenario being described. The UML diagram below illustrates the metadata structure:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/LaderrSpecification.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

### 3.1. Required Fields and Defaults

| Field           | Input Type                       | Converted Type | Multiplicity | Required | Default Value            | Description                                                                                                                                                                 |
| --------------- | -------------------------------- | -------------- | ------------ | -------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **baseURI**     | string                           | URIRef         | [1]          | **Yes**  | `https://laderr.laderr#` | Unique identifier for the specification. Must be a valid URI.                                                                                                               |
| **createdBy**   | string \| list[string]           | list[string]   | [1..*]       | **Yes**  | N/A                      | Author(s) responsible for the specification. If a single string is provided, it will be converted into a list.                                                              |
| **createdOn**   | datetime (TOML native) \| string | xsd:dateTime   | [1]          | **Yes**  | N/A                      | Creation timestamp. Must comply with `xsd:dateTime` format. See [time format documentation](https://github.com/pedropaulofb/laderr/blob/main/documentation/time_format.md). |
| **description** | string                           | string         | [0..1]       | No       | N/A                      | Explanation of the specification.                                                                                                                                           |
| **modifiedOn**  | datetime (TOML native) \| string | xsd:dateTime   | [0..1]       | No       | N/A                      | Timestamp of the last modification. Must comply with `xsd:dateTime` format.                                                                                                 |
| **scenario**    | string                           | `ScenarioType` | [1]          | **Yes**  | `operational`            | Defines the context of the specification. More information in [subsection 3.2.](#32-scenario-classification-and-determination)                                              |
| **title**       | string                           | string         | [1]          | **Yes**  | N/A                      | Title of the specification.                                                                                                                                                 |
| **version**     | string                           | string         | [1]          | **Yes**  | N/A                      | Version identifier of the specification (free string format, no validation enforced).                                                                                       |

An [additional documentation is provided](https://github.com/pedropaulofb/laderr/blob/main/documentation/time_format.md) to present the correct way to write time formats for the metadata `createdOn` and `modifiedOn`.

Regarding the _constructs_ relation between a LaderrSpecification and LaderrConstructs, the list of constructs in a specification is formed through the instantiation of the elements being specified. This means that users do not need to explicitly define this relation within the specification itself, as it is inherently derived from the instantiation process, being managed internally.

### 3.2. Scenario Classification and Determination

The `LaderrSpecification`'s attribute `scenario` (mandatory) defines the context in which the specified system is analyzed. It represents the moment in time that the system is being considered. The possible values for `scenario` are divided into two groups:

- **OPERATIONAL**: Represents an ongoing or regular situation. It is not necessarily related to threats, failures, or risks, but describes the system as it is functioning in normal conditions.
- **INCIDENT**: Represents a past situation, meaning an event has already occurred. In this context, the system either demonstrates resilience or does not.

If the `scenario` of a specification is set to `INCIDENT`, it must ultimately be classified as either `RESILIENT` or `NOT_RESILIENT`, but never both. The `INCIDENT` value is used when it is unknown whether the system is resilient or not, or when this classification is left to be determined automatically by the LaDeRR Engine (see [Section 5](#5-laderr-engine)).

#### Rules Governing Scenarios

The following rules define the `scenario` values and how they are determined.

- **Rule 1: A system is NOT_RESILIENT if damage has succeeded**

If a LaDeRR specification is `NOT_RESILIENT`, then there must exist at least one pair of entities within it where one has successfully damaged the other.

**FOL Representation:**

$$
\forall ls ( LaderrSpecification(ls) \land scenario(ls) = NOT_RESILIENT \leftrightarrow \exists o1, o2 ( Entity(o1) \land Entity(o2) \land constructs(ls, o1) \land constructs(ls, o2) \land succeededToDamage(o1, o2) ) )
$$

- **Rule 2: A system is RESILIENT if all vulnerabilities are mitigated**

If a LaDeRR specification is in the `INCIDENT` state and there is no vulnerability left unaddressed (i.e., all vulnerabilities are either disabled or not actively exploited), then the system is classified as `RESILIENT`.

**FOL Representation:**

$$
\forall ls ( LadderSpecification(ls) \land scenario(ls) = INCIDENT \land \neg \exists o1, v1 ( constructs(ls, o1) \land vulnerabilities(o1, v1) \land \neg ( state(v1) = DISABLED \lor \neg \exists c1 (Capability(c1) \land exploits(c1, v1)) ) ) \rightarrow scenario(ls) = RESILIENT )
$$

- **Rule 3: An INCIDENT must be either RESILIENT or NOT_RESILIENT**

For every LaDeRR specification, if its `scenario` is `INCIDENT`, then it must be classified as either `RESILIENT` or `NOT_RESILIENT`, but never both.

**FOL Representation:**

$$
\forall ls ( LaderrSpecification(ls) \rightarrow ( scenario(ls) = INCIDENT \rightarrow scenario(ls) = RESILIENT \oplus scenario(ls) = NOT_RESILIENT ) )
$$

### 3.3. Example of a Valid Metadata Specification

[**Example 01:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

Note that a specification containing only metadata is considered valid.

From this point onward, assume that a brief metadata is appended at the beginning of all following examples. To maintain conciseness, the metadata TOML section will be omitted in the next specification excerpts.

## 4. Defining Constructs

### 4.1. Common Aspects of LaDeRR Constructs

All elements within a LaDeRR specification are instances of **LaderrConstruct**, which serves as the base class for all constructs. This includes **Assets, Capabilities, Vulnerabilities, Threats, Resilience**, and **Control**. Each construct shares a common structure with the following attributes:

- **id** (_string, required, unique_): The unique identifier of the construct. This value is used to reference the construct throughout the specification.
- **label** (_string, optional_): A human-readable name for the construct. If not explicitly provided, it defaults to the `id` value.
- **description** (_string, optional_): A textual explanation of the construct.

The UML diagram below illustrates the **LaderrConstruct** class and its specializations.

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/LaderrConstructs.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

#### Example of a General Construct Specification

The following TOML snippet demonstrates how to define constructs using the common attributes.

[**Example 02:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

[Control.maintenance_program]
label = "Routine Maintenance Program"
description = "Scheduled inspections and repairs to prevent material fatigue."
```

In the specification above, note that without a defined label, the declared `reinforced_design` construct will have 'label = reinforced_design'. The label's default value equals the id.

### 4.2. Entities

An **Entity** represents a fundamental component within a LaDeRR specification, participating in resilience scenarios. Entities are classified into one or more of the types: **Assets**, **Threats**, and **Controls**. Each type plays a distinct role in modeling vulnerabilities, risks, and protective mechanisms.

Entities are characterized by their **Capabilities** and **Vulnerabilities**, defining their strengths and weaknesses in a given scenario. **Assets** are entities that require protection and may exhibit resilience. **Threats** attempt to exploit vulnerabilities within assets, potentially causing damage. **Controls** serve as protective mechanisms, mitigating the impact of threats by inhibiting their actions or neutralizing vulnerabilities.

The UML diagram below illustrates the **Entity** class, its subtypes, and their relationships.

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Entities.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

#### Fields of Entities

- **capabilities** (_list of strings, required_): Defines the set of functions or strengths the entity possesses.
- **vulnerabilities** (_list of strings, optional_): Represents the weaknesses that can be exploited by threats.

#### Assets

An **Asset** is an entity of value that must be safeguarded against potential threats. Assets possess **capabilities**, which define their functions or operational strengths, and **vulnerabilities**, which represent weaknesses that threats can exploit. Assets can be **threatened** by threats and **protected** by controls.

Examples of assets include a _regional power grid_, which ensures electricity supply but may be vulnerable to cyberattacks and infrastructure failures; a _hospital network_, which provides medical services but is susceptible to data breaches and equipment malfunctions; a _coral reef ecosystem_, which supports marine biodiversity but faces risks from ocean acidification and climate change; a _financial market system_, which enables global trade but is exposed to economic downturns and cyber fraud; and a _public transportation network_, which facilitates mobility but can be disrupted by mechanical failures and extreme weather events.

##### Additional Fields of Assets

- **resiliences** (_list of strings, optional_): References to resiliences protecting the asset's capabilities.

The LaDeRR Engine is capable of automatically detecting and associating resilience instances with assets based on system-wide analysis. Therefore, explicitly declaring resiliences is optional, as they will be inferred and correctly linked within the system.

##### Example of an Asset Specification

[**Example 03:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Asset.power_grid]
label = "Regional Power Grid"
description = "A critical infrastructure providing electricity."
capabilities = ["load_balancing", "fault_tolerance"]
vulnerabilities = ["cyber_attack", "equipment_failure"]
resiliences = ["distributed_generation"]
```

#### Threats

A **Threat** is an entity that actively exploits vulnerabilities in assets, potentially leading to harm. Threats can emerge from human actions, technical failures, or natural events. They attempt to compromise an asset’s resilience and can be inhibited by controls.

Examples of threats include a _cybercriminal group_, launching ransomware attacks to compromise data security; an _infectious disease outbreak_, spreading through populations and threatening public health infrastructure; an _oil spill_, contaminating marine ecosystems and disrupting local economies; a _social misinformation campaign_, influencing political outcomes and destabilizing trust in institutions; and an _earthquake_, damaging critical infrastructure and causing widespread economic losses.

##### Additional Fields of Threats

- **threatens** (_list of strings, required_): References to the assets that the threat targets. _(Automatically inferred when using LaDeRR Engine.)_
- **succeededToDamage** (_list of strings, optional_): Assets that the threat successfully damaged. This is automatically determined based on the scenario. _(Automatically inferred when using LaDeRR Engine.)_
- **failedToDamage** (_list of strings, optional_): Assets that the threat attempted but failed to damage. This is automatically determined based on the scenario. _(Automatically inferred when using LaDeRR Engine.)_

The relationships between threats and assets—whether a threat targets, successfully damages, or fails to damage an asset—can be inferred from the underlying interactions between capabilities and vulnerabilities. When using LaDeRR Engine, these relations do not need to be explicitly declared, as they will be automatically derived based on the system's defined capabilities, vulnerabilities, and their interactions.

If the scenario is **RESILIENT**, all damage attempts by threats result in `failedToDamage`. If the scenario is **NOT_RESILIENT**, some threats will have `succeededToDamage` relationships with assets.

##### Rules Governing Threats

- **Rule 1: A Threat succeeds in damaging an Asset if it exploits an enabled vulnerability**
  A threat is considered to have successfully damaged an asset if it possesses a capability that exploits a vulnerability in the asset, the vulnerability is enabled, and it exposes an essential capability of the asset.

**FOL Representation:**

$$
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = ENABLED \land state(c2) = ENABLED ) ) \leftrightarrow succeededToDamage(o2, o1) )
$$

- **Rule 2: A Threat fails to damage an Asset if the exploited vulnerability is disabled**
  A threat fails to cause damage if the vulnerability it exploits is disabled, meaning the exploit does not lead to a loss of the asset’s essential capability.

**FOL Representation:**

$$
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = DISABLED \land state(c2) = ENABLED ) ) \leftrightarrow failedToDamage(o2, o1) )
$$

##### Example of a Threat Specification

[**Example 04:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Threat.hacker_group]
label = "Advanced Persistent Threat Group"
description = "A cybercriminal organization targeting infrastructure."
capabilities = ["cyber_attack"]
threatens = ["power_grid"]
failedToDamage = ["hospital_network"]
```

#### Controls

A **Control** is an entity that actively mitigates threats or neutralizes vulnerabilities, thereby reducing risk. Controls **inhibit** threats, preventing them from successfully exploiting vulnerabilities in assets. Controls play a proactive role in resilience by providing protective mechanisms that prevent losses before they occur.

Examples of controls include a _network firewall_, which prevents unauthorized access to hospital systems; a _vaccination program_, which mitigates the spread of infectious diseases in a population; a _marine protected area_, safeguarding coral reefs from overfishing and habitat destruction; an _algorithmic fraud detection system_, identifying suspicious transactions in financial markets; and an _early warning system for natural disasters_, enabling rapid response to earthquakes and hurricanes.

##### Additional Fields of Controls

- **protects** (_list of strings, required_): References to the assets the control safeguards. _(Automatically inferred when using LaDeRR Engine.)_
- **inhibits** (_list of strings, required_): References to threats that are neutralized or reduced by the control. _(Automatically inferred when using LaDeRR Engine.)_

The relationships between controls, assets, and threats—whether a control protects an asset or inhibits a threat—can be inferred from the underlying interactions between capabilities and vulnerabilities. When using LaDeRR Engine, these relations do not need to be explicitly declared, as they will be automatically derived based on the system’s defined capabilities, vulnerabilities, and their interactions.

##### Example of a Control Specification

[**Example 05:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Control.firewall_system]
label = "Network Firewall"
description = "A security system preventing unauthorized access."
capabilities = ["intrusion_prevention"]
protects = ["hospital_network"]
inhibits = ["hacker_group"]
```

#### Rules Governing Entity Relationships

- **Rule 1: An Entity protects another if it disables a vulnerability**
  A control or another entity is said to protect an asset if it possesses a capability that disables a vulnerability in that asset.

**FOL Representation:**

$$
\forall o1, o2 ( Entity(o1) \land Entity(o2) \land \exists v1, c2 ( \land Vulnerability(v1) \land Capability(c2) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land disables(c2, v1) ) \leftrightarrow protects(o2, o1) )
$$

- **Rule 2: An Entity inhibits another if it neutralizes an exploited vulnerability**
  An entity inhibits another if it has a capability that disables a vulnerability, while the inhibited entity has a capability that exploits the same vulnerability.

**FOL Representation:**

$$
\forall o2, o3 ( Entity(o2) \land Entity(o3) \land \exists c2, c3, v1 ( \land Capability(c2) \land Capability(c3) \land capabilities(o2, c2) \land capabilities(o3, c3) \land Vulnerability(v1) \land disables(c2, v1) \land exploits(c3, v1) ) \leftrightarrow inhibits(o2, o3) )
$$

- **Rule 3: A Threat threatens an Asset if it exploits a vulnerability**
  A threat entity is said to threaten an asset if it has a capability that exploits a vulnerability within the asset.

**FOL Representation:**

$$
\forall o1, o3 ( Entity(o1) \land Entity(o3) \land ( \exists v1, c3 ( Vulnerability(v1) \land Capability(c3) \land vulnerabilities(o1, v1) \land capabilities(o3, c3) \land exploits(c3, v1) ) \leftrightarrow threatens(o3, o1) ) )
$$

### 4.3. Dispositions

Dispositions represent the inherent properties of entities within a LaDeRR specification that determine how they respond to changing conditions. They are divided into **Capabilities**, which represent positive dispositions that enable resilience, and **Vulnerabilities**, which represent negative dispositions that introduce risk. These elements are crucial for modeling how assets function under different conditions and how they interact with threats and controls.

Each disposition has a **state**, which can be either `enabled` or `disabled`. By default, all dispositions are set to `enabled`, meaning they actively contribute to the resilience or vulnerability of an entity. The state of a disposition influences whether it can be exploited or used to protect against threats.

- **state** (_string, optional, default: `"enabled"`_): Specifies whether the capability is active (`enabled`) and can perform its functions or inactive (`disabled`) and cannot affect its related elements.

#### Rules Governing Dispositions

- **Rule 1: A Disposition that disables another must be enabled**
  A disposition can only disable another if it is enabled, ensuring that only active dispositions can influence the system's resilience.

**FOL Representation:**

$$
\forall d1, d2 ( Disposition(d1) \land Disposition(d2) \land disables(d1, d2) \rightarrow state(d1) = ENABLED \land state(d2) = DISABLED )
$$

The UML diagram below illustrates the **Disposition** metamodel and its relationships with other constructs:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Dispositions.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

#### Capabilities

A **Capability** is a positive disposition that enables an entity to perform specific functions that contribute to resilience. Capabilities can **sustain resilience mechanisms**, ensuring the stability of an entity under adverse conditions, and can **disable vulnerabilities**, preventing them from being exploited by threats.

Examples of capabilities include **fire resistance in building materials**, which prevents the spread of flames during a fire; **immune response in living organisms**, which helps fight infections and maintain health; **automated failover in cloud computing**, which ensures system continuity in case of a server failure; **adaptive governance in socio-ecological systems**, which allows communities to respond to environmental changes; and **reinforced structural design in engineering**, which enhances resistance against natural disasters.

##### Additional Fields of Capabilities

- **exploits** (_list of strings, optional_): Active vulnerabilities. Defines an Entity as a Threat.
- **disables** (_list of strings, optional_): Vulnerabilities that are mitigated by this capability.
- **sustains** (_list of strings, optional_): References to resiliences supported by this capability. _(Automatically inferred when using LaDeRR Engine.)_

##### Example of a Capability Specification

[**Example 06:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Capability.fire_resistance]
label = "Fire Resistance"
description = "An advanced coating that protects against high temperatures."
state = "enabled"
sustains = ["fire_safety_measures"]
disables = ["flammable_material"]
```

#### Vulnerabilities

A **Vulnerability** is a negative disposition that makes an entity susceptible to threats. Vulnerabilities can be **exploited by threats**, potentially leading to damage, and can **expose capabilities** within the same entity, increasing the likelihood of operational failure.

Examples of vulnerabilities include **unpatched software**, which exposes systems to cyberattacks; **immune deficiencies in biological organisms**, making them susceptible to infections; **structural fatigue in engineering**, reducing the durability of infrastructure over time; **financial instability in economic systems**, making institutions vulnerable to market fluctuations; and **data breaches in digital networks**, leading to loss of sensitive information.

##### Additional Fields of Vulnerabilities

- **state** (_string, required, default: `"enabled"`_): Specifies whether the vulnerability is active (`enabled`) or has been mitigated (`disabled`).
- **exposes** (_list of strings, required_): References to capabilities that are negatively affected by this vulnerability. A vulnerability can only expose capabilities within the same entity.
- **exploits** (_list of strings, optional_): References to threats that exploit this vulnerability. _(Automatically inferred when using LaDeRR Engine.)_

#### Rules Governing Vulnerabilities

- **Rule 2: A Vulnerability can only expose Capabilities of the same Entity**
  A vulnerability must belong to the same entity as the capabilities it exposes, ensuring that resilience and threats are properly linked.

**FOL Representation:**

$$
\forall v, c ( Vulnerability(v) \land Capability(c) \land exposes(v, c) \rightarrow \exists! o ( Entity(o) \land vulnerabilities(o, v) \land capabilities(o, c) ) )
$$

##### Example of a Vulnerability Specification

[**Example 07:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Vulnerability.unpatched_software]
label = "Unpatched Software"
description = "A known software vulnerability that can be exploited by attackers."
state = "enabled"
exposes = ["system_integrity"]
exploits = ["malware"]
```

Capabilities and vulnerabilities define the operational characteristics of assets, influencing how resilience mechanisms interact with threats in a LaDeRR specification. The LaDeRR Engine automatically determines resilience relations, meaning explicit declarations of resilience-related attributes are optional when using the system.

### 4.4. Resilience

**Resilience** represents the mechanisms that enable entities to withstand adverse conditions, preserving capabilities, and mitigating the effects of threats. It serves as a fundamental aspect of maintaining system functionality against disruptions. Resilience mechanisms are associated with Assets, Capabilities, and Vulnerabilities, establishing structured ways to counteract risks and enhance stability.

When using the **LaDeRR Engine**, explicit declarations of resilience mechanisms are unnecessary. The tool automatically infers resilience relationships based on the capabilities, vulnerabilities, and threats defined in the scenario, identifying and structuring resilience mechanisms accordingly.

The UML diagram below illustrates the Resilience construct and its relationships:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Resilience.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

#### Fields of Resilience

A Resilience** construct is defined by its relationships to other elements:

- **preserves** (_list of strings, required_): The capabilities that are maintained by this resilience mechanism. _(Automatically inferred when using LaDeRR Engine.)_
- **preservesAgainst** (_list of strings, required_): Threats that the resilience mechanism helps to counteract. _(Automatically inferred when using LaDeRR Engine.)_
- **preservesDespite** (_list of strings, required_): Vulnerabilities that do not compromise the effectiveness of this resilience mechanism. _(Automatically inferred when using LaDeRR Engine.)_

#### Rules Governing Resilience

- **Rule 1: Resilience Emerges from a Specific Configuration of Entities and Dispositions**
  A resilience instance is created only if the following conditions hold:
- An entity possesses a capability that is at risk due to a vulnerability.
- A second entity has a capability that is **enabled** and mitigates the vulnerability.
- A third entity has a capability that exploits the vulnerability.
- The resilience preserves the first entity’s capability, preserves against the third entity’s capability, preserves despite the vulnerability, and is sustained by the second entity’s capability.

**FOL Representation:**

$$
\forall o1, c1, v1, o2, c2, o3, c3 (
  Entity(o1) \land Entity(o2) \land Entity(o3) \land
  Capability(c1) \land Capability(c2) \land Capability(c3) \land Vulnerability(v1) \land
  capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land
  capabilities(o3, c3) \land state(c2) = ENABLED \land disables(c2, v1) \land
  exposes(v1, c1) \land exploits(c3, v1)
  \rightarrow
  \exists! r ( Resilience(r) \land resiliences(o1, r) \land preserves(r, c1) \land
  preservesAgainst(r, c3) \land preservesDespite(r, v1) \land sustains(c2, r) )
)
$$

- **Rule 2: Each Resilience is Defined by a Unique Combination of Elements**
  For each resilience instance, there exists exactly one configuration of an entity, three capabilities, and a vulnerability that justify its existence:
- The entity possessing resilience must have both the preserved capability and the vulnerability.
- A second entity must have an **enabled** capability that disables the vulnerability.
- A third entity must have a capability that exploits the vulnerability.
- The resilience mechanism must preserve the first entity’s capability, counteract the third entity’s capability, withstand the vulnerability, and be sustained by the second entity’s capability.

**FOL Representation:**

$$
\forall r ( Resilience(r) \rightarrow
  \exists! o1, \exists c1, v1, o2, c2, o3, c3 (
    resiliences(o1, r) \land preserves(r, c1) \land preservesAgainst(r, c3) \land
    preservesDespite(r, v1) \land sustains(c2, r) \land
    Entity(o1) \land Entity(o2) \land Entity(o3) \land
    Capability(c1) \land Capability(c2) \land Capability(c3) \land Vulnerability(v1) \land
    capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land
    capabilities(o3, c3) \land state(c2) = ENABLED \land disables(c2, v1) \land
    exposes(v1, c1) \land exploits(c3, v1)
  )
)
$$

#### Example of a Resilience Specification

[**Example 08:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

```toml
[Resilience.flood_protection]
label = "Flood Protection Measures"
description = "A set of structural and non-structural measures to prevent flood damage."
preserves = ["housing_infrastructure"]
preservesAgainst = ["river_overflow"]
preservesDespite = ["weak_levees"]
sustains = ["levee_reinforcement"]
```

## 5. LaDeRR Engine

The **LaDeRR Engine** is a Python-based software tool that provides validation and inference capabilities for LaDeRR specifications. It consists of:

- **A library** for programmatic use and integration into applications.
- **A command-line script** for executing and processing LaDeRR models.

The engine ensures that specifications comply with the metamodel rules and derives implicit knowledge based on logical inference. More details about the engine, including installation and usage instructions, can be found at [w3id.org/laderr/engine/git](https://w3id.org/laderr/engine/git).

### 5.1. Writing a LaDeRR Specification with LaDeRR Engine

The LaDeRR Engine allows users to write **simplified** specifications by omitting explicit declarations that can be **inferred** by the system. This reduces the effort needed to specify a resilience scenario while maintaining correctness.

#### Automatic Inference

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

4. **Resilience Mechanisms are Automatically Created**

    - If an entity has a **capability** that is at risk due to a **threat exploiting a vulnerability**, and another **capability exists that can sustain resilience**, the **engine automatically introduces a resilience mechanism** to preserve the first capability.

Since resilience inference is a key feature of the LaDeRR Engine, the next subsection describes the conditions under which resilience mechanisms are automatically generated.

#### Automatic Resilience Generation

A key feature of the LaDeRR Engine is its ability to **automatically generate resilience mechanisms** when conditions for resilience exist. Instead of requiring users to explicitly define resilience constructs, the engine:

- **Identifies** when a resilience construct should exist based on the interplay between vulnerabilities, capabilities, and threats.
- **Instantiates** the resilience construct.
- **Establishes the necessary relations**, such as `preserves`, `preservesDespite`, and `preservesAgainst`.

For example, if an **Asset** has a **Capability** that is at risk due to a **Threat exploiting a Vulnerability**, and another **Capability exists that can sustain resilience**, the engine **automatically introduces a resilience mechanism**.

This behavior is formally defined by the **Resilience Requirement Rule** in **Section (Resilience Rules)**, which states:

> "If an entity has a **Capability** and a **Vulnerability**, and another entity has an **ENABLED Capability** that disables the Vulnerability, and the Vulnerability exposes the first entity’s Capability while being exploited by a third entity’s Capability, then there must exist exactly **one Resilience construct** that preserves the first Capability and is sustained by the second entity’s Capability."

By leveraging this inference mechanism, users can **omit explicit resilience definitions** in their specifications, allowing the LaDeRR Engine to dynamically determine and instantiate them when applicable.

#### Simplified Specification Example

A **manually defined** LaDeRR specification might look like this:

[**Example 09:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

[**Example 10:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

### 5.2. Engine Output and Inferred Model

When processed by **LaDeRR Engine**, the missing relations and resilience mechanisms are inferred, producing an expanded version of the specification. The resulting enriched model includes:

- **Threats are automatically linked to assets** (e.g., `threatens` relation is inferred between `earthquake` and `bridge`).
- **Protection relations are established** (e.g., `structural_integrity` protecting `bridge`).
- **Resilience mechanisms are instantiated** if the model meets the resilience conditions.
- **Scenario resilience is evaluated**, determining if threats are effectively mitigated.

This makes the **LaDeRR Engine** a powerful tool for simplifying specifications while ensuring correctness through logical inference.

## 6. Complete Example

This section provides a complete LaDeRR specification example. The first version explicitly defines all relevant elements, while the second version demonstrates how the **LaDeRR Engine** infers implicit relationships and resilience mechanisms.

### 6.1. Explicit Specification

The following specification fully defines an **operational** scenario, explicitly declaring all relationships.

[**Example 11:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

### 6.2. Simplified Specification with LaDeRR Engine

Using the **LaDeRR Engine**, users can omit certain elements that are **automatically inferred**. The engine derives **threats, protections, and resilience mechanisms** based on the existing capabilities, vulnerabilities, and their interactions.

[**Example 12:**](https://github.com/pedropaulofb/laderr/tree/main/documentation/examples)

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

### 6.3. Inferred Output by LaDeRR Engine

When processed by the **LaDeRR Engine**, the simplified specification is expanded, adding inferred relationships and resilience constructs:

- **Resilience mechanisms are created** when conditions for resilience are met.
- **Threats are linked to their target assets** (e.g., `threatens` relation is inferred between `hacker_group` and `city`).
- **Protection mechanisms are inferred** if a capability neutralizes a vulnerability.
- **Scenario resilience is evaluated**.

The resulting expanded model ensures consistency with the LaDeRR framework while reducing manual specification effort.
