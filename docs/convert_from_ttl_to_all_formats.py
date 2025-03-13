from rdflib import Graph
import os
from loguru import logger

# Define the input Turtle file
input_file = "laderr-vocabulary.ttl"

try:
    # Load the Turtle file into an RDFLib graph
    g = Graph()
    g.parse(input_file, format="turtle")
    logger.success(f"Successfully loaded {input_file}")

    # Define the output formats supported by RDFLib
    formats = {
        "xml": "owl",  # RDF/XML
        "nt": "nt",  # N-Triples
        "n3": "n3",  # Notation3
        "json-ld": "jsonld",  # JSON-LD
        "trig": "trig",  # TriG
    }

    # Get the base name of the file (without extension)
    base_name = os.path.splitext(input_file)[0]

    # Convert and save in each format
    for fmt, ext in formats.items():
        output_file = f"{base_name}.{ext}"
        try:
            g.serialize(destination=output_file, format=fmt)
            logger.success(f"Saved: {output_file}")
        except Exception as e:
            logger.error(f"Failed to save {output_file}: {e}")

    logger.success("Conversion completed!")
except Exception as e:
    logger.error(f"Failed to process {input_file}: {e}")
