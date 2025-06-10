# LaDeRR User Guide

<!-- omit from toc -->
## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1. LaDeRR Metamodel Presentation](#11-laderr-metamodel-presentation)
  - [1.2. Access to LaDeRR Specification Example and Results](#12-access-to-laderr-specification-example-and-results)
  - [1.3. Processing the Specification with the LaDeRR Engine](#13-processing-the-specification-with-the-laderr-engine)
  - [1.4. Understanding the Visual Graphs](#14-understanding-the-visual-graphs)
- [2. General Structure of a LaDeRR Specification](#2-general-structure-of-a-laderr-specification)
  - [2.1. Two Approaches to Writing LaDeRR Specifications](#21-two-approaches-to-writing-laderr-specifications)
  - [2.2. Validation Process](#22-validation-process)
- [3. Specification Metadata](#3-specification-metadata)
  - [3.1. Required Fields and Defaults](#31-required-fields-and-defaults)
  - [3.2. Examples of Valid Metadata Blocks](#32-examples-of-valid-metadata-blocks)
- [4. Specification Constructs](#4-specification-constructs)
  - [4.1. Common Attributes of All Constructs](#41-common-attributes-of-all-constructs)
  - [4.2. Example of Construct Definition](#42-example-of-construct-definition)
- [5. Scenarios](#5-scenarios)
  - [5.1. Scenario's Field Situation](#51-scenarios-field-situation)
  - [5.2. Scenario's Field Status](#52-scenarios-field-status)
  - [5.3. Rules Governing Scenarios](#53-rules-governing-scenarios)
  - [5.4. Examples of Scenario Definition](#54-examples-of-scenario-definition)
- [6. Scenario Components](#6-scenario-components)
  - [6.1. Linking Scenario Components to Scenarios](#61-linking-scenario-components-to-scenarios)
  - [6.2. Scenario-Specific Duplication in LaDeRR Engine](#62-scenario-specific-duplication-in-laderr-engine)
- [7. Entities](#7-entities)
  - [7.1. Common Attributes of Entities](#71-common-attributes-of-entities)
  - [7.2. Declaring Entities](#72-declaring-entities)
  - [7.3. Assets](#73-assets)
  - [7.4. Threats](#74-threats)
  - [7.5. Controls](#75-controls)
- [8. Dispositions](#8-dispositions)
  - [8.1. Rule Governing Dispositions](#81-rule-governing-dispositions)
  - [8.2. Capabilities](#82-capabilities)
  - [8.3. Vulnerabilities](#83-vulnerabilities)
- [9. Resilience](#9-resilience)
  - [9.1. Fields of Resilience](#91-fields-of-resilience)
  - [9.2. Rules Governing Resilience](#92-rules-governing-resilience)
- [10. Mapping to ResiliOnt Ontology](#10-mapping-to-resiliont-ontology)
- [11. Complete Savannah Example](#11-complete-savannah-example)
  - [10.1. Heatwave Response (Pre-Inference)](#101-heatwave-response-pre-inference)
  - [10.2. Dry Season Survival (Pre-Inference)](#102-dry-season-survival-pre-inference)
  - [10.3. Heatwave Response (Post-Inference)](#103-heatwave-response-post-inference)
  - [10.4. Dry Season Survival (Post-Inference)](#104-dry-season-survival-post-inference)

## 1. Introduction

This guide provides a complete walkthrough for writing specifications using the [**La**nguage for **De**scribing **R**isk and **R**esilience (LaDeRR)](https://w3id.org/laderr/git), an ontology-based domain-specific language (DSL) for modeling resilience scenarios. Grounded in the [**ResiliOnt**](https://github.com/pedropaulofb/resiliont/) ontology, LaDeRR enables users to represent the interplay between entities, their capabilities, and their vulnerabilities in a structured, analyzable format.

Specifications are written in [TOML](https://toml.io/en/), a human-readable and machine-processable syntax. This guide introduces each language construct alongside its metamodel representation, relevant rules, and example fragments, building up to a complete and valid LaDeRR specification.

The following sections cover all core elements of a LaDeRR specification. Each component is accompanied by:

- **Concept Overview**: A brief explanation of the purpose and role of the component within a LaDeRR specification.
- **Metamodel Representation**: A UML class diagram illustrating the structure and relationships of the language's elements.
- **Specification Example**: A LaDeRR specification snippet in TOML format, demonstrating a correct way to specify the component.
- **Rules and Constraints (if applicable)**: Formal constraints and derivations governing the use of the component.

### 1.1. LaDeRR Metamodel Presentation

The LaDeRR metamodel defines the core structural elements of the language, establishing the conceptual foundation for resilience and risk scenario modeling. It is presented through separate UML class diagrams, each representing a distinct aspect of the LaDeRR language.

The UML metamodel follows a color-coding and formatting scheme:

- **Blue**: Represents classes that are defined within the specific diagram being presented.
- **Gray**: Represents classes defined in other diagrams, shown for context.
- **White**: Represents enumerations, which define a set of predefined values.
- **Red**: Represents notes that provide additional constraints, rules, or clarifications.

### 1.2. Access to LaDeRR Specification Example and Results

All examples presented throughout this guide are part of a same domain. They all come from a same LaDeRR specification, but have small adjustments to better fit their exemplification purposes.

The final, complete version—containing all elements introduced throughout the guide—is available in the [`documentation/example`](https://github.com/pedropaulofb/laderr/tree/main/documentation/example) folder of the LaDeRR repository. While this guide focuses on the LaDeRR language itself, many of the outputs referenced below—such as inferred specifications, visualizations, and reports—were generated using the [**LaDeRR Engine**](https://w3id.org/laderr/engine/git), a supporting tool designed to validate and extend LaDeRR models.

This folder includes:

- [`example_doc_in.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_in.toml): the full input in TOML format, incrementally built and explained across the sections of this guide.

- [`example_doc_out`](https://github.com/pedropaulofb/laderr/tree/main/documentation/example/example_doc_out): directory containing the full set of outputs generated by the LaDeRR Engine, including:

  - **Post-Inference Specification in LaDeRR (.toml) and Graph (.ttl) formats**:
    - [`example_doc_out_post.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post.toml)
    - [`example_doc_out_post.ttl`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post.ttl)

  - **Visualizations (Pre- and Post-Inference)**:
    - [`example_doc_out_pre_dry_season.png`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_pre_dry_season.png)
    - [`example_doc_out_pre_heatwave_response.png`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_pre_heatwave_response.png)
    - [`example_doc_out_post_dry_season.png`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post_dry_season.png)
    - [`example_doc_out_post_heatwave_response.png`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post_heatwave_response.png)

  - **Analytical Reports (PDF)**:
    - [`example_doc_out_report_pre_dry_season.pdf`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_report_pre_dry_season.pdf)
    - [`example_doc_out_report_pre_heatwave_response.pdf`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_report_pre_heatwave_response.pdf)
    - [`example_doc_out_report_post_dry_season.pdf`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_report_post_dry_season.pdf)
    - [`example_doc_out_report_post_heatwave_response.pdf`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_report_post_heatwave_response.pdf)

  - **Validation Reports (TXT)**:
    - [`example_doc_out_validation_report_pre.txt`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_validation_report_pre.txt)
    - [`example_doc_out_validation_report_post.txt`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_validation_report_post.txt)

These outputs demonstrate how the [**LaDeRR Engine**](https://w3id.org/laderr/engine/git) processes a specification: transforming it into an RDF graph, applying inference mechanisms and validation, and producing a structured representation of the modeled scenario.

### 1.3. Processing the Specification with the LaDeRR Engine

The specification was processed using the [**LaDeRR Engine**](https://w3id.org/laderr/engine/git), a Python-based software that supports various operations over LaDeRR models. These operations are executed in two phases: **pre-inference** and **post-inference**. In addition to applying an OWL reasoner to infer implicit relations based on the model’s logical structure, the engine also applies inference rules defined in the LaDeRR metamodel. These rules enable the engine to extend the original specification with additional semantics—deriving new relations, instances, and properties—resulting in a more comprehensive model ready for analysis and visualization.

Upon processing the specification, the engine performs the following tasks:

- **OWL Graph Generation**: The TOML input is transformed into an RDF graph compliant with the [LaDeRR Vocabulary](https://w3id.org/laderr). This graph is exported in Turtle (`.ttl`) format.

- **Graph Visualizations**: Each scenario in the specification is rendered as a `.png` image using Graphviz, both **before** and **after** inference.

- **Analytical Reports**: For each scenario and phase (pre and post), the engine generates a detailed `.pdf` report. These reports include the visualization and a set of computed statistics and resilience metrics.

- **Validation Reports**: The engine validates the RDF graph against a set of SHACL shapes to ensure conformance with the expected structure and constraints.

Since the current example contains two scenarios, the engine generated four visualizations and four PDF reports (one per scenario and phase), along with the associated validation outputs.

For more technical details or to learn how to run the engine yourself, please refer to the [LaDeRR Engine repository](https://w3id.org/laderr/engine/git).

### 1.4. Understanding the Visual Graphs

Throughout this guide, several visualizations of LaDeRR scenarios are presented. These were generated automatically by the LaDeRR Engine using [Graphviz](https://graphviz.org/) and are based on the RDF representation of the input specification.

Each node and edge in the graph follows a consistent color and shape scheme to indicate its type and role within the scenario. The legend below provides a quick reference:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/documentation/images/visualization_legend.png" alt="Legend for Scenario Elements"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>
<p align="center"><em>Visual legend used in LaDeRR scenario diagrams, defining nodes' and edges' shapes and colors according to their roles in the specification.</em></p>

Here is how to interpret the visual elements:

- **Node Colors and Shapes**:
  - **Light Green / Dark Green Circles**: Capabilities (enabled / disabled).
  - **Light Red / Dark Red Circles**: Vulnerabilities (enabled / disabled).
  - **Orange Ellipses**: Resilience instances.
  - **Light Green Squares**: Assets.
  - **Blue Squares**: Controls.
  - **Pink Squares**: Threats.
  - **Gray Squares**: Entities that are not typed as asset, control, or threat.

- **Multicolored Nodes**:
  - **Dispositions** (capability and vulnerability at the same time) appear with **green and red wedges**, indicating dual classification.
  - **Entities** with multiple subtypes (e.g., both _Asset_ and _Control_) use **striped fills** combining their respective colors. If an entity has all three subtypes (_Asset_, _Control_, and _Threat_), a three-way split is used.

- **Edge Colors and Types**:
  - **Blue Arrows**: Links between entities (_protects_, _inhibits_, _threatens_).
  - **Orange Arrows**: Resilience relations (_preserves_, _preservesAgainst_, _preservesDespite_, _sustains_).
  - **Dark Red Arrows**: A capability disabling a vulnerability.
  - **Black Arrows**: Causal relations (_exploits_, _exposes_).
  - **Green Arrows**: Vulnerabilities that _did not_ cause damage.
  - **Red Arrows**: Vulnerabilities that _did_ cause damage.
  - **Black Arrows with Diamond Tail**: Relations from entities to their capabilities, vulnerabilities, or resiliences.

Refer back to this legend when reading visualizations throughout the guide to better understand the semantics encoded in the diagrams.

## 2. General Structure of a LaDeRR Specification

Each LaDeRR specification consists of two main parts that together define one or more resilience scenarios in a structured and analyzable way:

- **Metadata**: Contains general information about the specification, such as its title, authorship, versioning, and the type of scenario being described. (See [Section 3](#3-specification-metadata) for details.)

- **Scenario**: Represents a specific situation, grouping components that describe the resilience context at a given time (e.g., an operational state or an incident).
- **ScenarioComponents**: Represent the core elements of the scenario and their interrelations. These include:
  - **Assets**: Entities that hold value and are potentially exposed to threats.
  - **Threats**: Entities that possess capabilities capable of exploiting vulnerabilities.
  - **Controls**: Entities that inhibit threats and support resilience by blocking harmful effects.
  - **Capabilities**: The positive dispositions of entities—their abilities to perform protective or sustaining functions.
  - **Vulnerabilities**: Weaknesses that may be exploited by threats.
  - **Resilience**: Constructs that preserve the value of entities despite vulnerabilities or external pressures.

LaDeRR specifications are written in TOML, which [supports comments using the # symbol](https://toml.io/en/v1.0.0#comment). Users can freely annotate their specification files to explain choices, clarify constructs, or organize the file visually. Comments are ignored by the LaDeRR Engine and have no effect on validation or inference.

The next sections provide a detailed explanation of each part of the specification.

### 2.1. Two Approaches to Writing LaDeRR Specifications

When writing a LaDeRR specification, users can choose between two approaches, depending on their needs and familiarity with the language:

- **Complete (Manual) Specification**:
  In this approach, the user explicitly defines all elements and their properties using the full features of the LaDeRR language. Even fields that could be derived or assigned by default—such as types, statuses, or certain relationships—are specified directly. This method provides full control over the model and is useful for advanced users who want to fine-tune every aspect of a scenario.

- **Minimal (Auto-Completed) Specification**:  
  Alternatively, users can define only the essential structure of a scenario, leaving the rest to be automatically completed by the [LaDeRR Engine](https://w3id.org/laderr/engine/git). The engine applies reasoning, default values, and inference rules to generate a complete and semantically enriched version of the model. This saves time and reduces the learning curve, especially for new users or when modeling large (sets of) scenarios.

To illustrate the difference:

- A **minimal input specification** (92 lines): [`example_doc_in.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_in.toml)
- The **fully completed version** generated after the minimal version by the engine (324 lines): [`example_doc_out_post.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post.toml)

Throughout this guide, each language construct will be presented with examples showing **both styles**—the minimal form written by the user and the complete result produced by the engine. This will help readers understand not only how to write a specification, but also what the engine adds during its processing.

### 2.2. Validation Process

Before and after performing reasoning on a specification, the [LaDeRR Engine](https://w3id.org/laderr/engine/git) can optionally validate the model to help ensure completeness and consistency with the language’s metamodel.

Validation is based on [SHACL (Shapes Constraint Language)](https://www.w3.org/TR/shacl/), a W3C standard for RDF graph validation. The engine applies a set of predefined SHACL shapes that reflect the structural rules of the LaDeRR metamodel. These shapes are [available in this repository](https://github.com/pedropaulofb/laderr/tree/main/shapes).

The validation runs in two stages:

- **Pre-Inference Validation**: After parsing the user-written specification but before inference, to catch any structural issues early.
- **Post-Inference Validation**: After reasoning is complete, to verify that the enriched model remains logically consistent and structurally valid.

Each stage produces a report containing messages of the following types:

- **Passed**: No issues were found.
- **Info**: Non-mandatory elements are missing—these are not required but are recommended for completeness.
- **Warning**: A mandatory element is missing according to the LaDeRR metamodel. However, because LaDeRR adopts the [Open World Assumption (OWA)](https://www.dataversity.net/introduction-to-open-world-assumption-vs-closed-world-assumption/), the engine allows these omissions and continues processing.
- **Violation**: A critical inconsistency was detected that violates the defined structural rules.

Validation is implemented using the open-source [PySHACL](https://github.com/RDFLib/pySHACL) library. For more technical details on the validation logic and output structure, refer to the PySHACL documentation.

The figure below illustrates the typical processing flow of a simplified specification, highlighting validation stages before and after reasoning:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/documentation/images/processing_stages.png"  alt="LaDeRR Engine's Process"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>
<p align="center"><em>Simplified view of LaDeRR Engine’s processing stages, from a minimal user-defined specification to a fully enriched and validated model.</em></p>

## 3. Specification Metadata

A LaDeRR specification is represented by a single instance of the `Specification` class, which defines the overall structure and identity of the model. This instance encompasses:

- A set of **metadata attributes**, describing the specification itself (such as title, authorship, versioning, and creation date).
- An optional set of **constructs**, representing the components of one or more resilience scenarios.

The UML class diagram below presents the structure of the `Specification` class and its relationship to constructs:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Specification.png"
alt="LaDeRR Specification UML Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>UML representation of the LaDeRR Specification class and its relation to scenario constructs.</em></p>

It is important to note that a LaDeRR specification file is considered **valid** even if it contains only metadata—i.e., it does not require constructs to be defined. However, in most practical cases, constructs will be present to describe one or more resilience scenarios.

### 3.1. Required Fields and Defaults

The table below lists the metadata fields available in a LaDeRR specification, along with their types, cardinalities, and default values where applicable. Each metadata field is described using both an _Input Type_ and a _Converted Type_. The _Input Type_ refers to the format the user should adopt when writing the specification in TOML. The **Converted Type** indicates the internal representation used in the RDF graph generated by the LaDeRR Engine. This transformation enables more precise validation, as it allows the engine to detect malformed or inconsistent values that may otherwise go unnoticed if treated purely as free-form strings.

| Field           | Input Type                       | Converted Type | Multiplicity | Required | Default Value            | Description                                                                                                                                                           |
| --------------- | -------------------------------- | -------------- | ------------ | -------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **title**       | string                           | string         | [0..1]       | No       | N/A                      | A short name for the specification.                                                                                                                                   |
| **description** | string                           | string         | [0..1]       | No       | N/A                      | A brief explanation or summary of the content described in the specification.                                                                                         |
| **version**     | string                           | string         | [0..1]       | No       | N/A                      | A version identifier for the specification (free-form, no specific format required).                                                                                  |
| **createdBy**   | string \| list[string]           | list[string]   | [0..*]       | No       | N/A                      | Names or identifiers of the author(s). A single string is automatically converted into a list.                                                                        |
| **createdOn**   | datetime (TOML native) \| string | xsd:dateTime   | [0..1]       | No       | N/A                      | Timestamp of creation. Must follow the `xsd:dateTime` format. See [time format guide](https://github.com/pedropaulofb/laderr/blob/main/documentation/time_format.md). |
| **modifiedOn**  | datetime (TOML native) \| string | xsd:dateTime   | [0..1]       | No       | N/A                      | Timestamp of the last known update. Must follow the `xsd:dateTime` format.                                                                                            |
| **baseURI**     | string                           | URIRef         | [1]          | **Yes**  | `https://laderr.laderr#` | The base URI used to generate identifiers for all elements within the specification. Must be a valid URI string.                                                      |

A dedicated [time format guide](https://github.com/pedropaulofb/laderr/blob/main/documentation/time_format.md) is available to help ensure `createdOn` and `modifiedOn` values are formatted correctly.

While the UML diagram shows a `constructs` relation between a `Specification` and multiple `Construct` instances, this relation is optional. If no constructs are defined, the specification is still valid as long as all required metadata fields are provided.

### 3.2. Examples of Valid Metadata Blocks

To help clarify how metadata is defined in practice, the snippets below show two examples of valid metadata sections: one minimal and one more complete. Each conforms to the format and types described in the previous table.

#### Minimal Valid Metadata

Thanks to the default value assigned to the `baseURI` attribute, even a completely empty file is considered a syntactically valid LaDeRR specification. The following two examples illustrate the smallest valid definitions:

- **Empty file (implicitly valid)**:
  A specification file with no content at all is valid, as the default value of `baseURI` is automatically applied by the LaDeRR Engine.

- **Explicit minimal file**:
  The example below shows the same result, but with the base URI explicitly defined:

```toml
baseURI = "https://minimalexample.laderr#"
```

<p align="left"><em>Minimal metadata block explicitly setting the base URI.</em></p>

While such minimal files are valid, they are not useful in practice unless used for testing or incremental development.

> **Note:** When using the [LaDeRR Engine](https://w3id.org/laderr/engine/git), if no `Scenario` is explicitly defined in the specification, the engine will automatically create a default scenario and assign a generated identifier to it (e.g., `SX01`)(see [Section 5.4C](#c-no-scenario-declared)). However, since every scenario is required to include at least one scenario component, a blank or metadata-only file will result in a validation error. To avoid this, users should either define a scenario manually or include at least one construct (e.g., an entity) in addition to the metadata.

#### Complete Example with All Supported Fields

The example below illustrates a fully detailed metadata section. It includes multiple values where allowed and offers a comprehensive description of the specification's context and authorship.

```toml
baseURI = "https://savannahresilience.laderr#"
createdBy = ["Pedro Paulo F. Barcelos", "Jane Example", "Fictional Institute of Modeling"]
createdOn = "2025-03-28T12:00:00Z"
modifiedOn = "2025-04-01T10:30:00Z"
title = "Savannah Animal Survival Resilience Model"
description = "A resilience model for animal survival in the savannah. Inspired by real-world ecological dynamics including predation, shelter-seeking, and thermal stress."
version = "1.2"
```

<p align="left"><em>Complete metadata block with all supported fields.</em></p>

## 4. Specification Constructs

All elements that describe the resilience scenario in a LaDeRR specification—such as threats, capabilities, assets, and so on—are represented as instances of the abstract class `Construct`.

Note that, although `Specification` and its attributes are technically constructs in the LaDeRR metamodel, the term **Construct** is used—both in the metamodel formalization and throughout this guide—to refer specifically to scenarios and their defining elements, i.e., the entities and relations that constitute the resilience model being specified.

Constructs are used to express the aspects of a resilience scenario and are divided into `Scenario` and `ScenarioComponent` categories. These are further refined into more specific types, such as `Capability`, `Vulnerability`, `Asset`, `Threat`, `Control`, and `Resilience`. The full taxonomy of constructs is presented in the diagram below:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/documentation/images/construct_taxonomy.png"
alt="LaDeRR Construct Taxonomy Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>Taxonomy of constructs in LaDeRR. All user-defined elements in a resilience scenario belong to this hierarchy.</em></p>

### 4.1. Common Attributes of All Constructs

Regardless of their specific type, all constructs share the same basic structure defined in the `Construct` class. The following three attributes are required for every instance:

- **id** (_string, required, unique_): The identifier of the construct. It must be unique within the specification and is used to reference this element throughout the model.
- **label** (_string, required_): A human-readable name for the construct. If not explicitly provided in the input file, it automatically defaults to the same value as the `id`.
- **description** (_string, optional_): A description of the construct.

> **Note:** Unlike other attributes, `id` is not written as a separate key-value pair in the TOML body. Instead, it is specified as part of the TOML table header using the format `[<Type>.<id>]` (e.g., `[Entity.lion_pride]`). The string after the dot (e.g., `lion_pride`) becomes the `id` of the instance.

The UML class diagram below summarizes the definition of the `Construct` class, presenting its attributes, specializations, and its association with the class `Specification`.

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Constructs.png"
alt="LaDeRR Construct Class Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>UML diagram of the Construct class.</em></p>

### 4.2. Example of Construct Definition

Constructs are created by declaring new [TOML tables](https://toml.io/en/v1.0.0#table) using the format `[<Type>.<id>]`, where `<Type>` is the construct class (e.g., `Scenario`, `Entity`, `Capability`), and `<id>` is the unique identifier.

Below is an example of a scenario definition:

```toml
[Scenario.dry_season]
label = "Dry Season Survival"
description = "Models the challenges animals face during prolonged droughts, such as water scarcity, heat exposure, and increased territorial pressure."
```

<p align="left"><em>Definition of a scenario with label and description.</em></p>

Here, `dry_season` is the construct’s `id`. Since a `label` is explicitly provided, it will be used in place of the `id` in visualizations and reports. A `description` is also included for documentation purposes.

Minimal definitions are also allowed. The following snippet defines two entities using only their identifiers:

```toml
[Entity.lion_pride]
[Entity.zebra_herd]
```

<p align="left"><em>Minimal definitions of two entities without labels or descriptions.</em></p>

In this case, the `label` defaults to the same value as the `id`, and the `description` remains empty.

While such minimal forms are valid, adding labels and descriptions is strongly recommended to improve readability and interpretation—especially when generating reports or sharing models with others.

In the next sections, we will explore each specific subtype of construct in detail.

## 5. Scenarios

In LaDeRR, a **Scenario** represents a snapshot of a resilience context at a given point in time. It groups a set of components—entities and relations—that together express the conditions of the system in that moment. Scenarios enable users to analyze and reason about whether resilience is present or lacking, either in current operations or in past incidents.

Scenarios are essential for modeling dynamic systems that may change over time. A single specification can include multiple scenarios, allowing users to represent different temporal perspectives or stages of system evolution (e.g., before and after adding a resilience control).

All scenarios are defined as instances of the `Scenario` class and share the same required structure, which includes the following attributes:

- **situation** (_ScenarioSituationEnum, required, default = `operational`_): Specifies whether the scenario represents an ongoing moment (`operational`) or a past event (`incident`). This affects how threats and consequences are interpreted.
- **status** (_ScenarioStatusEnum, required, default = `vulnerable`_): Indicates the resilience level of the scenario, classifying it as either `resilient` or `vulnerable` based on the protection of asset capabilities.

If these attributes are omitted from the specification, the default values are applied automatically—ensuring that the scenario is treated as operational and vulnerable unless stated otherwise.

> **Note:**: When using the [LaDeRR Engine](https://w3id.org/laderr/engine/git):
>
> - It is **recommended** to explicitly define the `situation` attribute, as this affects how threats and outcomes are interpreted during inference.
> - It is **not required** to specify the `status` attribute manually. The engine automatically computes and updates the scenario status during post-inference processing. Any user-defined value for `status` may be overwritten by this automated evaluation.

The UML diagram below presents the metamodel structure for Scenarios and their relationship with `ScenarioComponents`:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/metamodel_images/Scenario.png"
alt="Scenario Metamodel"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
<p align="center"><em>Metamodel of the <code>Scenario</code> class, showing its attributes, enumerations, and relation to scenario components.</em></p>

If a `ScenarioComponent` is not explicitly linked to any `Scenario`, it is automatically interpreted as belonging to **all** scenarios defined within the same specification. This default behavior simplifies modeling in cases where certain components are relevant across multiple scenarios.

Moreover, if no `Scenario` is explicitly declared in the specification, a default one is assumed to exist. In such cases, all scenario components are treated as part of this single, implicit scenario. When using the LaDeRR Engine, this default scenario is generated automatically, and a randomly generated identifier is assigned to it.

### 5.1. Scenario's Field Situation

The `situation` attribute characterizes the temporal nature of the scenario. It accepts one of the following values:

- **`operational`**: Represents a current or ongoing situation. Threats may exist, but their outcomes are still uncertain. The scenario reflects the system's present state, where resilience might still be tested in the future.
  
- **`incident`**: Represents a past situation. All outcomes are known and assumed to have occurred unless explicitly stated otherwise. If a threat had the opportunity to cause damage and there was no resilience in place, it is assumed that the damage occurred.

This distinction is critical for interpreting the semantics of threats and resilience within the model.

### 5.2. Scenario's Field Status

The `status` attribute summarizes the overall condition of the scenario in terms of resilience. It can take one of two values:

- **`resilient`**: Indicates that **all** assets in the scenario are protected. This occurs when:
  - Every capability that is at risk is preserved by a corresponding instance of Resilience, **or**
  - The assets are not targeted by any threat.

- **`vulnerable`**: Indicates that **at least one** asset capability is unprotected and exposed to threats. This classification is conservative—if any vulnerability exists that is not counteracted by resilience, the entire scenario is deemed vulnerable.

These attributes together help define the scope and interpretation of each scenario within a LaDeRR specification.

### 5.3. Rules Governing Scenarios

This section presents the formal rules that govern the behavior of scenarios in LaDeRR. These rules determine how scenarios are classified, how damages are interpreted based on the situation type, and how vulnerabilities influence a scenario’s overall resilience status. All rules are based on the LaDeRR ontology and implemented within the LaDeRR Engine.

- **Rule 1: A Scenario can only be either _resilient_ or _vulnerable_**  
  Every scenario must have exactly one status. The two values are mutually exclusive: if a scenario is `resilient`, it is not `vulnerable`, and vice versa.

**FOL Representation:**

$$
\forall s ( Scenario(s) \rightarrow ( status(s) = RESILIENT \leftrightarrow \neg (status(s) = VULNERABLE) ) )
$$

- **Rule 2: A Scenario is _vulnerable_ if it contains an enabled vulnerability that is exploited by some capability**  
  If a scenario has at least one entity with an enabled vulnerability and there exists a capability that exploits it, the scenario is marked as `vulnerable`.

**FOL Representation:**

$$
\forall s ( Scenario(s) \rightarrow ( \exists o, v ( components(s, o) \land vulnerabilities(o, v) \land state(v) = ENABLED \land \exists c (Capability(c) \land exploits(c, v)) ) \leftrightarrow status(s) = VULNERABLE ) )
$$

- **Rule 3: Damage outcomes depend on scenario situation (operational or incident)**  
  The interpretation of `positiveDamage` and `negativeDamage` relations varies depending on whether the scenario situation is `operational` or `incident`:

  - In `incident` scenarios, damage relations are definitive: `positiveDamage` implies `damaged`, and `negativeDamage` implies `notDamaged`.
  - In `operational` scenarios, damage relations are potential: `positiveDamage` implies `canDamage`, and `negativeDamage` implies `cannotDamage`.

**FOL Representation:**

$$
\forall s ( Scenario(s) \rightarrow (
  ( situation(s) = INCIDENT \rightarrow (
    \forall x, y ( positiveDamage(x, y) \rightarrow damaged(x, y) ) \land
    \forall x, y ( negativeDamage(x, y) \rightarrow notDamaged(x, y) )
  ) ) \land
  ( situation(s) = OPERATIONAL \rightarrow (
    \forall x, y ( positiveDamage(x, y) \rightarrow canDamage(x, y) ) \land
    \forall x, y ( negativeDamage(x, y) \rightarrow cannotDamage(x, y) )
  ) )
) )
$$

### 5.4. Examples of Scenario Definition

Below are three examples illustrating different ways to work with scenarios in a LaDeRR specification:

#### A. Explicit Definition of a Scenario

This example shows how to define a named scenario with both `situation` and `status` attributes, along with components explicitly assigned to it:

```toml
[Scenario.heatwave_response]
label = "Heatwave Response"
situation = "operational"
status = "resilient"

[Scenario.dry_season]
label = "Dry Season Survival"
situation = "operational"
status = "vulnerable"
```

<p align="left"><em>Example of complete Scenario description.</em></p>

#### B. Components Without Scenario Assignment

In this example, scenario components are defined without specifying any associated scenario. They will automatically be considered part of **all** scenarios defined in the specification. This effect can be observed in the example below, where **zebra_herd** is not linked to any scenario.

```toml
[Scenario.heatwave_response]
label = "Heatwave Response"
situation = "operational"
status = "resilient"

[Scenario.dry_season]
label = "Dry Season Survival"

[Entity.zebra_herd]
label = "Zebra Herd"
# Additional attributes or relations for zebra_herd (omitted here for brevity)
```

<p align="left"><em>Example of unprocessed specification without scenario assignment.</em></p>

After being processed by LaDeRR Engine, the result of this is:

```toml
[Scenario.heatwave_response]
components = ["zebra_herd_heatwave_response"]
label = "Heatwave Response"
situation = "operational"
status = "resilient"

[Scenario.dry_season]
components = ["zebra_herd_dry_season"]
label = "Dry Season Survival"
situation = "operational"
status = "vulnerable"

[Entity.zebra_herd_heatwave_response]
label = "Zebra Herd"
scenarios = "heatwave_response"
# Additional attributes or relations for zebra_herd (omitted here for brevity)

[Asset.zebra_herd_dry_season]
label = "Zebra Herd"
scenarios = "dry_season"
```

<p align="left"><em>Example of processed specification without scenario assignment.</em></p>

As can be seen, **zebra_herd** was assigned to both scenarios contained in the specification. Additionally, note that, for scenario **dry_season**, as its attributes situation and status were not assigned, the default values were automatically attributed to it.

See subsections [6.2](#62-scenario-specific-duplication-in-laderr-engine) for a better understanding about the duplication and automatically assignment.

#### C. No Scenario Declared

This example shows a minimal case where no scenario is declared. A default scenario will be implicitly created by the LaDeRR Engine, and all components will be assigned to it:

```toml
[Entity.zebra_herd]
label = "Zebra Herd"
# Additional attributes or relations for zebra_herd (omitted here for brevity)
```

<p align="left"><em>Example of unprocessed specification without scenario definition.</em></p>

After processing, we get the following:

```toml
[Scenario.SX01]
components = ["zebra_herd"]
label = "SX01"
situation = "operational"
status = "vulnerable"

[Entity.zebra_herd]
label = "Zebra Herd"
scenarios = ["SX01"]
# Additional attributes or relations for zebra_herd (omitted here for brevity)
```

<p align="left"><em>Example of automatic creation of scenario from specification without scenario definition.</em></p>

## 6. Scenario Components

In LaDeRR, the elements that describe the structure and dynamics of a scenario are called **Scenario Components**. These include entities, dispositions, and resilience—each playing a specific role in representing how threats, vulnerabilities, and protections interact within a system.

All scenario components are instances of the abstract class `ScenarioComponent`, which does not define any attributes on its own but serves as a common superclass for the following three types:

- [`Entity`](#7-entities): Represents a system participant (e.g., asset, threat, or control).
- [`Disposition`](#8-dispositions): Represents an intrinsic property of an entity that manifests under specific conditions. It can be positive, as a capability that supports system functionality, or as a vulnerability that exposes the entity to potential harm.
- [`Resilience`](#9-resilience): Represents the preservation of functions (capabilities) in the face of threats and vulnerabilities.

These elements are the core building blocks that determine the structure and behavior of the system being modeled.

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/metamodel_images/ScenarioComponents.png"
alt="Scenario Components Metamodel"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>Metamodel overview of the abstract class <code>ScenarioComponent</code> and its three concrete subclasses: <code>Entity</code>, <code>Disposition</code>, and <code>Resilience</code>.</em></p>

Each of these types is described in detail in the following subsections. You will learn their purpose, required fields, how they relate to other components, and the inference rules used by the [LaDeRR Engine](https://w3id.org/laderr/engine/git) to compute additional structure based on their definitions.

The examples shown in the next sections are provided in both minimal and complete forms to help users understand how to author them manually or rely on the engine to infer missing information.

### 6.1. Linking Scenario Components to Scenarios

Each scenario component—whether an entity, disposition, or resilience—must be associated with one or more scenarios. This association determines the context in which the component exists and contributes to resilience analysis.

There are two supported ways to establish this connection in a LaDeRR specification:

#### A. Listing components inside the scenario definition

You can explicitly list component identifiers under a scenario's `components` attribute:

```toml
[Scenario.x]
components = ["y"]

[Entity.y]
# component definition
```

<p align="left"><em>Example of first option of scenario assignment.</em></p>

#### B. Referencing scenarios from the component

Alternatively, each scenario component can declare the scenarios to which it belongs by using the `scenarios` attribute:

```toml
[Scenario.x]
# scenario definition

[Entity.y]
scenarios = ["x"]
# component definition
```

<p align="left"><em>Example of second option of scenario assignment.</em></p>

Both approaches are semantically equivalent and can be used interchangeably. When using the engine, either method will correctly link the component to the intended scenario(s).

In addition, if a specification defines only one scenario, components do not need to explicitly declare the association—the LaDeRR Engine will assume all components belong to that scenario.

### 6.2. Scenario-Specific Duplication in LaDeRR Engine

As soon as a LaDeRR specification is loaded into the [LaDeRR Engine](https://w3id.org/laderr/engine/git), all scenario components are internally duplicated per scenario—even before validation or inference takes place. This ensures that each component is treated as context-specific from the very beginning of processing. Every rule, validation, and inference step is then applied individually to each scenario-specific version of the component, preserving their independence and enabling precise per-scenario analysis.

This duplication mechanism becomes especially important when a component is associated with multiple scenarios, as its behavior or interactions may differ depending on the context. For instance, a vulnerability might be exploited in one scenario but disabled in another.

To support this, the engine duplicates the component for each scenario to which it belongs. Each duplicated component has:

- A unique `id` generated by appending the scenario’s ID as a suffix to the original component ID.
- The **same label** as the original component (i.e., `label` remains unchanged across scenarios).
- Scenario-specific attributes, such as modified capabilities, relationships, or resilience links.

#### Example: Multi-Scenario Duplication

Given the following input:

```toml
[Scenario.dry_season]
label = "Dry Season Survival"
description = "Models the challenges animals face during prolonged droughts, such as water scarcity, heat exposure, and increased territorial pressure."

[Scenario.heatwave_response]
label = "Heatwave Response"
description = "Captures behavioral and environmental strategies animals use during extreme heat events, including movement, thermoregulation, and use of shelter."

[Entity.zebra_herd]
label = "Zebra Herd"
capabilities = ["efficient_thermoregulation", "rapid_movement_coordination"]
vulnerabilities = ["limited_water_access"]
scenarios = ["dry_season", "heatwave_response"]
```

<p align="left"><em>Example of a scenario component (zebra_herd) associated with multiple scenarios.</em></p>

LaDeRR Engine generates the following post-inference output:

```toml
[Asset.zebra_herd_heatwave_response]
capabilities = ["efficient_thermoregulation_heatwave_response", "rapid_movement_coordination_heatwave_response"]
vulnerabilities = ["limited_water_access_heatwave_response"]
inhibits = "lion_pride_heatwave_response"
protects = "lion_pride_heatwave_response"
label = "Zebra Herd"
scenarios = "heatwave_response"

[Asset.zebra_herd_dry_season]
capabilities = ["efficient_thermoregulation_dry_season", "rapid_movement_coordination_dry_season"]
vulnerabilities = ["limited_water_access_dry_season"]
inhibits = "lion_pride_dry_season"
protects = "lion_pride_dry_season"
label = "Zebra Herd"
scenarios = "dry_season"
```

<p align="left"><em>Example of post-inference duplication of a scenario component across two scenarios.</em></p>

This approach ensures accurate scenario-based analysis and prevents the reasoning process from mistakenly treating scenario-specific components as if they were identical.

## 7. Entities

In LaDeRR, an **Entity** represents a core component of a resilience scenario. Entities serve as participants in the system being modeled and may assume the role of **Asset**, **Threat**, or **Control**, depending on their roles within the scenario. These roles determine how an entity contributes to or is affected by vulnerabilities and resiliences.

All entities are instances of the abstract class `Entity`, which is further specialized into three concrete subtypes:

- **Asset**: Represents something of value that should be preserved and protected.
- **Threat**: Represents a potential source of harm capable of exploiting vulnerabilities.
- **Control**: Represents a mechanism that protects assets by inhibiting threats, contributing to resilience.

Entities are characterized by their **capabilities** and, optionally, **vulnerabilities**. These dispositions define their strengths and weaknesses and serve as the basis for determining protective, harmful, and resilience-enabling interactions.

The UML diagram below presents the `Entity` class, its three subtypes, and their associations with other components of the language:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/metamodel_images/Entities.png" alt="UML diagram of the Entity class in LaDeRR, showing its three subtypes—Asset, Threat, and Control—and their associations with Capabilities, Vulnerabilities, and Resilience." style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>UML metamodel of the <code>Entity</code> class and its subtypes, showing their associations with <code>Capability</code>, <code>Vulnerability</code>, and <code>Resilience</code>.</em></p>

### 7.1. Common Attributes of Entities

All entities share the same set of core attributes, used to define their positive and negative dispositions within a scenario:

- **capabilities** (_list of strings, required_): Identifiers of the capabilities possessed by the entity.
- **vulnerabilities** (_list of strings, optional_): Identifiers of the vulnerabilities associated with the entity.

Each entity must declare at least one **capability**, and may optionally include one or more **vulnerabilities**. These are referenced by their identifiers and must be declared separately in the specification.

### 7.2. Declaring Entities

In LaDeRR, entities can be declared in two different ways, depending on whether their classification into concrete types is known in advance or should be inferred automatically by [LaDeRR Engine](https://w3id.org/laderr/engine/git).

The first approach is to declare the entity using the abstract class `Entity`. This allows the modeler to describe the entity’s label, capabilities, vulnerabilities, and relationships without asserting its specific role (e.g., whether it is an asset, a threat, or a control). When the engine processes the specification, it will automatically determine the appropriate concrete classification(s) for the entity based on its context and interactions.

The example below demonstrates this approach:

```toml
[Entity.zebra_herd]
label = "Zebra Herd"
description = "A social group of zebras that relies on coordinated movement and thermoregulation to survive in arid environments."
capabilities = ["efficient_thermoregulation", "rapid_movement_coordination"]
vulnerabilities = ["limited_water_access"]
```

<p align="left"><em>Declaration of an entity using the abstract class <code>Entity</code>. The engine will classify it during inference as <code>Asset</code>, <code>Control</code>, or <code>Threat</code>, depending on its role in the model.</em></p>

Alternatively, if the entity’s role is already known, it can be declared directly using one or more of the concrete types—`Asset`, `Threat`, or `Control`.

In the example below, the same entity is declared as both a control and an asset:

```toml
[Control.zebra_herd]
[Asset.zebra_herd]
label = "Zebra Herd"
description = "A social group of zebras that relies on coordinated movement and thermoregulation to survive in arid environments."
capabilities = ["efficient_thermoregulation", "rapid_movement_coordination"]
vulnerabilities = ["limited_water_access"]
```

<p align="left"><em>Declaration of an entity using multiple concrete types. The roles of <code>Control</code> and <code>Asset</code> are asserted directly by the user.</em></p>

Both declaration styles are valid and supported. The choice between them depends on whether the user prefers to rely on automated classification by the engine or to assert entity roles explicitly within the model.

### 7.3. Assets

An **Asset** is an entity of value that is potentially exposed to risks and needs to be safeguarded. Assets may be targeted by threats and protected by controls. They can also be protected by `Resilience` instances, which preserve their capabilities despite the presence of vulnerabilities and threats.

Examples of assets include a _regional power grid_, which ensures electricity supply but may be vulnerable to cyberattacks and infrastructure failures; a _hospital network_, which provides medical services but is susceptible to data breaches and equipment malfunctions; a _coral reef ecosystem_, which supports marine biodiversity but faces risks from ocean acidification and climate change; a _financial market system_, which enables global trade but is exposed to economic downturns and cyber fraud; and a _public transportation network_, which facilitates mobility but can be disrupted by mechanical failures and extreme weather events.

In the savannah example, **Zebra Herd** and **Lion Pride** are treated as assets across different scenarios. Each holds valuable capabilities—such as coordinated movement or efficient thermoregulation—that are crucial for survival but may be compromised under certain vulnerabilities.

Assets are defined by the following additional field:

- **resiliences** (_list of strings, optional_): References to resilience instances associated with the asset. _(Automatically inferred when using LaDeRR Engine, but may also be declared manually.)_

> **Note:** The LaDeRR Engine automatically computes the occurrence of resilience instances based on the system's elements and their relations in accordance with specific rules (see [Section #9]((#9-resilience)). Users may provide explicit resilience declarations, but this is not required when using the engine.

#### Example of an Asset Specification

```toml
[Asset.lion_pride]
label = "Lion Pride"
capabilities = ["adaptive_ambush_strategy", "high_frequency_hunting", "unregulated_territory_roaming"]
vulnerabilities = ["prey_migration_barriers", "territory_dependency"]
resiliences = "R17"
protects = "lion_pride"
threatens = ["lion_pride", "zebra_herd"]
cannotDamage = "zebra_herd"
negativeDamage = "zebra_herd"
scenarios = ["heatwave_response", "dry_season"]
```

<p align="left"><em>Definition of an asset representing the Lion Pride, including capabilities, vulnerabilities, and a declared resilience instance that supports the preservation of its functions.</em></p>

### 7.4. Threats

A **Threat** is an entity that endangers assets by exploiting vulnerabilities. Its impact may vary depending on the scenario situation—whether the conditions are operational (present uncertainty) or incident (past certainty)—and depending on whether controls or resiliences are in place.

Examples of threats include a _cybercriminal group_, launching ransomware attacks to compromise data security; an _infectious disease outbreak_, spreading through populations and threatening public health infrastructure; an _oil spill_, contaminating marine ecosystems and disrupting local economies; a _social misinformation campaign_, influencing political outcomes and destabilizing trust in institutions; and an _earthquake_, damaging critical infrastructure and causing widespread economic losses.

In our savannah example, the **Poacher Group** is a clear example of a threat, possessing a harmful capability ("disruptive hunting influence") that targets the lion pride. In its scenarios, it cannot damage the lion pride due to protective mechanisms in place.

Threats may contain the following additional fields:

- **threatens** (_list of strings, required_): Assets that the threat targets. _(Automatically inferred.)_
- **canDamage** / **cannotDamage** (_list of strings, optional_): Used when the scenario situation is `operational`. Indicates whether a threat has the potential to cause damage.
- **damaged** / **notDamaged** (_list of strings, optional_): Used when the scenario situation is `incident`. Indicates whether a threat actually succeeded or failed in causing damage.

> **Note:** These outcome-specific relationships are automatically inferred by the LaDeRR Engine. Manual declarations are permitted but may be overwritten when using the engine.

#### Rules Governing Threats

- **Rule: A threat entity threatens an asset if it has a capability that exploits a vulnerability within that asset.**

In other words, if a threat has a capability that is designed to target a specific vulnerability of an asset, that threat is considered to pose a danger to the asset. The relationship does not depend on the current state (enabled/disabled) of the vulnerability—it reflects the structural potential for harm.

**FOL Representation:**

$$
\forall o1, o3 ( Entity(o1) \land Entity(o3) \land ( \exists v1, c3 ( Vulnerability(v1) \land Capability(c3) \land vulnerabilities(o1, v1) \land capabilities(o3, c3) \land exploits(c3, v1) ) \leftrightarrow threatens(o3, o1) ) )
$$

- **Rule: A threat fails to damage an asset if the vulnerability is disabled.**

If a threat’s capability targets a vulnerability, but that vulnerability is currently disabled (e.g., neutralized by a control or no longer active), then the threat cannot succeed in causing damage. In this case, the model records a negative damage relation, meaning protection was successful.

**FOL Representation:**

$$
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = DISABLED \land state(c2) = ENABLED ) ) \leftrightarrow negativeDamage(o2, o1) )
$$

- **Rule: A threat succeeds in damaging an asset if the vulnerability is enabled.**

A threat causes positive damage when its capability exploits a vulnerability that is both enabled and actively exposes a critical capability of the asset. This condition implies that resilience or control mechanisms were not sufficient to stop the harmful interaction.

**FOL Representation:**

$$
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = ENABLED \land state(c2) = ENABLED ) ) \leftrightarrow positiveDamage(o2, o1) )
$$

#### Example of a Threat Specification

```toml
[Threat.poacher_group]
label = "Illegal Hunting Party"
capabilities = "disruptive_hunting_influence"
threatens = "lion_pride"
cannotDamage = "lion_pride"
negativeDamage = "lion_pride"
scenarios = ["heatwave_response", "dry_season"]
```

<p align="left"><em>Threat entity representing an illegal hunting party. It targets the lion pride but fails to cause damage due to the latter's resilience.</em></p>

### 7.5. Controls

A **Control** is an entity designed to reduce risk by protecting assets or inhibiting threats. Controls typically act by **disabling vulnerabilities** or **inhibiting harmful capabilities** possessed by threats.

Controls do not need to be defensive technologies—they can also represent social, biological, or ecological actors. In the savannah model, examples include:

- **Meerkat Sentinels**, which inhibit threats by using predator detection calls that disable vulnerabilities in the lion pride.
- **Zebra Herd**, which acts both as a target and a protective control, helping inhibit the lion pride during the heatwave.
- **Shaded Savannah Shelter**, which protects the zebra herd by enabling dynamic heat refuge capabilities.

Controls must define at least one of the following relationships:

- **protects** (_list of strings, optional_): Assets that the control helps defend by disabling vulnerabilities. _(Can be automatically inferred by LaDeRR Engine.)_
- **inhibits** (_list of strings, optional_): Threats that are neutralized by the control. _(Can be automatically inferred by LaDeRR Engine.)_

> A valid `Control` must define at least one `inhibits` or `protects` relation, either explicitly or implicitly (when it has the basic associations from which this relation is inferred from by the LaDeRR Engine).

#### Rules Governing Controls

- **Rule: An Entity protects another if it disables a vulnerability that entity has.**

This means that protection occurs when one entity (a `Control`) possesses a capability that directly disables a vulnerability found in another entity. For example, if the lion pride has a vulnerability like _territory dependency_ and the zebra herd has a capability that disables this vulnerability, then the zebra herd is said to protect the lion pride. The protection is tied to the structural relationship between capability and vulnerability.

**FOL Representation:**

$$
\forall o1, o2 ( Entity(o1) \land Entity(o2) \land \exists v1, c2 ( Vulnerability(v1) \land Capability(c2) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land disables(c2, v1) ) \leftrightarrow protects(o2, o1) )
$$

- **Rule: An Entity inhibits another if it disables a vulnerability that the other exploits.**

Inhibition occurs when one entity (a `Control`) neutralizes a threat’s ability to exploit a vulnerability. This happens when both entities have capabilities connected to the same vulnerability—one exploiting it, the other disabling it. For example, if a poacher group exploits _prey migration barriers_ and the meerkat sentinels disable that same vulnerability, the sentinels inhibit the poacher group. Inhibition is about _cutting off the harm at its source_.

**FOL Representation:**

$$
\forall o2, o3 ( Entity(o2) \land Entity(o3) \land \exists c2, c3, v1 ( Capability(c2) \land Capability(c3) \land capabilities(o2, c2) \land capabilities(o3, c3) \land Vulnerability(v1) \land disables(c2, v1) \land exploits(c3, v1) ) \leftrightarrow inhibits(o2, o3) )
$$

These rules allow controls to exert influence over both threats and assets. By disabling vulnerabilities, controls serve as the essential mechanism in the creation of system resilience.

#### Example of a Control Specification

The example below defines the **Meerkat Sentinels** as a control in the `heatwave_response` scenario. It protects the lion pride and inhibits the poacher group using a capability that disables a vulnerability in the pride.

```toml
[Control.meerkat_sentinels_heatwave_response]
capabilities = "predator_detection_calls_heatwave_response"
inhibits = "poacher_group_heatwave_response"
protects = "lion_pride_heatwave_response"
label = "Meerkat Sentinels"
scenarios = "heatwave_response"
```

<p align="left"><em>Control representing Meerkat Sentinels in the heatwave scenario. It uses predator detection calls to inhibit a poacher group and protect the lion pride.</em></p>

Another example shows the **Shaded Savannah Shelter**, which protects the zebra herd by enabling a capability that disables the vulnerability `"limited_water_access_heatwave_response"`.

```toml
[Control.shaded_shelter]
capabilities = "dynamic_heat_refuge"
inhibits = "lion_pride_heatwave_response"
protects = "zebra_herd_heatwave_response"
label = "Shaded Savannah Shelter"
scenarios = "heatwave_response"
```

<p align="left"><em>Control entity representing shaded savannah shelters that protect the zebra herd by enabling dynamic heat refuge to counter limited water access.</em></p>

Both controls participate in resilience strategies by either _sustaining capabilities_, _reducing threat influence_, or _blocking vulnerability activation_, creating systemic protection mechanisms across scenarios.

## 8. Dispositions

Dispositions represent the inherent properties of entities within a LaDeRR specification that determine how they respond to changing conditions. They are divided into **Capabilities**, which represent positive dispositions that enable resilience, and **Vulnerabilities**, which represent negative dispositions that introduce risk. These elements are crucial for modeling how assets function under different conditions and how they interact with threats and controls.

Each disposition has a **state**, which can be either `enabled` or `disabled`. By default, all dispositions are set to `enabled`, meaning they actively contribute to the resilience or vulnerability of an entity. The state of a disposition influences whether it can be exploited or used to protect against threats.

- **state** (_string, optional, default: `"enabled"`_): Specifies whether the disposition is active (`enabled`) and can affect the scenario, or inactive (`disabled`) and has no effect.

### 8.1. Rule Governing Dispositions

- **Rule: A Disposition that disables another must be enabled**

A disposition can only disable another if it is enabled. Only active dispositions can influence the system's elements.

> **Note:** At present, LaDeRR supports only _direct_, one-to-one relationships between dispositions. This means that a disposition (e.g., a vulnerability) is disabled by a **single enabled capability** and not by combinations or logical conditions involving multiple constructs. Complex expressions—such as "a vulnerability is only disabled if two capabilities are simultaneously active" or "a capability is enabled only when at least one supporting capability exists"—are currently not supported. Future versions may introduce composite or conditional logic patterns, but these are not expressible in the current language or engine.

**FOL Representation:**

$$
\forall d1, d2 ( Disposition(d1) \land Disposition(d2) \land disables(d1, d2) \rightarrow state(d1) = ENABLED \land state(d2) = DISABLED )
$$

The UML diagram below illustrates the **Disposition** metamodel and its relationships with other ScenarioComponents:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Dispositions.png" alt="Disposition UML Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>
<p align="center"><em>Disposition metamodel showing the structural relations between Capabilities, Vulnerabilities, and Resilience.</em></p>

### 8.2. Capabilities

A **Capability** is a positive disposition that enables an entity to perform specific functions that contribute to resilience. Capabilities can disable vulnerabilities (thus protecting assets) and, consequently, sustain resiliences (ensuring the stability of an entity under adverse conditions). They may also be used by threats to exploit vulnerabilities.

Examples of capabilities include **fire resistance in building materials**, which prevents the spread of flames during a fire; **immune response in living organisms**, which helps fight infections and maintain health; **automated failover in cloud computing**, which ensures system continuity in case of a server failure; **adaptive governance in socio-ecological systems**, which allows communities to respond to environmental changes; and **reinforced structural design in engineering**, which enhances resistance against natural disasters.

#### Additional Fields of Capabilities

- **disables** (_list of strings, optional_): Vulnerabilities that this capability neutralizes.
- **exploits** (_list of strings, optional_): Vulnerabilities that this capability can exploit (if used by a threat).
- **sustains** (_list of strings, optional_): Resilience instances that this capability supports. _(Inferred by the LaDeRR Engine.)_

#### Capability Example from the Savannah Specification

The following capability, declared for the **shaded_shelter** in the `heatwave_response` scenario, contributes to resilience by disabling the vulnerability `"limited_water_access_heatwave_response"`:

```toml
[Capability.dynamic_heat_refuge]
description = "Provides adaptable shaded areas that reduce heat exposure during high-temperature events."
disables = "limited_water_access"
label = "Dynamic Heat Refuge"
scenarios = "heatwave_response"
state = "enabled"
sustains = "R1L"
```

<p align="left"><em>This capability is enabled, disables a vulnerability, and sustains a resilience instance.</em></p>

### 8.3. Vulnerabilities

A **Vulnerability** is a negative disposition that exposes an entity susceptible to threats. It may be exploited by threats' capabilities, and it exposes internal capabilities. If a vulnerability is disabled (e.g., via a Control), it cannot be exploited.

Examples of vulnerabilities include **unpatched software**, which exposes systems to cyberattacks; **immune deficiencies in biological organisms**, making them susceptible to infections; **structural fatigue in engineering**, reducing the durability of infrastructure over time; **financial instability in economic systems**, making institutions vulnerable to market fluctuations; and **data breaches in digital networks**, leading to loss of sensitive information.

#### Additional Fields of Vulnerabilities

- **state** (_string, required, default: `"enabled"`_): Specifies whether the vulnerability is active (`enabled`) or not (`disabled`).
- **exposes** (_list of strings, required_): Capabilities that are made vulnerable by this vulnerability. These capabilities must belong to the same entity.
- **exploits** (_list of strings, optional_): Capabilities that exploit this vulnerability. _(Automatically inferred when using LaDeRR Engine.)_

#### Rule: A Vulnerability can only expose Capabilities of the same Entity

This constraint ensures that vulnerabilities affect only their own host entity.

**FOL Representation:**

$$
\forall v, c ( Vulnerability(v) \land Capability(c) \land exposes(v, c) \rightarrow \exists! o ( Entity(o) \land vulnerabilities(o, v) \land capabilities(o, c) ) )
$$

#### Vulnerability Example from the Savannah Specification

The following vulnerability belongs to the zebra herd and exposes one of its capabilities. It is disabled in the `heatwave_response` scenario:

```toml
[Vulnerability.limited_water_access]
description = "Scarcity of water sources that increases physiological stress and drives risky movement patterns."
exposes = "efficient_thermoregulation"
label = "Limited Water Access"
scenarios = "heatwave_response"
state = "disabled"
```

<p align="left"><em>This vulnerability targets a capability within the same entity and is currently disabled.</em></p>

Capabilities and vulnerabilities define the operational characteristics of entities in a LaDeRR specification.
They serve as the foundation for inference mechanisms that determine protection, damage, inhibition, and resilience. Explicit resilience declarations are optional, as they can be inferred by the LaDeRR Engine based on rules.

## 9. Resilience

**Resilience** represents the mechanisms that enable an entity to preserve its capabilities despite vulnerabilities, even in the presence of threats. Resilience is not merely the absence of damage—it is the explicit preservation of function under adverse conditions. In LaDeRR, resilience is modeled as a dedicated scenario component, structurally linked to the capabilities it protects, the vulnerabilities it withstands, and the threats it counters.

When using the **LaDeRR Engine**, explicit resilience declarations are optional. The engine automatically infers resilience instances when the necessary configuration of capabilities, vulnerabilities, and threats is detected in the model, following formal inference rules.

The UML diagram below illustrates the structure of the `Resilience` class and its relationships:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Resilience.png" alt="UML diagram of the Resilience class in LaDeRR, showing its associations with Capability and Vulnerability via the preserves, preservesDespite, preservesAgainst, and sustains relations." style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

### 9.1. Fields of Resilience

A `Resilience` is defined through its connections to other components:

- **preserves** (_list of strings, required_): Capabilities maintained by the resilience mechanism. _(Automatically inferred when using LaDeRR Engine.)_
- **preservesAgainst** (_list of strings, required_): Capabilities used by threats that this resilience counters. _(Automatically inferred when using LaDeRR Engine.)_
- **preservesDespite** (_list of strings, required_): Vulnerabilities that expose the preserved capability and are exploited by threats, but that are neutralized within the configuration that gives rise to the resilience. _(Automatically inferred when using LaDeRR Engine.)_

Note that all the specific Resilience fields can be inferred by the LaDeRR Engine, provided the related constructs are correctly defined and related.

### 9.2. Rules Governing Resilience

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

#### Resilience Example from the Savannah Specification

The example below is taken from the `heatwave_response` scenario of the Savannah model. It demonstrates a resilience mechanism that allows the lion pride to preserve its hunting capability (`high_frequency_hunting_heatwave_response`) despite the presence of prey migration barriers and under threat from illegal hunting.

```toml
[Resilience.R17]
label = "R17"
preserves = "high_frequency_hunting_heatwave_response"
preservesAgainst = "disruptive_hunting_influence_heatwave_response"
preservesDespite = "prey_migration_barriers_heatwave_response"
scenarios = "heatwave_response"
```

<p align="left"><em>Automatically inferred resilience (R17) that maintains lion pride's hunting performance in the face of poaching and movement barriers.</em></p>

Another example is R1L, which illustrates a resilience construct preserving the zebra herd’s thermoregulation under heat stress conditions:

```toml
[Resilience.R1L]
label = "R1L"
preserves = "efficient_thermoregulation_heatwave_response"
preservesAgainst = "high_frequency_hunting_heatwave_response"
preservesDespite = "limited_water_access_heatwave_response"
scenarios = "heatwave_response"
```

<p align="left"><em>Resilience instance (R1L) preserving zebra herd's thermoregulation against the combined pressure of predatory behavior and water scarcity.</em></p>

Both examples were inferred by the LaDeRR Engine using only the constructs and relations explicitly declared in the specification.

## 10. Mapping to ResiliOnt Ontology

Each core domain construct in LaDeRR has been mapped to its corresponding ResiliOnt concept. The table below summarizes these mappings as declared in the [LaDeRR vocabulary](http://w3id.org/laderr) through `skos:note` annotations:

| LaDeRR Concept | ResiliOnt Concept   |
|----------------|---------------------|
| Asset          | Object at Risk      |
| Capability     | Capability          |
| Control        | Risk Inhibitor      |
| Disposition    | Disposition         |
| Entity         | Value Object        |
| Resilience     | Resilience          |
| Threat         | Threat Object       |
| Vulnerability  | Vulnerability       |

## 11. Complete Savannah Example

This section consolidates and presents the complete Savannah model used throughout this guide. Rather than introducing new concepts, this section provides a comprehensive view of the example specification and how it evolves after inference using the [LaDeRR Engine](https://w3id.org/laderr/engine/git). Readers will find here:

- The **original input specification**, as authored manually by the user.
- A **visual representation** of each scenario before inference (pre-inference).
- The **post-inference version** of each scenario, showing how constructs and relationships are enriched by the engine.
- A discussion of the key differences introduced during inference.

This section is useful for validating modeling choices, interpreting visual outputs, and understanding how LaDeRR formalizes and extends user-provided content. It also serves as a worked example of how to write and reason over LaDeRR models in practice.

You can download the full specification files here:

- [Input Specification (example_doc_in.toml)](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_in.toml)
- [Post-Inference Output (example_doc_out_post.toml)](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post.toml)

### 10.1. Heatwave Response (Pre-Inference)

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/documentation/example/example_doc_out/example_doc_out_pre_heatwave_response.png" alt="Heatwave Response – Pre-Inference">
</p>
<p align="center"><em>Figure: Visual representation of the "Heatwave Response" scenario before reasoning. Vulnerabilities are active, and no resilience is yet defined.</em></p>

This scenario models a high-temperature operational context where both the **Zebra Herd** and **Lion Pride** interact with elements such as the **Shaded Savannah Shelter**, **Poacher Group**, and **Meerkat Sentinels**.

Key features before reasoning:

- All capabilities and vulnerabilities are enabled.
- Vulnerabilities (e.g., `Limited Water Access`, `Territory Dependency`, `Prey Migration Barriers`) are still active and exposed.
- No resilience constructs are declared or inferred.
- Several capabilities exploit vulnerabilities, suggesting potential damage scenarios.
- Controls and threats are defined, but their protective or harmful effects have not yet been interpreted.

### 10.2. Dry Season Survival (Pre-Inference)

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/documentation/example/example_doc_out/example_doc_out_pre_dry_season.png" alt="Dry Season Survival – Pre-Inference">
</p>
<p align="center"><em>Figure: Visual representation of the "Dry Season Survival" scenario before reasoning. All relationships are explicitly declared; no inference has yet occurred.</em></p>

This scenario depicts prolonged drought conditions. Entities such as the **Zebra Herd**, **Lion Pride**, and **Poacher Group** coexist in a vulnerable ecosystem.

Key observations:

- No resilience components are defined at this point.
- Threats like the **Poacher Group** exploit active vulnerabilities.
- Some controls are in place (e.g., **Meerkat Sentinels**), but their effect has not been evaluated.
- The overall structure suggests exposure to risk without a protection mechanism being computed.

### 10.3. Heatwave Response (Post-Inference)

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/documentation/example/example_doc_out/example_doc_out_post_heatwave_response.png" alt="Heatwave Response – Post-Inference">
</p>
<p align="center"><em>Figure: Visual representation of the "Heatwave Response" scenario after inference. Inferred resilience constructs now structure the scenario as resilient.</em></p>

After inference, the **Heatwave Response** scenario is classified as `resilient`.

Key changes introduced by inference:

- **Resilience R1L** and **R17** are automatically created, showing how combinations of capabilities, vulnerabilities, and threats give rise to resilience.
- Vulnerabilities like `Limited Water Access` and `Prey Migration Barriers` are **disabled** by capabilities (`Dynamic Heat Refuge`, `Predator Detection Calls`).
- The **Zebra Herd** and **Shaded Shelter** are recognized as **controls**, enabling resilience indirectly.
- `preserves`, `preservesDespite`, and `preservesAgainst` links are clearly visible.
- The **status** of the scenario is updated from its default (`vulnerable`) to `resilient` by the engine.

This post-inference graph provides a complete, semantically enriched view of how threats are neutralized and vital functions are preserved.

### 10.4. Dry Season Survival (Post-Inference)

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/main/documentation/example/example_doc_out/example_doc_out_post_dry_season.png" alt="Dry Season Survival – Post-Inference">
</p>
<p align="center"><em>Figure: Visual representation of the "Dry Season Survival" scenario after inference. Although resilience is inferred (RE0), the scenario remains vulnerable.</em></p>

In this scenario, inference reveals partial protection mechanisms, but they are not enough to classify the scenario as resilient.

Key inference results:

- **Resilience RE0** is inferred to preserve the **Lion Pride’s** hunting capability against threats from the **Poacher Group** via protection from **Meerkat Sentinels**.
- However, other vulnerabilities—especially those affecting the **Zebra Herd**—remain enabled and exploited.
- The scenario’s **status** remains `vulnerable` because at least one asset capability is unprotected.
- The **Zebra Herd** does not participate in any resilience pattern and remains exposed to threats.

This example illustrates how resilience is **context-specific** and how partial protection does not suffice to reclassify an entire scenario.

This concludes the walkthrough of the Savannah Animal Survival Resilience Model. The progression from pre- to post-inference illustrates how LaDeRR enriches user-defined scenarios through rule-based reasoning, clarifies protection dynamics, and supports precise resilience classification. Users are encouraged to explore the full specification files and use the LaDeRR Engine to validate and extend their own models in similar fashion.
