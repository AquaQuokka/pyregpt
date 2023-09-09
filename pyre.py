import dotenv
import openai
import click
import os
import json

dotenv.load_dotenv(".env")
api_key = os.getenv("key")

@click.command()
@click.option('-c', help="Selects the conversation to use. E.g. 'foo' resolves to './channels/foo.json'")
@click.option('-q', help="The query to send to the server.")
def cli(c, q):
    msgp = []

    if c is None:
        c = "null.json"

    with open(f"./channels/{c}", "r") as f:
        file_content = f.read()

        if file_content:
            ctx = json.loads(file_content)
            msgp = ctx["ctx"]

    if q is not None:
        msgp.append({"role": "user", "content": q})

        openai.api_key = api_key
        res_json = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgp)
        res = res_json["choices"][0]["message"]["content"]
        
        click.echo_via_pager(res)

        msgp.append({"role": "assistant", "content": res})

        if c != "null.json":
            with open(f"./channels/{c}", "w") as f:
                json_file = json.dumps({"ctx": msgp})
                
                f.write(f"{json_file}")
    
    else:
        if q is None:
            click.echo(click.get_current_context().get_help())

if __name__ == "__main__":
    cli()