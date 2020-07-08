from config import Config

def config() -> Config:
    return Config(
        version = '1.0',
        author = ['Chris Schnaufer', 'Ken Youens-Clark'],
        author_email = ['schnaufer@arizona.edu', 'kyclark@arizona.edu'],
        write_betydb_csv = True)
