from pdf_to_image import pdf_to_images_high_quality
def convert_pdf_to_images(file_path, output_dir):  
    print("Converting PDF to images...")
    images = pdf_to_images_high_quality(pdf_path=file_path, output_folder=output_dir, dpi=300, image_format='PNG')
    return images

