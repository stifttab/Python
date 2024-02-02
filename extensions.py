# Define the main function
def main():
    # Prompt the user to enter a file name and remove leading/trailing spaces while converting to lowercase
    file_name = input("File name: ").strip().casefold()
    
    # Check if the file name ends with one of the specified extensions
    if file_name.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        # If the file name matches an extension, call the get_media_type function to get the media type and print it
        print(get_media_type(file_name))
    else:
        # If the file name doesn't match any of the specified extensions, print a default media type
        print("application/octet-stream")

# Define the get_media_type function that maps file extensions to media types
def get_media_type(file_name):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    # Iterate through the media_types dictionary to find a matching extension and return the associated media type
    for extension, media_type in media_types.items():
        if file_name.endswith(extension):
            return media_type

# Call the main function to start the program
main()
