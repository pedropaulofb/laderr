# LaDeRR User Guide

**WORK IN PROGRESS: PLEASE BE AWARE THAT THIS DOCUMENT IS STILL UNDER DEVELOPMENT. USE IT CAREFULLY.**

## Table of Contents

- [Table of Contents](#table-of-contents)
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
    - [Minimal Valid Metadata](#minimal-valid-metadata)
    - [Complete Example with All Supported Fields](#complete-example-with-all-supported-fields)
- [4. Specification Constructs](#4-specification-constructs)
  - [4.1. Common Attributes of All Constructs](#41-common-attributes-of-all-constructs)
  - [4.2. Example of Construct Definition](#42-example-of-construct-definition)
  - [3.2. Scenario Classification and Determination](#32-scenario-classification-and-determination)
    - [Rules Governing Scenarios](#rules-governing-scenarios)
  - [4.2. Entities](#42-entities)
    - [Fields of Entities](#fields-of-entities)
    - [Assets](#assets)
    - [Threats](#threats)
    - [Controls](#controls)
    - [Rules Governing Entity Relationships](#rules-governing-entity-relationships)
  - [4.3. Dispositions](#43-dispositions)
    - [Rules Governing Dispositions](#rules-governing-dispositions)
    - [Capabilities](#capabilities)
    - [Vulnerabilities](#vulnerabilities)
    - [Rules Governing Vulnerabilities](#rules-governing-vulnerabilities)
  - [4.4. Resilience](#44-resilience)
    - [Fields of Resilience](#fields-of-resilience)
    - [Rules Governing Resilience](#rules-governing-resilience)
    - [Example of a Resilience Specification](#example-of-a-resilience-specification)
- [5. LaDeRR Engine](#5-laderr-engine)
  - [5.1. Writing a LaDeRR Specification with LaDeRR Engine](#51-writing-a-laderr-specification-with-laderr-engine)
    - [Automatic Inference](#automatic-inference)
    - [Automatic Resilience Generation](#automatic-resilience-generation)
    - [Simplified Specification Example](#simplified-specification-example)
  - [5.2. Engine Output and Inferred Model](#52-engine-output-and-inferred-model)
- [6. Complete Example](#6-complete-example)
  - [6.1. Explicit Specification](#61-explicit-specification)
  - [6.2. Simplified Specification with LaDeRR Engine](#62-simplified-specification-with-laderr-engine)
  - [6.3. Inferred Output by LaDeRR Engine](#63-inferred-output-by-laderr-engine)

## 1. Introduction

This guide provides a complete walkthrough for writing specifications using the [**La**nguage for **De**scribing **R**isk and **R**esilience (LaDeRR)](https://w3id.org/laderr/git), an ontology-based domain-specific language (DSL) for modeling resilience scenarios. Grounded in the [**ResiliOnt**](https://github.com/pedropaulofb/resiliont/) ontology, LaDeRR enables users to represent the interplay between entities, their capabilities, and their vulnerabilities in a structured, analyzable format.

Specifications are written in [TOML](https://toml.io/en/), a human-readable and machine-processable syntax. This guide introduces each language construct alongside its metamodel representation, relevant rules, and example fragments, building up to a complete and valid LaDeRR specification.

The following sections cover all core elements of a LaDeRR specification. Each component is accompanied by:

- **Concept Overview**: A brief explanation of the purpose and role of the component within a LaDeRR specification.
- **Metamodel Representation**: A UML class diagram illustrating the structure and relationships of the language's elements.
- **Rules and Constraints (if applicable)**: Formal constraints and derivations governing the use of the component.
- **Specification Example**: A LaDeRR specification snippet in TOML format, demonstrating a correct way to specify the component.

### 1.1. LaDeRR Metamodel Presentation

The LaDeRR metamodel defines the core structural elements of the language, establishing the conceptual foundation for resilience and risk scenario modeling. It is presented through separate UML class diagrams, each representing a distinct aspect of the LaDeRR language.

The UML metamodel follows a color-coding and formatting scheme:

- **Blue**: Represents classes that are defined within the specific diagram being presented.
- **Gray**: Represents classes defined in other diagrams, shown for context.
- **White**: Represents enumerations, which define a set of predefined values.
- **Red**: Represents notes that provide additional constraints, rules, or clarifications.

### 1.2. Access to LaDeRR Specification Example and Results

All examples presented throughout this guide are part of a single, incrementally constructed LaDeRR model. Each new concept is introduced by extending the same base file step by step. This approach allows readers to follow the progressive development of a complete and semantically rich LaDeRR specification.

The final, complete version—containing all elements introduced throughout the guide—is available in the [`documentation/example`](https://github.com/pedropaulofb/laderr/tree/main/documentation/example) folder of the LaDeRR repository. While this guide focuses on the LaDeRR language itself, many of the outputs referenced below—such as inferred specifications, visualizations, and reports—were generated using the [**LaDeRR Engine**](https://w3id.org/laderr/engine), a supporting tool designed to validate and extend LaDeRR models.

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

These outputs demonstrate how the [**LaDeRR Engine**](https://w3id.org/laderr/engine) processes a specification: transforming it into an RDF graph, applying inference mechanisms and validation, and producing a structured representation of the modeled scenario.

### 1.3. Processing the Specification with the LaDeRR Engine

The specification was processed using the [**LaDeRR Engine**](https://w3id.org/laderr/engine), a Python-based software that supports various operations over LaDeRR models. These operations are executed in two phases: **pre-inference** and **post-inference**. In addition to applying an OWL reasoner to infer implicit relations based on the model’s logical structure, the engine also applies inference rules defined in the LaDeRR metamodel. These rules enable the engine to extend the original specification with additional semantics—deriving new relations, instances, and properties—resulting in a more comprehensive model ready for analysis and visualization.

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
<img src="https://github.com/pedropaulofb/laderr/blob/main/documentation/images/visualization_legend.png" alt="Legend for Scenario Elements"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>
<p align="center"><em>Visual legend used in LaDeRR scenario diagrams, defining node shapes, colors, and edge styles according to their roles in the specification.</em></p>

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
  - **Entities** with multiple subtypes (e.g., both *Asset* and *Control*) use **striped fills** combining their respective colors. If an entity has all three subtypes (*Asset*, *Control*, and *Threat*), a three-way split is used.

- **Edge Colors and Types**:
  - **Blue Arrows**: Links between entities (*protects*, *inhibits*, *threatens*).
  - **Orange Arrows**: Resilience relations (*preserves*, *preservesAgainst*, *preservesDespite*, *sustains*).
  - **Dark Red Arrows**: A capability disabling a vulnerability.
  - **Black Arrows**: Causal relations (*exploits*, *exposes*).
  - **Green Arrows**: Vulnerabilities that *did not* cause damage.
  - **Red Arrows**: Vulnerabilities that *did* cause damage.
  - **Black Arrows with Diamond Tail**: Relations from entities to their capabilities, vulnerabilities, or resiliences.

Refer back to this legend when reading visualizations throughout the guide to better understand the semantics encoded in the diagrams.

## 2. General Structure of a LaDeRR Specification

Each LaDeRR specification consists of two main parts that together define one or more resilience scenarios in a structured and analyzable way:

- **Metadata**: Contains general information about the specification, such as its title, authorship, versioning, and the type of scenario being described. (See [Section 3](#3-metadata) for details.)

- **ScenarioComponents**: Represent the core elements of the scenario and their interrelations. These include:
  - **Assets**: Entities that hold value and are potentially exposed to threats.
  - **Capabilities**: The positive dispositions of entities—their abilities to perform protective or sustaining functions.
  - **Vulnerabilities**: Weaknesses that may be exploited by threats.
  - **Threats**: Entities that possess capabilities capable of exploiting vulnerabilities.
  - **Resilience**: Constructs that preserve the value of entities despite vulnerabilities or external pressures.
  - **Control**: Entities that inhibit threats and support resilience by blocking harmful effects.

These components are interconnected through a set of logical constraints. These are enforced through formal rules.

The next sections provide a detailed explanation of each part of the specification, including conceptual background, metamodel diagrams, associated rules, and concrete TOML examples.

### 2.1. Two Approaches to Writing LaDeRR Specifications

When writing a LaDeRR specification, users can choose between two approaches, depending on their needs and familiarity with the language:

- **Complete (Manual) Specification**:  
  In this approach, the user explicitly defines all elements and their properties using the full features of the LaDeRR language. Even fields that could be derived or assigned by default—such as types, statuses, or certain relationships—are specified directly. This method provides full control over the model and is useful for advanced users who want to fine-tune every aspect of a scenario.

- **Minimal (Auto-Completed) Specification**:  
  Alternatively, users can define only the essential structure of a scenario, leaving the rest to be automatically completed by the [LaDeRR Engine](https://w3id.org/laderr/engine/git). The engine applies reasoning, default values, and inference rules to generate a complete and semantically enriched version of the model. This saves time and reduces the learning curve, especially for new users or when modeling large (sets of) scenarios.

To illustrate the difference:
- A **minimal input specification** (92 lines):  
  [`example_doc_in.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_in.toml)
- The **fully completed version** generated after the minimal version by the engine (324 lines):  
  [`example_doc_out_post.toml`](https://github.com/pedropaulofb/laderr/blob/main/documentation/example/example_doc_out/example_doc_out_post.toml)

Throughout this guide, each language construct will be presented with examples showing **both styles**—the minimal form written by the user and the complete result produced by the LaDeRR Engine. This will help readers understand not only how to write a specification, but also what the engine adds during its processing.

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
<img src="https://github.com/pedropaulofb/laderr/blob/main/documentation/images/processing_stages.png"  alt="LaDeRR Engine's Process"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>
<p align="center"><em>Simplified view of the LaDeRR Engine’s processing stages, from a minimal user-defined specification to a fully enriched and validated model.</em></p>

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
<p align="center"><em>UML representation of the LaDeRR Specification class and its relation to scenario constructs. At least one specification must exist, but constructs are optional.</em></p>

It is important to note that a LaDeRR specification file is considered **valid** even if it contains only metadata—i.e., it does not require constructs to be defined. However, in most practical cases, constructs will be present to describe one or more resilience scenarios.

### 3.1. Required Fields and Defaults

The table below lists the metadata fields available in a LaDeRR specification, along with their types, cardinalities, and default values where applicable. Each metadata field is described using both an *Input Type* and a *Converted Type*. The *Input Type* refers to the format the user should adopt when writing the specification in TOML. The **Converted Type** indicates the internal representation used in the RDF graph generated by the LaDeRR Engine. This transformation enables more precise validation, as it allows the engine to detect malformed or inconsistent values that may otherwise go unnoticed if treated purely as free-form strings.

| Field           | Input Type                       | Converted Type | Multiplicity | Required | Default Value            | Description                                                                                                                                                                 |
|-----------------|----------------------------------|----------------|--------------|----------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **title**       | string                           | string         | [0..1]       | No       | N/A                      | A short name for the specification.                                                                                                                                         |
| **description** | string                           | string         | [0..1]       | No       | N/A                      | A brief explanation or summary of the content described in the specification.                                                                                               |
| **version**     | string                           | string         | [0..1]       | No       | N/A                      | A version identifier for the specification (free-form, no specific format required).                                                                                        |
| **createdBy**   | string \| list[string]           | list[string]   | [0..*]       | No       | N/A                      | Names or identifiers of the author(s). A single string is automatically converted into a list.                                                                              |
| **createdOn**   | datetime (TOML native) \| string | xsd:dateTime   | [0..1]       | No       | N/A                      | Timestamp of creation. Must follow the `xsd:dateTime` format. See [time format guide](https://github.com/pedropaulofb/laderr/blob/main/documentation/time_format.md).      |
| **modifiedOn**  | datetime (TOML native) \| string | xsd:dateTime   | [0..1]       | No       | N/A                      | Timestamp of the last known update. Must follow the `xsd:dateTime` format.                                                                                                  |
| **baseUri**     | string                           | URIRef         | [1]          | **Yes**  | `https://laderr.laderr#` | The base URI used to generate identifiers for all elements within the specification. Must be a valid URI string.                                                           |

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

While such minimal files are valid, they are not useful in practice unless used for testing or incremental development.

#### Complete Example with All Supported Fields

The example below illustrates a fully detailed metadata section. It includes multiple values where allowed and offers a comprehensive description of the specification's context and authorship.

```toml
baseURI = "https://savannahresilience.laderr#"
createdBy = ["Pedro Paulo F. Barcelos", "M. J. Silva", "Institute for Ecological Modeling"]
createdOn = "2025-03-28T12:00:00Z"
modifiedOn = "2025-04-01T10:30:00Z"
title = "Savannah Animal Survival Resilience Model"
description = "A resilience model for animal survival in the savannah. Inspired by real-world ecological dynamics including predation, shelter-seeking, and thermal stress."
version = "1.2"
```

## 4. Specification Constructs

All elements that describe the resilience scenario in a LaDeRR specification—such as threats, capabilities, assets, and so on—are represented as instances of the abstract class `Construct`.

Note that, although `Specification` and its attributes are technically constructs in the LaDeRR metamodel, the term **Construct** is used—both in the metamodel formalization and throughout this guide—to refer specifically to scenarios and their defining elements, i.e., the entities and relations that constitute the resilience model being specified.

Constructs are used to express the aspects of a resilience scenario and are divided into `Scenario` and `ScenarioComponent` categories. These are further refined into more specific types, such as `Capability`, `Vulnerability`, `Asset`, `Threat`, `Control`, and `Resilience`. The full taxonomy of constructs is presented in the diagram below:

<p align="center">
<img src="https://github.com/pedropaulofb/laderr/blob/main/documentation/images/construct_taxonomy.png" 
alt="LaDeRR Construct Taxonomy Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>Taxonomy of constructs in LaDeRR. All user-defined elements in a resilience scenario belong to this hierarchy.</em></p>

### 4.1. Common Attributes of All Constructs

Regardless of their specific type, all constructs share the same basic structure defined in the `Construct` class. The following three attributes are required for every instance:

- **id** (_string, required, unique_): The identifier of the construct. It must be unique within the specification and is used to reference this element throughout the model.
- **label** (_string, required_): A human-readable name for the construct. If not explicitly provided in the input file, it automatically defaults to the same value as the `id`.
- **description** (_string, optional_): A description of the construct.

The UML class diagram below summarizes the definition of the `Construct` class, presenting its attributes, specializations, and its association with the class `Specification`.

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Constructs.png" 
alt="LaDeRR Construct Class Diagram"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;">
</p>
<p align="center"><em>UML diagram of the Construct class.</em></p>

### 4.2. Example of Construct Definition

The following TOML snippet illustrates how to define constructs using their attributes:

<!-- TODO -->
$$$toml
# Example construct definitions
# To be filled in later
$$$

<!-- TODO: MAKE IT SPECIFIC -->
As shown above, the `label` field is mandatory in the model but can be omitted in the TOML input. If omitted, it is automatically assigned the same value as the construct’s `id`.

In the next sections, we will explore each specific subtype of construct in detail, including their unique roles, rules, and configuration examples.

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

```
\forall ls ( LaderrSpecification(ls) \land scenario(ls) = NOT_RESILIENT \leftrightarrow \exists o1, o2 ( Entity(o1) \land Entity(o2) \land ScenarioComponents(ls, o1) \land ScenarioComponents(ls, o2) \land succeededToDamage(o1, o2) ) )
```

- **Rule 2: A system is RESILIENT if all vulnerabilities are mitigated**

If a LaDeRR specification is in the `INCIDENT` state and there is no vulnerability left unaddressed (i.e., all vulnerabilities are either disabled or not actively exploited), then the system is classified as `RESILIENT`.

**FOL Representation:**

```
\forall ls ( LadderSpecification(ls) \land scenario(ls) = INCIDENT \land \neg \exists o1, v1 ( ScenarioComponents(ls, o1) \land vulnerabilities(o1, v1) \land \neg ( state(v1) = DISABLED \lor \neg \exists c1 (Capability(c1) \land exploits(c1, v1)) ) ) \rightarrow scenario(ls) = RESILIENT )
```

- **Rule 3: An INCIDENT must be either RESILIENT or NOT_RESILIENT**

For every LaDeRR specification, if its `scenario` is `INCIDENT`, then it must be classified as either `RESILIENT` or `NOT_RESILIENT`, but never both.

**FOL Representation:**

```latex
\forall ls ( LaderrSpecification(ls) \rightarrow ( scenario(ls) = INCIDENT \rightarrow scenario(ls) = RESILIENT \oplus scenario(ls) = NOT_RESILIENT ) )
```

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

```
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = ENABLED \land state(c2) = ENABLED ) ) \leftrightarrow succeededToDamage(o2, o1) )
```

- **Rule 2: A Threat fails to damage an Asset if the exploited vulnerability is disabled**
  A threat fails to cause damage if the vulnerability it exploits is disabled, meaning the exploit does not lead to a loss of the asset’s essential capability.

**FOL Representation:**

```
\forall o1, o2 ( ( Entity(o1) \land Entity(o2) \land \exists c1, v1, c2 ( Capability(c1) \land Vulnerability(v1) \land Capability(c2) \land capabilities(o1, c1) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land exploits(c2, v1) \land exposes(v1, c1) \land state(v1) = DISABLED \land state(c2) = ENABLED ) ) \leftrightarrow failedToDamage(o2, o1) )
```

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

A **Control** is an entity that actively mitigates threats or neutralizes vulnerabilities, thereby reducing risk. Controls **inhibit** threats, preventing them from successfully exploiting vulnerabilities in assets. Additionally, controls **protect** assets by safeguarding them from potential risks. A control must establish at least one of these relationships (*inhibits* or *protects*) to be considered valid in the system.  

Examples of controls include a _network firewall_, which prevents unauthorized access to hospital systems; a _vaccination program_, which mitigates the spread of infectious diseases in a population; a _marine protected area_, safeguarding coral reefs from overfishing and habitat destruction; an _algorithmic fraud detection system_, identifying suspicious transactions in financial markets; and an _early warning system for natural disasters_, enabling rapid response to earthquakes and hurricanes.  

##### **Additional Fields of Controls**  

- **protects** (_list of strings, optional\*_): References to the assets the control safeguards. _(Automatically inferred when using LaDeRR Engine.)_ 
- **inhibits** (_list of strings, optional\*_): References to threats that are neutralized or reduced by the control. _(Automatically inferred when using LaDeRR Engine.)_  

\* A `Control` **must have at least one of these relationships** (`inhibits` or `protects`). 

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

```
\forall o1, o2 ( Entity(o1) \land Entity(o2) \land \exists v1, c2 ( \land Vulnerability(v1) \land Capability(c2) \land vulnerabilities(o1, v1) \land capabilities(o2, c2) \land disables(c2, v1) ) \leftrightarrow protects(o2, o1) )
```

- **Rule 2: An Entity inhibits another if it neutralizes an exploited vulnerability**
  An entity inhibits another if it has a capability that disables a vulnerability, while the inhibited entity has a capability that exploits the same vulnerability.

**FOL Representation:**

```
\forall o2, o3 ( Entity(o2) \land Entity(o3) \land \exists c2, c3, v1 ( \land Capability(c2) \land Capability(c3) \land capabilities(o2, c2) \land capabilities(o3, c3) \land Vulnerability(v1) \land disables(c2, v1) \land exploits(c3, v1) ) \leftrightarrow inhibits(o2, o3) )
```

- **Rule 3: A Threat threatens an Asset if it exploits a vulnerability**
  A threat entity is said to threaten an asset if it has a capability that exploits a vulnerability within the asset.

**FOL Representation:**

```
\forall o1, o3 ( Entity(o1) \land Entity(o3) \land ( \exists v1, c3 ( Vulnerability(v1) \land Capability(c3) \land vulnerabilities(o1, v1) \land capabilities(o3, c3) \land exploits(c3, v1) ) \leftrightarrow threatens(o3, o1) ) )
```

### 4.3. Dispositions

Dispositions represent the inherent properties of entities within a LaDeRR specification that determine how they respond to changing conditions. They are divided into **Capabilities**, which represent positive dispositions that enable resilience, and **Vulnerabilities**, which represent negative dispositions that introduce risk. These elements are crucial for modeling how assets function under different conditions and how they interact with threats and controls.

Each disposition has a **state**, which can be either `enabled` or `disabled`. By default, all dispositions are set to `enabled`, meaning they actively contribute to the resilience or vulnerability of an entity. The state of a disposition influences whether it can be exploited or used to protect against threats.

- **state** (_string, optional, default: `"enabled"`_): Specifies whether the capability is active (`enabled`) and can perform its functions or inactive (`disabled`) and cannot affect its related elements.

#### Rules Governing Dispositions

- **Rule 1: A Disposition that disables another must be enabled**
  A disposition can only disable another if it is enabled, ensuring that only active dispositions can influence the system's resilience.

**FOL Representation:**

```
\forall d1, d2 ( Disposition(d1) \land Disposition(d2) \land disables(d1, d2) \rightarrow state(d1) = ENABLED \land state(d2) = DISABLED )
```

The UML diagram below illustrates the **Disposition** metamodel and its relationships with other ScenarioComponents:

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

```
\forall v, c ( Vulnerability(v) \land Capability(c) \land exposes(v, c) \rightarrow \exists! o ( Entity(o) \land vulnerabilities(o, v) \land capabilities(o, c) ) )
```

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

The UML diagram below illustrates the Resilience ScenarioComponent and its relationships:

<p align="center">
<img src="https://raw.githubusercontent.com/pedropaulofb/laderr/refs/heads/main/metamodel_images/Resilience.png"
style="max-width: 600px; max-height: 350px; height: auto; width: auto;"></p>

#### Fields of Resilience

A Resilience** ScenarioComponent is defined by its relationships to other elements:

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

```
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
```

- **Rule 2: Each Resilience is Defined by a Unique Combination of Elements**
  For each resilience instance, there exists exactly one configuration of an entity, three capabilities, and a vulnerability that justify its existence:
- The entity possessing resilience must have both the preserved capability and the vulnerability.
- A second entity must have an **enabled** capability that disables the vulnerability.
- A third entity must have a capability that exploits the vulnerability.
- The resilience mechanism must preserve the first entity’s capability, counteract the third entity’s capability, withstand the vulnerability, and be sustained by the second entity’s capability.

**FOL Representation:**

```
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
```

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
   - Many relations between ScenarioComponents are inferred instead of being explicitly defined by the user.
   - Examples:
     - **Protection**: If an entity has a capability that disables a vulnerability in another entity, the **protects** relation is inferred.
     - **Threats**: If an entity has a capability that exploits a vulnerability, the **threatens** relation is inferred.

4. **Resilience Mechanisms are Automatically Created**

    - If an entity has a **capability** that is at risk due to a **threat exploiting a vulnerability**, and another **capability exists that can sustain resilience**, the **engine automatically introduces a resilience mechanism** to preserve the first capability.

Since resilience inference is a key feature of the LaDeRR Engine, the next subsection describes the conditions under which resilience mechanisms are automatically generated.

#### Automatic Resilience Generation

A key feature of the LaDeRR Engine is its ability to **automatically generate resilience mechanisms** when conditions for resilience exist. Instead of requiring users to explicitly define resilience ScenarioComponents, the engine:

- **Identifies** when a resilience ScenarioComponent should exist based on the interplay between vulnerabilities, capabilities, and threats.
- **Instantiates** the resilience ScenarioComponent.
- **Establishes the necessary relations**, such as `preserves`, `preservesDespite`, and `preservesAgainst`.

For example, if an **Asset** has a **Capability** that is at risk due to a **Threat exploiting a Vulnerability**, and another **Capability exists that can sustain resilience**, the engine **automatically introduces a resilience mechanism**.

This behavior is formally defined by the **Resilience Requirement Rule** in **Section (Resilience Rules)**, which states:

> "If an entity has a **Capability** and a **Vulnerability**, and another entity has an **ENABLED Capability** that disables the Vulnerability, and the Vulnerability exposes the first entity’s Capability while being exploited by a third entity’s Capability, then there must exist exactly **one Resilience ScenarioComponent** that preserves the first Capability and is sustained by the second entity’s Capability."

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

However, when using **LaDeRR Engine**, the user can omit explicitly defining inferred relations, such as `threatens` and `protects`, and even the **Resilience ScenarioComponent itself**, as the **engine** will infer and generate it when applicable.

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

When processed by the **LaDeRR Engine**, the simplified specification is expanded, adding inferred relationships and resilience ScenarioComponents:

- **Resilience mechanisms are created** when conditions for resilience are met.
- **Threats are linked to their target assets** (e.g., `threatens` relation is inferred between `hacker_group` and `city`).
- **Protection mechanisms are inferred** if a capability neutralizes a vulnerability.
- **Scenario resilience is evaluated**.

The resulting expanded model ensures consistency with the LaDeRR framework while reducing manual specification effort.
