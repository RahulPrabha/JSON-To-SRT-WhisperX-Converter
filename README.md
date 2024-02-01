# JSON to SRT Max Character Length Converter for WhisperX Output

## Introduction

This utility script is designed to convert JSON-formatted subtitle data produced by [WhisperX](https://github.com/m-bain/whisperX) into the SubRip Text (SRT) format.

**The script ensures that each subtitle segment adheres to a user-specified maximum character length for optimal readability.
**

## Prerequisites

- Python 3.x
- Basic knowledge of running Python scripts from the terminal or command line
- JSON output file from WhisperX

## Installation

1. Clone this repository or download the source code:

```
git clone https://github.com/RahulPrabha/json-to-srt-converter.git
```

2. Navigate to the cloned or downloaded directory.

## Usage

To convert a WhisperX JSON subtitle file to the SRT format, run the script from the terminal or command line with the following arguments:

```
python json_to_srt_converter.py path_to_whisperx_json_file.json max_characters_per_line -o output_file.srt
```

- `path_to_whisperx_json_file.json`: The path to your JSON file containing the subtitle data output from WhisperX.
- `max_characters_per_line`: The maximum number of characters allowed per subtitle line (segment).
- `output_file.srt` (optional): The name of the output SRT file. If not specified, the script defaults to `output.srt`.

### Example

```
python json_to_srt_converter.py whisperx_output.json 50 -o subtitles.srt
```

This command reads `whisperx_output.json`, ensures each subtitle line does not exceed 50 characters, and writes the output to `subtitles.srt`.

## Contributing

Contributions to improve the script or add new features are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
