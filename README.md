# PhotoHUNT

PhotoHUNT is a simple tool to extract EXIF metadata from images. It supports multi-language functionality (English and Russian) and allows users to view detailed information such as file size, camera make/model, geolocation data, and more.

## Features

- Extract EXIF metadata from image files.
- Multi-language support (English, Russian).
- Option to open files through file explorer or by providing the file path.
- Displays data in a user-friendly format.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/justoperator/photoHUNT.git
    cd PhotoHUNT
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the tool:

    ```bash
    python photohunt.py
    ```

## Usage

### Main Menu

- **1. Language** - Choose between English or Russian.
- **2. Get info** - Extract and view metadata from an image file.
- **3. How to use?** - View instructions on how to use the tool.
- **4. Exit** - Exit the program.

### File Selection

When extracting image metadata, you can:
- **Open by path** - Provide a file path to the image.
- **Open by explorer** - Use the file explorer to select the image file.

### Metadata Display

The tool will display key metadata such as:
- File name
- File size
- Camera model
- Date of image capture
- Geolocation (if available)

```bash
python photohunt.py
