from unstructured.partition.pdf import partition_pdf
from pathlib import Path
import os

def parser(file_path: str) -> str:
    """
    Basic pdf parsing using unstructured.
    
    Parameters
    ----------
    path : str
        Path to pdf document.
        
    Returns
    -------
    whole_text : str
        Parsed text in pdf-document.
    
    """
    
    # assert file exists
    assert os.path.isfile(file_path), "Not a file!"
    
    # assert it is a pdf
    assert file_path[-3:] == "pdf", "Not a pdf!"
    
    # parse
    raw_elements = partition_pdf(filename=file_path)
    
    # text elements
    whole_text = " ".join([element.text for element in raw_elements])
    
    return whole_text