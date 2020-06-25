def __set_defaults_smaai5():
    set_default('MACHINE', 'smaai5-am335x')
    set_default('DISTRO', 'smaai5')

def __after_init_smaai5_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-openembedded/meta-networking',
                        'meta-openembedded/meta-oe',
                        'meta-openembedded/meta-python',
                        'meta-qt5',
                        'meta-smaai5',
                    ]])

run_set_defaults(__set_defaults_smaai5)
run_after_init(__after_init_smaai5_yocto)
