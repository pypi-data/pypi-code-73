from ..helper import add_arg_group


def mixin_hub_pushpull_parser(parser):
    gp = add_arg_group(parser, title='Push Pull')
    gp.add_argument('name', type=str, help='the name of the image.')
    gp.add_argument('--no-overwrite', action='store_true', default=False,
                    help='Do not allow overwriting existing images (based on module version and jina version)')
