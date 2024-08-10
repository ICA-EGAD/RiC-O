"""
Simple consistency checker (and parser) for the RiC-O ontology, using the
Owlready2 module (pip install owlready2) and the Hermit reasoner built into
it. Requires that a JVM (Java virtual machine) be installed.

The environment variable ONTOLOGY_PATH can be either a path to an actual
version of the RiC-O ontology (expecting a .rdf file suffix and for the file
name to begin with 'RiC') or a directory. In the latter case the directory will
be searched for a file with a .rdf suffix whose name begins with 'RiC'; with
the current structure of the RiC-O ontology repository, this will allow for the
consistency checker to continue to work upon changes of version.
"""

from os import environ
from pathlib import Path
from sys import exit as sys_exit

from owlready2 import get_ontology, sync_reasoner  # type: ignore
from owlready2.base import (  # type: ignore
    OwlReadyInconsistentOntologyError,
    OwlReadyOntologyParsingError)

ONTOLOGY_PATH = environ["ONTOLOGY_PATH"]


def _find_ontology(directory: Path) -> Path:
    found = None
    for path in directory.glob("*"):
        if path.suffix == ".rdf" and path.name.startswith("RiC"):
            if found is not None:
                sys_exit(
                    "Cannot identify the current version of the ontology: "
                    f"found more than one .rdf file in {directory} whose name "
                    "begins with RiC")
            found = path
    if found is None:
        sys_exit("Cannot identify the current version of the ontology: did not "
                 f"find an .rdf file in {directory} whose name begins with RiC")
    return found


def _ontology_path() -> Path:
    given_path = Path(ONTOLOGY_PATH)
    if given_path.is_dir():
        return _find_ontology(given_path)
    if not given_path.is_file():
        sys_exit(f"No file found at the provided path: {ONTOLOGY_PATH}")
    return given_path


def check_consistency() -> None:
    """
    Obtains the RiC-O ontology by means of the ONTOLOGY_PATH environment
    variable, parses it, and checks its consistency (using the Hermit reasoner
    built into Owlready2).
    """
    ontology_path = _ontology_path()
    try:
        ontology = get_ontology(str(ontology_path)).load()
    except OwlReadyOntologyParsingError:
        sys_exit(f"Could not parse {ontology_path} to an ontology!")
    with ontology:
        try:
            sync_reasoner(debug=0)
        except OwlReadyInconsistentOntologyError:
            sys_exit("Ontology is inconsistent!")
    inconsistent_classes = list(ontology.inconsistent_classes())
    if inconsistent_classes:
        sys_exit("Ontology is not itself inconsistent, but has inconsistent "
                 f"classes: {inconsistent_classes}")
    print("Ontology is consistent!")


check_consistency()
