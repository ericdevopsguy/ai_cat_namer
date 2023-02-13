#!/usr/bin/env python3

import argparse
import openai


def cat_namer(api_key):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Suggest two names for a cat.",
            temperature=0.9
        )
        print(response)
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="run simple openai query")
    parser.add_argument("-k", "--key", type=str, required=True, help="your openapi key")
    args = parser.parse_args()

    if __name__ == "__main__":
        my_key = args.key

    cat_namer(my_key)


main()
