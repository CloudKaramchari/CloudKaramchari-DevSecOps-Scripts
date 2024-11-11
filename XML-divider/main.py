import xml.etree.ElementTree as ET

def split_xml(input_file, output_prefix, elements_per_file):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Initialize variables
    file_count = 0
    current_count = 0
    new_root = ET.Element(root.tag)  

    # Iterate over each child element in the root
    for child in root:
        new_root.append(child)
        current_count += 1

        # Check if we have reached the specified number of elements
        if current_count >= elements_per_file:
            # Create a new XML tree and write it to a file
            new_tree = ET.ElementTree(new_root)
            output_file = f"{output_prefix}_{file_count + 1}.xml"
            new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
            print(f"Created: {output_file}")
            
            # Reset for the next file
            file_count += 1
            current_count = 0
            new_root = ET.Element(root.tag)  # Reset the new root

    # Write any remaining elements to a new file
    if current_count > 0:
        new_tree = ET.ElementTree(new_root)
        output_file = f"{output_prefix}_{file_count + 1}.xml"
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print(f"Created: {output_file}")

if __name__ == "__main__":
    input_file = 'input_file.xml'  # Replace with your large XML file
    output_prefix = 'output/small_file'     # Prefix for output files
    elements_per_file = 100000           # Number of elements per small file

    split_xml(input_file, output_prefix, elements_per_file)
