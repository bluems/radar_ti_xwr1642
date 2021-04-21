from TI.XWR1642 import XWR1642


def main():
    radar = XWR1642('1642config.cfg')
    # radar.input_config('1642config.cfg')
    radar.print_config()
    pass


if __name__ == '__main__':
    main()
    pass
