def pdf_to_images_high_quality(pdf_path, output_folder, dpi=300, image_format='PNG'):
    import os 
    import fitz
    from PIL import Image
    """
    Convert PDF to high-quality images without losing text quality.
    
    Parameters:
    -----------
    pdf_path : str
        Path to the input PDF file
    output_folder : str
        Folder where images will be saved
    dpi : int
        Resolution in dots per inch (300 is print quality, 150 is screen quality)
        Higher DPI = better quality but larger file size
    image_format : str
        Output format: 'PNG' (lossless) or 'JPEG' (compressed)
    
    Returns:
    --------
    list : Paths to all generated images
    """
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Calculate zoom factor for desired DPI
    # PyMuPDF default is 72 DPI, so zoom = desired_dpi / 72
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    
    image_paths = []
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document[page_num]
        
        # Render page to an image with high quality
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        
        # Generate output filename
        output_filename = f"page_{page_num + 1:04d}.{image_format.lower()}"
        output_path = os.path.join(output_folder, output_filename)
        
        # Save the image
        if image_format.upper() == 'PNG':
            pix.save(output_path)
        else:
            # For JPEG, convert through PIL for better quality control
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save(output_path, quality=95, optimize=True)
        
        image_paths.append(output_path)
        print(f"Saved: {output_path}")
    
    pdf_document.close()
    
    return image_paths



