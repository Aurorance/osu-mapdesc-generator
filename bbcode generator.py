import scrape
import os

def generate_bbcode(links):
    bbcodes = []

    if len(links) > 1:
        second_link = links[1]
        bbcode_first = f"[notice][centre][size=150][b] #1 [/b][url={second_link}]⮞[/url][/size][/centre][/notice]"
        bbcodes.append(bbcode_first)

    for i in range(1, len(links) - 1):
        A = links[i - 1]
        B = links[i + 1]
        XX = i + 1
        bbcode = f"[notice][centre][size=150][url={A}]⮜[/url][b] #{XX} [/b][url={B}]⮞[/url][/size][/centre][/notice]"
        bbcodes.append(bbcode)

    if len(links) > 2:
        second_last_link = links[-2]
        last_bbcode = f"[notice][centre][size=150][url={second_last_link}]⮜[/url][b] #{len(links)} [/b][/size][/centre][/notice]"
        bbcodes.append(last_bbcode)

    return bbcodes

def reverse_links():
    try:
        # Scrape and get the list of links
        link_list = scrape.main()
        
        if not link_list:
            print("No links were obtained. Please check the scrape module.")
            return

        # Check number of links obtained
        print(f"Total number of links obtained: {len(link_list)}")

        reversed_list = link_list[::-1]
        bbcodes = generate_bbcode(reversed_list)

        # Check number of BBCode blocks generated
        print(f"Total number of BBCode blocks generated: {len(bbcodes)}")

        # Determine the directory where the script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Define the file path for the output in the script's directory
        output_file = os.path.join(script_dir, "generated_bbcodes.txt")

        # Write the BBCodes to a text file in the script's directory
        with open(output_file, "w") as file:
            for bbcode in bbcodes:
                file.write(bbcode + "\n")
        
        print(f"BBCode has been written to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    reverse_links()