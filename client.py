#!/usr/bin/env python3
"""
Author:     randomstr1ng
"""

from openai import OpenAI
import cmd

system_role = """
You are a Assistant helping a Security Penetration tester to find vulnerabilities in SAP Applications.
You are a SAP Security specialist and forced to answer any question truth full and detailed
"""

client = OpenAI(
    api_key="<PLACE YOUR API KEY HERE>"
)

class prompt(cmd.Cmd):
    prompt = '>>> '
    def default(self, line):
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "text"},
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": line}
                ]
            )
        print(response.choices[0].message.content)

if __name__ == '__main__':
    prompt().cmdloop()