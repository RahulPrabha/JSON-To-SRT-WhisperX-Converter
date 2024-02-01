import json
import argparse

def split_text(words, max_length):
    lines = []
    current_line = ""
    current_time = {"start": None, "end": None}

    for word_info in words:
        word = word_info["word"]
        if len(current_line + word) <= max_length:
            current_line += word + " "
            current_time["end"] = word_info["end"]
            if current_time["start"] is None:
                current_time["start"] = word_info["start"]
        else:
            lines.append((current_line.strip(), current_time.copy()))
            current_line = word + " "
            current_time = {"start": word_info["start"], "end": word_info["end"]}

    if current_line:
        lines.append((current_line.strip(), current_time))

    return lines

def generate_srt(subtitles_json, max_length):
    subtitles = json.load(subtitles_json)
    srt_output = ""
    counter = 1

    for segment in subtitles['segments']:
        text_sections = split_text(segment['words'], max_length)

        for text, times in text_sections:
            start_time = format_time(times['start'])
            end_time = format_time(times['end'])
            srt_output += f"{counter}\n{start_time} --> {end_time}\n{text}\n\n"
            counter += 1

    return srt_output

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:06.3f}".replace('.', ',')

def main():
    parser = argparse.ArgumentParser(description="Convert JSON subtitle file to SRT format.")
    parser.add_argument("json_file", type=argparse.FileType('r'), help="Path to the JSON subtitle file")
    parser.add_argument("max_length", type=int, help="Maximum number of characters per subtitle line")
    parser.add_argument("-o", "--output", default="output.srt", help="Output SRT file name (default: output.srt)")

    args = parser.parse_args()

    srt_content = generate_srt(args.json_file, args.max_length)

    with open(args.output, "w") as file:
        file.write(srt_content)

    print(f"SRT file created successfully: {args.output}")

if __name__ == "__main__":
    main()
