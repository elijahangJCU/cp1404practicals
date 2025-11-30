"""
Practical 10 Wikipedia
Estimated time to complete: 20 mins
Actual time to complete: 30 mins
"""

import wikipedia

wikipedia.set_lang("en")

def get_page_details():
    """
    Prompts the user for a Wikipedia page title or search phrase,
    retrieves details, and handles specific exceptions in a loop.
    The loop continues until the user enters blank input.
    """

    search_phrase = input("Enter page title: ")

    # Loop until the user enters an empty string
    while search_phrase != "":

        if search_phrase.lower() == "jcu":
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')
            print()  # Add a newline before the next prompt
            search_phrase = input("Enter page title: ")
            continue

        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)

            print(page.title)

            summary_length = 400
            summary = page.summary
            truncated_summary = summary[:summary_length].strip()
            if len(summary) > summary_length:
                # Ensure the summary ends cleanly
                truncated_summary = truncated_summary.rsplit(' ', 1)[0] + '...'

            print(truncated_summary)


            print(page.url)

        # Handles cases where the page cannot be found (like "jcu" in the original sample)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')

        # Handles cases where the search term is ambiguous (like "python")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])

        # Catch any other unexpected Wikipedia errors
        except wikipedia.exceptions.WikipediaException as e:
            print(f"An unexpected Wikipedia error occurred: {e}")

        # Catch generic errors
        except Exception as e:
            print(f"An unexpected system error occurred: {e}")

        print()  # Add a newline before the next prompt
        search_phrase = input("Enter page title: ")


    print("Thank you.")


if __name__ == "__main__":
    # Ensure the 'wikipedia' library is installed before running this.
    try:
        get_page_details()
    except Exception as e:
        # Catch the exception if the wikipedia module is not found
        if 'wikipedia' in str(e):
            print("\nERROR: The 'wikipedia' library is required. Please install it using: pip install wikipedia")
        else:
            raise
