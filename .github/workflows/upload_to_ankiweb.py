import json
import os
from argparse import ArgumentParser
from pathlib import Path
from zipfile import ZipFile

from webbot import Browser


def upload(
    repo_owner,
    ankiweb_username,
    ankiweb_password,
    addon_dir,
    build_file=None,
    show_window=False,
):
    build_files = list((Path(addon_dir) / 'build').glob('*.ankiaddon'))
    if len(build_files) == 1:
        build_file_path = build_files[0]
    elif (b := next((f for f in build_files if f.name == build_file), None)) is not None:
        build_file_path = b
    elif len(build_files) == 0:
        raise Exception("The build directory is empty")
    else:
        raise Exception(
            "Multiple build files and no build_file parameter provided")

    # unzip and read in manifest.json
    with ZipFile(build_file_path) as zipf:
        zipf.extract('manifest.json')

    with open('manifest.json') as f:
        manifest = json.load(f)
    os.unlink('manifest.json')

    # read in addon.json
    with open(Path(addon_dir) / 'addon.json') as f:
        addon = json.load(f)

    # use webbot to upload the add-on
    web = Browser(showWindow=show_window)
    web.go_to('https://ankiweb.net/shared/upload')
    web.type(ankiweb_username, into='username')
    web.type(ankiweb_password, into='password')
    web.press(web.Key.ENTER)

    if manifest["ankiweb_id"]:
        # update existing addon
        web.go_to(f'https://ankiweb.net/shared/upload?id={manifest["ankiweb_id"]}')
    else:
        # upload new addon
        web.go_to(f'https://ankiweb.net/shared/upload')

    web.type(addon['display_name'], into='title')
    web.type(
        f'https://github.com/{repo_owner}/{addon["repo_name"]}/issues', into='support url')

    web.type(
        str(build_file_path.absolute()),
        id='v21file0',
    )

    # copy description from ankiweb_description.html
    with open(Path(addon_dir) / 'ankiweb_description.html') as f:
        description = f.read()
    # ... this is slow (can take 5 seconds or more)
    web.type(description, id='desc')

    # optional values
    def enter_optional_value(dict_, key, into='', id=''):
        if dict_.get(key) is not None:
            web.type(dict_[key], into=into, id=id)

    enter_optional_value(addon, 'tags', 'tags')
    enter_optional_value(manifest, 'min_point_version', id='minVer0')
    enter_optional_value(manifest, 'max_point_version', id='maxVer0')

    if manifest["ankiweb_id"]:
        web.click('Update')
    else:
        web.click('Upload')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('repo_owner', type=str)
    parser.add_argument('--addon_dir', type=str, default='.')
    parser.add_argument('--build_file_name', type=str)
    args = parser.parse_args()

    upload(
        args.repo_owner,
        os.environ['USERNAME'],
        os.environ['PASSWORD'],
        args.addon_dir,
        args.build_file_name,
    )
